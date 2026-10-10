from dataclasses import dataclass

# @dataclass 는 아래와 같이 만들어 줌
# class Person:
#     def __init__(
#         self,
#         first_name: str,
#         last_name: str,
#         age: int | None = None,
#     ):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __repr__(self):
#         return (
#             f"Person(first_name={self.first_name!r}, "
#             f"last_name={self.last_name!r}, "
#             f"age={self.age!r})"
#         )
#
#     def __eq__(self, other):
#         if other.__class__ is not self.__class__:
#             return NotImplemented
#
#         return (
#             self.first_name == other.first_name
#             and self.last_name == other.last_name
#             and self.age == other.age
#         )

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int | None = None
    #
    # def __str__(self):
    #     return f"full_name: {self.full_name}, age: {self.age}"
    #
    # def __repr__(self):
    #     return f"full_name: {self.full_name}, age: {self.age}"
    #
    # def __eq__(self, other: object) -> bool:
    #     if not isinstance(other, Person):
    #         return NotImplemented
    #     return (
    #             self.first_name == other.first_name
    #             and self.last_name == other.last_name
    #             and self.age == other.age
    #     )

    @classmethod
    def from_dict(cls, dict: dict):
        return cls(dict['first_name'], dict['last_name'] ,dict.get('age'))

    @property
    def full_name(self):
        return f"{self.first_name}, {self.last_name}"
    #
    # @property
    # def age(self) -> int :
    #     return self._age
    #
    # @age.setter
    # def age(self, value: int | None) :
    #     if value is None:
    #         self._age = None
    #     else:
    #         if value < 0  :
    #             raise ValueError(f"age 가 음수일 수 없습니다.")
    #         self._age = value

if __name__ == '__main__':
    # person1 = Person.from_dict({'first_name': 'John', 'last_name': 'Doe','age': -42})
    # print(person1)
    # print(repr(person1))
    # print(person1.__str__())
    print(Person("John", "Doe"))
    # dataclass 가 property 객체 자체를 self.age 에 넣어버리면서 setter 를 호출함. 그래서 property 객체를 뺴줘야함
