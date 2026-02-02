# Exception & Error
- BaseException : 예외 최상위. 여기에 SystemExit / KeyboardInterrupt 같은 “프로그램 종료 계열”도 들어가서, 보통은 함부로 잡지 않음.
- SyntaxError : 파싱 단계에서 터짐(프로그램 실행 자체가 안 됨).
- Exception(런타임 예외): 실행 중에 발생. try/except로 처리 가능.

## 예외 계층구조
- BaseException
  - SystemExit 
  - KeyboardInterrupt 
  - GeneratorExit 
  - Exception 
    - ValueError 
    - TypeError
    - KeyError
    - IndexError
    - FileNotFoundError (OSError 계열)
    - ZeroDivisionError
    - RuntimeError 
    - …

## 예외 분류 기준 (Retry 정책용)
| 유형 | 대표 예외/상황 | 분류(정책) | 
|---|---|---|
| 네트워크 | `TimeoutError`, `ConnectionError` | **Retryable** | 
| 외부 API 5xx | HTTP 5xx (서버 오류) | **Retryable** | 
| DB Deadlock | (DB/드라이버가 던지는) deadlock 관련 예외 | **Retryable** | 
| 입력 데이터 오류 | `ValueError`, (커스텀) `ValidationError` | **NonRetryable** | 
| 스키마 불일치 | 컬럼 누락/타입 불일치/필드 구조 변경 | **NonRetryable** | 
| 코드 버그 | `AttributeError`, `TypeError` 등 로직 오류 | **NonRetryable (fail-fast)** | 

## try / catch
```python
try:
    x = int("abc")
except ValueError as e:
    print("숫자 변환 실패:", e)
# 숫자 변환 실패: invalid literal for int() with base 10: 'abc'

try:
    d = {"a": 1}
    print(d["b"])
except (KeyError, TypeError) as e:
    raise RuntimeError("KeyError Or TypeError Occurred") from e
# Traceback (most recent call last):
#   File "/Users/jungmo/Desktop/local-repo/github/python/basic/04_exception.py", line 9, in <module>
#     print(d["b"])
#           ~^^^^^
# KeyError: 'b'
# 
# The above exception was the direct cause of the following exception:
# 
# Traceback (most recent call last):
#   File "/Users/jungmo/Desktop/local-repo/github/python/basic/04_exception.py", line 11, in <module>
#     raise RuntimeError("KeyError Or TypeError Occurred") from e
# RuntimeError: KeyError Or TypeError Occurred
```

## else / finally
- else : 예외가 없을 때만 실행 
```python
try:
    n = int("123")
except ValueError:
    print("실패")
else:
    print("성공:", n)
```
- finally : 무조건 실행 - 리소스 정리
```python
f = None
try:
    f = open("a.txt", "w")
    f.write("hi")
finally:
    if f:
        f.close()
```

## raise 
- 예외 변환(랩핑) + 원인 보존 : raise ... from e
  - from e를 쓰면 traceback에 “원인 예외”가 같이 붙어서 디버깅이 쉬워짐.
  - throw new X("..", e) 느낌.
```python
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("숫자 파싱 실패") from e
# Traceback (most recent call last):
#   File "/Users/jungmo/Desktop/local-repo/github/python/basic/04_exception.py", line 23, in <module>
#     int("abc")
# ValueError: invalid literal for int() with base 10: 'abc'
# 
# The above exception was the direct cause of the following exception:
# 
# Traceback (most recent call last):
#   File "/Users/jungmo/Desktop/local-repo/github/python/basic/04_exception.py", line 25, in <module>
#     raise RuntimeError("숫자 파싱 실패") from e
# RuntimeError: 숫자 파싱 실패
```
- 원인 숨기기 : from None
  - 사용자에게 내부 구현 에러를 숨길 때 유용(하지만 로그에는 남기는 게 좋음)
```python
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("사용자 입력이 잘못됨") from None
# Traceback (most recent call last):
#   File "/Users/jungmo/Desktop/local-repo/github/python/basic/04_exception.py", line 32, in <module>
#     raise RuntimeError("사용자 입력이 잘못됨") from None
# RuntimeError: 사용자 입력이 잘못됨
```

## Custom Exception
- Exception 상속
```python
class DataValidationError(Exception):
    pass

def validate_age(age: int) -> None:
    if age < 0:
        raise DataValidationError("age must be >= 0")
validate_age(-20)

# Traceback (most recent call last):
#   File "/Users/jungmo/Desktop/local-repo/github/python/basic/04_exception.py", line 42, in <module>
#     validate_age(-20)
#   File "/Users/jungmo/Desktop/local-repo/github/python/basic/04_exception.py", line 40, in validate_age
#     raise DataValidationError("age must be >= 0")
# DataValidationError: age must be >= 0
```


## Example1 : ETL / Data Pipeline 에서 자주 쓰이는 예외전략(파이프라인 내부 - 분산(태스크별) 방식)
```python
class RetryableError(Exception):
    """일시적 문제 → retry 대상"""

class NonRetryableError(Exception):
    """데이터/로직 문제 → retry 의미 없음"""

def load():
    try:
        ...
    except TimeoutError as e:
        raise RetryableError("network timeout") from e
    except ValueError as e:
        raise NonRetryableError("bad data") from e

@task(retries=3, retry_delay=timedelta(minutes=5))
def task():
    try:
        load()
    except RetryableError:
        raise   # Airflow retry 발동
    except NonRetryableError:
        # 로그 남기고 성공 처리 or 별도 알림
        return
```

## Example2 : ETL / Data Pipeline 에서 자주 쓰이는 예외전략(파이프라인 경계 - 중앙집중(엔트리포인트) 방식)
- handle_pipeline_error()의 역할
  - 로그 레벨 결정 (warning / error / critical)
  - 메트 태깅 (error_type=retryable)
  - 알림(Slack, PagerDuty, Email)
  - 필요하면 상태 저장(DB, S3, XCom)
- 여기서도 retry를 직접 돌리지는 않음 
  - raise 해서 오케스트레이터(Airflow)가 하게 둠
```python
from airflow.exceptions import AirflowFailException, AirflowSkipException

class PipelineError(Exception): ...
class RetryableError(PipelineError): ...
class NonRetryableError(PipelineError): ...
class FatalError(PipelineError): ...
def load() : ...
def transform() : ...
def write() : ...


def handle_pipeline_error(e: PipelineError):
    if isinstance(e, RetryableError):
        logger.warning("retryable error", exc_info=e)
        metrics.increment("pipeline.retryable_error")

    elif isinstance(e, NonRetryableError):
        logger.error("non-retryable error", exc_info=e)
        alert("data issue detected")

    elif isinstance(e, FatalError):
        logger.critical("fatal error", exc_info=e)
        alert("pipeline aborted immediately")
        
@task(retries=3, retry_delay=timedelta(minutes=5))
def run_pipeline():
    try:
        load(); transform(); write()

    except RetryableError as e:
        handle_pipeline_error(e)
        raise   # Airflow retry 발동

    except NonRetryableError as e:
        handle_pipeline_error(e)
        # 정책 1: 실패로 남기되 retry는 끊고 싶다면
        raise AirflowFailException(str(e))
        # 정책 2: 스킵으로 남기고 싶다면
        # raise AirflowSkipException(str(e))

    except FatalError as e:
        handle_pipeline_error(e)
        raise AirflowFailException(str(e))  # 즉시 실패 + retry 없음
```