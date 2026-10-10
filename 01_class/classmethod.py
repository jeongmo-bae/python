class Person:

    min_name_length = 4

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def foo(cls):
        print('foo')

    @classmethod
    def from_dict(cls, data: dict):
        return cls(name=data["name"], age=data["age"])

    @classmethod
    def is_valid_name(cls,name):
        return len(name) > cls.min_name_length

    # print - __str__ 없으면 __repr
    def __str__(self):
        return f'str__ {self.name}, {self.age}'
    # 객체 표현
    def __repr__(self):
        return f'repr__ {self.name}, {self.age}'

class User(Person):
    min_name_length = 1
    # def __init__(self, name: str, age: int):
    #     super().__init__(name, age)

if __name__ == "__main__" :
    person1 = Person('John', 18)
    person2 = Person('Jane', 22)

    person1.foo()
    Person.foo()

    print(person1 is person2)
    person3 = Person.from_dict({"name": "민수", "age": 20})
    print(person3)

    user1 = User.from_dict({"name":"jm","age":32})
    print(user1)
    user1.foo()
    print(user1.is_valid_name(user1.name))
