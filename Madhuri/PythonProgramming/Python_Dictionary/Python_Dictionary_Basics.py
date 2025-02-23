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

print("_" * 50)
############################### Apply loop on the dictionary ##########

dict6 = {'a': 345, 'b': 678, 'c': 123}

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
    # print("key :", k, "value:", v)
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

print("_" * 50)
##############################################
# keys() method :  this method return list of keys from given dictionary.
dict_b = {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 456788923, 'city': 'Mumbai'}

print(dict_b.keys())
val = dict_b.keys()
print(val, type(val), list(val)[2])
# dict_keys(['Name', 'email', 'phone', 'city']) <class 'dict_keys'> phone

# dict_keys(['Name', 'email', 'phone', 'city'])

val2 = dict_b.keys()
for data in val2:
    print(data)
"""
Name
email
phone
city

"""
print("_" * 50)
#############################################
# values method() : This method return list of values from dictionary.
print(dict_b.values())
# dict_values(['Rahul', 'rahul@gmail.com', 456788923, 'Mumbai'])

data2 = dict_b.values()
print(data2)
# print(data2[0]) # can not use indexing directly.
# TypeError: 'dict_values' object is not subscriptable
print(list(data2)[0])  # Rahul

print("_" * 50)
########################
# add data to dict with new key

dict_c = {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 456788923, 'city': 'Mumbai'}
dict_c['age'] = 25

print("dict_c :", dict_c)
# {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 456788923, 'city': 'Mumbai', 'age': 25}

##################################
# update method : this method help to update one dictionary to another.
dict1 = {'a': 123, 'b': 456, 'c': 789, 'r': 999}
dict2 = {'p': 345, 'q': 222, 'r': 555}

dict2.update(dict1)
print("dict2 :", dict2)
# {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'b': 456, 'c': 789}

print("_" * 50)
###############
# pop method() : This method remove the key value pair with help of key and return the value

dict3 = {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'b': 456, 'c': 789}
rm_val = dict3.pop('b')
print("removed value :", rm_val)
# removed value : 456

print("dict_3 :", dict3)
# {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'c': 789}


print("_" * 50)
###############
# popitem method() : This remove key value pair from last value and return it in tuple form.

dict4 = {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'c': 789}

rm_data = dict4.popitem()
print(rm_data)  # ('c', 789)
print("dict4 :", dict4)
# {'p': 345, 'q': 222, 'r': 999, 'a': 123}


######################
# clear method() : this method clear all the data from dictionary

dict4 = {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'c': 789}
dict4.clear()
print("dict 4:", dict4)
# dict 4: {}

##########################
# del statement or keyword :  This can remove entire dict variable from memory

dict5 = {'p': 345, 'q': 222, 'r': 999, 'a': 123, 'c': 789}
del dict5
# print(dict5)
# NameError: name 'dict5' is not defined. Did you mean: 'dict1'?


# remove specific data using del statement
dict6 = {'p': 442, 'q': 444, 'r': 999, 'a': 33, 'd': 789}
del dict6['a']

print("dict6 :", dict6)
# {'p': 442, 'q': 444, 'r': 999, 'd': 789}

print("_" * 50)
############################
# copy method : This method help to copy data from one dict to another.

# shallow copy :  In shallow we make a reference of one dict, and if we will modify any of them, then
#                 changes will reflect on the both the dictionaries.

dict_x = {'p': 442, 'q': 444, 'r': 999, 'a': 33, 'd': 789}
dict_y = dict_x
dict_y['c'] = 1000

print("dict_y :", dict_y)
# {'p': 442, 'q': 444, 'r': 999, 'a': 33, 'd': 789, 'c': 1000}

print("dict_x :", dict_x)
# {'p': 442, 'q': 444, 'r': 999, 'a': 33, 'd': 789, 'c': 1000}


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
#####################################################
# get method :  this return the value with help of key
dict11 = {'Name': 'John', 'Surname': 'Doe', 'age': 25, 'email': 'john@gmail.com', 'city': 'Pune'}
val = dict11.get('email')
print(val)  # john@gmail.com

print(dict11['email'])  # john@gmail.com

print("_" * 50)
#####################################################
# setdefault method : ->  Set default method will return the current of the key, if it is available
#                      ->  Set default method will return the new value if key is not available, also
#                          it updates the dictionary data with new key value pair.
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
# fromkeys method: from key method create a dictionary with list of keys those are holding same value.

result = dict.fromkeys((34, 56, 78), 'A')
print(result)
# {34: 'A', 56: 'A', 78: 'A'}

result2 = dict.fromkeys('Python', [3, 5, 7, 8])
print(result2)
# {'P': [3, 5, 7, 8], 'y': [3, 5, 7, 8], 't': [3, 5, 7, 8], 'h': [3, 5, 7, 8], 'o': [3, 5, 7, 8], 'n': [3, 5, 7, 8]}

result3 = dict.fromkeys([4, 7, 8], 'Hello')
print(result3)  # {4: 'Hello', 7: 'Hello', 8: 'Hello'}

result4 = dict.fromkeys('Hello', 'P')
print(result4)
# {'H': 'P', 'e': 'P', 'l': 'P', 'o': 'P'}

#############################
# st_data
st_data = {'st_1': {},
           'st_2': {},
           'st_3': {},
           }


it_company = {
    'HR': {
        'Recruiter HR': [
            {'name': 'Aarav Sharma', 'email': 'aarav.sharma@itcompany.com', 'phone': '987-654-3210'},
            {'name': 'Ishita Verma', 'email': 'ishita.verma@itcompany.com', 'phone': '987-654-3211'}
        ],
        'Activity HR': [
            {'name': 'Ananya Reddy', 'email': 'ananya.reddy@itcompany.com', 'phone': '987-654-3212'},
            {'name': 'Karan Singh', 'email': 'karan.singh@itcompany.com', 'phone': '987-654-3213'}
        ],
        'Payroll HR': [
            {'name': 'Priya Patel', 'email': 'priya.patel@itcompany.com', 'phone': '987-654-3214'},
            {'name': 'Vikram Joshi', 'email': 'vikram.joshi@itcompany.com', 'phone': '987-654-3215'}
        ]
    },
    'Management': {
        'Managers': [
            {'name': 'Sanya Gupta', 'email': 'sanya.gupta@itcompany.com', 'phone': '987-654-3216'},
            {'name': 'Rohit Mehta', 'email': 'rohit.mehta@itcompany.com', 'phone': '987-654-3217'},
            {'name': 'Meera Chawla', 'email': 'meera.chawla@itcompany.com', 'phone': '987-654-3218'}
        ],
        'Teamlead': [
            {'name': 'Kabir Kapoor', 'email': 'kabir.kapoor@itcompany.com', 'phone': '987-654-3219'},
            {'name': 'Simran Bhatia', 'email': 'simran.bhatia@itcompany.com', 'phone': '987-654-3220'},
            {'name': 'Aditya Sethi', 'email': 'aditya.sethi@itcompany.com', 'phone': '987-654-3221'}
        ],
        'Module Lead': [
            {'name': 'Riya Nair', 'email': 'riya.nair@itcompany.com', 'phone': '987-654-3222'},
            {'name': 'Neeraj Malhotra', 'email': 'neeraj.malhotra@itcompany.com', 'phone': '987-654-3223'},
            {'name': 'Divya Yadav', 'email': 'divya.yadav@itcompany.com', 'phone': '987-654-3224'}
        ]
    },
    'Development': {
        'UI Dev': {
            'Sr Dev': [
                {'name': 'Rahul Rao', 'email': 'rahul.rao@itcompany.com', 'phone': '987-654-3225'},
                {'name': 'Neha Mishra', 'email': 'neha.mishra@itcompany.com', 'phone': '987-654-3226'}
            ],
            'Jr Dev': [
                {'name': 'Tara Kulkarni', 'email': 'tara.kulkarni@itcompany.com', 'phone': '987-654-3227'},
                {'name': 'Amit Deshmukh', 'email': 'amit.deshmukh@itcompany.com', 'phone': '987-654-3228'}
            ]
        },
        'API Dev': {
            'Sr Dev': [
                {'name': 'Rajesh Menon', 'email': 'rajesh.menon@itcompany.com', 'phone': '987-654-3229'},
                {'name': 'Pooja Ghosh', 'email': 'pooja.ghosh@itcompany.com', 'phone': '987-654-3230'}
            ],
            'Jr Dev': [
                {'name': 'Manoj Choudhury', 'email': 'manoj.choudhury@itcompany.com', 'phone': '987-654-3231'},
                {'name': 'Lavanya Shetty', 'email': 'lavanya.shetty@itcompany.com', 'phone': '987-654-3232'}
            ]
        },
        'Database Dev': {
            'Sr Dev': [
                {'name': 'Anil Gupta', 'email': 'anil.gupta@itcompany.com', 'phone': '987-654-3233'},
                {'name': 'Shalini Iyer', 'email': 'shalini.iyer@itcompany.com', 'phone': '987-654-3234'}
            ],
            'Jr Dev': [
                {'name': 'Gautam Kulkarni', 'email': 'gautam.kulkarni@itcompany.com', 'phone': '987-654-3235'},
                {'name': 'Sanya Bajaj', 'email': 'sanya.bajaj@itcompany.com', 'phone': '987-654-3236'}
            ]
        }
    },
    'Support': {
        'Internal Support': [
            {'name': 'Devika Singh', 'email': 'devika.singh@itcompany.com', 'phone': '987-654-3237'},
            {'name': 'Ajay Pawar', 'email': 'ajay.pawar@itcompany.com', 'phone': '987-654-3238'}
        ],
        'Customer Support': [
            {'name': 'Ritu Jain', 'email': 'ritu.jain@itcompany.com', 'phone': '987-654-3239'},
            {'name': 'Naveen Khan', 'email': 'naveen.khan@itcompany.com', 'phone': '987-654-3240'}
        ]
    },
    'Testing': {
        'Manual Tester': [
            {'name': 'Radhika Basu', 'email': 'radhika.basu@itcompany.com', 'phone': '987-654-3241'},
            {'name': 'Suresh Patil', 'email': 'suresh.patil@itcompany.com', 'phone': '987-654-3242'}
        ],
        'Automation Tester': [
            {'name': 'Mitali Joshi', 'email': 'mitali.joshi@itcompany.com', 'phone': '987-654-3243'},
            {'name': 'Vishal Prasad', 'email': 'vishal.prasad@itcompany.com', 'phone': '987-654-3244'}
        ],
        'Performance Tester': [
            {'name': 'Shruti Kulkarni', 'email': 'shruti.kulkarni@itcompany.com', 'phone': '987-654-3245'},
            {'name': 'Akash Desai', 'email': 'akash.desai@itcompany.com', 'phone': '987-654-3246'}
        ],
        'Security Tester': [
            {'name': 'Tanvi Kapoor', 'email': 'tanvi.kapoor@itcompany.com', 'phone': '987-654-3247'},
            {'name': 'Rakesh Rao', 'email': 'rakesh.rao@itcompany.com', 'phone': '987-654-3248'}
        ]
    },
    'Administration': {
        'Payroll admin': [
            {'name': 'Parul Nair', 'email': 'parul.nair@itcompany.com', 'phone': '987-654-3249'},
            {'name': 'Sameer Ahuja', 'email': 'sameer.ahuja@itcompany.com', 'phone': '987-654-3250'}
        ],
        'Employee admin': [
            {'name': 'Sneha Reddy', 'email': 'sneha.reddy@itcompany.com', 'phone': '987-654-3251'},
            {'name': 'Ravi Sharma', 'email': 'ravi.sharma@itcompany.com', 'phone': '987-654-3252'}
        ],
        'Facility admin': [
            {'name': 'Meghna Dixit', 'email': 'meghna.dixit@itcompany.com', 'phone': '987-654-3253'},
            {'name': 'Vijay Goel', 'email': 'vijay.goel@itcompany.com', 'phone': '987-654-3254'}
        ]
    }
}
