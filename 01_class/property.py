class Person:
    def __init__(self, first_name: str, last_name: str, age: int | None = None):
        if not isinstance(first_name, str):
            raise TypeError("first_name은 문자열이어야 합니다")
        if not isinstance(last_name, str):
            raise TypeError("last_name은 문자열이어야 합니다")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"full_name: {self.full_name}, age: {self.age}"

    def __repr__(self):
        return f"full_name: {self.full_name}, age: {self.age}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return (
                self.first_name == other.first_name
                and self.last_name == other.last_name
                and self.age == other.age
        )

    @classmethod
    def from_dict(cls, dict: dict):
        return cls(dict['first_name'], dict['last_name'] ,dict['age'])

    @property
    def full_name(self):
        return f"{self.first_name}, {self.last_name}"

    @property
    def age(self) -> int :
        return self._age

    @age.setter
    def age(self, value: int | None) :
        if value is None:
            self._age = None
        else:
            if value < 0  :
                raise ValueError(f"age 가 음수일 수 없습니다.")
            self._age = value

if __name__ == '__main__':
    person1 = Person('jungmo', 'bae',10)
    person2 = Person('jungmo', 'bae',10)
    print(person1)
    print(person1.full_name)
    print(person1.age)
    print(person1 is person2)
    print(person1 == person2)