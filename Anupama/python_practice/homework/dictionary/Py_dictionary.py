"""
# Dict Properties
->  Dict is mutable data type. we can modify it.
->  Dict store data in key value pair with curly braces e.g. {'a' : 123}
->  Dict only contains unique key, duplicate keys are not allowed.
->  If we provide duplicate key, then last defined key data will be consider.
    e.g. {'a' : 123, 'b' : 456, 'a':111}
     output = {'a': 111, 'b' : 456}
->  Only immutable data type can be key in dictionary, e.g. int, float, string, tuple, boolean.
->  All type of data can be value in the dictionary. e.g int, float, string, tuple, bool, set, list, dict
->  Dict can contain duplicate values.
->  Dict follows the LIFO(LAST IN FIRST OUT) concept.
->  Dict does not follow indexing.
"""

dict1 = {'a': 123, 'b': 456}
print(dict1, type(dict1))
# {'a': 123, 'b': 456} <class 'dict'>


# Add new content to dict
dict1['c'] = 567
print("dict1 :", dict1)
# dict1 : {'a': 123, 'b': 456, 'c': 567}


print("_" * 50)
# Dict only contains unique key, duplicate keys are not allowed.
dict2 = {'a': 456, 'b': 333, 'd': 333, 'a': 678, 'c': 555}
print(dict2)
# {'a': 678, 'b': 333, 'd': 333, 'c': 555}

dict2['b'] = 888
print("dict2 :", dict2)
# {'a': 678, 'b': 888, 'd': 333, 'c': 555}


print("_" * 50)
####################################
# Only immutable data type can be key in dictionary, e.g. int, float, string, tuple, boolean.

dict3 = {
    23: 3.4,
    44.5: 'Hello',
    'Python': [1, 4, 7],
    (3, 5, 7): {'a': 123, 'b': 234},
    True: (4, 77, 88),
}

print("dict3:", dict3)
# dict3: {23: 3.4, 44.5: 'Hello', 'Python': [1, 4, 7], (3, 5, 7): {'a': 123, 'b': 234}, True: (4, 77, 88)}


# add list, dict, set as key and check the error.
dict4 = {
    23: 3.4,
    44.5: 'Hello',
    'Python': [1, 4, 7],
    (3, 5, 7): {'a': 123, 'b': 234},
    True: (4, 77, 88),
    # [1, 6, 8] : {4, 6, 8, 1} # TypeError: unhashable type: 'list'
    # {'Name' : 'John'} : [5, 7, 89] # TypeError: unhashable type: 'dict'
    # {4, 6, 8} : (4, 7, 9, 11) # unhashable type: 'set'
}

print("dict4 :", dict4)

print("_" * 50)
############### get data from dictionary with help of key ############

dict5 = {
    23: 3.4,
    44.5: 'Hello',
    'Python': [1, 4, 7],
    (3, 5, 7): {'a': 123, 'b': 234},
    True: (4, 77, 88, [4, 6, 8]),
}

print(dict5['Python'])  # [1, 4, 7]
print(dict5['Python'][1])  # 4
print(dict5[(3, 5, 7)])  # {'a': 123, 'b': 234}
print(dict5[(3, 5, 7)]['b'])  # 234
print(dict5[True])  # (4, 77, 88, [4, 6, 8])
print(dict5[True][3][2])  # 8

print("_"*50)
############################### Apply loop on the dictionary ##########

dict6 = {'a' : 345, 'b' : 678, 'c': 123}

# print all the keys using loop
for val in dict6:
    print(val)
"""
a
b
c
"""

#  print key and value with the help of key
for x in dict6:
    print(x, dict6[x])

"""
a 345
b 678
c 123
"""
print(dict6.items())
# dict_items([('a', 345), ('b', 678), ('c', 123)])

# get key value pair in tuple using items methods.
for data in dict6.items():
    print(data)
"""
('a', 345)
('b', 678)
('c', 123)
"""

# get key and value in 2 separate variable
for k, v in dict6.items():
    #print("key :", k, "value:", v)
    print(k, v)

"""
key : a value: 345
key : b value: 678
key : c value: 123
"""

#############################################
# dict methods
print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


# Q write a python to create diction from list of data, val will be key and square of data will the value in dict

list1 = [4, 6, 8, 1, 6, 7]
# output = {4: 16, 6: 36, 8:64, 1:1, 7:49}
output = {}

for val in list1:
    if val not in output:
        output[val] = val ** 2
    else:
        continue

print("output :", output)
# {4: 16, 6: 36, 8: 64, 1: 1, 7: 49}


# Q2 : write a python to create dictionry from given string
# first char of each word should be key and word should be value
str1 = "Hello We Are Learning Python"
# output = {'H' : 'Hello', 'W': 'We', 'A': 'Are', 'L' : 'Learning', 'P': 'Python'}

output = {}
word_list = str1.split()
print(word_list)
# ['Hello', 'We', 'Are', 'Learning', 'Python']

for word in word_list:
    print(word, ":", word[0])
    output[word[0]] = word

print("output :", output)
# {'H': 'Hello', 'W': 'We', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

dict2 = {}
dict2['a'] = 'Hello'

print("_" * 50)
##############################
# Q3 : write a python to create total bill as per customer purchase from given dictionary

fruits_with_price = {'Banana': 10, 'watermelon': 60, 'mango': 70, 'Apple': 50}
cust_pur_with_quantity = {'Apple': 10, 'Banana': 20, 'watermelon': 5, 'mango': 20}

total_bill = 0

for k, v in cust_pur_with_quantity.items():
    # get each fruit price
    fruit_price = fruits_with_price[k]
    # get each fruit bill
    fruit_bill = v * fruit_price
    # print fruit_name, fruit_quant, fruit_price, fruit_bill
    print(k, v, fruit_price, fruit_bill)
    # all each fruit bill into total bill
    total_bill = total_bill + fruit_bill

print("Total bill amount :", total_bill)

print(fruits_with_price['Apple'])

# for fruit, quant in cust_pur_with_quantity.items():
#     fruit_price = fruits_with_price[fruit]
#     # fruits_with_price['Apple']
#     print(fruit, "|", fruit_price,"|", quant)
#     total_bill = total_bill + fruit_price*quant
#
# print("Total bill :", total_bill)


print("#" * 50)
##############################
# Q4 : write a python to calculate total bill and update the inventory

fruits_price = {'Banana': 10, 'watermelon': 60, 'mango': 70, 'Apple': 50, 'lichi': 20}
fruit_inventory = {'Apple': 100, 'Banana': 200, 'watermelon': 500, 'mango': 250, 'lichi': 300}
fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25}
total_bill = 0
for fruit, pur_quant in fruit_purchase.items():
    fruit_name = fruit
    fruit_pur_quant = pur_quant
    fruit_price = fruits_price[fruit]
    fruit_bill = fruit_pur_quant*fruit_price
    total_bill = total_bill + fruit_bill
    fruit_inventory_val = fruit_inventory[fruit]
    updated_inventory_val = fruit_inventory_val - fruit_pur_quant
    # updated_inventory_val = fruit_inventory[fruit] - fruit_pur_quant
    fruit_inventory[fruit] = updated_inventory_val
    print("Fruit name:", fruit_name)
    print("Fruit Purchase Quant:", fruit_pur_quant)
    print("Fruit Price :", fruit_price)
    print("Fruit Bill :", fruit_bill)
    print("Fruit inventory :", fruit_inventory_val)
    print("Fruit updated inventory :", updated_inventory_val)
    print("_" * 40)

print("Total Bill Amount :", total_bill)
print(fruit_inventory)


# Home work
##############################
# Q5: write a python to calculate total bill and update the inventory from given
# {'FruitName': [price, inventory]}

fruits_details = {'Banana': [10, 100], 'watermelon': [60, 500], 'mango': [70, 250],
                  'Apple': [50, 100], 'lichi': [20, 300]}

fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25}


my_tup=(6,7,4,9,44,23,64,21,1)
my_lst=list(my_tup)
my_lst.sort()
print(my_lst)
print(my_lst[8::])

def find_combinations(target_sum, max_value):
    combinations = []
    for i in range(max_value + 1):
        for j in range(max_value + 1):
            if i + j == target_sum:
                combinations.append((i, j))
    return combinations

target_sum = 20
max_value = 20  # Assuming the values range from 0 to 20
combinations = find_combinations(target_sum, max_value)

print("Combinations of two values whose sum is 20:")
for combo in combinations:
    print(combo)
print("*"*50)


#program to find all common values and all diffrent values
l1 = [4,76,9,22,55,77,8]
l2 = [4, 22,5,66,7,22,76,8]

comm = list(set(l1) & set(l2))
print(comm)

diff1 =set(l1) - set(l2)
diff2= set(l2)-set(l1)

print(diff1)
print(diff2)