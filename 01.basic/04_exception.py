try:
    x = int("abc")
except ValueError as e:
    print("숫자 변환 실패:", e)


# try:
#     d = {"a": 1}
#     print(d["b"])
# except (KeyError, TypeError) as e:
#     raise RuntimeError("KeyError Or TypeError Occurred") from e
#     print("맵 접근 에러:", e)


try:
    n = int("123")
except ValueError:
    print("실패")
else:
    print("성공:", n)


# try:
#     int("abc")
# except ValueError as e:
#     raise RuntimeError("숫자 파싱 실패") from e


# try:
#     int("abc")
# except ValueError as e:
#     raise RuntimeError("사용자 입력이 잘못됨") from None


class DataValidationError(Exception):
    pass

def validate_age(age: int) -> None:
    if age < 0:
        raise DataValidationError("age must be >= 0")

validate_age(-20)