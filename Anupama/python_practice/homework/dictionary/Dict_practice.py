#Python Dictionary program to add elements to the dictionary

dict= {}
dict ["Name"] = "Abby"
dict ["Age"] = "22"
dict ["Occupation"] ="Tester"
dict ["Organisation"] = "ABC corp"
print(dict)
print("*"*50)


# Program to shift values from one dictionary to another
dict1 = {'Name': 'Abby', 'Age': '22', 'Occupation': 'Tester', 'Organisation': 'ABC corp'}
dict2= {}
print("Before shifting Dictionary 1:", dict1)
temp = dict1.copy()
for val in temp:
    v1= dict1.pop(val)
    dict2[val]=v1
print("After shifting Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("*"*50)


#Program to print the square of all values in a dictionary
dict1 ={"a":5, "b":13,"c":7}
for val in dict1:
    print(val,":",dict1[val]**2)
print("*"*50)


#program to concatenate two dictionaries.
dict1 ={"a":5, "b":13,"c":7}
dict2 = {'Name': 'Abby', 'Age': '22', 'Occupation': 'Tester'}
dict1.update(dict2)
print(dict1)
print("*"*50)


#program to get a list of odd and even keys from the dictionary.
dict1={1:22, 5:"aaa", 3:"xyz", 2:"abc", 16:98}
l1= [[val,dict1[val]] for val in dict1 if val%2==0]
l2= [[val,dict1[val]] for val in dict1 if val%2!=0]
print("Even keys", l1)
print("Odd keys", l2)
print("*"*50)


#Program to create a dictionary using two lists.
l1=['a','b','c','d']
l2=[10,11,12,13,14,15]
dict1={}
for a,b in zip(l1,l2):
    dict1[a] =b
print(dict1)
print("*"*50)


#program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
l1=[3,6,2,5,7,8,9]
dict1={}
for val in l1:
    if val%2==0:
        dict1[val] = val**2
    else:
        dict1[val]=val**3
print("Result:", dict1)
print("*"*50)

#program to remove duplicate values from Dictionary
dict1 ={"a":5, "b":13,"c":7, "d":15, 'e':5,'f':13}
dict2={}
print("original dictionary",dict1)
for key,val in dict1.items():
    if val not in dict2.values():
        dict2[key]=val
print("updated dictionary",dict2)
print("*"*50)

#program to create a dictionary from the string
str="ilikepython"
dict3={}
for char in str:
    dict3[char]=str.count(char)
print(dict3)
print("*"*50)

# program to sort a dictionary using keys.
dict1 ={"b":5, "x":13,"c":7, "d":15, 'a':5,'r':13}
for key in sorted(dict1):
    print("%s: %s" % (key, dict1[key]))
print("*"*50)

# program to sort a dictionary using values.
dict1 = {'d':14,'b':52,'a':13,'c': 1}

sorted_ = {key: value for key, value in
             sorted(dict1.items(), key=lambda item: item[1])}
print(sorted_)
print("*"*50)

#program to add a key in a dictionary.
dict1 = {1:'a',2:'b'}
dict1.update({3:'c'})
print(dict1)
print("*"*50)

#Check whether a key exists in the dictionary or not
D1 = {'city':'pune','state':'maharashtra'}
count = 0

for key in D1.keys():
    if key == "Country":
        count += 1

if count > 0:
    print("Key exists")
else:
    print("Key does not exists")
print("*"*50)

#Python program to iterate over a dictionary
D1 = {'food':'burger','type':'fast food'}

for val in D1:
    print(val,D1[val])
print("*"*50)

#Insert a key at the beginning of the dictionary
dict1 = {'course':'python','institute':'sqatools' }
dict2 = {'name':'omkar'}

dict2.update(dict1)

print(dict2)
print("*"*50)

#python program to create dictionary where keys are numbers and valurs are squares of keys
dict1 = {}

for i in range(1,6):
    dict1[i] = i**2

print(dict1)
print("*"*50)

#Find the product of all items in the dictionary
dict1 =  {'a':2,'b':4,'c':5}
result = 1

for val in dict1.values():
    result *= val

print(result)