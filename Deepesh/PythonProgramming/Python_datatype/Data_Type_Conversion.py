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

#################### Int #######################

print("_"*50)
### Int -> float ###
n1 = 55
f1 = float(n1)
print(f1, type(f1))  # 55.0 <class 'float'>

print("_"*50)
### Int -> string ###
n2 = 67878
s1 = str(n2)
print(s1, type(s1), s1[2])
# 67878 <class 'str'> 8


print("_"*50)
### Int -> list ### Conversion is not possible
"""
n3 = 567
l3 = list(n3)
print(l3)
"""
# TypeError: 'int' object is not iterable


print("_"*50)
### Int -> tuple ### Conversion is not possible
### Int -> dict ### Conversion is not possible
### Int -> set ### Conversion is not possible
"""
b1 = 5
set1 = set(b1)
print(set1, type(set1))
#TypeError: 'int' object is not iterable
"""

### Int -> complex ### x+yj
a1 = 500
c1 = complex(a1)
print(c1, type(c1))
# (500+0j) <class 'complex'>
# default imaginary value will be zero

print("_"*50)
### int -> boolean ###
a2 = 0
b2 = bool(a2)
print(b2, type(b2)) # False <class 'bool'>

a3 = -4455
b3 = bool(a3)
print(b3, type(b3)) # True <class 'bool'>


################################# Float data type conversion ###################

print("_"*50)
### Float -> Int ###
f1 = 55.45
n1 = int(f1)
print(n1, type(n1))
# 55 <class 'int'>


print("_"*50)
### Float -> string ###
f2 = 57.345
s2 = str(f2)
print(s2, type(s2), s2[-2], s2[2])
# 57.345 <class 'str'> 4 .


print("_"*50)
### Float -> complex ###
f3 = 78.89
c3 = complex(f3)
print(c3, type(c3))
# (78.89+0j) <class 'complex'>

print("_"*50)
### Float -> list ### conversion is not possible
### Float -> tuple ### conversion is not possible
### Float -> dict ### conversion is not possible
### Float -> set ### conversion is not possible

print("_"*50)
### Float -> Boolean ###
v1 = 0.0000
b1 = bool(v1)
print(b1, type(b1))
# False <class 'bool'>

v2 = 4.56
b2 = bool(v2)
print(b2, type(b2))
# True <class 'bool'>


########################### String ###########################

print("_"*50)
### string -> int ###
"""
str1 = "Hello"
num1 = int(str1)
print(num1)
# invalid literal for int() with base 10: 'Hello'
"""

# note : If string only contains number than string to int conversion is possible
str2 = "4562"
num2 = int(str2)
print(num2, type(num2), num2*10)
# 4562 <class 'int'> 45620


print("_"*50)
### string -> float ###
# Note: if string contains only pointer value, than string to float conversion is possible
str4 = "453.67"
f3 = float(str4)
print(f3, type(f3), f3*10)
# 453.67 <class 'float'> 4536.7


print("_"*50)
### string -> complex ###
str5 = "50+60j"
c5 = complex(str5)
print(c5, type(c5), c5.real)
# (50+60j) <class 'complex'> 50.0

str6 = "50"
c6 = complex(str6)
print(c6) # (50+0j)

str7 = "80j"
c7 = complex(str7)
print(c7, type(c7), c7.real,  c7.imag) # 80j
# 80j <class 'complex'> 0.0 80.0



print("_"*50)
### string -> list ###
str_a = "Hi Python 3"
list_a = list(str_a)
print(list_a, type(list_a), list_a[2])
# ['H', 'i', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '3'] <class 'list'>

list_a.append(30)
print(list_a)
str1 = "Hello"
print(str1.upper())







