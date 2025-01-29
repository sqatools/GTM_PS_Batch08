# Integer data type

n1 = 30
print(n1, type(n1))

"""
1.Numbers
 - Integer
 - Float
 -Complex number

 2.Sequential
 - String
 - List
 - Tuple

 3.Dictionary
 4.Set
 5.Boolean

"""

# Float

a1 = 10.45
print(a1, type(a1))

# complex
b1 = 10 + 20j
print(b1, type(b1))

# String data type
c1 = "Hello"
print(c1, type(c1))

C2 = " "
C3 = 'A'
C4 = 'Python'
print(C2, C3, C4)

z1 = "Python"
print(z1[1])
print(len(z1))

# List datatype

list1 = [1, 2, 'three', 'four', [5, 6], 'seven']
print(list1)

print(list1[4])

print(list1[2], list1[5])

# Tuple data type
tup1 = (11, 12, 13, 'Forteen', [15, 16, 17],)
print(tup1)

print(dir(tup1))

print(tup1[-1])
print(tup1.count(5))
print(tup1.count([15, 16, 17]))

# dictionary data type

dic1 = {'a': 123, 'b': 456, 'c': 789, 'd': [1, 2, 3], 'e': (4, 'five', 'six')}
print(dic1)

dic2 = {'name': 'Anu',
        'age': 31,
        'email': 'anu@abc.com'}
print(dic2)

dic2['phone'] = 1234567890
print(dic2)

dic2.popitem()
print(dic2)
from pprint import pprint

dic3 = {'a': dic2, 'b': dic1}
pprint(dic3)

pprint(dic2)

# Sets data type
set1 = {1, 2, 3.5, 6.7, 8, 8, 3.5, 100, 1000, 103}
print(set1)

# Boolean data type

# It contains only two values - True and False
var1 = True
print(var1)

n2 = 123
f1 = float(n2)
print(f1, type(f1))

b1 = bool(n2)
print(b1, type(b1))

s1 = str(n2)
print(s1, type(s1))

#********************************************************** data type conversion
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

rint("_"*50)
### string -> list ###
str_a = "Hi Python 3"
list_a = list(str_a)
print(list_a, type(list_a), list_a[2])
# ['H', 'i', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '3'] <class 'list'>



print("_"*50)
### string -> tuple ###
str_b = "Good Morning"
tup1 = tuple(str_b)
print(tup1, type(tup1), tup1[3])
# ('G', 'o', 'o', 'd', ' ', 'M', 'o', 'r', 'n', 'i', 'n', 'g') <class 'tuple'> d


print("_"*50)
### string -> dictionary ###
"""
str_c = "Good Evening"
dict_c = dict(str_c)
print(dict_c)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
"""

# If string follows the dict rules and pattern than the string to dictionary conversion
# possible with the help json module.
import json
str_d = '{"a": 123, "b": 456, "c": 789}'
#str_d = "{'a': 123, 'b': 456, 'c': 789}"

print(str_d, type(str_d))
# {"a": 123, "b": 456, "c": 789} <class 'str'>

result = json.loads(str_d)
print(result, type(result))
# {'a': 123, 'b': 456, 'c': 789} <class 'dict'>
print(result["b"]) # 456


print("_"*50)
### string -> set ###
str_e = "Good Morning"
set_e = set(str_e)
print(set_e, type(set_e))
# {'i', 'M', 'G', 'o', 'r', 'd', 'n', 'g', ' '} <class 'set'>


print("_"*50)
### string -> boolean ###

str_f = ""
b1 = bool(str_f)
print(b1, type(b1))
# False <class 'bool'>

str_g = "Hello"
b2 = bool(str_g)
print(b2, type(b2))
# True <class 'bool'>


######################################## List Data Type Conversion ###############################

print("_"*50)
### list -> int ### conversion is not possible
### list -> float ### conversion is not possible
### list -> complex ### conversion is not possible

print("_"*50)
### list -> string ###
list1 = [4, 6, 7, 1]
str_a = str(list1)
print(str_a, type(str_a))
# [4, 6, 7, 1] <class 'str'>
print(str_a[0], str_a[3], str_a[1], str_a[2], str_a[-1])
# [   4 , ]
print(str_a[0], str_a[7], str_a[2], str_a[-1])
# [ 7 , ]



print("_"*50)
### list -> tuple ###
list2 = ['a', 3.5, [4, 6, 7], (3, 6)]
tup2 = tuple(list2)
print(tup2, type(tup2))
# ('a', 3.5, [4, 6, 7], (3, 6)) <class 'tuple'>
print(tup2[-2]) # [4, 6, 7]


print("_"*50)
### list -> dictionary ###
"""
list3 = [5, 7, 2, 8]
dict3 = dict(list3)
print(dict3)
"""
# TypeError: cannot convert dictionary update sequence element #0 to a sequence

# If we have two list and wants to convert into dictionary thn we can user zip function

list_a = ['a', 'b', 'c', 'd', 'e']
list_b = [23, 454, 67, 89, 90]

result = dict(zip(list_a, list_b))
print(result, type(result))
# {'a': 23, 'b': 454, 'c': 67, 'd': 89, 'e': 90} <class 'dict'>
print(result['d']) # 89


list_e = ('a', 'b', 'c', 'd', 'e')
list_f = [23, 454, 67, 89, 90]
result2 = dict(zip(list_f, list_e))
print(result2)
# {'a': 23, 'b': 454, 'c': 67, 'd': 89, 'e': 90}



print("_"*50)
### list -> set ###
list1 = [4, 6, 8, 2, 5, 7, 2, 6, 7]
set1 = set(list1)
print(set1, type(set1))
# {2, 4, 5, 6, 7, 8} <class 'set'>


print("_"*50)
### list -> boolean ###

list_a = []
b1 = bool(list_a)
print(b1, type(b1))
# False <class 'bool'>

list_b = [5, 6]
b2 = bool(list_b)
print(b2, type(b2))
# True <class 'bool'>


########################### Tuple Data Type Conversion ###################
# tuple -> int # conversion is not possible
# tuple -> float # conversion is not possible
# tuple -> complex # conversion is not possible

print("_"*50)
### tuple ->  string ###
tup_a = (5, 7, 9, 2)  # "(5, 7, 9, 2)"
str_a = str(tup_a)
print(str_a, type(str_a), str_a[0])
# (5, 7, 9, 2) <class 'str'> (


print("_"*50)
### tuple ->  list ###
tup_b = (5, 7, 9, 2, 5, 6)
list_b = list(tup_b)
print(list_b, type(list_b), list_b[0])
# [5, 7, 9, 2, 5, 6] <class 'list'> 5


print("_"*50)
### tuple ->  dictionary ### conversion it not possible
# only we can convert 2 tuple into dict using zip function as discussed.


tup_e = ('a', 'b', 'c', 'd', 'e')
tup_f = (23, 454, 67, 89, 90)
result2 = dict(zip(tup_e, tup_f))
print(result2)
# {'a': 23, 'b': 454, 'c': 67, 'd': 89, 'e': 90}


print("_"*50)
### tuple ->  set ###
tup_h = (5, 8, 22, 8, 1, 6, 5)
set_h = set(tup_h)
print(set_h, type(set_h))
# {1, 5, 6, 8, 22} <class 'set'>


print("_"*50)
### tuple ->  boolean ###
tup_j = tuple()
b1 = bool(tup_j)
print(b1, type(b1))
# False <class 'bool'>

tup_k = (4, 7, 8)
b2 = bool(tup_k)
print(b2, type(b2))
#True <class 'bool'>

tup2 = (b1, b2)
print(tup2) # (False, True)


# var1 = "Hello"
# var2 = "(5, 6, 8)"
# print(var1)
# print(var2)

##################################### Dictionary Data Type Conversion ###################

### dict -> int #### conversion is not possible
### dict -> float #### conversion is not possible
### dict -> complex #### conversion is not possible

print("_"*50)
### dict -> string ####

dict1 = {'a': 123, 'b' : 456, 'c': 789}
print(dict1)
str1 = str(dict1)
print(str1, type(str1))
# {'a': 123, 'b': 456, 'c': 789} <class 'str'>
print(str1[0], str1[2])
# { a


print("_"*50)
### dict -> list ####
dict2 = {'a': 123, 'b' : 456, 'c': 789}
list2 = list(dict2)
print(list2, type(list2))
# ['a', 'b', 'c'] <class 'list'>

print(list(dict1.items()))
# [('a', 123), ('b', 456), ('c', 789)]

print("_"*50)
### dict -> tuple ####
dict_a = {'a': 123, 'b' : 456, 'c': 789}
tup_a = tuple(dict_a)
print(tup_a, type(tup_a))
# ('a', 'b', 'c') <class 'tuple'>

print(tuple(dict1.items()))
# (('a', 123), ('b', 456), ('c', 789))


print("_"*50)
### dict -> set ####
dict_b = {'a': 123, 'b' : 456, 'c': 789}
set_b = set(dict_b)
print(set_b, type(set_b))

# {'a', 'c', 'b'} <class 'set'>


print("_"*50)
### dict -> boolean ####

dict_c = {}
b1 = bool(dict_c)
print(b1, type(b1))
# False <class 'bool'>

dict_d = {'a': 345, 'b' : 899}
b2 = bool(dict_d)
print(b2, type(b2))
# True <class 'bool'>


###################################### Set data type conversion ############################
### set -> int ## conversion is not possible
### set -> float ### conversion is not possible
### set -> complex ### conversion is not possible

print("_"*50)
### set -> string ###
set1 = {15, 27, 9, 3, 'a', 6, 17, 7, 17}
str1 = str(set1)
print(str1, type(str1), str1[1])
# {3, 6, 7, 9, 15, 17, 27, 'a'} <class 'str'> 3



print("_"*50)
### set -> list ###
set2 = {15, 27, 9, 3, 'a', 6, 17, 7, 17}
list2 = list(set2)
print(list2, type(list2))
# [3, 6, 7, 9, 15, 17, 'a', 27] <class 'list'>
print(list2[3]) # 9


print("_"*50)
### set -> tuple ###
set2 = {15, 27, 9, 3, 'a', 6, 17, 7, 17}
tup2 = tuple(set2)
print(tup2, type(tup2), tup2[4])
# (3, 'a', 6, 7, 9, 15, 17, 27) <class 'tuple'> 9


print("_"*50)
### set -> dict ### conversion is possible
# set3 = {15, 27, 9, 3, 'a', 6, 17, 7, 17}
# dict3 = dict(set3)
# print(dict3)
# cannot convert dictionary update sequence element #0 to a sequence


print("_"*50)
### set -> boolean ###

set1 = set()
b1 = bool(set1)
print(b1, type(b1))
# False <class 'bool'>

set2 = {5, 6, 7}
b2 = bool(set2)
print(b2, type(b2))
# True <class 'bool'>


################ Boolean Data Type Conversion ##############
## bool -> int ##
b1 = False
n1 = int(b1)
print(n1, type(n1))

# 1 <class 'int'> : for True
# 0 <class 'int'> : for False

print("_"*50)
## bool -> float ##
a1 = True
b1 = float(a1)
print(b1, type(b1))

# 1.0 <class 'float'> : True
# 0.0 <class 'float'> : False


print("_"*50)
### bool -> complex ###
c1 = False
b1 = complex(c1)
print(b1, type(b1))

# (1+0j) <class 'complex'> : True
# 0j <class 'complex'> : False


print("_"*50)
### bool -> string ###
d = True
s1 = str(d)
print(s1, type(s1), s1[1])
# True <class 'str'> r


print("_"*50)
### bool -> list ###  Conversion is not possible
# e = True
# l1 = list(e)
# print(l1)
# TypeError: 'bool' object is not iterable

print("_"*50)
### bool -> tuple ###  Conversion is not possible
### bool -> dict ###  Conversion is not possible
### bool -> set ###  Conversion is not possible
