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

print("#"*50)

"""
10). Python Dictionary program to create a dictionary from the string.
Input  = ‘SQATools’
Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
"""

str10 = 'SQATools'
dict10 = {}

for char in str10:
    dict10[char] = str10.count(char)
print(dict10)  #{'S': 1, 'Q': 1, 'A': 1, 'T': 1, 'o': 2, 'l': 1, 's': 1}



print("#"*50)

"""
11). Python Dictionary program to sort a dictionary using keys.
Input = {‘d’ : 21, ‘b’ : 53,  ‘a’: 13, ‘c’: 41}
Output =
(‘a’, 13)
(‘b’, 53)
(‘c’, 41)
(‘d’, 21)
"""

dict11 = {'d':21, 'b': 53, 'a': 13 , 'c' : 4}

for key in sorted(dict11):
    print(key, dict11[key])

"""
output:

a 13
b 53
c 4
d 21
"""

"""
12). Python Dictionary program to sort a dictionary in python using values.
Input = {‘d’ : 14, ‘b’ : 52,  ‘a’: 13, ‘c’: 1 }
Output= (c, 1) (a,13) (d, 14) (b, 52)
"""


print("#"*50)
"""
13). Python Dictionary program to add a key in a dictionary.
Input= {1:’a’, 2:’b’}
Output= (1:’a’, 2:’b’, 3:’c’}
"""

dict13 = {1:'a', 2:'b'}
dict13.update({3:'c'})
print(dict13) #{1: 'a', 2: 'b', 3: 'c'}


print("#"*50)

"""
14). Python Dictionary program to concatenate two dictionaries.
Input:
D1 = {‘name’ : ’yash’, ‘city’ :  ‘pune’}
D1 = {‘course’ : ’python’, ‘institute’ : ’sqatools’}
Output :
{ ‘name’ : ’yash’, city: ‘pune’, ‘course’ : ’python’, ‘institute’ : ’sqatools’ }
"""

D1 = {'name':'yash' , 'city': 'pune'}
D2 = {'cource': 'python', 'institute' : 'sqatools'}

D1.update(D2)
print(D1) #{'name': 'yash', 'city': 'pune', 'cource': 'python', 'institute': 'sqatools'}

print("#"*50)

"""
15). Python Dictionary program to swap the values of the keys in the dictionary.
Input = {name:’yash’, city: ‘pune’}
Output = {name:’pune’, city: ‘yash’}

Dict1 = {'name' : 'yash', 'city':'pune'}
Dict2 = {}
for key1, value1 in Dict1.items():
    value1[key1] = value1
    Dict2[key1] = value1
print(Dict2)

"""

"""
Dict1 = {'name' : 'yash', 'city':'pune'}
Dict2 = {}
for key1, value1 in Dict1.items():
    Dict2[value1] = key1
print(Dict2) #{'yash': 'name', 'pune': 'city'}
"""

"""
16). Python Dictionary program to get the sum of all the items in a dictionary.
Input = {‘x’ : 23, ‘y’ : 10 , ‘z’ : 7}
Output = 40
"""

Dict16 = {'x': 23, 'y' : 10 , 'z' : 7}
sum = 0
for val in Dict16.values():
    sum = sum+val
print(sum) #40


"""
17). Python program to get the size of a dictionary in python.
Hint : use sys.getsizeof(var) method.
Input = {‘name’ : ’virat’, ‘sport’ : ’cricket’}
Output = 232bytes


Dict17 = {'name':'virat', 'sport':'cricket'}
str17 = str(sys.getsizeof(Dict17))
print(str17)
"""

print("#"*50)
"""

18). Python Dictionary program to check whether a key exists in the dictionary or not.
Input:
Dict1 = {city:’pune’, state=’maharashtra’}
Dict1[country]
Output= ‘key does not exist in dictionary
"""

Dict18 = {'city': 'pune', 'state':'maharashtra'}
count = 0
for key in Dict18.keys():
    if key == "Country":
        count = count+1

if count > 0:
    print("It is Exist")
else:
    print("Key not Exist")
#Key not Exist

print("#"*50)

"""
19). Python program to iterate over a dictionary.
Input :
Dict1 = {food:’burger’, type:’fast food’}
Output :
food : burger
type : fast food
"""

Dict19 = {'food':'burger' , 'type':'fast food'}

for val in Dict19:
    print(val,Dict19[val])

"""
20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
Input: n=4
Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}
"""
"""
Dict20 = {1:1, 2:8, 3:27, 4:64}

Dict[20] = {}
for key, val in Dict20():
    Dict20[key] = val**3
print(Dict20)
"""

print("#"*50)
n = 4
Dict20 = {}

for i in range(1, 4+1):
    Dict20.update({i:i**3})

print(Dict20) #{1: 1, 2: 8, 3: 27, 4: 64}

print("#"*50)

"""

21). Python Dictionary program to insert a key at the beginning of the dictionary.
Input = { ‘course’ : ’python’,  ‘institute’ : ’sqatools’ }
Insert : ( ‘name’ : ’omkar’ )
Output= { ‘name’ : ’omkar’, ‘course’ : ’python’, ‘institute’ : ’sqatools’}
"""

Dict21 = {'cource': 'python', 'institute':'sqatools'}

Dict21_B = {'name':'omkar'}

Dict21.update(Dict21_B)
print(Dict21)  #{'cource': 'python', 'institute': 'sqatools', 'name': 'omkar'}
# ask to Deepesh


print("#"*50)


"""
22). Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.
Output ={1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}
"""


Dict22 = {}

for key in range(1,6):
    Dict22[key] = key**2
print(Dict22) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


"""
23). Python Dictionary program to find the product of all items in the dictionary.
Input = { ‘a’ : 2, ‘b’ : 4, ‘c’ : 5}
Output = 40
"""

dict23 = {'a':2, 'b':4, 'c':5}
result23 = 1

for val in dict23.values():
    result23 = result23 * val

print(result23) #40


"""
26). Python Dictionary program to find maximum and minimum values in a dictionary.
Input :
Dict = { ‘a’ : 10, ‘b’ : 44 , ‘c’ : 60, ‘d’ : 25}
Output :
Maximum value: 60
Minimum value: 10
"""

dict26 = {'a' : 10,'b':44,'c':60,'d':25}

list26= list(dict26)
print(max.dict26[val])
print(min.dict26[val])