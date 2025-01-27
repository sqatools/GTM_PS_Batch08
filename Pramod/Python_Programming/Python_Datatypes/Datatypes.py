"""
1) Integer == 123
2) Float == 2.4
3) Complex == 1+2j
4) String == "Good morning"
5) list1 = [5, 7, 22, 3.4, 'Hello', True] == mutable data type, we can modify any point of time.
6) Tupple == (5, 'Hii', 3.5, True, [4, 6], (2, 6)) ==is immutable data type, once it is defined, can not change.
7) Set== {55, 12, 3, 5.5, 6, 2, 7} only store unique values, duplicate data is not allowed.== mutable data type,
8) Distonary == dict2 = {'Name': 'Rahul', 'Age' : 25, 'City' : 'Mumbai',}
9) Boolean = True or false

##################################### Integer data type #############################################
1. Integer='554'
Properties of Integer
->  Integer is a immutable data type, once it is defined we can not change.
->  There is no limit for integer data type
->  Integer always consider a whole numbers (+ve and -ve both)

n2 = 8098908989080980980
print(n2, type(n2))
# 8098908989080980980 <class 'int'>

##################################### Float data type #############################################

2. Float='4.5'
# properties of float
->  Float is immutable data type
->  There is no specific limit for float data type
->  All the pointer values will be consider as float (Both positive and negative)
p1 = 50.56
print(p1, type(p1))
# 50.56 <class 'float'>

##################################### Complex data type #############################################

3. Complex='4+5j'
# complex number represent with x+yj
# x = real number
# y = imaginary number

q1 = 10 + 20j
print(q1, type(q1))
# (10+20j) <class 'complex'>
##################################### string data type #############################################

4. String="Hello, Good Morning"

s1 = "Hello"
print(s1, type(s1))
# Hello <class 'str'>

# properties
->  String is immutable data type, we can not modify.
->  Anything with single/double/triple quote will consider as string
->  String follows positive and negative indexing.
->  String can contain any type of data, int, str, float, special character etc.

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
s10 = "Hello we are learning
Python Programming, 'and' 'learning is fun.
Its very "easy" understand"

######################  List Data type ###############################
list1 = [5, 7, 22, 3.4, 'Hello', True]
print(list1, type(list1))
# [5, 7, 22, 3.4, 'Hello', True] <class 'list'>


Properties :
1.  List is mutable data type, we can modify any point of time.
2.  List follows positive, negative indexing.
3.  List can contain all different data type, int, float, string, list, tuple, dict, set, bool.
4.  We define the list with square bracket.

list of methods belongs to specific class:
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

################################# Tuple datatype ###############################
tup1 = (5, 7, 'Hello', 3.5, True, [4, 5, 6], (2, 6))
print(tup1, type(tup1))
# (5, 7, 'Hello', 3.5, True, [4, 5, 6], (2, 6)) <class 'tuple'>

# Properties of Tuple
->  Tuple is immutable data type, once it is defined, can not change.
->  Tuple can contain all different type of data
    int, float, string, list, tuple, dict, set, boolean
-> Tuple follows positive and negative indexing as like string, list
-> Tuple defined with round bracket.

#################################### Dictionary Data Type ###################
dict1 = {'a' : 345, 'b': 678, 'c': 123}
print(dict1, type(dict1))
# {'a': 345, 'b': 678, 'c': 123} <class 'dict'>


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

ex: dict2 = {'Name': 'Rahul', 'Age' : 25, 'City' : 'Mumbai', 'Email' : 'rahul@gmail.com'}
print(dict2['Email'])

#################################### Sets  Data type #############################
set1  = {55, 12, 3, 5.5, 6, 7, 3, 7, 2, 7}

print(set1, type(set1))
# {2, 3, 5.5, 6, 7} <class 'set'>

# Properties:
->  Set is mutable data type, we can modify it at any point of time.
->  Set only store unique values, duplicate data is not allowed.
->  Set store data in random order and print values in random order.
->  Set only contains immutable data type as set member
    int, float, string, tuple, boolean.
->  Set does not follow indexing or key value paid format

##################### Boolean ######################
# boolean data type only contains 2 values True and False
var1 = True
print(var1, type(var1))  #True <class 'bool'>

var2 = False
print(var2, type(var2))

print(dir(bool))
# 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

#print(var1.to_bytes()) # b'\x01';
"""

