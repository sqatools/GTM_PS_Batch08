set1 = {2, 3, 4, 5, 'Pankaj'}
print(set1, type(set1))
# {2, 3, 4, 5, 'Pankaj'} <class 'set'>

print("_"*70)
"""
# Properties of Set
1. Set is a mutable data type, we can modify like dict and list.
2. Set can contain only immutable data type as member. eg, int, float, tuple, bool,.
3. Set represents with curly braces {}.
4. Set store data in random order, it does't follow indexing.
5. Set only contains unique data, duplicate values are not allowed.
"""

print("_"*70)
set2 = {2, 3, 2.3, 'Pankaj', True, False, (2, 3, 9.9), None}
print(set2)
# {False, True, 2, 3, 2.3, (2, 3, 9.9), None, 'Pankaj'}

# Note if list is added : TypeError: unhashable type: 'list'

print("_"*70)
set3 = {2, 3, 4, 5,
      #  [2, 3, 4], # TypeError: unhashable type: 'list'
      #  {3, 9, 5, 'Pankaj'},# TypeError: unhashable type: 'set'
      #  {'a': 'Pankaj', 'b': 'Darshika'} # TypeError: unhashable type: 'dict'
        }
print(set3)
# {2, 3, 4, 5}

print("_"*70)
# Apply for loop for set
set4 = {2, 3.4, 'Pankaj', "DP", True, 3, 77, 99.9}
for val in set4:
        print(val)
"""
True
2
3
3.4
99.9
DP
77
Pankaj
"""

################################ Set methods ######################################
print("_"*70)
print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
# 'union', 'update'

print("_"*70)
# 1. Add Method: This method is used to add one value, and value will be stored in random place
set_a = {2, 3, 4, "Pankaj"}
set_a.add(100)
print("set_a: ", set_a)
# {2, 3, 100, 4, 'Pankaj'}

print("_"*70)
# 2. Update Method: Will update one set to another set and doest not return any value.
set_b = {2, 3, 4}
set_c = {'a', 'b', 'c'}
val = set_c.update(set_b)
print(set_c) # {2, 3, 'c', 4, 'a', 'b'}
print(set_b) # {2, 3, 4}
print(val) # None

print("_"*70)
# 3. Union Method: This will combine two set and return value
set_e = {4, 5, 7, 8, 9}
set_f = {'Pankaj', 'P', 'D'}
val1 = set_f.union(set_e)
print(set_e)
print(set_f)
print(val1)
# {4, 5, 7, 8, 9}
# {'P', 'Pankaj', 'D'}
# {4, 5, 'Pankaj', 'P', 7, 8, 9, 'D'}

# Concatenation is not allowed in se
# set_g = {4, 5, 7, 8, 9}
# set_h = {'Pankaj', 'P', 'D'}
# val2 = set_h + set_g # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(val2)

print("_"*70)
# 4. Remove method: This will remove existing value from set, and if value is not available will give error.
set_i = {2, 3, 4, 5, 6}
set_i.remove(2)
# set_i.remove(9) # KeyError: 9
print(set_i)
# {3, 4, 5, 6}

print("_"*70)
# 5. Discard method: It's similar to remove but does not give error if target value is not available.
set_j = {9, 8, 7, 3}
set_j.discard(4) # No error
set_j.discard(8)
print(set_j)
# {9, 3, 7}

print("_"*70)
# 6. pop() method: this will remove exhisting data from set and return it. No need to specify value as parameter.
set_k = {'a', 'b', 'c', 'd', 'e'}
val3 = set_k.pop()
print(val3)
# b

for i in range(3):
        print(set_k.pop())
"""
a
d
c
b
"""

print("_"*70)
# 6. Clear method : it will remove all data from set
set_l = {'a', 'b', 'c', 'd', 'e'}
set_l.clear()
print(set_l) # set() means empty

# del statement : remove specific set variable from memory
set_m = {'a', 'b', 'c', 'd', 'e'}
del set_m
# print(set_m)
# NameError: name 'set_m' is not defined. Did you mean: 'set_a'?

print("_"*70)
# 7.intersatcion() method: this will return common values between two set
set_n = {2, 3, 4, 5, 6, 7, 8, 9}
set_o = {1, 5, 6, 7.7, 8, 9}
common_value = set_n.intersection(set_n)
print(common_value)
# {2, 3, 4, 5, 6, 7, 8, 9}

print("_"*70)
# 8.intersection_update method: this method modify anyone original set with common value between two sets.

set_n.intersection_update(set_o)
print(set_n) # {8, 9, 5, 6}
print(set_o) # {1, 5, 6, 7.7, 8, 9}

print("_"*70)
# 9. difference method: this method return set of difference value in sets
set_1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
set_2 = {'c', 'd', 'e', 'f', 'g', 'h', 'i'}
value1 = set_2.difference(set_1)
value2 = set_1.difference(set_2)
print(value1) # {'i', 'h'}

print(value2) # {'a', 'b'}

print("_"*70)
# 10. difference_update method(): this method update the target set with difference output
set_11 = {1, 2, 3, 4}
set_22 = {4, 5, 6, 7}
set_11.difference_update(set_22)
print(set_11)
print(set_22)

print("_"*70)
# 11. Symmetric_Update(): this method will return the difference value from both the sets
set_33 = {1, 2, 3, 4}
set_44 = {4, 5, 6, 7}
value3 = set_33.symmetric_difference(set_44)
print(value3)

print("_"*70)
# 12. Symmetric_difference_update(): method is a built-in method in Python for sets. It updates a set by removing
# elements found in it that are also present in another set and adding the elements that are in the other set but
# not in it. In other words, it modifies the original set to be the symmetric difference of the two sets.
set_55 = {1, 2, 3, 'a', 'b', 'c'}
set_66 = {3, 4, 5, 'e', 'f', 'g'}
set_66.symmetric_difference_update(set_55)
print(set_66)

print("_"*70)
# 13. superset and subset method : The issuperset() and issubset() methods are used to check if one set is a superset
# or subset of another set in Python. These methods return True or False based on the relationship between the two sets.

set_55 = {1, 2, 3, 'a', 'b', 'c'}
set_66 = {3, 4, 5, 'b', 'c', 'g'}
set_77 = {'b', 'c', 'g'}
print(set_77.issuperset(set_66))# False
print(set_77.issubset(set_66))# True
print(set_66.issuperset(set_77))# True
print(set_77.issubset(set_55)) #False



print("_"*70)
# 14. isdisjoint method: it checks both sets are different to each other.
set_88 = {3, 4, 5, 'b', 'c', 'g'}
set_99 = {'b', 'c', 'g'}
set_100 = {'f', 'k', 'l'}

print(set_99.isdisjoint(set_88)) # False
print(set_100.isdisjoint(set_99)) # True


print("_"*70)
# 15. copy method: this method is used to copy one set to another set
# Shallow copy
set_111 = {3, 4, 5}
set_222 = set_111
set_111.add(100)
set_222.add(200)
print(set_111)
print(set_222)
#{3, 100, 4, 5, 200}
#{3, 100, 4, 5, 200}

# Deep copy
set_333 = {3, 4, 5}
set_444 = set_333.copy()
set_444.add(500)
print(set_333)# {3, 4, 5}
print(set_444)# {500, 3, 4, 5}









