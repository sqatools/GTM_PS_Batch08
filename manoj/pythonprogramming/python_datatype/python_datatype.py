"""

types of python data types
1.Number
 a) Integer : Immutable
 b)Float : Immutable
 c)complex number : Immutable

2.Sequential
 a) string : Immutable
 b) list : mutable
 c)Tuple : Immutable

3.Dictionary : mutable
4.set : mutable
5.Boolean : Immutable
"""
########## Integer data type ######
n1 = 30
print(n1, type(n1))
# 30 <class 'int'>
"""
Properties of Integer
-> Integer is a immutable data type , once it is defined we can not change.
-> There is no limit for integer data type
-> Integer always consider a whole number (positive and negative both) .
"""

n2 = 8938299332020
print(n2, type(n2))
# 8938299332020 <class 'int'>

n3 = 0
print(n3, type(n3))
# 0 <class 'int'>

n4 = -73882
print(n4, type(n4))
# -73882 <class 'int'>

# when we add 2 integer value then output will be integer only
v1 = 230
v2 = 345
v3 = v1 + v2
print("v3:", v3, type(v3))
# v3 :575 <class 'int'>

print("_"*40)
############ Float ###########
p1 = 50.57
print(p1, type(p1))
# 50.57 <class 'float'>

"""
# properties of float
-> Float is immutable data type
-> There is no specific limit for float dataa type
-> All the pointer values will be consider as float(both positive and negative)

"""

v2 = 50 + 50.57
print(v2, type(v2))

p2 = 0.0
print("p2 :", p2, type(p2))  # p2 : 0.0 <class 'float'>
p3 = 0.000456
print("p3 :", p3, type(p3))  # p3 : 0.000456 <class 'float'>
p4 = 12.342234
print("p4 :", p4, type(p4))  # p4 : 12.342234 <class 'float'>
p5 = 34444444445.33
print("p5 :", p5, type(p5))   # p5 : 34444444445.33 <class 'float'>

print("_"*50)

############# complex number ########
# complex number represent with x+yj
# x = real number
# y = imaginary number

q1 = 10 + 20j
print(q1, type(q1))
# (10+20j) <class 'complex'>

q2 = 3.4 + 44.4j
print(q2, type(q2))
# (3.4+44.4j) <class 'complex'>

result = q1 + q2
print(result, type(result))
# (13.4+64.4j) <class 'complex'>

# complex number
q4 = q1*2
print("multiplication :", q4, type(q4))
# (20+40j) <class 'complex'>

q5 = 55+60j
print("real number :", q5.real)  # 55.0
print("imaginary number :", q5.imag)  # 60.0

q6 = int()

print(q6)


# p7 = 10 + 20i
# print(p7)
print("_"*50)
############## string data type ###########3

s1 = "Hello"
print(s1, type(s1))
# Hello  <class 'str'>
""""
# properties
-> string is immutable data type, we cam not modify
-> anything with single/double/tripe quote will consider
-> string follows positive and negative indexing
-> string can contain any type of data , int, star
"""

s = str()
s0 = ''
s2 = ""
s3 = 'A'
s4 = 'B'
s5 = 'Python'
s6 = "Hello we are learning python @@@@@"
s7 = 'python programming is 3453'
s8 = "good evening 'how' are you **"
s9 = 'very good "morning" , good @#$%^&*'
s10 = """ 
hello we are learning python programming, and learning is fun.
its very "easy" understand        
"""
s11 = '''
hello we are learning
python programming, 'and' 'learning is fun. 
Its very "easy" understand
'''
var1 = "nice"
s12 = " Have a "+var1+" day "

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
print(v1, "hello", v2, "python", v3)

s12 = "334 4.5 [5,7,9] @#$%&( hello"
print(s12, type(s12)) # <class 'str'>

print("_"*50)
str_a = "python"

"""
0 1 2 3 4 5 +ve
p y t h o n
-6 -5 -4 -3 -2 -1 -ve
"""

print(str_a[0])  # p
print(str_a[-6])  # p

print(str_a[-3])  # h

length = len(str_a)
print("length of string :", length)

print("_"*50)

############# list data type ###########
list1 = [5, 7, 22, 3.4, 'hello', True]
print(list1, type(list1))

"""
properties :
1. List is mutable data type, we can modify any point of time.
2. List follows positive,negative indexing.
3. List can contain all different data type, int, float, string,list,tuple,dict,set,bool
4. we define the list with square bracket
"""

list2 = [(4 ,5 ,6), 66, 88, 22, [4, 6, 8], 'hello', 'python']


list2.append(100)
print(list2)
# [44, 66, 88, 22, [4, 6, 8], 'hello', 'python', 100]
print(dir(list))

#  'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(dir(str))


#          0         1   2  3      4         5         6
list3 = [(4, 5, 6), 66, 88, 22, [4, 6, 8], 'hello', 'python', 100]
#           -8      -7  -6  -5   -4           -3       -2      -1

# get hello from given list
print(list[5])  # hello
print(list3[-3])  # hello

var1 = 'Name'
var2 = 'age'
var3 = 300
list4 = [var1, var2, var3]
print(list4)  # ['Name', 'age', 300]

list5 = ([6, 8, 9]),

################## tuple data type ###############
tup1 = (5, 7, 'Hello', 3.5, [4, 5, 6],(2, 6))
print(tup1, type(tup1))
# (5, 7, 'Hello', 3.5, [4, 5, 6], (2, 6)) <class 'tuple'

"""

# properties of Tuple
-> Tuple is immutable data type, once it is defined, can not change
-> Tuple can contain all different type of data
   int, float, string, list, tuple, dict, set, boolean
-> Tuple follows positive and negative indexing as like string,list
-> Tuple defined with round bracket.
"""

#       0  1    2        3   4        5         6
tup2 = (5, 7, 'Hello', 3.5, True, [4, 5, 6], (2, 6), 5)
#       -7 -6  -5       -4    -3      -2         -1


# dir :  dir return list of methods belongs to specific names
print(dir(tup2))  # 'count', 'index'

print(tup2[5])  # [4, 5, 6]
print(tup2.count(5)) # 2

length_tup = len(tup2)
print("length of tuple :", length_tup)  # length of tuple : 8

tup5 = tuple()
print(tup5, type(tup5)) # () <class 'tuple'>


############# dictionary data type #######

dict1 = {'a': 345, 'b': 678, 'c': 123}

print(dict1, type(dict1))
#  {'a': 345, 'b': 678, 'c': 123} <class 'dict'>


"""
# properties of dictionary

->Dictionary is mutable data type, we can modify and update
->Dictionary only contains unique key, duplicate keys are not allowed
->Dictionary store data in key value format
->Dictionary only contains immutable data type as key, int, float, string, tuple, boolean
    ->list, dict, set can not be in dict
->Dictionary can contain all different data types as value
    ->for dict there is no restriction, it can contain all types of data
    int, float, string, list, tuple, dict, set, boolean
->Dictionary does not follow indexing
-Dictionary follows LIFO(Last In First Out)

"""

# get value from dictionary
dict2 = {'Name': 'Rahul', 'Age': 26, 'City': 'Hyderabad', 'Email': 'rahul1@gmail.com'}
print(dict2['Email'])

# add data to dictionary
dict2['phone'] = 78945215
print(dict2)

dict2.pop('City')
print(dict2)
