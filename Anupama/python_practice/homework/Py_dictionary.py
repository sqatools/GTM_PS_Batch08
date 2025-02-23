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
