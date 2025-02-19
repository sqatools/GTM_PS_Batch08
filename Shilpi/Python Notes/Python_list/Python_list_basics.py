"""
->  List is mutable data type, we update, add, remove value from list
->  List can contain all the types of data, int, float, string, list, tuple, dict, bool, set.
->  List Follows +ve and -Ve indexing as like string
->  We defined list with square brackets [].
"""

list1 = [4, 4.5, 'Hello', [2, 4, 5],(2, 7, 1), {'a' : 123, 'b': 567},
         True, {4, 6, 8, 1}]

print(list1, type(list1))
# [4, 4.5, 'Hello', [2, 4, 5], (2, 7, 1), {'a': 123, 'b': 567}, True, {8, 1, 4, 6}] <class 'list'>

#        0  1  2  3  4
list2 = [5, 7, 9, 2, 10]
#        -5-4 -3 -2  -1
print(list2[1])  # 7

print(list2[-1]) # 10

print("_"*50)
################ apply loop on the list ########

list3 = [5, 7, 2, 8, 11, 44, 77]

for val in list3:
    print(val)

"""
5
7
2
8
11
44
77
"""
print("_"*50)
# Loop with indexing

for i in range(len(list3)):
    print(i, list3[i])

"""
0 5
1 7
2 2
3 8
4 11
5 44
6 77
"""

print("_"*50)
##################### Slicing in the list ###############

list_a = [5, 7, 2, 8, 11, 7, 22, 88, 3]
print(list_a[3:7])  # [8, 11, 7, 22]
print(list_a[1:6])  # [7, 2, 8, 11, 7]
print(list_a[-5:-1]) # [11, 7, 22, 88]
print(list_a[-1:-5]) # []
print(list_a[1:8:2]) # [7, 8, 7, 88]
print(list_a[-2:-9:-2])  # [88, 7, 8, 7]
print(list_a[-8:-1:1])  # [7, 2, 8, 11, 7, 22, 88]
print(list_a[-8:-1:2])  # [7, 8, 7, 88]

print(list_a[::-1])  # [3, 88, 22, 7, 11, 8, 2, 7, 5]
# list_a[-1:-len(list)-1:-1]

print(list_a[::1]) # [5, 7, 2, 8, 11, 7, 22, 88, 3]

list_b = ['a', 'b', 'c', 'd', 'e']
print(list_b[-5:-1:])  # ['a', 'b', 'c', 'd']
print(list_b[-1:-5:]) # []

print("_"*50)
##################### List Methods ##################
print(dir(list))
"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

############## Add content to the list ############
print("_"*50)
###############
# append method() : This method add value to the list at last index.
list_c = [54, 7, 2, 5, 7]
list_c.append(400)
list_c.append('Hello')
print("list_c :", list_c)
# list_c : [54, 7, 2, 5, 7, 400, 'Hello']


print("_"*50)
###############
# insert method() :  This method add value to specified index position
list_d = [6, 8, 22, 55, 88, 9]
list_d.insert(2, 700)
print("list_d :", list_d)
# list_d : [6, 8, 700, 22, 55, 88, 9]

list_d.insert(3, 'Python')
print("list_d :", list_d)
# list_d : [6, 8, 700, 'Python', 22, 55, 88, 9]

list_d.insert(-1, [4, 6, 8])
print("list_d :", list_d)
# list_d : [6, 8, 700, 'Python', 22, 55, 88, [4, 6, 8], 9]

print("_"*50)
###############
# extend method()  :  Thin method help to add one list data to another list at end of another.
list_p = ['a', 'b', 'c']
list_q = [3, 6, 8, 2]
list_q.extend(list_p)
print("list_q :", list_q)
# [3, 6, 8, 2, 'a', 'b', 'c']

list_r = [4, 6, 7]
list_r.append(list_p)
print("list_r :", list_r)
#list_r : [4, 6, 7, ['a', 'b', 'c']]

list_t = [4, 6, 7, ['a', 'b', 'c', [17, 18, 19]]]
print(list_t[3][1]) # b
print(list_t[3][3][2]) # 19


print("_"*50)
################### Replace data in current #################
# we can replace data in the list with help of index position and
# slicing, no need to use any method
"""
->  Using slicing replacement we can replace one index value to multiple value
->  Using slicing replacement we can replace multiple index value with one single value
"""
list_y = [5, 7, 9, 22, 55]
# replace with index
list_y[3] = 100

print("list_y :", list_y)
# [5, 7, 9, 100, 55]


# replace with help of slicing
list_z = [4, 6, 7, 8, 1, 5]

list_z[1:4] = [100, 200, 300]
print("list_z:", list_z)
# list_z: [4, 100, 200, 300, 1, 5]

# replace one value with multiple value
list_w = [4, 6, 7, 8, 1, 5]
list_w[2:3] = [500, 600]
print("list_w:", list_w)
list_w: [4, 6, 500, 600, 8, 1, 5]


# replace multiple value with one value
list_q = [4, 6, 7, 8, 1, 5]
list_q[1:4] = [500]
print("list_q : ", list_q)
# list_q :  [4, 500, 1, 5]
