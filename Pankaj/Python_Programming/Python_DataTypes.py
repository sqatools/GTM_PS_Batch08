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

# Integer Data Type
a = 10
print(a, type(a))
# 10 <class 'int'>
"""
Properties of Integer:
->  Integer is a immutable data type, once it is defined we can not change.
->  There is no limit for integer data type
->  Integer always consider a whole numbers (+ve and -ve both)
"""

b = -3231312312323123123123123123123123123123
c = 0
print(b, type(b))
print(c, type(c))
# 3231312312323123123123123123123123123123 <class 'int'>
# 0 <class 'int'>

d = b+c
print("sum of a plus b: ", d, type(d))
print("_"*50)

############ Float ##############
a1 = 33.3
print(a1, type(a1))
# float is immutable data type
# float don't have any specific limit
# All the decimal values will be considered as float both + and - value also.

b1 = 40 + a1
print(b1, type(b1))
print("_"*50)

############ Complex Numbers ##############
# Complex numbers represent with x+yj
# x = real number
# y = imaginary number

q1 = 10+20j
print(q1, type(q1))
# (10+20j) <class 'complex'>

q2 = 33.3 + 44.4j
print(q2, type(q2))
# (33.3+44.4j) <class 'complex'>

result = q1+q2
print(result, type(result))
# (43.3+64.4j) <class 'complex'>

q3 = q1*q2
print(q3, type(q3))
# (-555+1110j) <class 'complex'>

q4 = 33+44.5j
print("Real Number:", q4.real) # Real Number: 33.0
print("Imaginary Number:", q4.imag) # Imaginary Number: 44.5

q5 = int()
print(q5)

# p7 = 10+20i
# print(p7)
# SyntaxError: invalid decimal literal
print("_"*50)

##################### String Datatype #######################
s1 = "hello"
print(s1, type(s1))
# hello <class 'str'>

s2 = ""
s3 = "1"
s4 = 'b'
s5 = 'python'
s6 = """Hello everyone how are you ?"""
s7 = """Hello%&@^#%(!@%#!@*"""
s8 = "python is fun to  " \
     "learn"
hi1 = "Hello"
s9 = "Yo"+hi1+"are you"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7,)
print(s8, s9)

v1 = 40
print(v1, "Hello")





