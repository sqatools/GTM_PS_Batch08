# 1.Python Dictionary program to print the square of all values in a dictionary.
# Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
# Output :
# a : 25
# b : 9
# c : 36
# d : 64
print("1. Python Dictionary program to print the square of all values in a dictionary")
Input = {'a': 5, 'b':3, 'c': 6, 'd' : 8}

for k, v in Input.items():
    val = v ** 2
    print(k ,":",val)
print("_"*50)


#2. Python Dictionary program to move items from dict1 to dict2.
#Input :
dict1 = {'name': 'john', 'city': 'London', 'country': 'UK'}
dict2 = {}
#Output :
#dict1 = {}
#dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}

print("2. Python Dictionary program to move items from dict1 to dict2")
dict2 = dict1.copy()
print("Dict2: ",dict2)
dict1.clear()
print("Dict1: ",dict1)
print("_"*50)


# 3. Python Dictionary program to concatenate two dictionaries.
# Input :
dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict2 = {'Age' : 25, 'salary': '$25k'}
# Output :
# dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}

print("3. Python Dictionary program to concatenate two dictionaries.")
dict1.update(dict2)
print(dict1)
print("_"*50)


# 4. Python Dictionary program to get a list of odd and even keys from the dictionary.
dict1 = {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
# Output :
# Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
# Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]

print("4. Python Dictionary program to get a list of odd and even keys from the dictionary")
evenKey = [[val,dict1[val]] for val in dict1 if val%2 == 0]
oddKey = [[val,dict1[val]] for val in dict1 if val%2 != 0]

print("Even Keys: ",evenKey)
print("Odd Keys: ",oddKey)
print("_"*50)


# 5. Python Dictionary Program to create a dictionary from two lists.
# Input :
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
# Output :
# {‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}

print("5. Python Dictionary Program to create a dictionary from two lists")
dict1 = {}
for a,b in (zip(list1,list2)):
    dict1[a] = b

print(dict1)
print("_"*50)


# 6. Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
# Input :
# [4, 5, 6, 2, 1, 7, 11]
# Output :
# {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
print("6. Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary")
list1 = [4, 5, 6, 2, 1, 7, 11]
dict1 = {}

for val in list1:
    dict1[val] = val**2

print(dict1)
print("_"*50)


# 7. Python Dictionary program to remove duplicate values from Dictionary.
# Input :
# {‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
# Output :
# {‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
print("7. Python Dictionary program to remove duplicate values from Dictionary")
dict7 = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
dictA = {}

for k,v in dict7.items():
    if v not in dictA.values():
        dictA[k] = v
    else:
        continue

print(dictA)
print("_"*50)


# 8. Python Dictionary program to create a dictionary from the string.
# Input  = ‘SQATools’
# Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
print("8. Python Dictionary program to create a dictionary from the string")

str1 = "SQAToolsss"
dict8 = {}

for char in str1:
    dict8[char] = str1.count(char)

print(dict8)
print("_"*50)


# 9. Python Dictionary program to sort a dictionary using keys.
# Input = {‘d’ : 21, ‘b’ : 53,  ‘a’: 13, ‘c’: 41}
# Output =
# (‘a’, 13)
# (‘b’, 53)
# (‘c’, 41)
# (‘d’, 21)

print("9. Python Dictionary program to sort a dictionary using keys")
dict9 = {'d' : 21, 'b' : 53, 'a': 13, 'c': 41}

for key in sorted(dict9):
    print("'",key,"'",":", dict9[key])
print("_"*50)


####################  Doubt 12th on website #######################
#10. Python Dictionary program to sort a dictionary in python using values.
dict10 = {'d' : 14, 'b' : 52, 'a': 13, 'c': 1 }
#Output= (c, 1) (a,13) (d, 14) (b, 52)

A = sorted(dict10.values())




# 11. Python Dictionary program to concatenate two dictionaries.
# Input:
dict1 = {'name' : 'yash', 'city' : 'pune'}
dict2 = {'course' : 'python', 'institute' : 'sqatools'}
# Output :
# { ‘name’ : ’yash’, city: ‘pune’, ‘course’ : ’python’, ‘institute’ : ’sqatools’ }

print("11. Python Dictionary program to concatenate two dictionaries")
dict1.update(dict2)
print(dict1)
print("_"*50)


############## Doubt 15th on website ##############
# 12. Python Dictionary program to swap the values of the keys in the dictionary.
# Input = {name:’yash’, city: ‘pune’}
# Output = {name:’pune’, city: ‘yash’}
print("12. Python Dictionary program to swap the values of the keys in the dictionary")
dict12 = {'name':'yash', 'city': 'pune'}
l1=[]
l2=[]
l3=[]
for k,v in dict12.items():
    l1.append(k)
    l2.append(v)

l2.reverse()
# print(l2)
dictA = dict(zip(l1,l2))
print(dictA)
print("_"*50)


# 13. Python Dictionary program to get the sum of all the items in a dictionary.
# Input = {‘x’ : 23, ‘y’ : 10 , ‘z’ : 7}
# Output = 40
print("13. Python Dictionary program to get the sum of all the items in a dictionary")

dict13 = {'x' : 23, 'y' : 10 , 'z' : 7}
sum = 0

for val in dict13.values():
    sum = sum + val

print(sum)
print("_"*50)


# 14. Python Dictionary program to check whether a key exists in the dictionary or not.
# Input:
dict14 = {'city':'pune', 'state':'maharashtra'}
# Dict1[country]
# Output= ‘key does not exist in dictionary

print("14. program to check whether a key exists in the dictionary or not")
val = 'country'
if val in dict14.keys():
    print("Key Exists in dictionary")
else:
    print("Key does not exist in dictionary")
print("_"*50)


# 15. Python program to iterate over a dictionary.
# Input :
dict15 = {'food':'burger', 'type':'fast food'}
# Output :
# food : burger
# type : fast food

print("15. Python program to iterate over a dictionary")
for k,v in dict15.items():
    print(k,":",v)

print("_"*50)


# 16. Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
# Input: n=4
# Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}
print("16. Program to create a dictionary in the form of (n^3) i.e. if key=2 value=8")
n = 4
dict16 = {}

for n in range(1,5):
    dict16[n] = n**3

print(dict16)
print("_"*50)


# 17. Python Dictionary program to insert a key at the beginning of the dictionary.
# Input = { ‘course’ : ’python’,  ‘institute’ : ’sqatools’ }
# Insert : ( ‘name’ : ’omkar’ )
# Output= { ‘name’ : ’omkar’, ‘course’ : ’python’, ‘institute’ : ’sqatools’}
print("17. Python Dictionary program to insert a key at the beginning of the dictionary")

dictA = {'name' : 'omkar'}
dictB = {'course' : 'python', 'institute' : 'sqatools'}
dictA.update(dict2)
print(dictA)
print("_"*50)


# 18. Python Dictionary program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.
# Output ={1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}
print("18. program to create a dictionary where keys are between 1 to 5 and values are squares of the keys")
dict18 = {}
for n in range(1,6):
    dict18[n] = n**2

print(dict18)
print("_"*50)


# 19. Python Dictionary program to remove a key from the dictionary.
# Input = {a:2,b:4,c:5}
# Output = (a:1,b:4)
print("19. Python Dictionary program to remove a key from the dictionary")
dict19 = {'a':2, 'b':4, 'c':5}
dict19.pop('c')
print(dict19)
print("_"*50)


# 20. Python Dictionary program to map two lists into a dictionary.
# Input :
a = ['name', 'sport', 'rank', 'age']
b = ['Virat', 'cricket', 1,  32]
# Output =  { ‘name’ : ’virat’, ‘sport’ : ’cricket’, ‘rank’: 1, ‘age’ : 32}

print("20. Python Dictionary program to map two lists into a dictionary")
dict20 = dict(zip(a,b))
print(dict20)
print("_"*50)

