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
var1 = 'hello'
print(var1, type(var1))
'''
#Properties
-> String is immutable data type, we can not modify
-> Anything with single/double/triple quote is string
-> String follows positive and negative indexing
-> String can contain any type of data int,str,float,special character etc.
'''

s12 = "334 5.5 [4,5,6] @&*!^!(*@&"
print(s12, type(s12))

print("_" * 60)

str_a = "Pankaj"
"""
0    1   2   3   4   5
P    a   n   k   a   j
-6  -5  -4  -3  -2   -1
"""

print(str_a[0], str_a[-1])
print(str_a[-3])

length = len(str_a)
print("Length of string : ", length)

print(str_a.index('j'))
# slicing
print(str_a[2:4])

######### List Data Type ###########
list1 = [22, "Pankaj", 33.3, 'prasad', True]
print(list1, type(list1))

"""
# properties of list data type
1. List is mutable data type, we can modify any point of time
2. List follows both +ve and -ve indexing
3. List can contain all different data type, int, float, string, list, tuple, dict, set, bool
4. We define the list inside square bracket
"""
#        0   1   2      3        4         5        6
list2 = [22, 1, 33, [3, 4, 5], 'Hello', "Python", list1]
#        -7  -6 -5     -4        -3        -2      -1
print(list2[3])  # child list
print(list2[-3])
list2.append(100)  # method, it starts with .
# append is used for modification of data
print(list2)
print(list2[4])  # print hello
print(list2[-3])  # here why output python is coming because append 100 is at there

print(list2[6])
# how to find all methods of list
print(dir(list2))  # dir is function
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print(dir(str))
# anything stating with def is function
# __add__ are called as magic functions, python use it internally
"""
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
# 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', '
# isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
# 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

var1 = 'Name'
var2 = 'Age'
var3 = 300

list3 = [var1, var2, var3]
print(list3)

list4 = [(6, 7, 8), {'a': 123}, {2, 3, 4}]
#           tuple      dict         set
# set doesnot follow indexing or order
print(list4)
print(list4[0])
print(list4[1]['a'])
print(list4[2])

print("_" * 50)
############## Tuple ##############
# once value is stored we can not modify
# it also can also store all data types
tup1 = (5, 3.3, 'r', 'Pankaj', True, [1, 2, 3], (3, 5, 7))
print(tup1)

"""
# Properties of set
-> tuple is a immutable data type, once it is defined we can not change
-> tuple can contain all different type of data int float str list boolean list dict tuple set
-> Tuple follows + and - indexing as like string and list
-> Tuple defined with round bracket

"""
#       0   1    2      3       4       5          6
tup2 = (5, 3.3, 'r', 'Pankaj', True, [1, 2, 3], (3, 5, 7))
#       -7 -6    -5    -4       -3      -2        -1

print(tup2[0])
print(dir(tuple))
# 'count', 'index'
# dir : dir return list of method belongs to specific class
print(tup2[-3], type(tup2))

########### List Data Type ############
from pprint import pprint

list1 = [2, 3.3, "Pankaj", 'Q', True]
print(list1, type(list1))
"""
# Properties:
1. List is mutable data type, we can modify later
2. List follows positive and negative indexing
3. List can contain all different kind of data types, eg, int,float, string,bool,list,tuple,set,dict
4. we define list under square bracket [].
"""
#        0   1     2       3           4           5                6
list2 = [2, 3.3, False, 23 + 3.3j, [2, 3.3, 'D'], "Pankaj", (2, 5, 7, "Prasad")]
#        -7   -6   -5      -4          -3           -2              -1
print(list2, type(list2))
print(list2[-6])

print(dir(list))
"""
# Method for list
'append', 'clear', 'copy', 'count', 'extend', 
'index', 'insert', 'pop', 'remove', 'reverse', 'sort
'"""
list2.append(100)  # it's for adding data to existing list
print(list2)
print(list2[-6], list2[3])
print(list2[3:5])  # it will ignore last vale of index 5 and give value of 3 and 4 index position
print(list2[4][1])  # need to check output

var1 = "Name"
var2 = "Age"
var3 = 300
list3 = [var1, var2, var3]
print(list3)
print("_" * 60)

########### Tuple Data Type ############
tup1 = (2, 4.4, "Pankaj", True, [2, 3, 4], (4, 7.7, 'e'))
print(tup1, type(tup1))
"""
# Properties:
1. Tuple is immutable data type, once defined it can not be changed.
2. Tuple can store int,bool, string, float, tuple,set, list,dict
3. Tuple follows positive and negative indexing
4. Tuple defined with round bracket ().
"""

print(dir(tuple))
# Methods : 'count', 'index'
print(tup1[4])
# Length of tuple
print("Length of tuple : ", len(tup1))
print(tup1.count(5))  # Need to check

########### Dictionary Data Type ############
print("_" * 60)
# dict data type store values in key and value pair
dict1 = {'a': "Pankaj", 'b': "Prasad", 'c': "Chabua"}
print(dict1, type(dict1))

"""
# Properties:
1. Dictionary is mutable data type, we can modify and update
2. Dictionary only contain unique key and duplicate keys are not allowed.
3. Dictionary store data in key value format
4. Dictionary only contains immutable data type as key, int, float, string,boolean, tuple
    -> list, dict, set can not be the key in dictionary
5. Dictionary can contain all types of data in value
    -> int, float, string, bool, list,tuple,set,dict
6. dict does not follow indexing
7. dict follows LIFO (Lat in first out)
"""

dict1 = {'Name': "Pankaj", 'Age': 38, 'City': "Bangalore", 'Email': "pankajprasad4798@gmail.com"}
print(dict1, type(dict1))

print(dict1['Email'])
print(dict1['Name'])
# Add value to dict2
dict1['Phone'] = 9930034615
print(dict1)
# pop will remove city
dict1.pop('City')
print(dict1)
print("_" * 60)

var1 = 1000
var2 = {'emp_name': "Pankaj", 'emp_salary': 4000000, 'emp_job': "QA"}
dict2 = {
    123: 3.5,
    3.5: "Pankaj",
    "Hobby": "Playing Games",
    "Python": [1, 2, 3, 4],
    var1: "Programming",
    'emp_details': var2
    }
# from pprint import pprint
pprint(dict2)

########### Set Data Type ############
print("_" * 60)
"""
# Properties:
1. Set is a mutable data type, we can modify it any point of time.
2. set can only store unique values, duplicate values are not allowed.
3. Set store data in random order and print values in random order.
4. Set only contains immutable data types as det member
int, float, string,boolean,tuple
5. Set doest not follow indexing or key value format
"""

set1 = {2, 3.3, "Pankaj", (2, 5, 89)}
print(set1, type(set1))

set2 = {2, 2, 3, 3.3, 3.4, "Pankaj", "pankaj", "Pankaj"}
print(set2)
set2.add(100)
print(set2)
set2.add(100)
print(set2)

print(dir(set))
"""
'add', 'clear', 'copy', 'difference', 'difference_update', 
'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 
'union', 'update'
"""





