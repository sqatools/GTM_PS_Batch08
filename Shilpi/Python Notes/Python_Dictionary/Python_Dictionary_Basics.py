"""
# Dict properties
-> Dict is mutable data type. we can modify it
-> Dict store data in key value pair with curly braces eg.{'a' : 123}
-> Dict only contains unique key, duplicate keys are not allowed.
-> If we provide duplicate key, then last defined key data will be consider.
   e.g . {'a' ; 123, 'b' : 456 'a' : 111}
   output = {'a': 111, 'b' : 456}
-> only immutable data type can be key in dictionary, e.g. int, float , string, tuple, tuple,boolean
-> All type of data can be value in the dictionary. e.g. int, float , string, tuple, bool, set, list,
-> Dict can contain duplicate values
-> Dict follows the LIFO(LAST IN FIRST OUT) concept
-> Dict does not follow indexing.
"""

dict1 = {'a': 123, 'b': 456}
print(dict1, type(dict1))
# {'a': 123, 'b': 456} <class 'dict'>


# Add new content to dict
dict1['c'] = 567
print("dict1 :", dict1)
# dict1 : {'a': 123, 'b': 456, 'c': 567}
print("_"*50)

# Dict only contains unique key, duplicate keys are not allowed.
dict2 = {'a': 456, 'b': 567, 'c': 333, 'a': 567}
print(dict2)
# {'a': 567, 'b': 567, 'c': 333}


print("_"*50)
############################
# only immutable data type can be key in dictionary, e.g. int, float , string, tuple, tuple,boolean

dict3 = {
    23 : 3.5,
    44.5 : 'heyy',
    'pycharm' : [2, 4, 6],
    (3, 5, 7) : {'a': 123, 'b': 234},
    True : (4, 77, 88)
}

print("dict3 :", dict3)
# dict3 : {23: 3.5, 44.5: 'heyy', 'pycharm': [2, 4, 6], (3, 5, 7): {'a': 123, 'b': 234}, True: (4, 77, 88)}

###########
dict5 = {
    23 : 3.5,
    44.5 : 'heyy',
    'pycharm' : [2, 4, 6],
    (3, 5, 7) : {'a': 123, 'b': 234},
    True : (4, 77, 88, [4, 6, 8])
}

print(dict5['pycharm']) # [2, 4, 6]
print(dict5['pycharm'][1]) # 4
print(dict5[(3, 5, 7)]) # {'a': 123, 'b': 234}
print(dict5[True]) # (4, 77, 88, [4, 6, 8])
print(dict5[True][3][2]) # 8


##################### apply loop on the dictionary ###########

dict6 = {'a': 345, 'b': 678, 'c' : 123}

for val in dict6:
    print(val)
"""
a
b
c
"""

for k in dict6:
    print(k, dict6[k])
"""
a 345
b 678
c 123
"""

for data in dict6.items():
    print(data)
"""
('a', 345)
('b', 678)
('c', 123)
"""

# get key and value in 2 seperate variaable
for k, v in dict6.items():
    print("key :", k, "value", v)

"""
key : a value 345
key : b value 678
key : c value 123
"""
