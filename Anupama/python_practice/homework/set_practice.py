set1 = {3, 5, 7, 'Hello'}
print(set1, type(set1))
# {5, 3, 'Hello', 7} <class 'set'>

"""
# Properties of Set
1.  Set is mutable datatype, we can modify any time as like list and dict.
2.  Set can contain only immutable data type as member. e.g int, float, string, tuple, bool
3.  Set represent with curly braces {}.
4.  Set store data in random order, it does not follow any indexing
5.  Set only contains unique data, duplicate values are not allowed.
"""

print("_" * 50)
set2 = {3, 5.6, 'Python', (3, 6, 8), True, None, 3, 5.6, False}
print(set2)
# {None, True, False, 3, 5.6, 'Python', (3, 6, 8)}


print("_" * 50)
# defined mutable data type as set member
set3 = {4, 6, 7,
        # [5, 7, 8],
        # {'a': 123, 'b': 567},
        # {3, 6, 9, 1, 55},
        (3, 1, 5)}

print(set3)
# TypeError: unhashable type: 'list'
# TypeError: unhashable type: 'dict'
# TypeError: unhashable type: 'set'


print("_" * 50)
# apply for loop on set data type
set4 = {5, 7, 9, 11, 55, 66, 'a', 'b'}

for val in set4:
    print(val)

"""
66
5
b
7
9
11
55
a
"""

######################### Set Methods #################
print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']


print("_" * 50)
####################
# add method :  This method add one value at a time in given set, value may store at any random place in set.
set_a = {4, 6, 8, 11, 55, 77}
set_a.add(100)
print("set_a :", set_a)  # {4, 100, 6, 55, 8, 11, 77}

print("_" * 50)
####################
# update method : This method update one set to another set.
set_b = {5, 7, 8, 2}
set_c = {'a', 'b', 'c', 'd'}

val = set_c.update(set_b)
print("set_c :", set_c)  # {2, 5, 7, 'a', 8, 'd', 'c', 'b'}
print("set_b :", set_b)  # {8, 2, 5, 7}
print(val)  # None

print("_" * 50)
####################
# union() method : This method helps to combine two sets value and return new set, does not modify original set.

set_d = {5, 7, 8, 2}
set_e = {'a', 'b', 'c', 'd'}

set_f = set_d.union(set_e)
print("set_f :", set_f)  # {2, 5, 7, 8, 'd', 'c', 'a', 'b'}
print("set_d :", set_d)  # {8, 2, 5, 7}
print("set_e :", set_e)  # {'b', 'd', 'c', 'a'}
print(set_d.union(set_e))  # {2, 5, 7, 8, 'b', 'd', 'c', 'a'}

# concatenation is not allowed in set
# set_k = {44, 55, 77}
# set_g = set_d + set_k
# print(set_g) # unsupported operand type(s) for +: 'set' and 'set'

print("_" * 50)
####################
# remove() method : This method remove existing available value from set, and it value is not available
#                   it fails with keyError
set_q = {'a', 'b', 'v', 'n', 'm'}

# remove available value
set_q.remove('n')
print("set_q :", set_q)  # {'a', 'b', 'm', 'v'}

# remove non - available value
# set_q.remove('z')
# KeyError: 'z'


print("_" * 50)
####################
# discard() method  : This method works similar like remove method, but it does not throw error if
#                     target value is not available in the set.

set_r = {'a', 'b', 'v', 'n', 'm'}

# discard existing value
set_r.discard('m')
print("set_r :", set_r)  # {'v', 'n', 'a', 'b'}

# discard non-existing value

set_r.discard('x')  # it does not throw error.
print("set_r :", set_r)  # {'v', 'a', 'b', 'n'}

print("_" * 50)
####################
# pop() method : This method remove existing data from set and return it. No need to specify value as parameter.

set_w = {'a', 'b', 'v', 'n', 'm', 'x', 'y', 'z'}

val = set_w.pop()
print("removed value :", val)
# removed value : m
print("set_w :", set_w)
# set_w : {'x', 'v', 'a', 'z', 'b', 'n', 'y'}

for i in range(3):
    print(set_w.pop())
"""
x
v
y
"""
print("set_w :", set_w)
# {'b', 'a', 'z', 'm'}


print("_" * 50)
####################
# clear() method :  clear method remove all the data from set and remain empty set

set_p = {'b', 'a', 'z', 'm', 's', 'd', 'f'}
set_p.clear()
print("set_p :", set_p)  # set_p : set()

var1 = set()  # empty set.

print("_" * 50)
####################
# del statement : remove specific set variable from memory

set_l = {'b', 'a', 'z', 'm', 's', 'd', 'f'}
del set_l

# print("set_l :", set_l)
# NameError: name 'set_l' is not defined. Did you mean: 'set_a'?


print("_" * 50)
##############################################
# intersection() Method :  This method return the common values between 2 sets
set_11 = {'a', 'b', 'c', 'd', 'e', 'f'}
set_12 = {'p', 'q', 'a', 'r', 'b', 'c', 's'}

common_val = set_11.intersection(set_12)
print("common values :", common_val)  # {'b', 'c', 'a'}
print("set11 :", set_11)  # {'c', 'a', 'd', 'e', 'b', 'f'}
print("set_12:", set_12)  # {'s', 'a', 'c', 'b', 'q', 'r', 'p'}

print("_" * 50)
# intersection_update() Method :  This method modify anyone original set with command value between two sets.

set_12.intersection_update(set_11)
print("set11 :", set_11)  # {'b', 'c', 'a'}
print("set_12:", set_12)  # {'r', 's', 'q', 'b', 'p', 'c', 'a'}