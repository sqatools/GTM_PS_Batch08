print("_" * 70)
# 1). Python Dictionary program to add elements to the dictionary.
dict1 = {'a': "Pankaj", 'b': 77, 'c': 'D', 'e': 33.3, 'f': True}
print(dict1, type(dict1))

print("_" * 70)
"""
2). Python Dictionary program to print the square of all values in a dictionary.
Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
Output :
a : 25
b : 9
c : 36
d : 64
"""
dictionary = {'a': 5, 'b': 3, 'c': 6, 'd': 8}
for val in dictionary:
    print(val, ":", dictionary[val] ** 2)

print("_" * 70)
"""
3). Python Dictionary program to move items from dict1 to dict2.
Input :
dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
dict2 = {}
Output :
dict1 = {}
dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
"""
D1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
D2 = {}
for val in D1:
    D2[val] = D1[val]
print(D2)

print("_" * 70)
""" 
4). Python Dictionary program to concatenate two dictionaries.
Input :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’}
dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
Output :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}
"""
dict1 = {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan'}
dict2 = {'Age': 25, 'salary': '$25k'}
dict1.update(dict2)
print(dict1)
