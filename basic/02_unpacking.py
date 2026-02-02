# unpacking
## *args
def args_func(*args):
    for i, v in enumerate(args):
        print(f'{i}: {v}')
        print('============')

args_func(1,2,3,(4,5),[1,2,3])

print('')
## **kwargs
def kwargs_func(**kwargs):
    print(kwargs.items())
    for k, v in kwargs.items():
        print(f'{k}: {v}')
        print('==========')

kwargs_func(name1='bae',name2='bye',name3='bye2',sendSMS=True)
print('')

## mix
def example(arg1,arg2,*args,**kwargs):
    print(arg1,arg2,args,kwargs)

example(1,2,3,4,5,6,7,8,9,10,arg_1=10,arg_2=20)
print('')
