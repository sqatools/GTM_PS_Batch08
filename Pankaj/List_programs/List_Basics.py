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

# sort the list in descending order
list_Q.sort(reverse=True)
print("List_Q :", list_Q)
# [55, 30, 14, 12, 11, 5, 1]


