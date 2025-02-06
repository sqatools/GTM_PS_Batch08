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
print("############## Set Data Type #########")
set1  = {55, 12, 3, 5.5, 6, 7, 3, 7, 2, 7}

print(set1, type(set1))
# {2, 3, 5.5, 6, 7} <class 'set'>

"""
 properties of Set:
                -->  Set is mutable data type, we can modify it at any point of time.
                -->  Set only store unique values, duplicate data is not allowed.
                -->  Set store data in random order and print values in random order.
                -->  Set only contains immutable data type as set member
                     int, float, string, tuple, boolean.
                -->  Set does not follow indexing or key value pair format
"""

set2 = {44, 77, 22, 'Hello', (4, 6, 7, 6), True, 44, (4, 6, 6, 7)}
print(set2)
# {True, 22, (4, 6, 7), 'Hello', 44, 77}

tup1 = (4, 6, 6, 6, 6, 6, 9)
print(tup1)

print("_"*50)
# add value to the set
set2.add(100)
print(set2)
set2.add(100) # It won't through error if we try to add same value again.
print(set2)
# {True, (4, 6, 7, 6), 100, 'Hello', 22, (4, 6, 6, 7), 44, 77}

print(dir(set))  # dir return list of method belongs to specific data type
"""
'add', 'clear', 'copy', 'difference', 'difference_update',
 'discard', 'intersection', 'intersection_update', 'isdisjoint', 
 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
  'symmetric_difference_update', 'union', 'update'
"""

# set3 = {4, 5, 6, [4, 5, 7]}
# print(set3)
# TypeError: unhashable type: 'list'
# can not add list/dict/set as member of set
# list/dict/set is mutable datatype which is not allowed in the set.


print("_"*50)
