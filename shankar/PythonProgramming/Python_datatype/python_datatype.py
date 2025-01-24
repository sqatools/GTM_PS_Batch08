"""
Types of Python data types.
1. Numbers
   i). Integer :  Immutable
   ii). Float : Immutable
   iii). Complex number  : Immutable

2. Sequential
   i). String : Immutable
   ii). List :  mutable
   iii). Tuple : Immutable

3. Dictionary : mutable
4. Set : mutable
5. Boolean : Immutable
"""
#### Integer data type ########
n1 = 30
print(n1, type(n1))
# 30 <class 'int'>
"""
Properties of Integer
->  Integer is a immutable data type, once it is defined we can not change.
->  There is no limit for integer data type
->  Integer always consider a whole numbers (+ve and -ve both)
"""

n2 = 8098908989080980980
print(n2, type(n2))
# 8098908989080980980 <class 'int'>

n3 = 0
print(n3, type(n3))
# 0 <class 'int'>

n4 = -5665654
print(n4, type(n4))
# -5665654 <class 'int'>

# when we add 2 integer value then output will be integer only
v1 = 200
v2 = 300
v3 = v1 + v2
print("v3 :", v3, type(v3))
# v3 : 500 <class 'int'>


print("_"*50)
################# Float #####################
p1 = 50.56
print(p1, type(p1))
# 50.56 <class 'float'>
"""
# properties of float
->  Float is immutable data type
->  There is no specific limit for float data type
->  All the pointer values will be consider as float (Both positive and negative)

"""
v2 = 50 + 55.56
print(v2, type(v2))

p2 = 0.0
print("p2 :", p2, type(p2))  # p2 : 0.0 <class 'float'>
p3 = 0.000345 #
print("p3 :", p3, type(p3))  # p3 : 0.000345 <class 'float'>
p4 = 11.343434334
print("p4 :", p4, type(p4))  # p4 : 11.343434334 <class 'float'>
p5 = 655464565654.454
print("p5 :", p5, type(p5))  # p5 : 655464565654.454 <class 'float'>



print("_"*50)
################# Complex number #####################
# complex number represent with x+yj
# x = real number
# y = imaginary number
q1 = 10+ 20j
print(q1, type(q1))
# (10+20j) <class 'complex'>

q2 = 3.4 + 44.3j
print(q2, type(q2))
# (3.4+44.3j) <class 'complex'>

result = q1 + q2
print(result, type(result))
# (13.4+64.3j) <class 'complex'>

# complex number
q4 = q1*2
print("multiplication :", q4, type(q4))
# (20+40j) <class 'complex'>

q5 = 55+75j
print("real number :", q5.real) # 55.0
print("imaginary number :", q5.imag) # 75.0

q6 = int()

print(q6)

# p7 = 10 + 20i
# print(p7) # SyntaxError: invalid decimal literal

print("_"*50)
##################################### string data type #############################################

s1 = "Hello"
print(s1, type(s1))
# Hello <class 'str'>

s = str()
s0 = ''
s2 = ""
s3 = 'A'
s4 = "B"
s5 = 'Python'
s6 = "Hello we are learning Python $$$$"
s7 = 'Python programming easy is 45334'
s8 = "Good Morning 'Hope' you are good **&*"
s9 = 'Very good "evening", enjoy your party ^^%$^^-\n gfsadfgj;lkjkj   jjkljklhuuiyrwqeb \nqafhhjdsahfjskdhflk'
s10 = """ Hello we are learning
Python Programming, 'and' 'learning is fun.
Its very "easy" understand
"""

s11 = '''
Hello we are learning
Python Programming, 'and' 'learning is fun.
Its very "easy" understand
'''

var1 = "nice"
s12 = "Have a"+var1+" day"


print("_"*40)
print(s1)
print("_"*40)
print(s2)
print("_"*40)
print("s3:", s3)
print("_"*40)
print("s4:", s4)
print("_"*40)
print("s5:", s5)
print("_"*40)
print("s6:", s6)
print("_"*40)
print("s7:", s7)
print("_"*40)
print("s8:", s8)
print("_"*40)
print("s9:", s9)
print("_"*40)
print("s10:", s10)
print("_"*40)
print("s11:", s11)
print("_"*40)
print("s12:", s12)

v1 = 40
v2 = 60
v3 = 70
print(v1,"Hello",v2,"python",v3)
