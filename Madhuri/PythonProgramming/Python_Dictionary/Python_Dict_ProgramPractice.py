# 1). Python Dictionary program to add elements to the dictionary.
dict1 = {}
dict1["id"] = "1"
dict1["Name"] = "Mohit"
dict1["age"] = "25"

print(dict1) #{'id': '1', 'Name': 'Mohit', 'age': '25'}


print("#"*50)
#2). Python Dictionary program to print the square of all values in a dictionary.
dict2 = {'a': 5, 'b':3, 'c': 6, 'd': 8}
"""
Output :
a : 25
b : 9
c : 36
d : 64
"""

for val in dict2:
    print(val, ":" , dict2[val]**2)

"""
{'id': '1', 'Name': 'Mohit', 'age': '25'}
a : 25
b : 9
c : 36
d : 64
"""

print("#"*50)
""" Need to ask deepesh  
3). Python Dictionary program to move items from dict1 to dict2.
Input :
dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
dict2 = {}
Output :
dict1 = {}
dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
"""

dict3a = {'name' : 'john', 'city':'Landon', 'country' : 'UK'}
dict3b = {}

for val in dict3a:
    dict3b[val] = dict3a[val]

print(dict3a) #{'name': 'john', 'city': 'Landon', 'country': 'UK'}
print(dict3b) #{'name': 'john', 'city': 'Landon', 'country': 'UK'}

# OR
dict3b = dict3a
print(dict3b) #{'name': 'john', 'city': 'Landon', 'country': 'UK'}
print(dict3b) #{'name': 'john', 'city': 'Landon', 'country': 'UK'}


print("#"*50)

#4). Python Dictionary program to concatenate two dictionaries.
dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict2 = {'Age' : 25, 'salary':'$25k'}
#Output :
#dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}

#dict3 = dict1 + dict2
#print(dict3) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

dict1.update(dict2)
print(dict1) #{'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan', 'Age': 25, 'salary': '$25k'}


print("#"*50)
"""
5). Python Dictionary program to get a list of odd and even keys from the dictionary.
Input :
{1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’}
Output :
Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
"""
print("#"*50)
"""
6). Python Dictionary Program to create a dictionary from two lists.
Input :
list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
list2 = [12, 23, 24, 25, 15, 16]
Output :
{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}
"""
print("#"*50)
"""
7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
Input :
[4, 5, 6, 2, 1, 7, 11]
Output :
{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
"""
print("#"*50)
"""
8). Python Dictionary program to clear all items from the dictionary.
"""

dict8 = {'Name':'Harry','Rollno':345,'Address':'Jordan'}
dict8.clear()
print(dict8) #{}


"""
9). Python Dictionary program to remove duplicate values from Dictionary.
Input :
{‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
Output :
{‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
"""

dict9 = {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
Output9 = {}

for key,val in dict9.items():
    if val not in Output9.values():
        Output9[key] = val

print(Output9) #{'a': 12, 'b': 2, 'd': 5, 'e': 35}



