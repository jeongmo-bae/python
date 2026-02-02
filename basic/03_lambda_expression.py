# 메모리 절약, 가독성 향상, 코드 간결 -> 과연 좋은가?
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화

def mul_func(x,y):
    return x*y

mul_lambda = lambda x, y: x * y

print(mul_func(10,50))
mul_func_var = mul_func
print(mul_func_var(10,50))

print(mul_lambda(10,50))

print('')

def func_final(a,b,func):
    print(f'a * b * func(a,b) : {a*b*func(a,b)}')


func_final(10,20,mul_func)
func_final(10,20,mul_func_var)
func_final(10,20,mul_lambda)

