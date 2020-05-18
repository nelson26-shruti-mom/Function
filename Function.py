
def minus_new(a, b):
    return a-b
c= minus_new(-3, 100)
print(c)


def gr8(d,a):
    return d > a
f=gr8(5, 10)
print(f)
f1=gr8(101.1, 101)
print(f1)


a= 100
def add_n(b,c):
    return b+c
p=add_n(10, 10)
print(p)



def total(arg1, arg2):
    total = arg1+arg2
    return total
sum = total(20, 30)
print('Total is =' , sum )


a=50
def tot(arg1):
    b= 100
    sum= a+b+arg1
    return sum
ans= tot(30)
print("total ans",ans)


def info(name, age=23):
    print('Name =', name)
    print('Age =', age)
    return
info(name= "nelson", age= 29)
#info(age = 60, name = 'dad')
info(name='shruti')
#info(name)


def var_s(user, *users):
     #print("User of python")
     print(user)
     for var in users:
         #print("Users of python")
         print(var)
         return

var_s("Nelson")
var_s(10,20,30)       #dout = why dady is not printing
