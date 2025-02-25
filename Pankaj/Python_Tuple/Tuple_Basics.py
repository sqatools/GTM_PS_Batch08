"""
Tuple Properties:
1. tuple is immutable data type, and we can not modify it.
2. tuple can contain all data types. int, float, bool, string, set, list, dict, tuple.
3. tuple follows +ve and -ve indexing, like list and string.
4. tuple defined with round brackets().
5. Generally we use tuple when data is going to be fixed in size.
    --> eg. days, year, month etc.
"""
print("_"*70)
tup = (2, 2.2, True, [2, 3, 4], (2, 3, 4, 5, 6), """Pankaj""", "Prasad", 'Neha', {'a': 'video', 'b': 'game'}, {2, 3, 4})
print(tup, type(tup))

print("_"*70)
# Get value from tuple via indexing
print(tup[-1]) # {2, 3, 4}
print(tup[1]) # 2
print(tup[5]) # pankaj
print(tup[3][1]) # 2 Note--> second index means inside of list

print("_"*70)
# without indexing
tup1 = (2, 3, 4, 5, 6, 7, 8)
for val in tup1:
    print(val)

# With indexing
for i in range(len(tup1)):
    print(i, tup1[i])
"""
0 2
1 3
2 4
3 5
4 6
5 7
6 8
"""

############################ Slicing in tuple ########################

