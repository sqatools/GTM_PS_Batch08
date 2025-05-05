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


##############################
# keys() method : This method return list of keys from given dictionary
dict_b = {'Name' : 'manoj', 'email': 'manoj12@gmail.com', 'phone' : '1234113', 'City': 'hyderabad'}

print(dict_b.keys())
# dict_keys(['Name', 'email', 'phone', 'City'])

val2 = dict_b.keys()
for data in val2:
    print(data)
"""
Name
email
phone
City

"""
print("_"*50)
############################################
# values method() : This method return list of values from dictionary
print(dict_b.values())
# dict_values(['manoj', 'manoj12@gmail.com', '1234113', 'hyderabad'])

data2 = dict_b.values()
print(data2)
# print(data2[0]) # can not use indexing directly
# TypeError: 'dict_values' object is not subscriptable
print(list(data2)[0])  # manoj


############################
# add data to dict

dict_c = {'Name' : 'manoj', 'email': 'manoj12@gmail.com', 'phone' : '1234113', 'City': 'hyderabad'}
dict_c['age'] = 25

print("dict_C :", dict_c)
# dict_C : {'Name': 'manoj', 'email': 'manoj12@gmail.com', 'phone': '1234113', 'City': 'hyderabad', 'age': 25}

################################
# update method : this method help to update one dictionary to another
dict1 = {'a': 123, 'b': 456, 'c': 789}
dict2 = {'p': 345, 'q': 222, 'r': 555}

dict2.update(dict1)
print("dict2:", dict2)
# dict2: {'p': 345, 'q': 222, 'r': 555, 'a': 123, 'b': 456, 'c': 789}

####################
# pop method(): This method remove the key value pair with help of key and return  the value

dict3 = {'p': 345, 'q': 222, 'r': 555, 'a': 123, 'b': 456, 'c': 789}
rm_val = dict3.pop('b')
print("removed value :", rm_val)
# removed value : 456
print("dict_3 :", dict3)
# {'p': 345, 'q': 222, 'r': 555, 'a': 123, 'c': 789}

print("_"*50)

##################
# popitem method() : This method remove key value pair from last value and return it in tuple form

dict4 =  {'p': 345, 'q': 222, 'r': 555, 'a': 123, 'c': 789}

rm_data = dict4.popitem()
print(rm_data) # ('c', 789)
print("dict4 :", dict4)
# {'p': 345, 'q': 222, 'r': 555, 'a': 123}

###############################
# clear method () : this method clear all the data from dictionary

dict4 =  {'p': 345, 'q': 222, 'r': 555, 'a': 123, 'c': 789}
dict4.clear()
print("dict4:", dict4)
# dict4: {}


# del statement or keyword
dict5 = {'p': 345, 'q': 222, 'r': 555, 'a': 123, 'c': 789}
del dict5

#####################
# name error : name 'dict5' is not defined. did you mean: 'dict1'?

dict6 =  {'p': 442, 'q': 444, 'r': 999, 'a': 123, 'c': 789}
del dict6['a']

print("dict6:", dict6)
# {'p': 442, 'q': 444, 'r': 999, 'c': 789}

######################
# copy method : this method help to copy data from one dict to another


# shallow copy : IN shallow we make a reference of one mdict, and if  we will modify  any of them , then
#                changes will reflect on the both the dictionaries

dict_x =  {'p': 442, 'q': 444, 'r': 999, 'a': 123, 'c': 789}
dict_y = dict_x
dict_y['c'] = 1000

print("dict_y:", dict_y)
# {'p': 442, 'q': 444, 'r': 999, 'a': 123, 'c': 1000
print("dict_x:", dict_x)
# {'p': 442, 'q': 444, 'r': 999, 'a': 123, 'c': 1000}

#Deep copy

dict_p = {'Name': 'mj', 'surname': 'jaini', 'age': 25, 'email': 'mj@gmail com'}
dict_q = dict_p.copy()
dict_q['city'] = 'hyderabad'
dict_p['phone'] = '123455'
print("dict_p", dict_p)
# dict_p {'Name': 'mj', 'surname': 'jaini', 'age': 25, 'email': 'mj@gmail com', 'phone': '123455'}
print("dict_q", dict_q)
# dict_q {'Name': 'mj', 'surname': 'jaini', 'age': 25, 'email': 'mj@gmail com', 'phone': '123455'}

print("_"*50)
##############################3
# get method : This method return the value with help of key
dict11 =  {'Name': 'mj', 'surname': 'jaini', 'age': 25, 'email': 'mj@gmail com'}
val = dict11.get('email')
print(val) # mj@gmail com
print(dict11['email']) #  mj@gmail com


print("_"*50)

######################################
# setdefault method :-> set default method will return the current of the way,if it is available
#                    -> sset default method will return the new value if key is not available, also
#                       it updates the dictionary data with new key value pair
dict12 =  {'Name': 'mj', 'surname': 'jaini', 'age': 25, 'email': 'mj@gmail com'}

# when key is available, then it will return current value
result = dict12.setdefault('city', 'goa')
print(result) # goa


# when key is not available, then it will return current new value with new key  and update the dict as well
result2 = dict12.setdefault('phone', '123445')
print("result12:", result2) # 123445
print("dict_12:", dict12)
# dict_12: {'Name': 'mj', 'surname': 'jaini', 'age': 25, 'email': 'mj@gmail com', 'city': 'goa', 'phone': '123445'}


print("_"*50)
###################################
# from keys method: from key method create a dictionary with the help of list of keys those are holding same value.

result = dict.fromkeys([34, 56, 78], 'A')
print(result)
# {34: 'A', 56: 'A', 78: 'A'}

result2 = dict.fromkeys('python', [3, 5, 7, 8])
print(result2)
# {'p': [3, 5, 7, 8], 'y': [3, 5, 7, 8], 't': [3, 5, 7, 8], 'h': [3, 5, 7, 8], 'o': [3, 5, 7, 8], 'n': [3, 5, 7, 8]}

result3 = dict.fromkeys([4, 7, 8], 'helllo')
print(result3) #{ 4: 'helllo', 7: 'helllo', 8: 'helllo'}

result4 = dict.fromkeys('hello', 'p')
print(result4)
# {'h': 'p', 'e': 'p', 'l': 'p', 'o': 'p'}

############################
# st_data
st_data = { 'st_1': {},
           'st_2': {},
           'st_3': {},
          }
