# First-Class Function
# Closure
#     - 파이썬 변수범위(Scope)
#     - Global 선언
#     - Class -> Closure 구현

## 파이썬 변수 범위
c = 30
def func_v3(a) :
    global c
    print('in func >> a : ', a)
    print('in func >> c : ', c)
    c = 40

func_v3(10)
print('out func >> a : ', c)

## Closure - 상태를 기억한다
### 서버 프로그래밍 -> 동시성(Conccurency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
### 메모리를 공유하지 않고, 메시지 전달로 처리하기 위함
### 클로저는 공유하되, 변경되지 않는(Immutable, Read Only)
### 클로저는 불변 자료구조 및 Atom,STM -> 멀티스레드(coroutine) 프로그래밍에 강점

class Averager():
    def __init__(self):
        self._series = []

    def __call__(self,v) :
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

averager_cls = Averager()
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))

print('##########')
def closure_ex1() :
    series = [] # Free variable
    def averager(v):
        series.append(v)
        print('inner >> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

closure_ex1 = closure_ex1()
print(dir(closure_ex1))
print(closure_ex1.__closure__[0].cell_contents)

print(closure_ex1(10))
print(closure_ex1.__closure__[0].cell_contents)
print(closure_ex1(30))
print(closure_ex1.__closure__[0].cell_contents)
print(closure_ex1(50))
print(closure_ex1.__closure__[0].cell_contents)

print('##########')
print(closure_ex1.__code__.co_freevars)
print(dir(closure_ex1.__closure__[0]))


# series 는 로컬 변수였지만
# 내부 함수가 참조하는 순간
# free variable 이 되어
# 함수 객체의 __closure__ 안에 저장된다.

# 스코프 문제가 아니라 생명주기(lifecycle) 문제
# 함수가 끝나도
# 참조가 남아있으면 안 죽는다

def closure_ex1() :
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total
        # 변수 재할당(재바인딩)이 발생하므로 런타임에서 지역변수로 간주됨 -> nonlocal 로 지역변수가 아닌 바로 바깥 스코프 변수를 쓰겠다 명시해줘야함 (변수 재할당(재바인딩)이 일어나는 경우)
        cnt += 1
        total += v
        return cnt / total
    return averager
