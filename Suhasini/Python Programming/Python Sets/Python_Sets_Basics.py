set1 = {3, 5, 7, 'Hello'}
print(set1, type(set1))   # {3, 'Hello', 5, 7} <class 'set'>

"""
Properties of Set :
1. Set is mutable data type, we can modify it.
2. Set can contain only immutable data type as member i.e int, float, string, tuple, bool
3. Set is represented with curly braces {}
4. Set stores data in random order, it does not follow any indexing
5. Set contains only unique data, duplicates are not allowed.

"""
print("_" * 50)

set2 = {3, 5.6, 'Python', (3, 6, 8), True, None, 3, 5.6, False}
print(set2)
# {None, True, False, 3, 5.6, (3, 6, 8), 'Python'}

print("_" * 50)

# defined mutable data type as set member
set3 = {4, 6, 7,
       #  [5, 7, 8],
       #  {'a': 123, 'b': 567},
       #  {3, 6, 9, 1, 55},
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
a
66
b
5
7
9
11
55

"""
print("_"*50)

######################### Set Methods #################
print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

print("_" * 50)

####################
# add method : This method adds one value at any given time and the value is
#              added at any random position

setA = {4, 6, 8, 11, 55, 77}
setA.add(100)
print(setA)
# {4, 100, 6, 55, 8, 11, 77}
print("_" * 50)

######################
# update method : This method updates one set to another

setB = {5, 7, 8, 2}
setC = {'a', 'b', 'c', 'd'}

val = setC.update(setB)
print("SetB: ",setB) # SetB:  {8, 2, 5, 7}
print("SetC: ",setC) # SetC:  {2, 'a', 5, 7, 8, 'c', 'd', 'b'}
print(val) # None

print("_" * 50)

####################
# union() method : This method combines 2 sets and gives a new set.
#                   This method does not modify original sets

set_d = {5, 7, 8, 2}
set_e = {'a', 'b', 'c', 'd'}

set_f = set_d.union(set_e)
print("Set_d: ",set_d)  # Set_d:  {8, 2, 5, 7}
print("set_e: ",set_e)   # set_e:  {'d', 'b', 'a', 'c'}
print("Union of the sets: ",set_f)
# Union of the sets:  {'d', 2, 5, 'b', 7, 8, 'a', 'c'}
print("_" * 50)

####################
# concatenation is not allowed in set
# set_k = {44, 55, 77}
# set_g = set_d + set_k
# print(set_g) # unsupported operand type(s) for +: 'set' and 'set'

print("_" * 50)

####################
# remove() method : This method removes existing value from the set, if the value is not present in set then
#                   it fails with keyError

# Remove available item:
set_q = {'a', 'b', 'v', 'n', 'm'}
set_q.remove('b')
print(set_q)
#  {'n', 'v', 'm', 'a'}

# Remove item that is not available:
# set_q.remove('z')   # KeyError: 'z'
print("_" * 50)

#######################
# discard() method  : This method works like remove() but it does not throw error
#                       if item is not present in the set

set_r = {'a', 'b', 'v', 'n', 'm'}

# discard existing value
set_r.discard('a')
print(set_r)
# {'m', 'n', 'b', 'v'}

# discard non-existing item:
set_r.discard('a')   # it does not throw error
print(set_r)
# {'m', 'b', 'n', 'v'}
print("_"*50)

########################
# pop() method : This method removes existing item from set and returns it. This method
#                   does not take any parameter as there is no need to specify value

set_w = {'a', 'b', 'v', 'n', 'm', 'x', 'y', 'z'}

val = set_w.pop()
set_w = {'a', 'b', 'v', 'n', 'm', 'x', 'y', 'z'}

val = set_w.pop()
print("removed value :", val)
# removed value : y
print("set_w :", set_w)
# set_w : {'z', 'n', 'm', 'v', 'x', 'b', 'a'}

for i in range(3):
    print(set_w.pop())

"""
z
m
x

"""
print(set_w) # {'b', 'n', 'y', 'a'}
print("_"*50)

############################
# clear() method : This method clears all data from set and empty set remains

set_p = {'b', 'a', 'z', 'm', 's', 'd', 'f'}
set_p.clear()
print("set_p :", set_p)  # set_p : set()

var1 = set()  # empty set.

print("_" * 50)

############################
# del statement : remove specific set variable from memory

set_l = {'b', 'a', 'z', 'm', 's', 'd', 'f'}
del set_l

##print("set_l :", set_l)
# NameError: name 'set_l' is not defined. Did you mean: 'set_a'?

#############################
# intersection() Method : This method returns common values from 2 sets

set_11 = {'a', 'b', 'c', 'd', 'e', 'f'}
set_12 = {'p', 'q', 'a', 'r', 'b', 'c', 's'}

commonVal = set_11.intersection(set_12)
print("Common values from the sets are: ",commonVal)
# Common values from the sets are:  {'b', 'c', 'a'}
print("set11 :", set_11)  # {'c', 'a', 'd', 'e', 'b', 'f'}
print("set_12:", set_12)  # {'s', 'a', 'c', 'b', 'q', 'r', 'p'}

print("_" * 50)

################################
# intersection_update() Method : This method modifies any one set with the common values of 2 sets

set_12.intersection_update(set_11)
print("set11 :", set_11)  # set11 : {'f', 'b', 'c', 'a', 'e', 'd'}
print("set_12:", set_12)  # set_12: {'b', 'c', 'a'}

print("_" * 50)

######################
# difference method() : This method returns a set of difference values from set1 to set2

set_13 = {'a', 'b', 'c', 'd', 'e', 'f', 3, 5}
set_14 = {'p', 'q', 'a', 'r', 'b', 'c', 's'}

diff_output = set_13.difference(set_14)
print("Difference: ",diff_output)
# Difference:  {'f', 3, 5, 'd', 'e'}

diff_output2 = set_14.difference(set_13)
print("diff output2 :", diff_output2)
# diff output2 : {'p', 's', 'r', 'q'}

print("_" * 50)

######################
# difference_update method() : This method updates the target set with difference output

# this will update set_13 with difference value.
set_13.difference_update(set_14)
print("Set_13: ",set_13)
# Set_13:  {3, 5, 'd', 'f', 'e'}

print("_" * 50)

######################
# symmetric_difference() : This method returns difference values from both the sets.

set_15 = {1, 4, 7, 8, 'a', 'b'}
set_16 = {'p', 'q', 1, 4, 7, 8}

sym_difference = set_15.symmetric_difference(set_16)
print("Symmetric Difference: ",sym_difference)
# Symmetric Difference:  {'b', 'a', 'p', 'q'}

# symmetric_difference_update
set_15.symmetric_difference_update(set_16)
print("set_15 :", set_15) # {'b', 'p', 'a', 'q'}
print("set_16 :", set_16) # {1, 4, 'p', 7, 8, 'q'}

print("_" * 50)

###############################
# superset and subset method : Superset method check the given value in set, has all the value
#                           from other child set as well, then it super set.
#                           ->  When we have big set values and compare with small set, which
#                           ->  can include child set values, thn it is known as subset.

set_17 = {1, 4, 7, 8, 'a', 'b', 'P', 'Q', 'R'}
set_18 = {'P', 'Q', 'R'}
set_19 = {'a', 'b', 8, 10}

print("set_17 is super set :", set_17.issuperset(set_18)) # True
print("set_18 is subset of set_17 :", set_18.issubset(set_17)) # True
print("set_19 is subset of set_17 :", set_19.issubset(set_17)) # False

print("_"*50)
#####################################

set_17 = {1, 4, 7, 8, 'a', 'b', 'P', 'Q', 'R'}
set_18 = {'P', 'Q', 'R'}
set_20 = {'P','Q', 'R'}
print(set_18.issubset(set_20))
print(set_18.issuperset(set_20))

print("_"*50)

##############################
# isdisjoint method : this method checks if both the sets have completely different items in them

set_21 = {1, 4, 7, 8, 'a', 'b', 'P', 'Q', 'R'}
set_22 = {'P', 'Q', 'R'}
set_23 = {'A', 'B', 'C'}

print(set_22.isdisjoint(set_21)) # False
# set_23 has completely different value from target set.
print(set_22.isdisjoint(set_23)) # True
print("_"*50)

##############################
# copy method  :  This method help to copy content from on set to another.

# shallow copy
set_24 = {5, 7, 9, 11}
set_25 = set_24
set_25.add(100)
set_24.add(200)

print("set_24 :", set_24 ) # {100, 5, 7, 200, 9, 11}
print("set_25 :", set_25 ) # {100, 5, 7, 200, 9, 11}

# Deep Copy
print("_"*50)
set_27 = {11, 66, 88, 22, 26}

set_26 = set_27.copy()
set_26.add(400)

print("set_26 :", set_26) # {400, 66, 22, 88, 26, 11}
print("set_27 :", set_27) # {66, 22, 88, 26, 11}




