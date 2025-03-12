"""
frozen set is immutable
"""

list1 = [4, 6, 8, 9, 10, 22, 5, 7]

fr_set = frozenset(list1)
print(fr_set)

# fr_set.add(40)
# attributeError: 'frozenset' object has no attribute 'add'

tup1 =(4, 'q', 'a', 'b')
var2 = frozenset(tup1)
print(var2)  # frozenset({'b', 4, 'q', 'a'})

dict1 = {'a' : 123, 'b':456, 'c':543, 't': 567}
var3 = frozenset(dict1)
print(var3) # frozenset({'t', 'c', 'b', 'a'})
