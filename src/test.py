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
b = 2

if( a and b):
    print("a")
else:
    print("b")
if not(a and b):
    print("a")
else:
    print("b")
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
a = 2
if(a in list):
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
if (a is not b):
    print("bushi")
else:
    print("shi")

if (a == b):
    print("shi")
else:
    print("bushi")

d = [1, 2, 3]
e = d
print(e is d)
print(e == d)
e = d[:]
print(e is d)
print(e == d)
'''






























































