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
# list_a[0:len(list_a):1]

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

print("_"*50)
############################################
# list concatenation :  we can add two list values and create new list without updating the original list

list_n = [5, 6, 8, 22]
list_m = ['a', 'b', 'c', 'd']
list_v = [4.5, 6.7, 88.9, 22.3]

list_o = list_n + list_m + list_v
print("list output :", list_o)
# [5, 6, 8, 22, 'a', 'b', 'c', 'd', 4.5, 6.7, 88.9, 22.3]



############################  Remove data from list ################
print("_"*50)
# remove method : This method remove any specific value from list
#                 ->  If any value repeated multiple time, then it will remove first occurrence.
#                 -> remove method does not return anything, default return is None
#                 -> In remove method if specified value is not available the it will throw error
#                    ValueError: list.remove(x): x not in list

list_k = [4, 7, 9, 2, 6, 7, 11]
list_k.remove(6)

print("list_k :", list_k)
# list_k : [4, 7, 9, 2, 7, 11]
val = list_k.remove(7)
print(val)
print("list_k :", list_k)


print("_"*50)
#########################
# pop method  : -> pop method remove value from list and return it.
#               -> pop method remove value from specific index position, default index position -1
#               ->  If pop method is specified index is not available then it will given error index out of range
#

list_g = [44, 66, 88, 22, 55, 6]
# remove value from default index -1
val = list_g.pop()
print("removed value :", val) # removed value : 6
print("list_g :", list_g) # [44, 66, 88, 22, 55]

# remove value from specific index

val2 = list_g.pop(2)
print("removed value :", val2) # removed value : 88
print("list_g :", list_g) # [44, 66, 22, 55]


list_h = [44, 66, 88, 22, 88, 55, 6]
list_h.pop(2)
print("list_h :", list_h) # [44, 66, 22, 88, 55, 6]


print("_"*50)
#########################
# remove data with help del keyword: del keyword remove the object from memory
# del can any type of variable from memory. int, float, string, list, tuple, dict, set, bool
list_j = [4, 6, 8, 9, 12]
# remove the list object from memory
del list_j
#print(list_j) # list_j removed from memory


# remove value with slicing using del keyword
list_y = [55, 66, 88, 22, 51]

del list_y[1:3]
print("list_y :", list_y) # [55, 22, 51]

del list_y[-1]
print("list_y :", list_y)   # [55, 22]


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

print("list_aa :", list_aa) # list_aa : []


print("_"*50)
########################## List data manupulation #############
# sort method:  ->  This method sort the list values in ascending and descending order.
#               ->  sort method modify the original list
#               -> sort method does not return anything


list_P = [4, 11, 1, 3, 5, 2, 55]

# sort the list in ascending order
val = list_P.sort()
print("List_P :", list_P, val)
# [1, 2, 3, 4, 5, 11, 55], None

list_Q = [14, 11, 1, 30, 5, 12, 55]

# sort the list in descending order
list_Q.sort(reverse=True)
print("List_Q :", list_Q)
# [55, 30, 14, 12, 11, 5, 1]


#########
# sorted function:  This function accept list as parameter and return the list in ascending and descending order
#                     ->  sorted function does not modify the original list
#                     ->  This function return required result.

list_aa = [4, 1, 6, 11, 77, 10, 12]

result1= sorted(list_aa)
print("ascending order list :", result1)
# ascending order list : [1, 4, 6, 10, 11, 12, 77]

result2= sorted(list_aa, reverse=True)
print("descending order list :", result2)
# descending order list : [77, 12, 11, 10, 6, 4, 1]


# list_bb = [4, 1, 6, 11, 'Hello', 77, 10, 12]
# result3 = sorted(list_bb)
#print(result3)
# TypeError: '<' not supported between instances of 'str' and 'int'

list_cc = ['B', 'a', 'z', 'b', 'd', 'y', 'A', 'hello']
result4 = sorted(list_cc)
print(result4) # ['A', 'B', 'a', 'b', 'd', 'hello', 'y', 'z']


print("_"*50)
#############################
# reverse() method :  This method reverse the list values
#                     -> This method modify the original list and does not return anything

list_xx = [14, 7, 9, 11, 55, 88, 1]
list_xx.reverse()

print("list_xx :", list_xx)
# list_xx : [1, 88, 55, 11, 9, 7, 14]

#########
# reversed function :  This function reverse the list values and return the required result.
#                      -> This function does not modify original list
#                      -> This function return the revers interator object that we can convert into list

list_yy = [1, 7, 2, 40, 22, 34, 25]
result1 = list(reversed(list_yy))
print("result1 :", result1)
# [25, 34, 22, 40, 2, 7, 1]

list_vv = [11, 17, 12, 40, 22, 34, 25]
result2 = reversed(list_vv)
print(result2) # list_reverseiterator object at 0x0000016B6EF70E20>
for val in result2:
    print(val)

"""
25
34
22
40
12
17
11
"""

print("_"*50)
################################
# count method :  This method count the numbers of occurrences of any value in list
list_ee = [4, 6, 8, 4, 7, 22, 33, 7, 6, 4]
print("count of 4 :", list_ee.count(4))
# count of 4 : 3
print("count of 6 :", list_ee.count(6))
# count of 6 : 2

print("count of 11 :", list_ee.count(11))
# count of 11 : 0

print("_"*50)
################################
# index method : This method return index position of any specific value
list_nn = [4, 6, 8, 22, 55, 66]
print("index of 8 :", list_nn.index(8)) # 2
print("index of 55 :", list_nn.index(55)) # 4

# print("index of 100 :", list_nn.index(100))
# ValueError: 100 is not in list


print("_"*50)
####################################
# copy method :

# shallow copy : In shallow copy concept when we assign one list to another list, then it does not copy the content
#                It pass the reference of one list to another, and if we modify anyone of the list, then changes will
#                reflect in both list.

list_mm = [5, 7, 9, 2, 66, 7]
list_pp = list_mm
list_pp.append(100)
list_mm.append(500)

print("list_pp :", list_pp)
print("list_mm :", list_mm)

print("_"*50)
# deep copy : In Deep copy, when we copy data from one list to another list, then it create a new list with all value of
#             first list, If we do change in any of list, then it will reflect in another list.

list_jj = [4, 6, 8, 11, 55, 77]
list_kk = list_jj.copy()

list_kk.append(100)
list_jj.append(200)

print("list_kk :", list_kk)
# list_kk : [4, 6, 8, 11, 55, 77, 100]

print("list_jj :", list_jj)
# list_jj : [4, 6, 8, 11, 55, 77, 200]

print("_"*50)
#############################################
# get sum of list value, max and mini number from list

list_rr = [44, 6, 77, 22, 55, 88, 12]
print("sum of all values :", sum(list_rr))
# sum of all values : 304

print("max value from list :", max(list_rr))
# max value from list : 88

print("Mini value from list :", min(list_rr))
# Mini value from list : 6

print("total number of value :", len(list_rr))
# total number of value : 7

print("_"*50)
############################################################
# write a python program to return the output list this
list1 = [55, 77, 88, 11, 23, 56, 77]
# output = [(55, 'odd'), (77, 'odd'), (88, 'even'), (11, 'odd'), (23, 'odd'), (26, 'even')]
#output2 = [{55: 'odd'}, {77 :'odd'}, {88: 'even'}, {11: 'odd'}, {23:'odd'}, {26: 'even'}]

output = []
for val in list1:
    if val%2 == 0:
        output.append((val, 'even'))
    else:
         output.append((val, 'odd'))


print("output :", output)
# [(55, 'odd'), (77, 'odd'), (88, 'even'), (11, 'odd'), (23, 'odd'), (56, 'even')]


output2 = []
for val in list1:
    temp = {}
    if val%2 == 0:
        output2.append({val: 'even'})
    else:
        temp[val] = 'odd'
        output2.append(temp)

print("output2 :", output2)
# [{55: 'odd'}, {77: 'odd'}, {88: 'even'}, {11: 'odd'}, {23: 'odd'}, {56: 'even'}]
list3 = [5, 7, 2, 8, 11, 44, 77]
for i in range(-1, -len(list3)-1, -1):
    print(i, list3[i])
# List Comprehension
"""
->  List comp return result in list format, no need to use append method to add data.
->  List comp is a compaq way to deal with simple loop and if condition in programs.
->  When we use if condition without else then we have to write if condition right of the loop.
->  When we use if condition with else then we have to write if condition left of the loop.
->  We can defined nested loop condition as well in list compression
"""

list1 = [3, 6, 8, 3, 7, 11, 13]
# get square of the value using list comp.

result = [x**2 for x in list1]
print("square of values :", result)
# square of values : [9, 36, 64, 9, 49, 121, 169]


# get even value from list using list comp.
list2 = [12, 8, 3, 18, 11, 13, 2]

result2 = [x for x in list2 if x%2 == 0]
print("even values :", result2) # [12, 8, 18, 2]


# Write a python program to print below output using list comp.
list3 = [55, 77, 88, 11, 23, 56, 77]
# output = [(55, 'odd'), (77, 'odd'), (88, 'even'), (11, 'odd'), (23, 'odd'), (26, 'even')]

result3 = [(x, 'even') if x%2 == 0 else (x, 'odd') for x in list3]
print("result 3:", result3)
# [(55, 'odd'), (77, 'odd'), (88, 'even'), (11, 'odd'), (23, 'odd'), (56, 'even'), (77, 'odd')]


# Nested for loop with list comp

result4 = [(x, y) for x in range(1, 3) for y in ['a', 'b', 'c']]
print("result4 :", result4)
# [(55, 'odd'), (77, 'odd'), (88, 'even'), (11, 'odd'), (23, 'odd'), (56, 'even'), (77, 'odd')]

for x in range(1, 3):
    for y in ['a', 'b', 'c']:
        print((x, y))



print("_"*50)
###########################################################################
# write a python program to remove duplicate values from list without using method.
list_a = [4, 7, 9, 2, 4, 7, 8]
#output = [4, 7, 9, 2, 8]

output = []
for val in list_a:
    if val not in output:
        output.append(val)
    else:
        continue

print("Output :", output)
# [4, 7, 9, 2, 8]



print("_"*50)
##########
# write a python to move all positive value in left of list and negative values to right side of list
list_b = [4, -6, 8, -22, 77, -99, 22, -13, 56]
# output = [4, 8, 77, 22, 56, -6, -22, -99, -13]

l1 = []
l2 = []
for val in list_b:
    if val > 0 :
        l1.append(val)
    else:
        l2.append(val)

print("output :", l1+l2) # [4, 8, 77, 22, 56, -6, -22, -99, -13]


print("_"*50)
##########
#Q1 write a python program to get average of all list value without using any function or method.
list_c = [55, 66, 33, 22, 12]
# average :


#Q2 . write a python check value can be divide by 3 and 7
list_d = [9, 42, 33, 21, 28, 25]
# output : [42, 21]



in_list_1 = [23, 2, 4, 6, 7]
k = 6
count = 0

for i in range(0, len(in_list_1)):
    if in_list_1[i] < k:
        count += in_list_1[i]
        j = i+1
        while count < k:
            count += in_list_1[j]
            j += 1
            if count == k:
                print("True")
                break
            else:
                count = 0
    else:
        continue

for i in range(0, len(in_list_1)):
    if in_list_1[i] < k:
        count += in_list_1[i]
        j = i+1
        while count < k:
            count += in_list_1[j]
            j += 1
            if count == k:
                print("True")
                break
            else:
                count = 0
    else:
        continue
# This is the question:
#
# Given a list of non-negative numbers and a target integer k,
# ,check if the array has a continuous subarray of size at least 2 that sums up to k
# #Example 1:

# Input: [23, 2,4, 6, 7], k=6
#
# Output: True
#
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.