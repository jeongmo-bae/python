from datetime import date, datetime

from pydantic import BaseModel, ValidationError, Field, field_validator, model_validator, computed_field, ConfigDict, \
    ValidationInfo


class Person(BaseModel):
    model_config = ConfigDict(extra="ignore",validate_assignment=True,)
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    # age: int | None = Field(None,ge=0,le=150) # 이젠 입력받지 않고 직접 처리한다 가정
    birth: date = Field(date(1995, 10, 24),ge=date(1995, 10, 24))
    death: date | None = Field(None)
    tags: list[str] = Field([], min_length=0, max_length=100)

    @field_validator("first_name", "last_name")
    @classmethod
    def name_validator(cls, value: str, info: ValidationInfo) -> str:
        value = value.strip()
        if not value:
            raise ValueError(f"{info.field_name} 은 빈 문자열일 수 없습니다.")
        return value

    @field_validator("birth", "death", mode="before")
    @classmethod
    def parse_compact_date(cls, value: str | date | None, info: ValidationInfo) -> str | date | None:
        if isinstance(value, str) and len(value) == 8 and value.isdigit():
            try:
                return datetime.strptime(value, "%Y%m%d").date()
            except ValueError as e:
                raise ValueError(f"{info.field_name} 는 유효한 YYYYMMDD 형식이어야 합니다") from e
        return value

    @model_validator(mode="after")
    def check_dates(self):
        if self.death and self.death < self.birth:
            raise ValueError("death 가 birth 보다 과거일 수 없음.")
        return self

    @computed_field
    @property
    def age(self) -> int:
        end_date = self.death or date.today()
        age = end_date.year - self.birth.year
        if (end_date.month, end_date.day) < (self.birth.month, self.birth.day):
            age -= 1
        return age

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


if __name__ == '__main__':
    # region person1
    person1 = Person(first_name="John", last_name="Doe")
    print(person1.age)  # None
    # endregion

    # region 필수 필드와 선택 필드
    print("")
    try:
        Person(first_name="John")
    except ValidationError as e:
        print("catch ValidationError")
        # print(type(e))
        # print(e.errors)
        # print(e)

    except Exception as e:
        print("catch Exception")
        print(type(e))
        print(e.errors)
        print(e)
        raise e
        """
        1 validation error for Person
        last_name
          Field required [type=missing, input_value={'first_name': 'John'}, input_type=dict]
            For further information visit https://errors.pydantic.dev/2.14/v/missing
        """
    # endregion

    # region 값 검증 & 변환
    print("")
    person2 = Person(first_name="John", last_name="Doe", age="32")

    print(type(person2.age))  # <class 'int'>
    try:
        Person(first_name="John", last_name="Doe",
               age="서른둘")  # pydantic_core._pydantic_core.ValidationError: 1 validation error for Person
    except ValidationError as e:
        print(e)
    # endregion

    # region Field
    print("")
    person2 = Person(first_name="John", last_name="Doe", age="32")
    print(person2)  # first_name='John' last_name='Doe' age=32
    # endregion

    # region field_validator
    print("")
    try:
        print(Person(first_name="jj  jj    ", last_name="Doe", age="32").first_name)
        print(Person(first_name="    ", last_name="Doe", age="32").first_name)

    except ValueError as e:
        print(e)
    # endregion

    # region model validator
    print("")

    # endregion

    # region computed_field & model_dump()
    print("")
    person3 = Person(first_name="John", last_name="Doe", age="32")
    person4 = Person.from_dict({'first_name': 'John', 'last_name': 'Doe', 'age': 32, 'tags': ['python', 'django']})
    print(person3.model_dump())
    print(person4.model_dump())
    # endregion

    print("")
    person5 = Person(
        first_name="Jungmo",
        last_name="Bae",
        birth="1995-10-24",
    )
    print(person5.model_dump())
    print(person5.birth)

    print("")
    # person5.birth = date.fromisoformat("1994-10-24")
    person5.birth = "19961024"
    print(person5.model_dump())
    print(person5.age)
