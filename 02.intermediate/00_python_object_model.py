# __dict__
# attribute lookup
# __getattr__
# attribute assignment
# __setattr__
# shadowing

class A :
    x = 10
    def __init__(self):
        self._id = id(self)

    @classmethod
    def f(cls):
        cls.id = id(cls)

class B(A) :
    pass
print("--------")
print('A.__dict__ : ', A.__dict__)
# {
# '__module__': '__main__',
# 'x': 10,
# '__init__': <function A.__init__ at 0x100e28180>,
# 'f': <classmethod(<function A.f at 0x100edef20>)>,
# '__dict__': <attribute '__dict__' of 'A' objects>,
# '__weakref__': <attribute '__weakref__' of 'A' objects>,
# '__doc__': None
# }
a = A()
# a.f()
A.f()
B.f()
print("--------")
print('A.__dict__ : ', A.__dict__)
print(a.__dict__)
print(B.__dict__)
a.x = 20
print("--------")
A.f()
print(A.__dict__)
a.f()
b = B()
print("--------")
print(a.x)
print("A.__dict__['id'] : {}".format(A.__dict__['id']))
print("a.__dict__['_id'] : {}".format(a.__dict__['_id']))
print("B.__dict__['id'] : {}".format(B.__dict__['id']))
print("b.__dict__['_id'] : {}".format(b.__dict__['_id']))