"""
frozenset is immutable version of the set.
"""
list1 = [4, 6, 8, 22, 6, 7, 4]

fr_set = frozenset(list1)
print(fr_set) # frozenset({4, 6, 7, 8, 22})

# fr_set.add(40)
# AttributeError: 'frozenset' object has no attribute 'add'

tup1 = (4, 'q', 'a', 'b', 'c', 'a')
var2 = frozenset(tup1)
print(var2)  # frozenset({'a', 4, 'q', 'c', 'b'})

dict1 = {'a' : 123, 'b': 456, 'p': 666, 'q': 999}
var3 = frozenset(dict1)
print(var3) # frozenset({'b', 'a', 'p', 'q'})
