"""
Types of Python Data Types:
1. Numbers
    i. Integer : Immutable
    ii. Float : Immutable
    iii. Complex Numbers : Immutable

2. Sequential
    i. String : Immutable
    ii. List : Mutable
    iii. Tuple : Immutable

3. Dictionary : Mutable
4. Set : Mutable
5. Boolean : Immutable

"""

#################  Integer Numbers ##############
print("Different examples of Integers")
n1 = 25
print(n1,type(n1))   # 25 <class 'int'>

"""
Properties of Integer
->  Integer is an immutable data type, once it is defined we can not change.
->  There is no limit for integer data type
->  Integer is always considered as a whole numbers (+ve and -ve both)
"""

n2 = 743563847534990934728489930
print(n2, type(n2))   # 743563847534990934728489930 <class 'int'>

n3 = 0
print(n3, type(n3))   # 0 <class 'int'>

n4 = -65364367
print(n4, type(n4))   # -65364367 <class 'int'>

# When we add 2 integers then sum will be also Integer
v1 = 34
v2 = 578
v3 = v1 + v2
print("Sum of numbers is: ",v3)    #Sum of numbers is:  612

print("_"*100)

####################### Float Numbers ############################

print("Different examples of Float numbers")

p1 = 23.988
print(p1, type(p1))   # 23.988 <class 'float'>

"""
# Properties of Float :
->  Float is an immutable data type
->  There is no specific limit for float data type
->  All the pointer values will be considered as float (Both positive and negative)

"""

p2 = 0.000
print("p2 :", p2, type(p2))  # p2 : 0.0 <class 'float'>
p3 = 0.000345000
print("p3 :", p3, type(p3))  # p3 : 0.000345 <class 'float'>
p4 = 11.343434334543
print("p4 :", p4, type(p4))  # p4 : 11.343434334543 <class 'float'>
p5 = 655464565654.1234
print("p5 :", p5, type(p5))  # p5 : 655464565654.1234 <class 'float'>

print("_"*100)

#################### Complex Numbers #########################
# complex number represent with x+yj
# x = real number
# y = imaginary number

print("Different examples of Complex Numbers")

c1 = 20 + 30j
print(c1, type(c1))   # (20+30j) <class 'complex'>

c2 = 34.34 + 46.28j
print(c2, type(c2))  # (34.34+46.28j) <class 'complex'>

c3 = c1 + c2
print(c3, type(c3))   # (54.34+76.28j) <class 'complex'>

c4 = c2*3              # Multiplying a complex number
print(c4, type(c4))    # (103.02000000000001+138.84j) <class 'complex'>

c5 = 55 + 38j
print("Real Number is: ",c5.real)
print("Imaginary number is: ",c5.imag)
# Real Number is:  55.0
# Imaginary number is:  38.0

c6 = int()
print(c6)   # 0

# p7 = 10 + 20i
# print("p7 : ",p7) # SyntaxError: invalid decimal literal

#     p7 = 10 + 20i
# IndentationError: unexpected indent

print("_"*100)


########################### String Data Type ##########################
print("String Datatype related Examples")

s1 = "Hello"
print(s1, type(s1))    # Hello <class 'str'>

s = str()
s0 = ""
s2 = ''
s3 = 'A'
s4 = "B"
s5 = 'Python'
s6 = "Hello we are learning Selenium with Python $$$$"
s7 = 'Python programming is easy 2324'
s8 = "Good morning 'Hope' you are good"
s9 = 'Very good "evening". Enjoy your party &&^&^  \nThere is gonna be a party tomorrow as well \n I will attend a party tomorrow'
s10 = """We are leaning Python programming.
'and' learning is fun. It's
very easy to understand this concept
"""
s11 = '''
Hello we are learning
Python Programming, 'and' 'learning is fun.
Its very "easy" understand
'''

var1 = "great"
s12 = "Have a"+var1+" day"

print("_"*40)
print("s :",s)   # s :
print("_"*40)
print("s0 :",s0)   # s0 :
print("_"*40)
print("s1: ",s1)   # s1:  Hello
print("_"*40)
print("s2: ",s2)   # s2:
print("_"*40)
print("s3:", s3)   # s3: A
print("_"*40)
print("s4:", s4)   # s4: B
print("_"*40)
print("s5:", s5)   # s5: Python
print("_"*40)
print("s6:", s6)   # s6: Hello we are learning Selenium with Python $$$$
print("_"*40)
print("s7:", s7)   # s7: Python programming is easy 2324
print("_"*40)
print("s8:", s8)   # s8: Good morning 'Hope' you are good
print("_"*40)
print("s9:", s9)
#  s9: Very good "evening". Enjoy your party &&^&^
# There is gonna be a party tomorrow as well
#  I will attend a party tomorrow
print("_"*40)
print("s10:", s10)
# s10: We are leaning Python programming.
# 'and' learning is fun. It's
# very easy to understand this concept
print("_"*40)
print("s11:", s11)
# s11:
# Hello we are learning
# Python Programming, 'and' 'learning is fun.
# Its very "easy" understand
print("_"*40)
print("s12:", s12)  #  s12: Have agreat day
print("_"*40)

v1 = 40
v2 = 60
v3 = 70
print(v1,"Hello",v2,"python",v3)    # 40 Hello 60 python 70
print("_"*40)

s12 = "334 5.5 [5, 6, 7] ^&^*&^ Hello"
print(s12, type(s12))   # 334 5.5 [5, 6, 7] ^&^*&^ Hello <class 'str'>
print("_" * 50)

str_a = "Python"

"""
    0   1   2   3   4   5      (Positive Indexing)
    P   y   t   h   o   n
   -6  -5  -4  -3  -2   -1     (Negative Indexing)
"""

print(str_a[2])   # t
print(str_a[-4])  # t

length = len(str_a)
print("Length of string is: ",length)    #  6

print("Index value of 'P' is: ",str_a.index('P'))   # Index value of 'P' is:  0
print(str_a[2:4])  # th   Slicing : where we are printing text between index 2 and 4. Substring.
print("_" * 100)


##########################  List Data Type ##############################

print("Examples of List Data Type")

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

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse',
# 'sort'

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

print("_" * 100)


######################## Tuple Data Type ########################

print("Tuple Data Type Examples")
tup1 = (5, 6, 'Hello', 3.5, True, [4, 5, 6], (2, 6))
print(tup1, type(tup1))
# (5, 6, 'Hello', 3.5, True, [4, 5, 6], (2, 6)) <class 'tuple'>

"""
# Properties of Tuple Data Type:
1. Tuple is immutable data type, it cannot be changed once defined.
2. Tuple can contain data of different data types : 
    int, float, string, list, tuple, dict, set, boolean
3. Tuple follows positive and negative indexing just like string, list
4. Tuple is defined with round brackets

"""

print("_" * 50)
#       0  1    2       3    4       5         6     7
tup2 = (5, 7, 'Hello', 3.5, True, [4, 5, 6], (2, 6), 5)
#      -8  -7  -6      -5    -4     -3         -2   -1

# dir : dir return list of methods belongs to specific class
print(dir(tup2))  # 'count', 'index'

print(tup2[5])  # [4, 5, 6]
print(tup2.count(5))  # 2

length_tup = len(tup2)
print("length of tuple :", length_tup)

tup5 = tuple()
print(tup5, type(tup5))  # () <class 'tuple'>

print("_"*50)

######################### Dictionary Data Type ########################

print("Example of Dictionary Data Type\n")

dict1 = {'a' : 345, 'b': 678, 'c': 123}
print(dict1, type(dict1))
# {'a': 345, 'b': 678, 'c': 123} <class 'dict'>

"""
# Properties of Dictionary Data Type :
 1. Dictionary is mutable data type so we can modify and update it.
 2. Dictionary should contain unique keys and duplicate keys are not allowed
 3. Dictionary stores data in Key : Value format
 4. Dictionary contains only immutable data types as keys :
     int, float, complex num, string, tuple, boolean
     list, set, dict cannot be used as key
 5. Dictionary can contain all different data types as value.
     for dict there is no restriction, it can contains all types of data 
        int, float, string, list, tuple, dict, set, boolean
 6. Dictionary does not follow indexing
 7. Dictionary follows LIFO [Last in first out]

"""

# get value from dictionary:
dict2 = {'name' : 'Rahul', 'Age' : 25, 'City' : 'Mumbai', 'Email' : 'rahul@gmail.com'}
print("Email of Rahul is: ",dict2['Email'])

# add data to dictionary :
dict2['Phone'] = 2771236
print("Dictionary after updating with Phone number: \n",dict2)

# remove data from dictionary
dict2.pop('City')
print("Dictionary after removing City :\n", dict2)

print("_"*80)

var1 = 1000
val2 = {'em_name' : 'Vishal', 'emp_salary': 500000, 'designation': 'software engineer'}
dict3 = {
         123: 3.5,
         3.5 : 'Hello',
         'Python' : [5, 6, 8, 9],
          # [1, 3, 4] : (4, 5, 6)  #   TypeError: unhashable type: 'list'
         (4, 7, 1) : {'a' : 123, 'b' : 456},
         # 123 : 500  # duplicate key are not allowed
         var1 : 'Programming',
         'emp_details' : val2,
       }

from pprint import pprint

pprint(dict3)      # formatted output

dict4 = {3.5: 'Hello',
 123: 3.5,
 1000: 'Programming',
 'Python': [5, 6, 8, 9],
 'emp_details': {'designation': 'software engineer',
                 'em_name': 'Vishal',
                 'emp_salary': 500000},
 (4, 7, 1): {'a': 123, 'b': 456}}

print(dict4['emp_details']['em_name']) # Vishal
print(dict4[3.5])  # Hello
print(dict4[(4,7,1)]['a'])  # 123
print("_"*80)

#############################  Set Data Type. ###################

print("Examples of Set Data Type\n")
set1  = {55, 12, 3, 5.5, 6, 7, 3, 7, 2, 7}

print(set1, type(set1))
# {2, 3, 5.5, 6, 7} <class 'set'>

"""
# Properties of Set Data Type:
1. Set is a mutable data type, it can be modified at at any point of time.
2. Set only stores unique values, duplicates are eliminated automatically
3. Set stores data in random order and prints also in random order
4. Set contains only immutable data type values
    int, float, String, tuple, boolean
5. Set does not follow indexing or key value format

"""

set2 = {44, 77, 22, 'Hello', (4, 6, 7, 6), True, 44, (4, 6, 6, 7)}
print(set2) # {True, (4, 6, 7, 6), 'Hello', 22, (4, 6, 6, 7), 44, 77}

# add value to set
set2.add(100)
print("Set after adding value: \n", set2)
# Set after adding value:
#  {True, (4, 6, 7, 6), 100, 'Hello', 22, (4, 6, 6, 7), 44, 77}
set2.add(100) # It won't through error if we try to add same value again.
print(set2)
# {True, (4, 6, 7, 6), 100, 'Hello', 22, (4, 6, 6, 7), 44, 77}
print("_"*80)

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


print("_"*80)

####################### Boolean Data Type #############################

print("Examples of Boolean Data Type\n")

var1 = True
print(var1, type(var1))  #True <class 'bool'>

var2 = False
print(var2, type(var2))

print(dir(bool))
# 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag',
# 'is_integer', 'numerator', 'real', 'to_bytes']

n1 = 500
n2 = 600
print(n1+n2)
print(n1.__add__(n2))






