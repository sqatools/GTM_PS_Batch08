"""
Data types in Python:
1. Numbers
   i. Integer : Immutable
   ii. Float  : Immutable
   iii. Complex Numbers  # Immutable

2. Sequential
   i. String  : Immutable
   ii. List   : Mutable
   iii. Tuple  :  Immutable

3. Set  : Mutable
4. Dictionary : Mutable
5. Boolean : Immutable

"""

################## Integer Data Type to others #####################
print("1. Integer Data Type to other Data Types\n")
print("i. Integer to Float Conversion:")
n1 = 50
f1 = float(n1)
print("Integer value is ",n1,"\nValue after converting int to float is:")
print(f1, type(f1))
print("_"*50)

print("ii. Integer to String Conversion:")
n2 = 34
s1 = str(n1)
print("Integer value is ",n2,"\nValue after converting int to String is:")
print(s1, type(s1), s1[1])
print("_"*50)

print("iii. Integer to List Conversion: This conversion is not possible\n")
#n3 = 211012
#l1 = list(n3)
#print("Integer value is ",n1,"\nValue after converting int to String is:")
#print(l1, type(l1))   # TypeError: 'int' object is not iterable
###  Integer to List Conversion is not possible
print("_"*50)

### Int -> tuple ### Conversion is not possible
### Int -> dict ### Conversion is not possible
### Int -> set ### Conversion is not possible

print("iv. Integer to Complex number Conversion:")
a1 = 34
c1 = complex(a1)
print("Integer value is ",a1,"\nValue after converting int to Complex number is:")
print(c1, type(c1))
# default imaginary value will be zero
print("_"*50)

print("v. Integer to Boolean Conversion:")
a2 = 0
b2 = bool(a2)
print("Integer value is ",a2,"\nValue after converting int to bool is:")
print(b2, type(b2))
print("_"*20)
a3 = 1
b3 = bool(a3)
print("Integer value is ",a3,"\nValue after converting int to bool is:")
print(b3, type(b3))
print("_"*50)

################################# Float data type conversion ###################

# Float to Int conversion
print("2. Float Data Type to other Data Types\n")
print("i. Float to Int Conversion:")
f1 = 2354.8678
n1 = int(f1)
print("Float value is ",f1,"\nValue after converting float to int is:")
print(n1, type(n1))   # 2354 <class 'int'>
print("_"*50)

print("ii. Float to String Conversion:")
f1 = 2354.8678
s1 = str(f1)
print("Float value is ",f1,"\nValue after converting float to String is:")
print(s1, type(s1), s1[3])    # 2354.8678 <class 'str'> 4
print("_"*50)

print("iii. Float to complex number Conversion:")
f1 = 2354.8678
c1 = complex(f1)
print("Float value is ",f1,"\nValue after converting float to Complex num is:")
print(c1, type(c1))    #   (2354.8678+0j) <class 'complex'>
print("_"*50)

### Float -> list ### conversion is not possible
### Float -> tuple ### conversion is not possible
### Float -> dict ### conversion is not possible
### Float -> set ### conversion is not possible

print("iv. Float to Boolean Conversion:")
f2 = 0.000
b1 = bool(f2)
print("Float value is ",f2,"\nValue after converting float to Boolean is:")
print(b1, type(b1))    # False <class 'bool'>
print("_"*20)

f3 = 45.2445
b2 = bool(f3)
print("Float value is ",f3,"\nValue after converting float to Boolean is:")
print(b2, type(b2))    #  True <class 'bool'>
print("_"*50)


################################# String data type conversion ###################

# String to Int conversion
print("3. String Data Type to other Data Types\n")
"""
print("i. String to Int Conversion:")
s1 = 'Hello'
n1 = int(s1)
print("String value is ",s1,"\nValue after converting String to Int is:")
print(n1, type(n1))     # ValueError: invalid literal for int() with base 10: 'Hello'
"""

# Note : If String contains only number then String --> Int conversion is possible
print("i. String to Int Conversion:")
str2 = '23478'
n3 = int(str2)
print("String value is ",str2,"\nValue after converting String to Int is:")
print(n3, type(n3))     # 23478 <class 'int'>
print('_'*50)

### string -> float ###
# Note: if string contains only pointer value, then string to float conversion is possible
print("ii. String to Float Conversion:")
str4 = "453.67"
f3 = float(str4)
print("String value is ",str4,"\nValue after converting String to Float is:")
print(f3, type(f3), f3*10)
# 453.67 <class 'float'> 4536.7
print('_'*50)

print("iii. String to Complex number Conversion:")
str5 = "50+60j"
c5 = complex(str5)
print("String value is ",str5,"\nValue after converting String to complex num is:")
print(c5, type(c5), c5.real, c5.imag)   # (50+60j) <class 'complex'> 50.0 60.0

str6 = "50"
c6 = complex(str6)
print("Complex when String is ",str6 ," is: ",c6) # (50+0j)

str7 = "80j"
c7 = complex(str7)
print("Complex when String is ",str7 ," is: ",c7)
print(c7, type(c7), c7.real,  c7.imag) # 80j
# 80j <class 'complex'> 0.0 80.0
print("_"*50)

print("v. String to List conversion")
str8 = "Hi Python 3"
l1 = list(str8)
print("String value is ",str8,"\nValue after converting String to list is:")
print(l1, type(l1), l1[4])  # ['H', 'i', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '3'] <class 'list'> y
print("_"*50)

print("vi. String to Tuple conversion")
str9 = "Good night"
t1 = tuple(str9)
print("String value is ",str9,"\nValue after converting String to Tuple is:")
print(t1, type(t1))   # ('G', 'o', 'o', 'd', ' ', 'n', 'i', 'g', 'h', 't') <class 'tuple'>
print(t1[3])    # d
print('_'*50)

"""
str_c = "Good Evening"
dict_c = dict(str_c)
print(dict_c)   # ValueError: dictionary update sequence element #0 has length 1; 2 is required
# Direct String to Dict conversion is not possible
"""

# Note : If string follows the dict rules and pattern than the string to dictionary conversion
# possible with the help json module.

print("String to Dictionary Conversion")
import json
str_d = '{"a": 123, "b": 456, "c": 789}'
#str_d = "{'a': 123, 'b': 456, 'c': 789}"

print(str_d, type(str_d))
# {"a": 123, "b": 456, "c": 789} <class 'str'>

result = json.loads(str_d)
print(result, type(result))
# {'a': 123, 'b': 456, 'c': 789} <class 'dict'>
print(result["b"]) # 456
print('_'*80)


### string -> set ###
print("String to Set conversion")
str_e = "Good Morning"
set_e = set(str_e)
print("The String ",str_e," is converted to Set. After conversion the set is: ")
print(set_e, type(set_e))
# {'i', 'M', 'G', 'o', 'r', 'd', 'n', 'g', ' '} <class 'set'>
print("_"*50)

## string -> boolean ###
print("String to Boolean Conversion")
str_f = ""
b1 = bool(str_f)
print("String '' after converting to boolean is: " )
print(b1, type(b1))
# False <class 'bool'>
print('_'*20)
str_g = "Hello"
b2 = bool(str_g)
print("String 'Hello' after converting to boolean is: ")
print(b2, type(b2))
# True <class 'bool'>
print('_'*50)

######################################## List Data Type Conversion ###############################

print("Converting List to other Data Types")
### list -> int ### conversion is not possible
### list -> float ### conversion is not possible
### list -> complex ### conversion is not possible

### list -> string ###
print("Converting List to STring")
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
print("Converting List to Tuple")
list2 = ['a', 3.5, [4, 6, 7], (3, 6)]
tup2 = tuple(list2)
print(tup2, type(tup2))
# ('a', 3.5, [4, 6, 7], (3, 6)) <class 'tuple'>
print(tup2[-2]) # [4, 6, 7]
print("_"*50)

### list -> dictionary ###
print("Converting List to Dictionary")
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
print("List to Set Conversion")
list1 = [4, 6, 8, 2, 5, 7, 2, 6, 7]
set1 = set(list1)
print(set1, type(set1))
# {2, 4, 5, 6, 7, 8} <class 'set'>
print("_"*50)

### list -> boolean ###
print("List to Boolean conversion")
list_a = []
b1 = bool(list_a)
print(b1, type(b1))
# False <class 'bool'>

list_b = [5, 6]
b2 = bool(list_b)
print(b2, type(b2))
# True <class 'bool'>
print("_"*50)


############################# Tuple Data Type ####################################
print("Tuple to other data type conversion")

# tuple -> int # conversion is not possible
# tuple -> float # conversion is not possible
# tuple -> complex # conversion is not possible

# Tuple --> String Conversion
print("\nTuple to string conversion")
tup1 = (5, 6, 2, 4, 5)
str1 = str(tup1)
print("Tuple after converting to string is: \n",str1, type(str1))
# (5, 6, 2, 4, 5) <class 'str'>
print("_"*80)

### tuple ->  list ###
print("Tuple to List conversion")
tup_b = (5, 7, 9, 2, 5, 6)
list_b = list(tup_b)
print("Tuple after converting to List is: \n",list_b, type(list_b), list_b[0])
# [5, 7, 9, 2, 5, 6] <class 'list'> 5
print("_"*80)

### tuple ->  dictionary ### direct conversion it not possible
# only we can convert 2 tuple into dict using zip function as discussed.

print("Converting Tuple to Dictionary using zip function")
tup_e = ('a', 'b', 'c', 'd', 'e')
tup_f = (24, 10, 21, 12, 267)

dict_a = dict(zip(tup_e, tup_f))
print("Dictionary after conversion is: ")
print(dict_a, type(dict_a))
print("_"*80)

### tuple ->  set ###
print("Tuple to Set conversion")
tup_h = (5, 8, 22, 8, 1, 6, 5)
set_h = set(tup_h)
print("Set after conversion is:")
print(set_h, type(set_h))
# {1, 5, 6, 8, 22} <class 'set'>
print("_"*80)

### tuple ->  boolean ###
print("Tuple to Boolean Conversion")
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
print("_"*80)

##################################### Dictionary Data Type Conversion ###################

### dict -> int #### conversion is not possible
### dict -> float #### conversion is not possible
### dict -> complex #### conversion is not possible

### dict -> string ####
print("Dictionary to String Conversion")
dict1 = {'a': 123, 'b' : 456, 'c': 789}
print("The dictionary is: ",dict1)
str1 = str(dict1)
print("String after converting from Dict is: ")
print(str1, type(str1))
# {'a': 123, 'b': 456, 'c': 789} <class 'str'>
print(str1[0], str1[2])
# { a
print("_"*80)

### dict -> list ####
print("Dictionary to List conversion")
dict2 = {'a': 123, 'b' : 456, 'c': 789}
list2 = list(dict2)
print("List after conversion is: ")
print(list2, type(list2))
# ['a', 'b', 'c'] <class 'list'>

print("Using items() function to get both key and value as list members")
print(list(dict1.items()))
# [('a', 123), ('b', 456), ('c', 789)]
print("_"*80)

### dict -> tuple ####
print("Converting Dictionary to Tuple")
dict_a = {'a': 123, 'b' : 456, 'c': 789}
tup_a = tuple(dict_a)
print("Dictionary after converting to Tuple")
print(tup_a, type(tup_a))
# ('a', 'b', 'c') <class 'tuple'>
print("\nUsing items() function")
print(tuple(dict1.items()))
# (('a', 123), ('b', 456), ('c', 789))
print("_"*80)

### dict -> set ####
print("Dictionary to Set Convertion")
dict_b = {'a': 123, 'b' : 456, 'c': 789}
set_b = set(dict_b)
print("Set after conversion")
print(set_b, type(set_b))
# {'a', 'c', 'b'} <class 'set'>
print("_"*80)

### dict -> boolean ####
print("Dictionary to Boolean conversion")
dict_c = {}
b1 = bool(dict_c)
print("When dict is empty,")
print(b1, type(b1))
# False <class 'bool'>

dict_d = {'a': 345, 'b' : 899}
b2 = bool(dict_d)
print("Dictionary to Boolean :")
print(b2, type(b2))
# True <class 'bool'>
print("_"*80)

###################################### Set data type conversion ############################
### set -> int ## conversion is not possible
### set -> float ### conversion is not possible
### set -> complex ### conversion is not possible

### set -> string ###
print("Set to String Conversion:")
set1 = {15, 27, 9, 3, 'a', 6, 17, 7, 17}
str1 = str(set1)
print("String after conversion: ")
print(str1, type(str1), str1[1])
# {3, 6, 7, 9, 15, 17, 27, 'a'} <class 'str'> 3
print("_"*80)

### set -> list ###
set2 = {15, 27, 9, 3, 'a', 6, 17, 7, 17}
list2 = list(set2)
print("The List is: ")
print(list2, type(list2))
# [3, 6, 7, 9, 15, 17, 'a', 27] <class 'list'>
print(list2[3]) # 9
print("_"*80)

### set -> tuple ###
print("Set to Tuple conversion")
set2 = {15, 27, 9, 3, 'a', 6, 17, 7, 17}
tup2 = tuple(set2)
print("The Tuple is: ")
print(tup2, type(tup2), tup2[4])
# (3, 'a', 6, 7, 9, 15, 17, 27) <class 'tuple'> 9
print("_"*80)

### set -> dict ### conversion is possible
"""
set3 = {15, 27, 9, 3, 'a', 6, 17, 7, 17}
dict3 = dict(set3)
print(dict3)
# cannot convert dictionary update sequence element #0 to a sequence
"""

### set -> boolean ###
print("Set to Boolean conversion")
set1 = set()
b1 = bool(set1)
print("When Set is empty: ")
print(b1, type(b1))
# False <class 'bool'>

set2 = {5, 6, 7}
b2 = bool(set2)
print("Set to Boolean : ")
print(b2, type(b2))
# True <class 'bool'>
print("_"*80)

print("Converting Boolean data type to others")
## bool -> int ##
print("Boolean to Int conversion")
b1 = False
n1 = int(b1)
print(n1, type(n1))

# 1 <class 'int'> : for True
# 0 <class 'int'> : for False
print("_"*80)

## bool -> float ##
print("Boolean to Float Conversion")
a1 = True
b1 = float(a1)
print(b1, type(b1))

# 1.0 <class 'float'> : True
# 0.0 <class 'float'> : False
print("_"*80)

### bool -> complex ###
print("Boolean to Complex number Conversion")
c1 = False
b1 = complex(c1)
print(b1, type(b1))

# (1+0j) <class 'complex'> : True
# 0j <class 'complex'> : False
print("_"*80)

### bool -> string ###
print("Boolean to String Conversion")
d = True
s1 = str(d)
print(s1, type(s1), s1[1])
# True <class 'str'> r
print("_"*80)

### bool -> list ###  Conversion is not possible
# e = True
# l1 = list(e)
# print(l1)
# TypeError: 'bool' object is not iterable

# print("_"*50)
### bool -> tuple ###  Conversion is not possible
### bool -> dict ###  Conversion is not possible
### bool -> set ###  Conversion is not possible
