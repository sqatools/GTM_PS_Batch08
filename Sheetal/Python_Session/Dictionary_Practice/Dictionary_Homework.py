print("_" * 40)
print("Q5: write a python to calculate total bill and update the inventory from given")
# {'FruitName': [price, inventory]}

fruits_details = {'Banana': [10, 100], 'watermelon': [60, 500], 'mango': [70, 250],
                  'Apple': [50, 100], 'lichi': [20, 300]}

fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 750, 'mango': 25}
total_bill = 0
fruit_inv = []
for fruit,quant in fruit_purchase.items():
    if fruit in fruits_details and quant < fruits_details[fruit][1]:
        price_per_unit = fruits_details[fruit][0]
        stock_available = fruits_details[fruit][1]
        if stock_available >=quant:
            total_bill = total_bill + price_per_unit*quant
            fruits_details[fruit][1] = fruits_details[fruit][1] - quant
        else:
            print("The inventory is less than purchase")
    else:
        print(f" Not enough stock for {fruit}. Available Quantity: {fruits_details[fruit][1]}, Quantity For Purchase: {quant}")
print("The Total bill is", total_bill)
print(fruits_details)

print("\nUpdated Inventory:")
for fruit, details in fruits_details.items():
    print(f"{fruit}: {details[1]}")

print("_" * 40)
print("Python Dictionary program to add elements to the dictionary.")

print("_" * 40)
print("Python Dictionary program to print the square of all values in a dictionary.")
Input : {'a': 5, 'b':3, 'c': 6, 'd' : 8}
# Output :
# a : 25
# b : 9
# c : 36
# d : 64


print("_" * 40)
print("Python Dictionary program to move items from dict1 to dict2.")
# Input :
dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}
# Output :
# dict1 = {}
# dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}


print("_" * 40)
print("Python Dictionary program to concatenate two dictionaries.")
# Input :
dict3 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict4 = {'Age' : 25, 'salary': '$25k'}
# Output :
# dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}


print("_" * 40)
print("Python Dictionary program to get a list of odd and even keys from the dictionary.")
Input = {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
# Output :
# Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
# Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]


print("_" * 40)
print("Python Dictionary Program to create a dictionary from two lists.")
# Input :
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
# Output :
# {‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}


print("_" * 40)
print("Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.")
Input = [4, 5, 6, 2, 1, 7, 11]
# Output :
# {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}


print("_" * 40)
print("Python Dictionary program to clear all items from the dictionary.")

print("_" * 40)
print("Python Dictionary program to remove duplicate values from Dictionary.")
Input = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
# Output :
# {‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}

#
print("_"*40)
print("Python Dictionary program to create a dictionary from the string.")
Input  = 'SQATools'
# Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}


print("_"*40)
print("Python Dictionary program to sort a dictionary using keys.")
Input = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
# Output =
# (‘a’, 13)
# (‘b’, 53)
# (‘c’, 41)
# (‘d’, 21)


print("_" * 40)
print("Python Dictionary program to sort a dictionary in python using values.")
Input = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
# Output= (c, 1) (a,13) (d, 14) (b, 52)


print("_" * 40)
print("Python Dictionary program to add a key in a dictionary.")
Input= {1:'a', 2:'b'}
# Output= (1:’a’, 2:’b’, 3:’c’}


print("_" * 40)
print("Python Dictionary program to add a key in a dictionary.")
Input= {1:'a', 2:'b'}
# Output= (1:’a’, 2:’b’, 3:’c’}


print("_" * 40)
print("Python Dictionary program to swap the values of the keys in the dictionary.")
Input = {'name':'yash', 'city': 'pune'}
# Output = {name:’pune’, city: ‘yash’}


print("_" * 40)
print("Python Dictionary program to get the sum of all the items in a dictionary.")
Input = {'x' : 23, 'y' : 10 , 'z' : 7}
# Output = 40


print("_" * 40)
print("Python program to get the size of a dictionary in python.")
# Hint : use sys.getsizeof(var) method.
Input = {'name' : 'virat', 'sport' : 'cricket'}
# Output = 232bytes


print("_"*40)
print("Python Dictionary program to check whether a key exists in the dictionary or not.")
# Input:
Dict1 = {'city':'pune', 'state':'maharashtra'}
# Dict1[country]
# Output= ‘key does not exist in dictionary


print("_"*40)
print("Python program to iterate over a dictionary.")
# Input :
Dict1 = {'food':'burger', 'type':'fast food'}
# Output :
# food : burger
# type : fast food


print("_" * 40)
print("Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8")
 # Input:
n=4
# Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}


print("_" * 40)
print("Python Dictionary program to insert a key at the beginning of the dictionary.")
Input = { 'course' : 'python',  'institute' : 'sqatools' }
# Insert : ( ‘name’ : ’omkar’ )
# Output= { ‘name’ : ’omkar’, ‘course’ : ’python’, ‘institute’ : ’sqatools’}


print("_" * 40)
print("Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.")
# Output ={1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}


print("_" * 40)
print("Python Dictionary program to find the product of all items in the dictionary.")
Input = { 'a' : 2, 'b' : 4, 'c' : 5}
# Output = 40


print("_" * 40)
print("Python Dictionary program to remove a key from the dictionary.")
Input = {'a':2,'b':4,'c':5}
# Output = (a:1,b:4}


