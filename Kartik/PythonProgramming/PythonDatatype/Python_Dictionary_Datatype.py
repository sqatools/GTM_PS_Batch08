"""
Types of Python data types.
1. Numbers
   i). Integer :  Immutable
   ii). Float : Immutable
   iii). Complex number  : Immutable

2. Sequential
   i). String : Immutable
   ii). List :  mutable
   iii). Tuple : Immutable

3. Dictionary : mutable
4. Set : mutable
5. Boolean : Immutable
"""

print("_" * 50)
print("#############$## Dictionary Data Type #########")

dict1 = {'a' : 345, 'b': 678, 'c': 123}
print(dict1, type(dict1)) # {'a': 345, 'b': 678, 'c': 123} <class 'dict'>

"""
# properties of Dictionary
                    --> Dictionary is mutable data type, we can modify and update.
                    --> Dictionary only contains unique key, duplicate keys are not allowed.
                    --> Dictionary store data in key value format
                    --> Dictionary only contains immutable data type as key, int, float, string, tuple , boolean.
                         list, dict, set can not be key in dict.
                    -->  Dictionary can contain all different data types as value
                    -->  for dict there is no restriction, it can contains all types of data 
                         int, float, string, list, tuple, dict, set, boolean
                    -->  Dictionary does not follow indexing.
                    -->  Dictionary follows LIFO (Last In First Out)
"""

# get value from dictionary
dict2 = {'Name': 'Rahul', 'Age' : 25, 'City' : 'Mumbai', 'Email' : 'rahul@gmail.com'}
print(dict2['Email'])

# add data to dictionary
dict2['phone'] = 647567567
print(dict2)

dict2.pop('City')
print(dict2)

print("_"*50)
var1 = 1000
val2 = {'em_name' : 'Vishal', 'emp_salary': 500000, 'designation': 'software engineer'}
dict3 = {
         123: 3.5,
         3.5 : 'Hello',
         'Python' : [5, 6, 8, 9],
          # [1, 3, 4] : (4, 5, 6)  #   TypeError: unhashable type: 'list'
         (4, 7, 1) : {'a' : 123, 'b' : 456},
         # 123 : 500  # duplicate are not allowed
         var1 : 'Programming',
         'emp_details' : val2,
}

from pprint import pprint

#print(dict3)
pprint(dict3)


dict4 = {3.5: 'Hello',
 123: 3.5,
 1000: 'Programming',
 'Python': [5, 6, 8, 9],
 'emp_details': {'designation': 'software engineer',
                 'em_name': 'Vishal',
                 'emp_salary': 500000},
 (4, 7, 1): {'a': 123, 'b': 456}}

print(dict4['emp_details']['em_name']) # Vishal

print("_"*50)