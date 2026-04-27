# First-Class Function
# 파이썬 함수 특징
#     - 런타임 초기화
#     - 변수 할당 가능
#     - 함수를 인수로 전달 가능
#     - 함수를 결과로 반환 가능
# 고위함수(Higher-order function)
# 익명함수(Lambda)
# Callable
# Partial
from collections.abc import Callable


def factorial(n : int) -> int:
    '''Factiral Function -> n : int '''
    if n == 0:
        return 1
    return n*factorial(n-1)

class A :
    pass

print('factorial : ', factorial)
print('type(factorial) : ',type(factorial))
print('type(A) : ',type(A))
print('only function has : ',set(dir(factorial))- set(dir(A)))
# {'__annotations__', '__defaults__', '__kwdefaults__', '__qualname__', '__globals__', '__name__', '__builtins__', '__get__', '__call__', '__closure__', '__code__'}
print('##########')

## 변수 할당
var_func = factorial
print('var_func : ',var_func)
print('type(var_func) : ',type(var_func))
print('var_func(5) : ',var_func(5))
print('list(map(var_func,range(1,11))) : ',list(map(var_func,range(1,11))))
print('##########')


## 함수 인수 전달 및 함수로 결과 반환 -> 고위함수(Higher-order function)
### map, filter, reduce
print('[var_func(i) for i in range(1,11) if i % 2 == 0] : ',[var_func(i) for i in range(1,11) if not i % 2])
print('list(map(var_func,filter(lambda x : not x % 2 ,range(1,11)))) : ',list(map(var_func,filter(lambda x : not x % 2 ,range(1,11)))))

from functools import reduce
print('reduce(var_func,range(1,11)) : ',reduce(lambda x,y : x + y,map(var_func,range(2,11,2))))

from typing import Callable
def mul2(x : int) -> Callable[[int], int] :
    def inner(y : int) -> int:
        return y * x
    return inner
five2 = mul2(5)
print(five2(10))
print('##########')


## callable : 호출 연산자 -> 메서드 형태로 호출 가능한지 확인
### __call__ 이 있으면 callable
### 행동을 값처럼 다룰 수 있느냐
print('callable(var_func) : ',callable(var_func))
print('callable(A) : ',callable(A))
print('callable(list) : ',callable(list))
print('callable(3.14) : ',callable(3.14))
print('callable(mul2) : ',callable(mul2))
print('##########')

## partial : 인수 고정 -> 콜백 함수에 사용
from operator import mul
from functools import partial

print(mul(5,10))
five = partial(mul,5)
print(five(10))

# from typing import Callable
# def mul2(x : int) -> Callable[[int], int] :
#     def inner(y : int) -> int:
#         return y * x
#     return inner
# five2 = mul2(5)
print(five2(10))
