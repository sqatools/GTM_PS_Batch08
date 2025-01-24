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

print("_" * 50)
print("######## String Data Type #########")
s="Hello"
print(s,type(s)) # Hello <class 'str'>

""""
 Properties of String:
                        -->String is immutable data type, we can not modify.
                        -->Anything with single/double/triple quote will consider as string.
                        -->String follows positive and negative indexing.
                        -->String can contain any type of data, int, str, float, special character etc.
"""
print("_" * 40)
s = str() # empty String
print(s)

print("_" * 40)
s0 = '' # empty strings2 = "" # empty string
print(s0)

print("_" * 40)
s3 = 'A'
print(s3)

print("_"*40)
s4 = "B"
print(s4)

print("_"*40)
s5 = 'Python'
print(s5)

print("_"*40)
s6 = "Hello we are learning Python $$$$"
print(s6)

print("_"*40)
s7 = 'Python programming easy is 45334'
print(s7)

print("_"*40)
s8 = "Good Morning 'Hope' you are good **&*"
print(s8)

print("_"*40)
s9 = 'Very good "evening", enjoy your party ^^%$^^-\n gfsadfgj;lkjkj   jjkljklhuuiyrwqeb \nqafhhjdsahfjskdhflk'
print(s9)

print("_"*40)
s10 = """ Hello we are learning
Python Programming, 'and' 'learning is fun.
Its very "easy" understand
"""
print(s10)

print("_"*40)
s11 = '''
Hello we are learning
Python Programming, 'and' 'learning is fun.
Its very "easy" understand
'''
print(s11)

print("_"*40)
var1 = "nice"
s12 = "Have a" + var1 + " day"
print(s12)

print("_" * 40)
v1 = 40
v2 = 60
v3 = 70
print(v1, "Hello", v2, "python", v3)

print("_" * 50)
s12 = "334 5.5 [5, 6, 7] ^&^*&^ Hello"
print(s12, type(s12))  # <class 'str'>

print("_" * 50)
print("?????????????????????????????????????")
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
print("################### List data type ###############################")
list1 = [5, 7, 22, 3.4, 'Hello', True]
print(list1, type(list1))
# [5, 7, 22, 3.4, 'Hello', True] <class 'list'>

"""
Properties of List:
            -->  List is mutable data type, we can modify any point of time.
            --> List follows positive, negative indexing.
            --> List can contain all different data type, int, float, string, list, tuple, dict, set, bool.
            --> We define the list with square bracket.
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
print("################### Tuple data type ###############################")
tup1 = (5, 7, 'Hello', 3.5, True, [4, 5, 6], (2, 6))
print(tup1, type(tup1))
# (5, 7, 'Hello', 3.5, True, [4, 5, 6], (2, 6)) <class 'tuple'>

"""
# Properties of Tuple
                    -->  Tuple is immutable data type, once it is defined, can not change.
                    -->  Tuple can contain all different type of data
                          int, float, string, list, tuple, dict, set, boolean
                    --> Tuple follows positive and negative indexing as like string, list
                    --> Tuple defined with round bracket.
"""

print("_" * 50)
#       0  1   2       3    4     5          6
tup2 = (5, 7, 'Hello', 3.5, True, [4, 5, 6], (2, 6), 5)
#      -7  -6  -5      -4   -3   -2          -1

#           Note: dir : dir return list of methods belongs to specific class

print(dir(tup2))  # 'count', 'index'

print(tup2[5])  # [4, 5, 6]
print(tup2.count(5))  # 2

length_tup = len(tup2)
print("length of tuple :", length_tup)

tup5 = tuple()
print(tup5, type(tup5))  # () <class 'tuple'>





