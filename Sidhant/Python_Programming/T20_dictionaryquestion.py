# 1). Python Dictionary program to add elements to the dictionary.
dict1 = {'a': 1, 'b': 1, "c": 3, 'd': 4}
print( dict1 )

# 2). Python Dictionary program to print the square of all values in a dictionary.
dict1 = {'a': 11, 'b': 12, "c": 3, 'd': 4}
for val in dict1:
    print( val, ":", dict1[val] ** 2 )

# 3). Python Dictionary program to move items from dict1 to dict2.
dict1 = {'a':1,'b':2,'c':3,'d':4}
dict2 = dict1.copy()
print(dict2)

# 4). Python Dictionary program to concatenate two dictionaries.
dict1 = {'Name':'sid','class':10,'Roll_no':23}
dict2 = {'height':5,'colr':'brownish','Nationality':'indian'}
dict1.update(dict2)
print(dict1)

# 5). Python Dictionary program to get a list of odd and even keys from the dictionary.
dict1 = {1: 25, 5: 'abc', 8: 'pqr', 21: 'xyz', 12: 'def', 2: 'utv'}
even_dict = [[val, dict1[val]] for val in dict1 if val % 2 == 0]
odd_dict = [[val, dict1[val]] for val in dict1 if val % 2 != 0]
print( even_dict )
print( odd_dict )

# 6). Python Dictionary Program to create a dictionary from two lists.
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
dict1 = {}
for a, b in zip( list1, list2 ):
    dict1[a] = b
print( dict1 )

# 7).  Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
list1 = [4, 5, 6, 2, 1, 7, 11]
dict1 = {val: pow( val, 2 ) if val % 2 == 0 else pow( val, 3 ) for val in list1}
print( dict1 )

# 8). Python Dictionary program to clear all items from the dictionary.
dict1 ={'a':12,'b':23,'c':23,'d':45,'e':56}
dict1.clear()
print(dict1)

# 9). Python Dictionary program to remove duplicate values from Dictionary.
dict1 ={'a':12,'b':23,'c':23,'d':45,'e':56, 'f':23,'g':45}
dict2 ={}
for key,value in dict1.items():
    if value not in dict2.values():
        dict2[key]=value
print(dict2)

# 10). Python Dictionary program to create a dictionary from the string.
str1 = 'SQATools'
str2 ={}
for val in str1:
    str2[val]= str1.count(val)
print(str2)

# 11). Python Dictionary program to sort a dictionary using keys.
Input = {'d': 21, 'b': 53, 'a': 13, 'c': 41}
for key in sorted( Input ):
    print( f"{key} :", Input[key] )

# 12). Python Dictionary program to sort a dictionary in python using values.
Input = {'d': 21, 'b': 53, 'a': 13, 'c': 41}
sorted1 ={key:value for key,value in sorted(Input.items(), key= lambda item : item[1])}
print(sorted1)
# 13). Python Dictionary program to add a key in a dictionary.
dict1 = {'a':2,'b':3,'c':5}
dict1.update({'d':9})
print(dict1)

# 14). Python Dictionary program to concatenate two dictionaries.
D1 = {'name' : 'yash', 'city' :  'pune'}
D2 = {'course' : 'python', 'institute' : 'sqatools'}
D1.update(D2)
print(D1)

# 15). Python Dictionary program to swap the values of the keys in the dictionary.
dict1 = {'name': 'Sid', 'Class': 'classic'}
keys = list( dict1.keys() )
dict1[keys[0]], dict1[keys[1]] = dict1[keys[1]], dict1[keys[0]]
print( dict1 )

# 16). Python Dictionary program to get the sum of all the items in a dictionary.
Input = {'x' : 23, 'y' : 10 , 'z' : 7}
Tsum =0
for i in Input.values():
    Tsum+=i
print(Tsum)

# 17). Python Dictionary program to insert a key at the beginning of the dictionary.
dict1 ={'age':15,'role':'developer'}
dict2 ={'name':'Sidhant'}
dict2.update(dict1)
print(dict2)

# 18). Python Dictionary program to check whether a key exists in the dictionary or not.
dict1 = {'Virat': 'batter', 'Sports': 'Cricket'}
count = 0
for i in dict1.keys():
    if i == "Virat":
        count += 1
        if count > 0:
            print( 'key exist' )

        else:
            print( 'do not exist' )

#  19). Python program to iterate over a dictionary.
dict1 = {'food': 'burger','type':'fast food'}
for i in dict1.items():
    print(i)

#  20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2
dict1 = 5
dict2 ={}
for i in range(1,5+1):
    dict2.update({i:i**3})
print(dict2)







