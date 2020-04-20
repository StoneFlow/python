# 逻辑运算符号
'''
def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output

if __name__ == "__main__":
    input = 'You like me ni mei shi ba'
    rw = reverseWords(input)
    print(rw)
'''
'''
student = ['Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose']
print(student)
if 'Rose' in student:
    print('Rose you')
else:
    print('Rose wu')
'''
'''
a = set('abcdefg')
b = set('abcdhij')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
'''

'''
dict1 = {}
dict1['noe'] = 1
dict1[2] = 2
tindict = {'name':'runoob', 'code':1, 'site':'nihao'}
print(dict1['noe'])
print(dict1[2])
print(tindict)
print(tindict.keys())
print(tindict.values())
print(dict1)
'''
'''
a = 2
b = 3
d = 4
print("d is %d and %d" % (d, b))
'''


'''
2进制的
a = 60
b = 13
c = 0

c = a & b
print("1 - c de zhi:", c)
相交
c = a | b 
print('2 - c de zhi:', c)
全部
c = a ^ b
print('3 - c de zhi:', c)
去除相交的值，留剩下的
c = ~a
print('4 - c de zhi:', c)
取a的返值，00110011 = 11001100
c = a << 2
print("5 - c de zhi:", c)
往左补二进制，
c = a >> 2
print("6 - c de zhi wei:", c)
往右补二进制
'''
'''
a = 1
b = 0
if( a and b):
    print("a")
else:
    print("b")
if a or b:
    print('a')
else:
    print('b')
'''
'''
a = 10 
b = 20 
list = [1, 2, 3, 4, 5, 6]

if(a in list):
    print("zai")
else:
    print("buzai")
if(b not in list):
    print("shi de bu zai")
else:
    print("bushi, zaide ")
b = 2
if(b in list):
    print("zai")
else:
    print("buzai")
'''
'''
a = 20
b = 20 
if (a is b):
    print("shi")
else:
    print("bushi")

b = 30
if (id(a) == id(b)):
    print("shi")
else:
    print("bushi")
if (a is b):
    print("shi")
else:
    print("bushi")

if (a == b):
    print("shi")
else:
    print("bushi")
'''
'''
e = d = [1, 2, 3]
print(e is d)
print(e == d)
e = d[:]
print(e is d)
print(e == d)
'''
'''
A = []
for i in range(101):
    A.append(i)
print(A)

for i in A:
    if i % 2 == 0:
        A.remove(i)
print(A) 
'''


'''
for letter in 'Python':
    print ('dang',letter)

fruits = ['fefefe', 'appp', 'meee']
for fruits in fruits:
    print("dang",fruits)

'''
'''
q = []
for i in range(100):
    q.append(i)
print(q)

for o in q:
    if o % 2 == 0:
        print(o)
'''
'''
w = [100,1, 2,34,5,6,7,3]
for index in range(len(w)):
    print('d', index, w[index])
'''    

'''
# 确定选择功能界面，显示余额 存款 取款
def sel_func():
    print("yue")
    print("cunkuan")
    print("qu kuan")


#1，搭建整体框架
'''
'''
输入密码后显示功能，查询余额后显示功能，取完钱后显示功能
print('qing shu ru')
#显示“选择功能”界面
sel_func()
print('wanbi')
#显示“选择功能”界面
sel_func()
print("qu le")
#显示“选择功能”界面
sel_func()
'''

'''
def info_print():
    print("hello world\n")

info_print()
'''


'''
def add_num1(x, y):
    result = x + y
    c = x * y
    w = x / y
    f = x % y
    e = x // y
    print(result, c, '%0.2f' %w, f, e)

a = 4
b = 3

add_num1(a, b)
'''

'''
def buy(c):
    return c

a = 20
print(buy(a))
'''
'''
def sum_num1(x, y):
    return x + y

a = 20 
b = 39
print(sum_num1(a, b))
'''
'''
def sum_num1():
    """nihao"""
    return a + b

help(sum_sum1)
'''

'''
def sum_num1(a, b):
    ''''''
    return a + b
'''
'''
def a():
    print("a")
def b():
    print("b")
    a()
    print("b")
    return 0

b()
'''

'''
def print_line():
    print('-' * 20)
def print_linec(x):
    i = 0
    while i < x:
        print_line()
        i += 1
a = input('xingyunshu')
a = int(a)
print_linec(a)
'''
'''
def b():
    i = 0
    while i < 5:
        print(print_line())
        i += 1
b()
'''

'''
a = 100
print(a)
def w():
    print(a)

def e():
    global a
    a = 200
    print(a)

w()
e()
print(a)
'''
'''
def and1(x, y):
    if x and y:
        return x
    else:
        return y

def or1(x, y):
    if x or y:
        return x
    else:
        return y
a = 0
b = 2
print(and1(a, b))
print(or1(a, b))
'''



'''
a = [1,3,45,6,78,9,43,6,2,345]
b = 15
c = 52
d = 2
if b in a:
    print('zai')
else:
    print('buzai')
if c in a:
    print('zai')
else:
    print('buzai')
if d not in a:
    print('bushi')
else:
    print('zai')
'''
'''
glo_num = 0

def test1():
    global glo_num
    glo_num = 100
def test2():
    print(glo_num)

test1()
test2()
'''
'''
def test1():
    return 39
def test2(x):
    print(x)


test2(test1()) 
'''

'''
def return_num(x, y):
    return {x, y}

a = 2
b = 45
print(return_num(a, b))
'''
'''
def user_info(name, age, sex):
    print(f'xingming:{name}, nianlingshi{age},xingbieshi{sex}')

user_info('gou', 21, 'nan')
'''

'''
def user_info(name, age, sex):
    print(f'name:{name}, age:{age}, sex:{sex}')


user_info(age = 23, sex ='boy', name ='gl')
'''
'''
def user_info(name, age, sex = 'boy'):
    print(f'name:{name}, age:{age}, sex:{sex}')

user_info('tmo', 23)
user_info('we', 23, 'nv')
'''
'''
def user_info(*args):
    print(args)
user_info('tom')
user_info('tom', 12)

user_info()
'''
'''
def user_info(**kwargs):
    print(kwargs)

user_info()
user_info(name = 'eig', dsj = 'ja')
'''


'''
def return_num():
    return 100, 200, 434
num, num1, num2 = return_num()
print(num, num1, num2)
'''
'''
te = {'name': 'tom', 'age': 32}
w, r = te
print(w, r)
print(te[w])
print(te[r])
'''
'''
def i(x, y):
    o = 0
    o = x
    x = y
    y = o
    return x, y
a = 20
b = 30
print(i(a, b))
'''
'''
a, b = 1, 2
a, b =b, a
print(a, b)
'''
'''
a = [1]
b = a
print(id(a))
print(id(b))
if b is a[:]:
    print('shi')
else:
    print('bushi')
if b == a:
    print('deng')
else:
    pritn('bu')
'''

'''
a = 1
print(id(a))

a = 2

b = a
print(b)
'''
'''
aa = [10, 20]
bb = aa
print(bb)
print(id(bb))
print(id(aa))
aa.append(30)
print(id(aa))
print(id(bb))
'''
'''
def num1(x):
    print(x)
    print(id(x))
    x += x
    print(x)
    print(id(x))


a = [100,23]
num1(a)
'''
'''
mylist = [1, 2, 3, 4, 5]

def func(obj):
    print('func:', obj)
    def func1():
        obj[0] += 1
        print('func1:',obj)
    return func1
var = func(mylist)
var()
var()
var()
'''
'''
def func1(func):
    def func2():
        print('aaabbb')
        return func()
    return func2
@func1  #@func1(myprint)()
def myprint():
    print("hello,I am print")
myprint()
'''

'''
def arg_func(sex):
    def func1(b_func):
        def func2():
            if sex == "man":
                print('no')
            else:
                print('ke')
            return b_func()
        return func2
    return func1

@arg_func(sex = 'man')
def man():
    print('shangban')

@arg_func(sex = 'woman')
def woman():
    print('shengwa')

man()
woman()
'''

'''
def func(func1):
    def func2(x, y):
        print(x, y)
        x += 5
        y += 5
        return func1(x, y)
    return func2

@func
def sum(a, b):
    print(a + b)

sum(1, 5)
'''


'''
def fun():
    def fun1():
        print('I am inner')
    return fun1
    
f = fun()
f()
'''
'''
def counter():
    x = 0
    def counter1():
        nonlocal x
        x += 1
        return x
    return counter1


y = counter()
print(y())
print(y())
print(y())
print(y())

n = counter()
print(n())
'''
'''
                        3.27     
'''
'''
class Cat:
    # 属性

    #当创建完一个对象后，立马会自动调用
    def __init__(self,newColor,newWeigh,newWeiba):
        self.color = newColor
        self.weight = newWeigh
        self.weiba = newWeiba
        print("hahahahahahah")
    # 方法
    def eat(self,):
        print("----chi----")
    def drink(self):
        print("----he----")
    def la(self):
        print("----la----")
    def sa(self):
        print("----sa----")
    def sleep(self, a, b):
        print("----sleep----%d%d"%(a,b))
    def printInfo(self):
        print(self.weiba)


#创建一个 猫 对象
xiaohuamao = Cat("red", 5, "have")
xiaohuamao.eat()
xiaohuamao.drink()
xiaohuamao.la()
xiaohuamao.sa()
xiaohuamao.sleep(11, 32)
xiaohuamao.on(12, 23, 53)
#给xiaohuamao对象添加属性
xiaohuamao.color = "red"
xiaohuamao.weight = 5 #kg
xiaohuamao.weiba = 20 #cm
#获取xiaohuamao对象的数据
a = xiaohuamao.color
print(a)
print(xiaohuamao.weight)

print(xiaohuamao.high)
xiaohuamao.printInfo()
w = Cat()
w.drink()
'''

'''
class Cat:
    

    def __init__(self):
        self.wheelNum = 4
        self.color = 'blue'
    def move(self):
        print('cat run  xiaweiyi')

BMW = Cat()
print(BMW.wheelNum)
print(BMW.color)
'''

'''
def scope_test():
    def do_local():
        spam = "local spam"
    def do_global():
        global spam
        spam = "global spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    spam = "test spam"
    do_nonlocal()
    print(spam)
    do_local()
    print(spam)
    do_global()
    print(spam)
    
scope_test()
print(spam)
'''
'''
class MyClass:
    i = 13224
    def f(self):
        return "hello world"
w = MyClass()
print(w.i)
print(w.f())
'''
'''
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)
'''
'''
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in[B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
'''    
'''
s = 'abc'
it = iter(s)
next(it)
next(it)
print(next(it))
'''
'''
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one': 1, 'two': 2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line,end = '')
'''
'''
def reverse(data):
    for index in range(len(data)):
        yield data[index]
    for char in reverse('golf'):
        print(char)



print(reverse('nih'))
'''
'''
for element in [1, 2, 3]:
        print(element)
'''
'''
class Cat:
    def __init__(self, chang):
        self.chang = chang
    def san(self, d, h):
        self.chang = d*h/2
        print(self.chang)
    def zheng(self, b):
        self.chang = b*b
        print(self.chang)

w = Cat(0)
w.san(5, 4)
w.zheng(8)
'''
'''
class vector2:
    global x, y
    x = 1
    y = 2
class vector3(vector2):
    global z
    z = 3
v = vector3()
print(x, y, z)
'''
'''
class Fu:
    def myMethod(self):
        print('diaoyong')
class Child(Fu):
    def myMethod(self):
        super().myMethod()
        print('zilei')
c = Child()
c.myMethod()
super(Child, c).myMethod()
'''
'''
class People:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s %d " %(self.name, self.age))
class Student(People):
    grade = ''
    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g
    def speak(self):
        print("%s %d %d"%(self.name, self.age, self.grade))

s = Student("ken", 10, 60, 3)
s.speak()
'''
'''
class Vector2:
    x = 1
    y = 2
    print(x, y)
class Vector3(Vector2):
    z = 3
    print(z)
Vector3()
'''
'''
class A:
    def __init__(self):
        print("A")
class B(A):
    pass
class C(A):
    def __init__(self):
        print("C")
A()
B()
C()
'''
'''
class A:
    def __init__(self):
        print('A')
class B(A):
    def __init__(self):
        super().__init__()
        print("B")
B()
'''

'''
class Player():
    def __init__(self, name):
        self.name = name
    def say(self):
        print("helo",self.name.title())

    def intro(self):
        print("I am player.")
class MyPlayer(Player):
    def __init__(self,name):
        super().__init__(name)
        print(self.name)
        self.category = name
    
    def intro(self):
        print("I am "+ self.category+"palyer.")

print("----------------------")
curry = Player("curry")
curry.say()
curry.intro()
daxia = MyPlayer('nihao')
daxia.__init__('wo')
daxia.intro()
'''
'''
class Area:
    def __init__(self):
        pass
        
class Triangle(Area):
    def __init__(self, x, y):
        self.bottom = x
        self.high = y
    def CountArea(self):
        self.area = self.bottom * self.high / 2
        return self.area

class Square(Area):
    def __init__(self, b):
        self.SideLength = b
    def CountArea(self):
        self.area = self.SideLength * self.SideLength
        return self.area

w = Triangle(5, 3)
w.CountArea()
q = Square(5)
q.CountArea()
'''
'''
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def personInfo(self):
        print(f"name:{self.name} age:{self.age} sex:{self.sex}")

class Student(Person):
    def __init__(self, name, age, sex, college, class1):
        super().__init__(name, age, sex)
        self.college = college
        self.class1 = class1
    def personInfo(self):
        print(f"name:{self.name} age:{self.age} sex:{self.sex} college:{self.college} class1:{self.class1}")
    def learn(self, Teacher):
        print("老师%s，我终于学会了！" %Teacher.teachOBJ())
    def addStudent(self):
        coutent = {}
        couten['name'] = self.name
        couten['age'] = self.name
        couten['sex'] = self.name
        couten['college'] = self.name
        couten['class1'] = self.name
        couten.append(coutent)
    def show_all():
        for dict in student:
            for key in dict.keys():
                if key == 'name':
                    print('name:'+dict[key])
                if key == 'age':
                    print('age'+dict[key])
                if key == 'sex':
                    print('sex:'+dict[key])
                if key == 'college':
                    print('college'+dict[key])
                if key == 'class1':
                    print('college'+dict[key])
            print('*'*50)
    def __str__(self):
        return Student.personInfo()

class Teacher(Person):
    def __init__(self, name, age, sex, college, professional):
        super().__init__(name, age, sex)
        self.college = college 
        self.professional = professional
    def personInfo(self):  
        print(f"name:{self.name} age:{self.age} sex:{self.sex} college:{self.college} professional{self.professional}")
    def teachOBJ(self):
        return "今天讲了如何面向对象设计程序"

xiaoming = Student("xiaoming", 20, "boy", "ruanjian", 100)
xiaozhang = Student("xiaohong", 20, "boy", "ruanjian", 100)
xiaozhang = Student("xiaozhang", 20, "boy", "ruanjian", 100)
xiaoming.personInfo()
laoshi = Teacher("zhang", 29, "man", "ruanjian", "hongxing")
laoshi.personInfo()
'''
'''
import sys
print('-----')
for i in sys.argv:
    print(i)

print('\n\nPython lujinwei:', sys.path,)
'''
'''
def print_func(par):
    print("Hello:", par)
    return

import support

support.print_func("nihao")
'''
'''
import sys
print(sys.path)
'''



'''
import support
support.print_func("nihao")
import sys
print(sys.path)
'''
'''
import fibo
fibo.fib(1000)
print(fibo.fib2(100))

print(fibo.__name__)
fib = fibo.fib
fib(200)
'''
'''
from fibo import fib, fib2
print(fib2(500))
'''
'''
from fibo import *
fib(233)
print(fib2(500))
'''
'''
import name
'''
'''
import fibo, sys
print(dir(fibo))
print(dir(sys))
'''
'''
a = [1,2,3,4,5]
import fibo
print(dir())
a = 5
dir()
'''
'''
import name
'''

'''
my_file = open("ni.txt")
print(my_file.read())
'''
'''
w = open("ni.txt")
print(w.read())
print('*'*20)
print(w.read())
e = open("name.py")
print(e.read())
print(w.closed)
w.close()
print(w.closed)
e.close()
w = open("ni.txt")
print(w.read())
'''
'''
my_file = open("ni.txt")
print(my_file.read())
my_file.seek(0)
print(my_file.readlines())
my_file.close()
'''
'''
my_file = open("ni.txt",'w')
my_file.write("hahaha")
my_file.close()
my_file = open("ni.txt",'w')
my_file.write("sigou")
my_file.close()
'''
'''
my_file = open("ni.txt","a")
my_file.write("\nADD content")
my_file.close()
my_file = open("ni.txt","r")
print(my_file.read())
'''
'''
my_file = open("New_file.txt","w")
my_file.write("add")
my_file.close()
'''
'''
my_file = open("ni.txt","r+")
my_file.write("HIasdfghjkasdfghjkasdfghjkasdfghjk")
my_file.close()
'''
'''
with open("ni.txt","a") as my_file:
    my_file.write("Add other content")
'''
'''
my_file = open("ni.txt")
print(my_file.read())
my_file.seek(0)
print(my_file.readlines())
'''
'''
my_file = open("ni1.txt","x")
'''
'''
import name
from name import *
'''
'''
my_file = open("ni1.txt","r")
print(my_file.read())
my_file.close()
''''''
my_file = open("ni1.txt","w")
my_file.write("nihaoya")
my_file.close()
'''
'''
my_file = open("ni1.txt","r+")
my_file.write("ni")
print(my_file.read())
my_file.close()
'''
'''
import os
import sys

os.chdir('E:/')
result = os.getcwd()
print(result)
open("ni1.txt","w")
'''
'''
import os
result = os.listdir('f:/python/src')
print(result)
'''
'''
import os 
result = os.listdir('c:/')
print(result)
'''

'''
os.mkdir("f:/nihao",0o777)
'''

import os
'''
result = os.makedirs('f:/a/b/c')
'''
'''
os.rmdir('f:/a/b')
'''
'''
os.removedirs('f:/a/b')
'''
'''
os.rename("f:/www","f:/qqq")
'''
'''
result  = os.stat('f:/qqq')
print(result)
'''
'''
os.system('ping www.baidu.com')
'''
'''
result = os.getenv('path')
print(result)
allpath = result.split(';')
print(allpath)
'''
'''
os.putenv('path','f:/a/b/c')

result = os.getenv('path')
print(result)
'''
'''
os.environ['path'] += 'F:/abc/xyz'
print(os.environ['path'])
'''
'''
print(os.environ['path'])
'''
'''
print(os.curdir)
print(os.pardir)
print(os.path)
print(os.name)
'''
'''
print(os.sep)
print(os.extsep)
print(repr(os.linesep))
'''
'''
open('xd1.txt','w')
open('./xd2.txt','w')
open('../../xd3.txt','w')
'''
'''
path1 = '../../123.txt'
print(os.path.abspath(path1))
'''
'''
path1 = 'c:/window/system32/abc.txt'
result = os.path.basename(path1)
print(result)

result2 = os.path.dirname(path1)
print(result2)
'''
'''
path1 = 'c:\\window\\abc'
path2 = 'xyz\\123.txt'
result = os.path.join(path1,path2)
print(result)
'''
'''
path1 = 'D:/a/b/c/d/xyz.exe'
result = os.path.split(path1)
print(result)
'''
'''
path1 = 'D:/a/b/c/d/123.jgb'
result = os.path.splitext(path1)
print(result)
'''
'''
path1 = 'D:/python/NEWS.txt'
result = os.path.getsize(path1)
print(result)
'''
'''
path1 = 'C:/windows'
result = os.path.isdir(path1)
print(result)
'''
'''
path = 'E:/ni1.txt'
result = os.path.isfile(path)
print(result)
'''
'''
path = 'e:/ni1.txt'
result = os.path.getmtime(path)
print(result)
'''
'''
path = 'c:/123.jpg'
result = os.path.isabs(path)
print(result)
'''
'''
path1 = './bao.py'
path2 = 'f:/python/src/bao.py'
result = os.path.samefile(path1,path2)
print(result)
'''
'''
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
'''
'''
a = set('asdfghjkl')
b = set('asdfghbnm')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)
'''

'''
dict1 = {'name': 3, 'sex': 5}
print(dict1)
print(dict1.keys())
print(dict1.values())
'''
'''
var1 = 100
if var1:
    print("1 - if ")
    print(var1)
var2 = 0
if var2:
    print("2 - if")
    print(var2)
    print("Good bye")
else:
    print("No")
'''
'''
import bao
'''
'''
print(4 == 2)
x = 5
y = 8
print(x == y)
'''
'''
count = 0
while count < 5:
    print(count,'5')
    count += 1
else:
    print(count,'5')
'''
'''
wo = []
for i in range(100):
    if i %2 == 0 :
        if i %3 == 0:
            wo.append(i)
print(wo)
'''
'''
w = []
for i in range(10):
    w.append(i)
print(w)
'''
'''
for letter in 'runoob':
    if letter == 'o':
        break

    print(letter)

var = 10
while var > 0:
    print(var)
    var = var -1
    if var == 5:
        break
print('bye')
'''
'''
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0 :
            print(n,'deng',x,'*',n)
            break
        else:
            print(n,'shi')
            break
'''
'''
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('zhixing pass kuai')
    print(letter)
print('Good bye')
'''
'''
class nihao:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = nihao()
myiter = iter(myclass)

for x in myiter:
    print(x)
'''
'''
import sys
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)

while True:
    try:
        print(next(f),end = ' ')
    except StopIteration:
        sys.exit()
'''
'''
def c(a):
    a = 10
    return a
b = 2 
print(c(b))
print(b)
'''
'''
def c(mylist):
    mylist.append([1,2,3,4])
    print(mylist)
    return
mylist = [10,20,30]
c(mylist)
print(mylist)
'''
'''
def f( *sex):
    print(sex)

def z(**dict1):
    print(dict1)
z(a=2,b=3)
'''
'''
def f(a,b,*,c):
    return a + b + c
print(f(1,2,c=3))
'''
'''
result = lambda x: x * x
print(result(5))
'''
'''
def Foo(x):
    if (x==1):
        return x
    else:
        return x * Foo(x-1)

print(Foo(100))
'''
'''
import name
import bao
import support
support.print2(3)
'''
'''
from fibo import fib, fib2
fib(1000)
print(fib2(200))
'''
'''
a = [1,2,3,4,5]
import fibo
fib = fibo.fib
print(dir())
del a
print(dir())
'''
'''
w = open('ni.txt')
print(w.read())
'''
'''
w = open('meishi.txt','x')
w.close()
'''
'''
w = open('meih.txt','a+')
w.write('\nnidkjalj')
w.closed
'''
'''
w = open('meih.txt','a+')
w.write('nihaoya')
'''
'''
print(os.stat('f:/python'))
'''
'''
w = os.path.basename('./ni1.txt')
e = os.path.dirname('../../python/ni.txt')
print(os.path.join(e, w))
print(os.path.split('f:/python/src/name.py'))
'''
'''
x = input('')
if x == 1:
    class de:
        def i(self):
            print('ni')
        def u(self):
            print('hao')
    w = de()
    w.i()
    w.u()
else:
    class w:
        def w(self):
            print('buhao')
        def q(self):
            print('henbuhao')
    i = w()
    i.w()
    i.q()
'''
'''
class fu:
    name = ''
    age = 0
    sex = ''
    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.sex = s
    def speak(self):
        print('%s %d'%(self.name, self.age))
class er(fu):
    grade = ''
    def __init__(self,n,a,s,e):
        fu.__init__(self,n,a,s)
        self.grade = e
    def speak1(self):
        print('%s %d %s %s'%(self.name,self.age,self.sex,self.grade))

w = er(1,2,3,4)
w.speak1()
'''
'''
class fu:
    def __init__(self):
        name = '1'
        print(name)
w = fu()
'''
'''
class Parent:
    def myMethod(self):
        print('fu')
class Child(Parent):
    def myMethod(self):
        print('zi')
w = Child()
w.myMethod()
super(Child,w).myMethod()
'''
'''
class j:
    __secretCount = 0
    publicCout = 0

    def count(self):
        self.__secretCount += 1
        self.publicCout += 1
        print(self.publicCout)

counter = j()
counter.count()
counter.count()
print(counter.publicCout)
print(counter.__secretCount)
'''
'''
class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name :', self.name)
        print('url :', self.__url)

    def __foo(self):
        print('si')
    
    def foo(self):
        print('gong')
        self.__foo()

x = Site('cai','www.runoob.com')
x.who()
x.foo()
x.__foo()
'''
'''
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return 'Vector(%d, %d)' %(self.a, self.b)

    def __add__(self, other,other):
        return Vector(self.a + other.a , self.b + other.b)

v1 = Vector(2,3)
v2 = Vector(33,22)
print(v1 + v2)
'''

w = r'\thabit'
print(w[2])






































































































