"""
Tuple Properties:
1. tuple is immutable data type, and we can not modify it.
2. tuple can contain all data types. int, float, bool, string, set, list, dict, tuple.
3. tuple follows +ve and -ve indexing, like list and string.
4. tuple defined with round brackets().
5. Generally we use tuple when data is going to be fixed in size.
    --> eg. days, year, month etc.
"""
print("_" * 70)
tup = (2, 2.2, True, [2, 3, 4], (2, 3, 4, 5, 6), """Pankaj""", "Prasad", 'Neha', {'a': 'video', 'b': 'game'}, {2, 3, 4})
print(tup, type(tup))

print("_" * 70)
# Get value from tuple via indexing
print(tup[-1])  # {2, 3, 4}
print(tup[1])  # 2
print(tup[5])  # pankaj
print(tup[3][1])  # 2 Note--> second index means inside of list

print("_" * 70)
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
tup1 = (4, 5, 2, 9, 10, 22, 3, 0, 11)
print(tup1[1:-3:1])  # (5, 2, 9, 10, 22)
print(tup1[1:8])  # (5, 2, 9, 10, 22, 3, 0)
print(tup1[-3:2:-1])   # (3, 22, 10, 9)
print(tup1[-3:-7:-1])  # (3, 22, 10, 9)
print(tup1[1:len(tup1):1])  # (5, 2, 9, 10, 22, 3, 0, 11)
print(tup1[1:len(tup1):2])  # (5, 9, 22, 0)
print(tup1[0:-1])  # (4, 5, 2, 9, 10, 22, 3, 0)

print("_"*70)
####################### print all tuple methods##############
print(dir(tuple))
# 'count', 'index'

#1. count method: This will give number of occurrence of value in tuple
tup2 = (2, 3, 7, 6, 4, 1, 4, 9, 4)
print(tup2.count(4))

#2. index method: index of value
tup3 = (2, 3, 7, 6, 4, 1, 4, 9, 4)
print(tup3.index(7))

####################### max and min value from tuple #########################
tup4 = (2, 3, 77, 6, 44, 1, 4, 90, 4)
print("Maximum Value: ", max(tup4))  # Maximum Value:  90
print("Minimum Value: ", min(tup4))  # Minimum Value:  1

#############################################################################
# get index position of any specific repeated value from given tuple.
tup8 = (5, 7, 8, 7, 2, 7, 8,  3, 7, 8)
#second_7_index
num = 8
count_of_num = 2
count = 0
for i in range(len(tup8)):
    if tup8[i] == num:
        count += 1
        if count_of_num == count:
            print(i)
            break
    else:
        continue


print("_"*50)
####################################
tup_a = (4, 7, 1, 8, 22, 6, 17)
# get sorted value from tuple

