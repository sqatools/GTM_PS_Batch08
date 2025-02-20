"""
--> List is mutable data type, so we can update its value
--> List can contain all data types, eg: int, float,bool,set, tuple,string, list,dict
--> List follows positive and negative indexing
--> we can define list under square bracket
"""
# list1 = [1, 2.2, "Pankaj", 'P', True, (2, 3.3, "Prasad"[1, 2, 3]), (1, 2, 3, 4), {'a':'Darshika', 'b':"Neha"}]

list1 = [1, 2.2, 3.5, "Pankaj", 'p', True, (2, 4, 'Prasad'), [2, 4, 7], {'a': 'Darshika', 'b': 'Pankaj'}]
print(list1, type(list1))

#        0  1  2  3   4
list2 = [5, 7, 9, 2, 10]
#       -5 -4 -3 -2  -1
print(list2[2])
print(list2[-3])

print("_" * 50)
################ apply loop on the list ########

list3 = [1, 4, 6, 7, 88, 99, 5]
for value in list3:
    print(value)

# Important ***************************
print("_" * 50)
# Loop with indexing
for i in range(len(list3)):
    print(i, list3[i])

#         0  1  2  3  4   5   6  7   8
list_a = [5, 7, 2, 8, 11, 7, 22, 88, 3]
#        -9 -8 -7 -6  -5 -4 -3  -2  -1
print(list_a[0:8])
print(list_a[3:7])
print(list_a[-7:-3])
print(list_a[-3:-7]) # No output
print(list_a[1:8:2])
print(list_a[-2:-9:-2])
print(list_a[-9:-2:2])

list_1 = [0, 1, 2, 3, 4]
print(list_1[-4:-1:2])
# print list in reverse order
print(list_1[::-1])
print(list_1[::1])

############## Add content to the list ############
print("_"*50)
###############
print(dir(list))
"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""
###############
# append method() : This method add value to the list at last index.
list_d = [1, 2, 3, 4, 5, 6]
list_d.append(100)
print(list_d)
list_d.append("Pankaj")
print(list_d)

print("_"*50)
###############
# insert method() :  This method add value to specified index position
list_d = [1, 2, 3, 4, 5, 6]
list_d.insert(2, 700)
print(list_d)
list_d.insert(1, "Pankaj")
list_d.insert(-1, [5, 6, 7])
print(list_d)

print("_"*50)
###############
# extend method()  :  Thin method help to add one list data to another list at end of another.
list_e = ['a', 'b', 'c', 'd']
list_f = [3, 4, 5, 6]
list_e.extend(list_f)
print(list_e)

list_g = ["Pankaj", "Darshika", "Neha"]
list_g.append(list_e)
print(list_g)

print(list_g[3])

list_h = [4, 6, 7, ['a', 'b', 'c', [17, 18, 19]]]
print(list_h[3][1])
print(list_h[3][3][2])


print("_"*50)
################### Replace data in current #################
# we can replace data in the list with help of index position and
# slicing, no need to use any method
"""
->  Using slicing replacement we can replace one index value to multiple value
->  Using slicing replacement we can replace multiple index value with one single value
"""

list_i = [5, 7, 9, 22, 55, 77, 99]
list_i[3] = "Pankaj"
print(list_i)

# replace with help of slicing
list_z = [4, 6, 7, 8, 1, 5]
list_z[0:3] = [100, 200, 300]
print(list_z)

# replace one value with multiple value
list_w = [4, 6, 7, 8, 1, 5]
list_w[2:3] = [500, 600]
print(list_w)


print("_"*50)
############################################
# list concatenation :  we can add two list values and create new list without updating the original list

list_n = [5, 6, 8, 22]
list_m = ['a', 'b', 'c', 'd']
list_v = [4.5, 6.7, 88.9, 22.3]

list_o = list_n + list_m + list_v
print(list_o)


############################  Remove data from list ################
print("_"*50)
# remove method : This method remove any specific value from list
#  -> If any value repeated multiple time, then it will remove first occurrence.
#  -> remove method does not return anything, default return is None
#  -> In remove method if specified value is not available it will throw error
#     ValueError: list.remove(x): x not in list

list_k = [4, 7, 9, 2, 6, 7, 11]
list_k.remove(6)
print(list_k)

print("_"*50)
#########################
# pop method  : -> pop method remove value from list and return it.
#               -> pop method remove value from specific index position, default index position -1
#               ->  If pop method is specified index is not available then it will given error index out of range
#

list_j = [44, 66, 88, 22, 55, 6]
# remove value from default index -1
list_l = list_j.pop()
print(list_l)

# remove value from specific index
val2 = list_j.pop(2)
print("removed value :", val2) # removed value : 88
print("list_g :", list_j) # [44, 66, 22, 55]

print("_"*50)
#########################
# remove data with help del keyword: del keyword remove the object from memory
# del can any type of variable from memory. int, float, string, list, tuple, dict, set, bool
list_a1 = [4, 6, 8, 9, 12]
# remove the list object from memory
del list_a1
# print(list_a1)

# remove value with slicing using del keyword
list_b1 = [55, 66, 88, 22, 51]

del list_b1[1:3]
print(list_b1)

del list_b1[-1]
print("list_y :", list_b1)   # [55, 22]

list_Q = [5, 7, 8, 2, 6, 3, 6, 9, 22]
del list_Q[1::2]
print("list_Q :", list_Q)  # [5, 8, 6, 6, 22]

list_z = [5, 7, 99]
# list_z.remove(100)
# ValueError: list.remove(x): x not in list

# list_z.pop(5)
# IndexError: pop index out of range

print("_"*50)
################################
# clear method : this method clear all the data from list and remain only blank list

list_aa = [5, 7, 22, 55, 88]
list_aa.clear()
print(list_aa)


print("_"*50)
########################## List data manupulation #############
# sort method:  ->  This method sort the list values in ascending and descending order.
#               ->  sort method modify the original list
#               -> sort method does not return anything


list_P = [4, 11, 1, 3, 5, 2, 55]
list_P.sort()
print(list_P)
# [1, 2, 3, 4, 5, 11, 55]

# sort the list in descending order
list_Q.sort(reverse=True)
print("List_Q :", list_Q)
# [55, 30, 14, 12, 11, 5, 1]


##################################### Sorted Function #####################
# 1. This function accept list as parameter and return the list in ascending and descending order
# 2. Sorted function does not modify the original list
# 3. This function return required result

list_aa = [3, 6, 99, 101, 2, 0]
result_1 = sorted(list_aa)
print("Ascending Order list: ", result_1)
# Ascending Order list:  [0, 2, 3, 6, 99, 101]

result_2 = sorted(list_aa, reverse=True)
print("Descending order list: ", result_2)
# Descending order list:  [101, 99, 6, 3, 2, 0]

list_abc = ['a', 'z', 'love', 'e', 'd']
result_abc = sorted(list_abc)
print("Ascending Order Alphabets: ", result_abc)
# Ascending Order abc:  ['a', 'd', 'e', 'l', 'z']

# list_3 = ['a', 2, 3, "D"]
# sorted_list_3 = list_3.sort()
# print(sorted_list_3)
# TypeError: '<' not supported between instances of 'int' and 'str'

print("_"*50)
############################## reverse() method : ####################
# -> This method reverse the list values
# -> This method modify the original list and does not return anything
list_4 = [12, 4, 5, 6, 7, 10]
rev_list_4 = list_4.reverse()
print(list_4)
# [10, 7, 6, 5, 4, 12]

print("_"*50)
###################### Reversed Function ######################
# -> This function reverse the list values and return the required result.
# -> This function does not modify original list
# -> This function return the revers interator object that we can convert into list

list_5 = [10, 20, 30, 40, 50]
reverse_list_5 = reversed(list_5)
print(reverse_list_5)
# <list_reverseiterator object at 0x000001176CF93370>
for val in reverse_list_5:
    print(val, end=" ")
    # 50 40 30 20 10
print()

print("_"*50)
################################
# count method :  This method count the numbers of occurrences of any value in list
list_6 = [0, 4, 7, 1, 2, 9, 10, 9, 0, 9]
print(list_6.count(9)) # put the number for which you want count not indexing
print(list_6.count(0))
print(list_6.count(7))

print("_"*50)
################################
# index method : This method return index position of any specific value
list_7 = [0, 1, 22, 34, 4, 5, 6, 7]
print(list_7.index(22)) # enter value to check indexing of value in list
print(list_7.index(34))
# print(list_7.index(100)) # ValueError: 100 is not in list


print("_"*50)
####################################
# copy method :

# shallow copy : In shallow copy concept when we assign one list to another list, then it does not copy the content
#                It pass the reference of one list to another, and if we modify anyone of the list, then changes will
#                reflect in both list.
list_8 = [33, 77, 11, 99, 48, 92]
list_empty = list_8
list_empty.append(200)
list_8.append(300)
print(list_8)
print(list_empty)

print("_"*50)
# deep copy : In Deep copy, when we copy data from one list to another list, then it create a new list with all value of
#             first list, If we do change in any of list, then it will reflect in another list.

list_9 = [2, 9, 4, 7, 8, 1, 0]
list9_1 = list_9.copy()

list_9.append(100)
list9_1.append(200)

print(list_9)
print(list9_1)

print("_"*70)
#############################################
# get sum of list value, max and mini number from list

list_10 = [1, 2, 3, 4, 5, 6, 7]
print(sum(list_10))
print(max(list_10))
print(min(list_10))
print(len(list_10))

print("_"*50)
############################################################
# write a python program to return the output list this
list11 = [55, 77, 88, 11, 23, 56, 77]
# output = [(55, 'odd'), (77, 'odd'), (88, 'even'), (11, 'odd'), (23, 'odd'), (26, 'even')]
#output2 = [{55: 'odd'}, {77 :'odd'}, {88: 'even'}, {11: 'odd'}, {23:'odd'}, {26: 'even'}]

output = []
for val1 in list11:
    if val % 2 == 0:
        output.append((val1, 'Even'))
    else:
        output.append((val1, 'Odd'))
print(output)
# [(55, 'Even'), (77, 'Even'), (88, 'Even'), (11, 'Even'), (23, 'Even'), (56, 'Even'), (77, 'Even')]

print("_"*50)
list12 = [55, 77, 88, 11, 23, 56, 77]
output12 = []
for val in list12:
    temp = {}
    if val % 2 == 0:
        output12.append({val: 'even'})
    else:
        temp[val] = 'odd'
        output12.append(temp)

# Print value with negative indexing 
list_13 = [3, 2, 5, 7, 9, 10, 0, 10, 22, 88, 87]
for i in range(-1, -len(list_13)-1, -1):
    print(i, list_13[i])


