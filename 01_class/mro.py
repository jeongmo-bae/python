class A :

    def __init__(self,x : int):
        print("A")
        self.x = x + 1
        print(f"self.x: {self.x}")

    @classmethod
    def foo(cls):
        print(f"foo {cls}")

    def __str__(self):
        return f'str__ - {self.x}'

    def print_x(self):
        print(f'print_x: {self.x}')



class B(A) :
    def __init__(self,x : int):
        super().__init__(x)
        print("B")
        self.x = x + 2
        print(f"self.x: {self.x}")



class C(A):
    def __init__(self,x : int):
        super().__init__(x)
        print("C")
        self.x = x + 3
        print(f"self.x: {self.x}")

class D(B,C):
    def __init__(self,x : int):
        print("D")
        super().__init__(x)


d = D(1)
d.print_x() # print_x: 3
print(D.__mro__)