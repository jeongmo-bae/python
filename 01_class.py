class Car:
    """
    Car Class
    Author : Bae
    Date : 2026.01.30
    """
    def __init__(self ,company, details):
        self._company = company
        self._details = details
    # 일반 print 결과
    def __str__(self):
        return f'str : {str(self._company)} - {self._details}'
    # 객체 정보(?)
    def __repr__(self):
        return f'repr : {str(self._company)} - {self._details}'

    def __eq__(self, other):
        return self._company == other._company and self._details == other._details

    def detail_info(self):
        print(f'Current ID  : {id(self)}')
        print(f'Car Detail Info : {self._company} {self._details.get("price")}')


car1 = Car('Ferrari',{'color' : 'white', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw',{'color' : 'black', 'horsepower' : 400, 'price' : 8000})
car3 = Car('Audi',{'color' : 'silver', 'horsepower' : 400, 'price' : 8000})
print(car1)
print(repr(car1))
print(car1.__dict__)

# dir & __dict__
print('dir(car1) : {}'.format(dir(car1)))
print(car1.__dict__)

# Docstring
print(f'Car.__doc__ : {Car.__doc__}')

print('')
car1.detail_info()
car2.detail_info()
Car.detail_info(car1)
