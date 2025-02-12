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


print("_" * 50)
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
p3 = 0.000345  #
print("p3 :", p3, type(p3))  # p3 : 0.000345 <class 'float'>
p4 = 11.343434334
print("p4 :", p4, type(p4))  # p4 : 11.343434334 <class 'float'>
p5 = 655464565654.454
print("p5 :", p5, type(p5))  # p5 : 655464565654.454 <class 'float'>

print("_" * 50)
################# Complex number #####################
# complex number represent with x+yj
# x = real number
# y = imaginary number
q1 = 10 + 20j
print(q1, type(q1))
# (10+20j) <class 'complex'>

q2 = 3.4 + 44.3j
print(q2, type(q2))
# (3.4+44.3j) <class 'complex'>

result = q1 + q2
print(result, type(result))
# (13.4+64.3j) <class 'complex'>

# complex number
q4 = q1 * 2
print("multiplication :", q4, type(q4))
# (20+40j) <class 'complex'>

q5 = 55 + 75j
print("real number :", q5.real)  # 55.0
print("imaginary number :", q5.imag)  # 75.0

q6 = int()

print(q6)

# p7 = 10 + 20i
# print(p7) # SyntaxError: invalid decimal literal

print("_" * 50)
##################################### string data type #############################################

s1 = "Hello"
print(s1, type(s1))
# Hello <class 'str'>
"""
# properties
->  String is immutable data type, we can not modify.
->  Anything with single/double/triple quote will consider as string
->  String follows positive and negative indexing.
->  String can contain any type of data, int, str, float, special character etc.
"""
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
s12 = "Have a" + var1 + " day"

print("_" * 40)
print(s1)
print("_" * 40)
print(s2)
print("_" * 40)
print("s3:", s3)
print("_" * 40)
print("s4:", s4)
print("_" * 40)
print("s5:", s5)
print("_" * 40)
print("s6:", s6)
print("_" * 40)
print("s7:", s7)
print("_" * 40)
print("s8:", s8)
print("_" * 40)
print("s9:", s9)
print("_" * 40)
print("s10:", s10)
print("_" * 40)
print("s11:", s11)
print("_" * 40)
print("s12:", s12)

v1 = 40
v2 = 60
v3 = 70
print(v1, "Hello", v2, "python", v3)

print("_" * 50)
s12 = "334 5.5 [5, 6, 7] ^&^*&^ Hello"
print(s12, type(s12))  # <class 'str'>

print("_" * 50)
str_a = "Python"

"""
 0  1  2  3  4  5  +ve
 P  y  t  h  o  n
-6 -5 -4 -3 -2  -1
"""

print(str_a[0])  # P
print(str_a[-6])  # P

print(str_a[-3])  # h

length = len(str_a)
print("length of string :", length)

print(str_a.index('o'))  # 4
print(str_a[2:4])  # th

print("_" * 50)
######################  List Data type ###############################
list1 = [5, 7, 22, 3.4, 'Hello', True]
print(list1, type(list1))
# [5, 7, 22, 3.4, 'Hello', True] <class 'list'>

"""
Properties :
1.  List is mutable data type, we can modify any point of time.
2.  List follows positive, negative indexing.
3.  List can contain all different data type, int, float, string, list, tuple, dict, set, bool.
4.  We define the list with square bracket.
"""
#            0       1   2   3   4           5        6        7
list2 = [(5, 6, 7), 6.6, 88, 22, [4, 6, 8], 'Hello', 'Python', 100]
#          -8       -7  -6   -5  -4         -3        -2       -1

print(list2)
# [44, 66, 88, 22, [4, 6, 8], 'Hello', 'Python', 100]
print(dir(list))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print(dir(str))

print("_" * 50)
#            0       1   2   3   4           5        6        7
list3 = [(5, 6, 7), 6.6, 88, 22, [4, 6, 8], 'Hello', 'Python', 100]
#          -8       -7  -6   -5  -4         -3        -2       -1

# Get hello from given list
print(list3[5])  # Hello
print(list3[-3])  # Hello

print(list3[5:7])  # ['Hello', 'Python']
print(list3[5], list3[6])  # Hello Python
print(list3[4])  # [4, 6, 8]
print(list3[4][1])  # 6

var1 = 'Name'
var2 = 'age'
var3 = 300
list4 = [var1, var2, var3]
print(list4)  # ['Name', 'age', 300]

list5 = [(6, 8, 9), {'a': 123, 'b': 567}, {4, 6, 8, 9}]
print(list5[0])  # (6, 8, 9)
print(list5[1])  # {'a': 123, 'b': 567}
print(list5[1]['a'])  # 123
print(list5[2])  # {8, 9, 4, 6}

print("_" * 50)
################################# Tuple datatype ###############################
tup1 = (5, 7, 'Hello', 3.5, True, [4, 5, 6], (2, 6))
print(tup1, type(tup1))
# (5, 7, 'Hello', 3.5, True, [4, 5, 6], (2, 6)) <class 'tuple'>

"""
# Properties of Tuple
->  Tuple is immutable data type, once it is defined, can not change.
->  Tuple can contain all different type of data
    int, float, string, list, tuple, dict, set, boolean
-> Tuple follows positive and negative indexing as like string, list
-> Tuple defined with round bracket.
"""

print("_" * 50)
#       0  1   2       3    4     5          6
tup2 = (5, 7, 'Hello', 3.5, True, [4, 5, 6], (2, 6), 5)
#      -7  -6  -5      -4   -3   -2          -1

# dir : dir return list of methods belongs to specific class
print(dir(tup2))  # 'count', 'index'

print(tup2[5])  # [4, 5, 6]
print(tup2.count(5))  # 2

length_tup = len(tup2)
print("length of tuple :", length_tup)

tup5 = tuple()
print(tup5, type(tup5))  # () <class 'tuple'>

print("_" * 50)
#################################### Dictionary Data Type ###################

dict1 = {'a': 345, 'b': 678, 'c': 123}
print(dict1, type(dict1))
# {'a': 345, 'b': 678, 'c': 123} <class 'dict'>

"""
# properties of dictionary
-> Dictionary is mutable data type, we can modify and update.
-> Dictionary only contains unique key, duplicate keys are not allowed.
-> Dictionary store data in key value format
-> Dictionary only contains immutable data type as key, int, float, string, tuple , boolean.
   ->  list, dict, set can not be key in dict.

->  Dictionary can contain all different data types as value
    ->  for dict there is no restriction, it can contains all types of data 
        int, float, string, list, tuple, dict, set, boolean
->  Dictionary does not follow indexing.
->  Dictionary follows LIFO (Last In First Out)
"""

# get value from dictionary
dict2 = {'Name': 'Rahul', 'Age': 25, 'City': 'Mumbai', 'Email': 'rahul@gmail.com'}
print(dict2['Email'])

# add data to dictionary
dict2['phone'] = 647567567
print(dict2)

dict2.pop('City')
print(dict2)

print("_" * 50)
var1 = 1000
val2 = {'em_name': 'Vishal', 'emp_salary': 500000, 'designation': 'software engineer'}
dict3 = {
    123: 3.5,
    3.5: 'Hello',
    'Python': [5, 6, 8, 9],
    # [1, 3, 4] : (4, 5, 6)  #   TypeError: unhashable type: 'list'
    (4, 7, 1): {'a': 123, 'b': 456},
    # 123 : 500  # duplicate are not allowed
    var1: 'Programming',
    'emp_details': val2,
}

from pprint import pprint

# print(dict3)
pprint(dict3)

dict4 = {3.5: 'Hello',
         123: 3.5,
         1000: 'Programming',
         'Python': [5, 6, 8, 9],
         'emp_details': {'designation': 'software engineer',
                         'em_name': 'Vishal',
                         'emp_salary': 500000},
         (4, 7, 1): {'a': 123, 'b': 456}}

print(dict4['emp_details']['em_name'])  # Vishal

print("_" * 50)
#################################### Python Sets #############################
set1 = {55, 12, 3, 5.5, 6, 7, 3, 7, 2, 7}

print(set1, type(set1))
# {2, 3, 5.5, 6, 7} <class 'set'>

"""
# properties:
->  Set is mutable data type, we can modify it at any point of time.
->  Set only store unique values, duplicate data is not allowed.
->  Set store data in random order and print values in random order.
->  Set only contains immutable data type as set member
    int, float, string, tuple, boolean.
->  Set does not follow indexing or key value paid format
"""

set2 = {44, 77, 22, 'Hello', (4, 6, 7, 6), True, 44, (4, 6, 6, 7)}
print(set2)
# {True, 22, (4, 6, 7), 'Hello', 44, 77}

tup1 = (4, 6, 6, 6, 6, 6, 9)
print(tup1)

print("_" * 50)
# add value to the set
set2.add(100)
print(set2)
set2.add(100)  # It won't through error if we try to add same value again.
print(set2)
# {True, (4, 6, 7, 6), 100, 'Hello', 22, (4, 6, 6, 7), 44, 77}

print(dir(set))  # dir return list of method belongs to specific data type
"""
'add', 'clear', 'copy', 'difference', 'difference_update',
 'discard', 'intersection', 'intersection_update', 'isdisjoint', 
 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
  'symmetric_difference_update', 'union', 'update'
"""

# set3 = {4, 5, 6, [4, 5, 7]}
# print(set3)
# TypeError: unhashable type: 'list'
# can not add list/dict/set as member of set
# list/dict/set is mutable datatype which is not allowed in the set.


print("_" * 50)
##################### Boolean ######################
# boolean data type only contains 2 values True and False
var1 = True
print(var1, type(var1))  # True <class 'bool'>

var2 = False
print(var2, type(var2))

print(dir(bool))
# 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

# print(var1.to_bytes()) # b'\x01'


n1 = 500
n2 = 600
print(n1 + n2)
print(n1.__add__(n2))
