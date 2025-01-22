#Integer data type

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

#Float

a1 = 10.45
print(a1, type(a1))

#complex
b1= 10+20j
print(b1, type(b1))

#String data type
c1 = "Hello"
print(c1, type(c1))

C2 = " "
C3 = 'A'
C4 = 'Python'
print(C2, C3, C4)

z1 = "Python"
print(z1[1])
print(len(z1))

#List datatype

list1 = [1, 2, 'three', 'four', [5, 6], 'seven']
print(list1)

print(list1[4])

print(list1[2], list1[5])

#Tuple data type
tup1 = (11, 12, 13, 'Forteen', [15, 16, 17],)
print(tup1)

print(dir(tup1))

print(tup1[-1])
print(tup1.count(5))
print(tup1.count([15, 16, 17]))

#dicstionary data type

dic1 = {'a': 123, 'b': 456, 'c': 789, 'd': [1, 2, 3], 'e': (4, 'five', 'six')}
print(dic1)

dic2 = {'name': 'vishal',
        'age': 31,
        'email': 'abc@outlook.com'}
print(dic2)

dic2['phone'] = 1234567890
print(dic2)

dic2.popitem()
print(dic2)
from pprint import pprint

dic3 = {'a': dic2, 'b': dic1}
pprint(dic3)

pprint(dic2)

#Sets data type
set1 ={1,2,3.5,6.7,8,8,3.5,100, 1000, 103}
print(set1)

#Boolean data type

# It contains only two values - Tre and False
var1 = True
print(var1)



