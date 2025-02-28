"""
Dictionary Properties:
1. Dict is Mutable data type. We can modify it.
2. Dict stores data in key:value pair, with curly braces. Ex: {'a':123, 'b':456}
3. Dict contains only unique key, however duplicate values are allowed.
4. If we provide duplicate key value then last defined key:value pair will be considered.
    e.g. {'a' : 123, 'b' : 456, 'a':111}
     output = {'a': 111, 'b' : 456}
5. Only immutable data type can be key in Dictionary : int, float, string, tuple, bool
6. Value can be of any data type: int, float, string, list, tuple, dict, set, bool
7. Dict can contain duplicate values for different keys
8. Dict follows the LIFO(LAST IN FIRST OUT) concept
9. Dict does not follow indexing

"""

dict1 = {'a': 123, 'b': 456}
print(dict1, type(dict1))
# {'a': 123, 'b': 456} <class 'dict'>

# Add new content to dict
dict1['c'] = 789
print(dict1)
# {'a': 123, 'b': 456, 'c': 789}
print("_"*50)

# Dict only contains unique key, duplicate keys are not allowed.
dict2 = {'a': 456, 'b': 333, 'd': 333, 'a': 678, 'c': 555}
print(dict2)
# {'a': 678, 'b': 333, 'd': 333, 'c': 555}

dict1['b'] = 888
print(dict1)
# {'a': 123, 'b': 888, 'c': 789}


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
    True: (4, 77, 88)
    # [1, 6, 8] : {4, 6, 8, 1}, # TypeError: unhashable type: 'list'
    # {'Name' : 'John'} : [5, 7, 89], # TypeError: unhashable type: 'dict'
    # {4, 6, 8} : (4, 7, 9, 11) # unhashable type: 'set'
}
print(dict4)
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

print("_" * 50)

############################### Apply loop on the dictionary ##########
dict6 = {'a': 345, 'b': 678, 'c': 123}

# print all the keys using loop
for val in dict6:
    print(val)
""""
a
b
c
"""
print("_"*50)

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
    print("Key:",k, "Value:",v)

"""
Key: a Value: 345
Key: b Value: 678
Key: c Value: 123
"""

#############################################
# dict methods
print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items',
# 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

print("_"*50)
##########################
# keys() method --> This method returns list of keys from given dictionary

dict_b = {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 456788923, 'city': 'Mumbai'}
val = dict_b.keys()
# print(val, type(val), list(val[2])) --> Error : TypeError: 'dict_keys' object is not subscriptable
print(val, type(val), list(val)[1])
# dict_keys(['Name', 'email', 'phone', 'city']) <class 'dict_keys'> email
print("_"*50)

val1 = dict_b.keys()
for data in val1:
    print(data)
"""
Name
email
phone
city

"""
print("_"*50)

###################################
# value() method --> this method returns all values from given dictionary

print(dict_b.values())
# dict_values(['Rahul', 'rahul@gmail.com', 456788923, 'Mumbai'])

val2 = dict_b.values()
for data in val2:
    print(data, type(data))

"""
Rahul <class 'str'>
rahul@gmail.com <class 'str'>
456788923 <class 'int'>
Mumbai <class 'str'>

"""
print("_"*50)


########################
# add data to dict with new key

dictA = {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 456788923, 'city': 'Mumbai'}
dictA['age'] = 25

print(dictA)
# {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 456788923, 'city': 'Mumbai', 'age': 25}
print("_"*50)

##################################
# update method : this method help to update one dictionary to another.
dict1 = {'a': 123, 'b': 456, 'c': 789, 'r': 999}
dict2 = {'p': 345, 'q': 222, 'r': 555}

dict2.update(dict1)
print(dict2)
# {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'b': 456, 'c': 789}
print("_"*50)


##################################
# pop() method : This method removes key:value pair with the help of key and return the value

dict3 = {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'b': 456, 'c': 789}
rmval1 = dict3.pop('b')
print("Removed value is: ",rmval1)
# Removed value is:  456

print("dict_3 :", dict3)
# {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'c': 789}
print("_"*50)

#######################################
# popitem() method --> This method removes key:value pair from last value of the dictionary and
#                       returns it in tuple form

dict4 = {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'c': 789}
rmval2 = dict4.popitem()
print("Removed value is: ",rmval2)
# Removed value is:  ('c', 789)

print(dict4)
# {'p': 345, 'q': 222, 'r': 999, 'a': 123}
print("_"*50)


#######################################
# clear() method --> This method clears all the data from dictionary

dict4 = {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'c': 789}
dict4.clear()

print(dict4)      # {}
print("_"*50)


#######################################
# del statement or keyword : This removes dictionary variable from the memory

dict5 = {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'c': 789}
del dict5
# print(dict5)
# NameError: name 'dict5' is not defined. Did you mean: 'dict1'?

# remove specific data using del statement
dict6 = {'p': 442, 'q': 444, 'r': 999, 'a': 33, 'd': 789}
del dict6['a']
print(dict6)
# {'p': 442, 'q': 444, 'r': 999, 'd': 789}

print("_" * 50)

##########################################
# copy method --> This method copies data from one dictionary to another

# shallow copy :  In shallow we make a reference of one dict, and if we will modify any of them,
#               then changes will reflect on the both the dictionaries.

dict_x = {'p': 442, 'q': 444, 'r': 999, 'a': 33, 'd': 789}
dict_y = dict_x
dict_y['c'] = 1000

print(dict_x)
# {'p': 442, 'q': 444, 'r': 999, 'a': 33, 'd': 789, 'c': 1000}

print("dict_x :", dict_x)
# {'p': 442, 'q': 444, 'r': 999, 'a': 33, 'd': 789, 'c': 1000}

print("_"*50)

# Deep Copy :  In deep copy we can create new copy of one dict to another, and if we will modify any of them
#              and then changes will not reflect on each other.

dict_p = {'Name': 'John', 'Surname': 'Doe', 'age': 25, 'email': 'john@gmail.com'}
dict_q = dict_p.copy()
dict_q['city'] = 'Pune'
dict_p['Phone'] = 76575766766
print("dict_p", dict_p)
# dict_p {'Name': 'John', 'Surname': 'Doe', 'age': 25, 'email': 'john@gmail.com', 'Phone': 76575766766}

print("dict_q", dict_q)
# dict_q {'Name': 'John', 'Surname': 'Doe', 'age': 25, 'email': 'john@gmail.com', 'city': 'Pune'}

print("_" * 50)

###########################################
# get() method --> This method returns the value with the help of key

dict11 = {'Name': 'John', 'Surname': 'Doe', 'age': 25, 'email': 'john@gmail.com', 'city': 'Pune'}
val = dict11.get('email')
print(val)  # john@gmail.com
print(dict11['email'])  # john@gmail.com

print("_" * 50)

#####################################################
# setdefault method :
# --> Set default method will return the current value of the key, if it is available
# --> Set default method will return the new value if key is not available, also
#         it updates the dictionary data with new key value pair.

dict12 = {'Name': 'John', 'Surname': 'Doe', 'age': 25, 'email': 'john@gmail.com', 'city': 'Pune'}

# when key is available, then it will return current value
result = dict12.setdefault('city', 'Mumbai')
print(result)  # Pune

# when key is not available, then it will return current new value with key and update the dict as well
result2 = dict12.setdefault('phone', '6789343434')
print("result2 :", result2)  # 6789343434
print("dict_12 :", dict12)
# dict_12 : {'Name': 'John', 'Surname': 'Doe', 'age': 25, 'email': 'john@gmail.com', 'city': 'Pune', 'phone': '6789343434'}

print("_" * 50)

#####################################################
# fromkeys method --> fromkeys method create a dictionary with list of keys those are holding same value.

result1 = dict.fromkeys((34, 56, 78), 'A')
print(result1)

result2 = dict.fromkeys('Python', [3, 5, 7, 8])
print(result2)
# {'P': [3, 5, 7, 8], 'y': [3, 5, 7, 8], 't': [3, 5, 7, 8], 'h': [3, 5, 7, 8], 'o': [3, 5, 7, 8], 'n': [3, 5, 7, 8]}

result3 = dict.fromkeys([4, 7, 8], 'Hello')
print(result3)  # {4: 'Hello', 7: 'Hello', 8: 'Hello'}

result4 = dict.fromkeys('Hello', 'P')
print(result4)
# {'H': 'P', 'e': 'P', 'l': 'P', 'o': 'P'}
print("_"*50)



