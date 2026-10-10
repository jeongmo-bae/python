class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # print - __str__ 없으면 __repr
    def __str__(self):
        return f'str__ {self.name}, {self.age}'

    # 객체 표현
    def __repr__(self):
        return f'repr__ {self.name}, {self.age}'


if __name__ == "__main__" :

    person1 = Person('bae', 18)

    print(person1)
    print(person1.__dict__)

    print(repr(person1))


    print( [person1] ) # [repr__bae, 18]


