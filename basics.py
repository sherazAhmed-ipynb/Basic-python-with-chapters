# # ************************summary about chap 1**********************

#escape sequence
print("line A \nline B")

print(r"line A \nline B")

print(4/2) #float division
print(4//2) #integer divsion

# #************************summary about chap 2***********************
# #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Strings^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

name = "sheraz"

print(dir(name))

tell = name.isnumeric()
print(tell)

print(name.casefold())
print(name.upper())
print(name.title())

# # **************************summary about chap 3*********************
name = "sheraz"

if name == "sheraz":
    print(f"you are {name}")

for i in range(1,11):
    print(i)
for i in range(1,21,2):
    print(i)
    
# **************************summary about chap 4*********************

def find_greatest(num1,num2,num3):
    check_list = [num1,num2,num3]
    print(max(check_list))
    
print(find_greatest(23,2,4))

def greatest(a,b,c):
    if a>b and a>c:
        return print(f'{a} is greatest')
    
    elif b>a and b>c:
        return print(f'{b} is greatest')
    elif c>a and c>b:
        return print(f'{c} is greatest')

print(greatest(31,21,41))

# ****************************list chap 5********************************

words = ['word1','word2']

mixed = [1,2,3,[4,5,6],'seven',8.0,'nine']

mixed.append([10,11,12])

print(mixed)

mixed.extend([13,14,15])

print(mixed)
print(mixed.sort())

print(dir(mixed))

# ****************************tuple chap 6********************************

mixed = (1,2,3,4,5,6,7,8,'nine')

days = ('mon','thu','wen')

# ****************************dict chap 6********************************

dic1 = {
    'name': 'sheraz',
    'age' : 24
}
dic3 = dict(
    name = 'sheraz',
    age = 24
)

print(dic1['name'])

epmty_dict = {}

epmty_dict['key1'] = 'val 1'

for key, val in dic1.items():
    print(key,val)

keys = dic1.keys()
print(keys)

#use always get method to get key

print(dic1.get('names'))

# ****************************sets chap 7********************************

# unordered collection of unique items

sets = {1,2,3,2}
print(sets)

li = [1,3,1,41,1,24,24,1,4,7,7,7,7,6,7,8,87,6,4,3,21]

unique_list = list(set(li))
print(unique_list)

sets.add(4)
print(sets)

sets.remove(2)
print(sets)

# *****************************list comprehension************************

#simple list
sqaures = []
for i in range(1,11):
    sqaures.append(i**2)
print(sqaures)

sqaure2 = [i**2 for i in range(1,11)]
print(sqaure2)

sqa  = [-i for i in range(1,11)]
print(sqa)

names = ['saad','sheraz','ahmed']
# new_list = ['s','s','a']
new_list = [name[0] for name in names ]
print(new_list)

even_nums = [i for i in range(1,11) if i%2==0]
print(even_nums)


li = [[1,2,3],[1,2,3],[1,2,3]]
new_list2 = [[i for i in range(1,4)] for j in range(3)]


print(new_list2)
# *************************dictionary comprehension******************
square = {f"square of {num} is":num**2 for num in range(1,11)}
square = {num:num**2 for num in range(1,11)}
for key,value in square.items():
    print(f"Square of {key} is : {value}")

 
# ***************************sets comprehensions***********************
s = {key**2 for k in range(1,11)}
print(s)

# *****************************functions chap 11 summary***************************

def add(a,b):
    return a+b

def new_add(*args):
    total = 0
    for num in args:
        total += num
    return total
print(new_add(1,2,3))

li = [1,2,3,4]
print(new_add(*li))

# kwargs -> keyword arguments **

def func(**kwargs):
    print(kwargs)

func(name='sheraz', age = 25)

# if you want to use *args,**kwargs, normal parameter, default parameter
#PADK parameter,args,default, kwargs

def func2(name, *args,last_name = 'unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func2('sheraz',1,2,3,a= 1,b=2)

# ************************lambda exp or anonymous function*************

def add(a,b):
    return a+b

add2 = lambda a,b: a+b
print(add2(2,3))

print(add2)

even = lambda num: num % 2 == 0 

print(even(6))

func = lambda num : print("number is even") if num % 2==0 else print("number is odd")

func(5)

# **************************enumerate function***********************
#without enumerate func
names = ['sheraz','ahmed','asim','usman']

# pos = 0
# for name in names:
#     print(f'{pos}-------->{name}')
#     pos += 1 
    
# with enu
for pos, name in enumerate(names):
    print(f'{pos}-------->{name}')

# *****************************map function**************************

numbers = [1,2,3,4]

squares = list(map(lambda a:a**2,numbers))
print(squares)

squares2 = [num**2 for num in numbers]
print(squares2)

# # ******************************filterfunction**************************

def is_even(a):
    return a%2==0

numbers2 = [3,4,1,5,2,6,8,2,3,7,8,9,10]

evens = list(filter(is_even,numbers2))
print(evens)

evens2 = tuple(filter(lambda a:a%2==0, numbers2))
print(evens)

# *****************oop chap16*******************

# class and object(instance), meht

l = [1,2,3,4]
l.append(5)

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    

p1 = Person('sheraz','ahmed',24)
p2 = Person('Ali','waseem',22)

print(p1.first_name)
print(p2.last_name)

print(p1.full_name())

# ************************encapsulation,abstraction******************
#__init__ dunder/magic method
#__name (not a convension)

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price
    
    def make_a_cell(self,phone_number):
        print(f'calling{phone_number}.......')
    
    def full_name(self):
        return f'{self.brand} {self.model_name}'

phone1 = Phone('nokia','1100',100)
print(phone1.__dict__)

print(phone1._price)

# *****************************files******************************
f = open('text.txt')
print(f.read())
f.close()

# *****************************csv file ***************************

from csv import DictReader

with open('file.csv','r') as f:
    pass
    