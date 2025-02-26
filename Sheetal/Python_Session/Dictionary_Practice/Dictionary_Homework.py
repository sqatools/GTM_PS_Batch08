import sys

from colorama import *
print("_" * 40)
print("Q5: write a python to calculate total bill and update the inventory from given")
# {'FruitName': [price, inventory]}

fruits_details = {'Banana': [10, 100], 'watermelon': [60, 500], 'mango': [70, 250],
                  'Apple': [50, 100], 'lichi': [20, 300]}

fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25}
total_bill = 0
updated_inventory ={}
for fruit,quant in fruit_purchase.items():
    if fruit in fruits_details and quant < fruits_details[fruit][1]:
        fruit_price = fruits_details[fruit][0]
        inventory_available = fruits_details[fruit][1]
        if inventory_available >=quant:
            total_bill = total_bill + fruit_price * quant
            fruits_details[fruit][1] = fruits_details[fruit][1] - quant
        else:
            print("The inventory is less than purchase")
    else:
        print(f" Not enough inventory for {fruit}. Available Quantity: {fruits_details[fruit][1]}, Quantity For Purchase: {quant}")

print("The Total bill is", Fore.BLUE+ f"{total_bill}" +Style.RESET_ALL)
print(f"Actual Inventory was: \n {fruits_details}")

print("\nUpdated Inventory is:")
for fruit, details in fruits_details.items():
    # updated_inventory = "".join(f"{fruit}: {details[1]}")
    # updated_inventory = f"{fruit}: {details[1]}"
    updated_inventory[fruit] = details[1]
print(updated_inventory)

print("_" * 40)
print("Python Dictionary program to add elements to the dictionary.")
dictionary = {}
dictionary['Name'] = "Sheetal"
dictionary['Course'] = "Python"
dictionary['Duration'] = 3


print(dictionary)
print("_" * 40)
print("Python Dictionary program to print the square of all values in a dictionary.")
Input = {'a': 5, 'b':3, 'c': 6, 'd' : 8}
# Output :
# a : 25
# b : 9
# c : 36
# d : 64
#Key : Val
for sqr_val in Input:
    # Input[sqr_val] = Input[sqr_val] * Input[sqr_val]
    Input[sqr_val] = Input[sqr_val] **2
    print(sqr_val, ":", Input[sqr_val])

print("_" * 40)

print("Python Dictionary program to move items from dict1 to dict2.")
# Input :
dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}
# Output :
# dict1 = {}
# dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}

dict12 = dict1
dict1 = {}
print(f"First Dictionary is {dict1}")
print(f"Second Dictionary is {dict12}")

#OR
for val in dict1:
    temp = dict2
    dict2 = dict1
    dict1 = temp
print(f"First Dictionary is {dict1}")
print(f"Second Dictionary is {dict2}")


print("_" * 40)
print("Python Dictionary program to concatenate two dictionaries.")
# Input :
dict3 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict4 = {'Age' : 25, 'salary': '$25k'}
# Output :
# dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}
dict3.update(dict4)
print(dict3)

print("_" * 40)
print("Python Dictionary program to get a list of odd and even keys from the dictionary.")
Input5 = {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
# Output :
# Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
# Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
# dict6 = {f"Even Key= {val}:{Input[val]}" if val%2 == 0 else f"Odd Key= {val}:{Input[val]}" for val in Input }
# print(dict6)

Ekey =[]
Okey = []
for val in Input5:
    if val % 2 == 0:
        Ekey.append([val, Input5[val]])
    else:
        Okey.append([val, Input5[val]])

print(f"Even Key = {Ekey}")
print(f"Odd Key = {Okey}")

print("_" * 40)
print("Python Dictionary Program to create a dictionary from two lists.")
# Input :
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
# Output :
# {‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}

dict5 ={}
for val1 in range(len(list1)):
    dict5[list1[val1]] = list2[val1]

print(dict5)



print("_" * 40)
print("Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.")
Input = [4, 5, 6, 2, 1, 7, 11]
# Output :
# {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}

dict6 = {val: (val**2 if val%2 == 0 else val**3) for val in Input}
print("The final dictionary is: ", dict6)

print("_" * 40)
print("Python Dictionary program to clear all items from the dictionary.")
print(f"The value inside the dictionary  before clear is : {dict6}")
dict6.clear()
print(f"The value inside the dictionary after clear is : {dict6}")

print("_" * 40)
print("Python Dictionary program to remove duplicate values from Dictionary.")
Input = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
# Output :
# {‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
dict7 = {}
temp_val = set()

for key,val in Input.items():
    if val not in dict7.values():
        dict7[key] = val
        # temp_val.add(val)

print(dict7)

print("_"*40)
print("Python Dictionary program to create a dictionary from the string.")
Input  = 'SQATools'
# Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
dict8 ={}

for val in Input:
    if val not in dict8.keys():
        dict8[val] = 1
    else:
        dict8[val] += 1
print(dict8)


print("_"*40)
print("Python Dictionary program to sort a dictionary using keys.")
Input = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
# Output =
# (‘a’, 13)
# (‘b’, 53)
# (‘c’, 41)
# (‘d’, 21)

sorted_dict = dict(sorted(Input.items()))
for key,val in sorted_dict.items():
    print((key,val))

print("_" * 40)
print("Python Dictionary program to sort a dictionary in python using values.")
Input = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
# Output= (c, 1) (a,13) (d, 14) (b, 52)

sorted_dict = dict(sorted(Input.items(), key=lambda item: item[1]))

for key,val in sorted_dict.items():
    print(f"({key},{val})", end="")

print()

print("_" * 40)
print("Python Dictionary program to add a key in a dictionary.")
Input12 = {1:'a', 2:'b'}
# Output= (1:’a’, 2:’b’, 3:’c’}

Input12[3] = 'c'

print(Input12)

print("_" * 40)

print("Python Dictionary program to swap the values of the keys in the dictionary.")
Input = {'name':'yash', 'city': 'pune'}
# Output = {name:’pune’, city: ‘yash’}

keys = list(Input.keys())
values = list(Input.values())
# rotated_values = values[1:] + values[:1]  # Shift left and wrap around
#
# # Assign rotated values back to dictionary
# for i in range(len(keys)):
#     Input[keys[i]] = rotated_values[i]
#
# # Printing swapped dictionary
# print(Input)
# for key in range(len(Input)):
#     Input[key] = Input[1]


print("_" * 40)
print("Python Dictionary program to get the sum of all the items in a dictionary.")
Input = {'x' : 23, 'y' : 10 , 'z' : 7}
# Output = 40

Total = 0
for key,val in Input.items():
    Total = Total + val

print(f"The sum of al the values is: {Total}")

print("_" * 40)
print("Python program to get the size of a dictionary in python.")
# Hint : use sys.getsizeof(var) method.
Input = {'name' : 'virat', 'sport' : 'cricket'}
# Output = 232bytes

print(sys.getsizeof(Input),"bytes")

print("_"*40)
print("Python Dictionary program to check whether a key exists in the dictionary or not.")
# Input:
Dict1 = {'city':'pune', 'state':'maharashtra'}
# Dict1[country]
# Output= key does not exist in dictionary

# for key,val in Dict1.items():
key = 'country'
if key in Dict1:
    print(f"The key {Fore.GREEN}{Style.BRIGHT}{key}{Style.RESET_ALL} exists in dictionary")
else:
    print(f"The key {Fore.BLUE}{Style.BRIGHT}{key}{Style.RESET_ALL} does not exists in dictionary")

print("_"*40)
print("Python program to iterate over a dictionary.")
# Input :
Dict1 = {'food':'burger', 'type':'fast food'}
# Output :
# food : burger
# type : fast food

for key,val in Dict1.items():
    print(f"{key} : {val}")


print("_" * 40)
print("Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8")
# Input
n=4
# Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}

dict1[n] = n**3
print(dict1)


print("_" * 40)
print("Python Dictionary program to insert a key at the beginning of the dictionary.")
Input = { 'course' : 'python',  'institute' : 'sqatools' }
Insert = { 'name' : 'omkar' }
# Output= { ‘name’ : ’omkar’, ‘course’ : ’python’, ‘institute’ : ’sqatools’}

Insert.update(Input)

print(Insert)

print("_" * 40)
print("Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.")
# Output ={1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}

dict ={}
for key in range(1,6):
    dict[key] = key**2

print(dict)
print("_" * 40)
print("Python Dictionary program to find the product of all items in the dictionary.")
Input = { 'a' : 2, 'b' : 4, 'c' : 5}
# Output = 40

prod =1
for key,val in Input.items():
    prod =prod * val

print(f"The product of all numbers is {prod}")

print("_" * 40)
print("Python Dictionary program to remove a key from the dictionary.")
Input = {'a':2,'b':4,'c':5}
# Output = (a:1,b:4}

Input.pop('c')

print(Input)

