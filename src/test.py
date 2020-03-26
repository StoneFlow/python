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
a = 0
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
a = 1
b = 2
print(and1(a, b))
print(or1(a, b))
'''














































    























































