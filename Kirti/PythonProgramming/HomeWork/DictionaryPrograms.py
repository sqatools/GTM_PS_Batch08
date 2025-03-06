"""
#Program 1 :  Write a proram to create bill as per cust requirement
fruits_with_price = {'Apple': 50, 'Banana': 10, 'watermelon': 60, 'mango': 70}
cust_pur_with_quantity = {'Apple': 10, 'Banana': 20, 'watermelon': 5, 'mango': 20}

total_bill=0
for fruit,quantity in cust_pur_with_quantity.items():
    fruit_price=fruits_with_price[fruit]
    total_bill =total_bill + fruit_price * quantity

print("Total bill = ",total_bill)


#==========================================================================================

print("==="*30)
# Home work
##############################
# Q2: write a python to calculate total bill and update the inventory from given
# {'FruitName': [price, inventory]}

fruits_details = {'Banana': [10, 100], 'watermelon': [60, 500], 'mango': [70, 250],
                  'Apple': [50, 100], 'lichi': [20, 300]}

fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25}

total_bill=0

for fruit, quant in fruit_purchase.items():
    fruit_charges = quant*fruits_details[fruit][0]
    total_bill= total_bill + fruit_charges
    fruits_details[fruit][1]=fruits_details[fruit][1]-quant

print(fruits_details)
print(total_bill)

#=================================================================

print("_" * 50)
##############################
# Q3 : Python Dictionary program to add elements to the dictionary.
k=int(input("Enter how many key value pairs needs to be inserted in dictionary"))
dict3={}
for i in range(k):
    key= input("Enter key : ")
    val= input("Enter value : ")
    dict3[key]=val

print(dict3)

#=================================================================

print("==="*30)
# Q4 : write a python to calculate total bill and update the inventory
fruits_price = {'Banana': 10, 'watermelon': 60, 'mango': 70, 'Apple': 50, 'lichi': 20}
fruit_inventory1 = {'Apple': 100, 'Banana': 200, 'watermelon': 500, 'mango': 250, 'lichi': 300}
fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25}

total_bill = 0
for fruit, quant in fruit_purchase.items():
    total_bill = total_bill + quant*fruits_price[fruit]
    fruit_inventory1[fruit]= fruit_inventory1[fruit]-quant

print(fruit_inventory1)
print(total_bill)



print("==="*30)
'''
Q. 5 - Python Dictionary program to print the square of all values in a dictionary.
Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
Output :
a : 25
b : 9
c : 36
d : 64
'''
dict5 = {"a": 5, "b":3, "c": 6, "d" : 8}
for k,v in dict5.items():
    print(str(k) +" : "+ str(v**2))




print("==="*30)
'''
Q. 6 - Python Dictionary program to move items from dict1 to dict2.
Input :
dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
dict2 = {}
Output :
dict1 = {}
dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
'''
dict1 = {"name": "john", "city": "London", "country": "UK"}
dict2 = {}
for key in dict1:
    dict2[key]=dict1[key]

dict1.clear()
print(dict1)
print(dict2)



print("==="*30)
'''
Q. 7 - Python Dictionary program to concatenate two dictionaries.
Input :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’}
dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
Output :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}
'''
dict1 = {"Name": "Harry", "Rollno":345, "Address": "Jordan"}
dict2 = {"Age" : 25, "salary": "$25k"}

#dict1.update(dict2)
print(dict1)
print(dict2)

for key in dict2:
    dict1[key]=dict2[key]

print(dict1)
print(dict2)



print("==="*30)
'''
Q. 8 - Python Dictionary program to get a list of odd and even keys from the dictionary.
Input :
{1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’}
Output :
Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
'''
dict8={1: 25, 5: "abc", 8: "pqr", 21: "xyz", 12: "def", 2: "utv"}
even_key_dict={}
odd_key_dict={}

for key in dict8:
    if key % 2 == 0:
        even_key_dict[key] = dict8[key]
    else:
        odd_key_dict[key] = dict8[key]

print("even_key_dict : ",even_key_dict)
print("odd_key_dict : ",odd_key_dict)



print("==="*30)
'''
Q. 9 - Python Dictionary Program to create a dictionary from two lists.
Input :
list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
list2 = [12, 23, 24, 25, 15, 16]
Output :
{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}
'''
list1 = ["a", "b", "c", "d", "e"]
list2 = [12, 23, 24, 25, 15, 16]

print(dict(zip(list1, list2)))

# OR

dict1={}
for i in range(len(list1)):
    dict1[list1[i]]=list2[i]

print(dict1)



print("==="*30)
'''
Q. 10 - Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
Input :
[4, 5, 6, 2, 1, 7, 11]
Output :
{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
'''

list1=[4, 5, 6, 2, 1, 7, 11]
result={x:x**2 if x%2==0 else x**3 for x in list1}
print(result)



print("==="*30)
'''
Q. 11- Python Dictionary program to clear all items from the dictionary.
'''
dict1={4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}

dict1.clear()
print(dict1)



print("==="*30)
'''
Q. 12- Python Dictionary program to remove duplicate values from Dictionary.
Input :
{‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
Output :
{‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
'''

dict12={"a": 12, "b": 2, "c": 12, "d": 5, "e": 35, "f": 5}
key_list = dict12.keys()
values_list = dict12.values()
dict13 = {}
for k,v in dict12.items():
    if k not in dict13.keys() and dict12[k] not in dict13.values():
        dict13[k] = v

print(dict13)



print("==="*30)
'''
Q. 13- Python Dictionary program to create a dictionary from the string.
Input  = ‘SQATools’
Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
'''

str1  = "SQATools"
dict13 = {}
list1 = list(str1)
for item in list1:
    if item not in dict13.keys():
        dict13[item] = list1.count(item)

print(dict13)



print("==="*30)
'''
Q. 14- Python Dictionary program to sort a dictionary using keys.
Input = {‘d’ : 21, ‘b’ : 53,  ‘a’: 13, ‘c’: 41}
Output =
(‘a’, 13)
(‘b’, 53)
(‘c’, 41)
(‘d’, 21)
'''

dict14 = {"d" : 21, "b" : 53,  "a": 13, "c": 41}

for key in sorted(dict14):
    print(f"{key} : {dict14[key]}")




'''
Q. 15 Python Dictionary program to sort a dictionary in python using values.
Input = {‘d’ : 14, ‘b’ : 52,  ‘a’: 13, ‘c’: 1 }
Output= (c, 1) (a,13) (d, 14) (b, 52)
'''

dict15 = {"d" : 14, "b" : 52,  "a": 13, "c": 1 }

val1=sorted(dict15.values())
for val in val1:
    for key in dict15:
        if dict15[key]==val:
            print(f"{key} : {dict15[key]}")




'''
Q. 16 Python Dictionary program to add a key in a dictionary.
Input= {1:’a’, 2:’b’}
Output= (1:’a’, 2:’b’, 3:’c’}
'''
dict16= {1:"a", 2:"b"}
new_key= input("Enter key : ")
new_value= input("Enter Value : ")

dict16[new_key]=new_value
print(dict16)



'''
Q. 18 Python Dictionary program to concatenate two dictionaries.
Input:
D1 = {‘name’ : ’yash’, ‘city’ :  ‘pune’}
D1 = {‘course’ : ’python’, ‘institute’ : ’sqatools’}
Output :
{ ‘name’ : ’yash’, city: ‘pune’, ‘course’ : ’python’, ‘institute’ : ’sqatools’ }
'''
D1 = {"name" : "yash", "city" :  "pune"}
D2 = {"course" : "python", "institute" : "sqatools"}

D1.update(D2)
print(D1)



'''
Q. 19 Python Dictionary program to swap the values of the keys in the dictionary.
Input = {name:’yash’, city: ‘pune’}
Output = {'yash': 'name', 'pune': 'city'}
'''
dict19 = {"name":"yash", "city": "pune"}
dict20={}
for key, val in dict19.items():
    dict20[val]=key

print(dict20)

"""

'''
Q. 20 Python Dictionary program to get the sum of all the items in a dictionary.
Input = {‘x’ : 23, ‘y’ : 10 , ‘z’ : 7}
Output = 40
'''

Input = {"x" : 23, "y" : 10 , "z" : 7}
result = sum(Input.values())
print("Sum of values = ", result)