"""
-> List is mutable data type, we update, add, remove value from list
-> List can contain all the typr of data,int,float,string,list,tuple ,dict,bool etc
-> List follows +ve and -be indexing as like string
-> we defined list with square brackets [].
"""

list1 =[4, 4.5, 'hello', [2, 4, 5],(2, 7, 2), {'a': 123, 'b': 567},
        True, {4, 6, 8, 1}]

print(list1, type(list))
# [4, 4.5, 'hello', [2, 4, 5], (2, 7, 2), {'a': 123, 'b': 567}, True, {8, 1, 4, 6}] <class 'type'>




print("_"*50)
#################### apply loop on the list ######
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
# loop with indexing

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
############### slicing in the list ##################

list_a = [5, 7, 2, 8, 11, 7, 22, 88, 3]
print(list_a[3:7])  # [8, 11, 7, 22]
print(list_a[1:6])  # [7, 2, 8, 11, 7]
print(list_a[-5:-1])  # [11, 7, 22 ,88]
print(list_a[-1:-5])  # []
print(list_a[1:8:2])  # [7, 8 , 7 ,88]
print(list_a[-2:-9:-2])  # [88, 7, 8, 7]
print(list_a[-8:-1:1])  # [7, 2, 8, 11, 7, 22, 88]
print(list_a[::-1]) # [3, 88, 22, 7, 11, 8, 2, 7, 5]
# list_a[]-1:-len(list)-1: -1]


print(list_a[::1])  # [5, 7, 2, 8, 11, 7, 22, 88, 3]

list_b = ['a', 'b', 'c', 'd', 'e']
print(list_b[-5:-1:])  # ['a', 'b', 'c', 'd']
print(list_b[-1:-5])  # []

print("_"*50)
########## list methods ########
print(dir(list))

###### add content to the list ########3
print("_"*50)
#########
# append method() : This method add valur to the list at last index
list_c = [54, 7, 2, 5, 7]
list_c.append(400)
list_c.append('hello')
print("list_c:", list_c)
# list_c: [54, 7, 2, 5, 7, 400, 'hello']
print("_"*50)
#############
# insert method() : This method add value to specified index position
list_d = [6, 8, 22, 55, 99, 9]
list_d.insert(2, 900)
print("list_d:", list_d)
# list_d: [6, 8, 900, 22, 55, 99, 9]

list_d.insert(3, 'python')
print("list_d:", list_d)
# list_d: [6, 8, 900, 'python', 22, 55, 99, 9]

list_d.insert(-1, [4, 6, 8])
print("list_d :", list_d)
# list_d : [6, 8, 900, 'python', 22, 55, 99, [4, 6, 8], 9]

print("_"*50)
############
# extend method() : This method help to add one list data to  another list  at end of another
list_p = ['a', 'b', 'c']
list_q = [3, 6, 8, 2]
list_q.extend(list_p)
print("list_q :", list_q)
# list_q : [3, 6, 8, 2, 'a', 'b', 'c']
list_r = [4, 6, 7]
list_r.append(list_r)
print("list_r :", list_r)
# list_r : [4, 6, 7, ['a', 'b', 'c']

list_t = [4, 6, 7, ['a', 'b', 'c', [17, 18, 19]]]
print(list_t[3][1]) # b
print(list_t[3][3][2]) # 19

print("_"*50)

########### replace data in current ########
# we can replace data in the list with help of index position
list_Y = [5, 7, 9, 22, 55]
list_Y[3] = 100

print("list_y :", list_Y)
# list_y : [5, 7, 9, 100, 55]


# replace with help of slicing

list_z = [4, 6, 7, 8, 1, 5]

list_z[1:4] = [100, 200, 300]
print("list_z:", list_z)
# list_z: [4, 100, 200, 300, 1, 5]

list_z[2:3] = [500, 600]
print("list_z:", list_z)
# list_z: [4, 100, 500, 600, 300, 1, 5]

# replace one value with multiple value
list_w = [4, 6, 7, 8, 1, 5]
list_w[2:3] = [500, 600]
print("list_w :", list_w)
# list_w : [4, 6, 500, 600, 8, 1, 5]

# replace multiple value with one value
list_q = [4, 6, 7, 8, 1, 5]
list_q[1:4] =[500]
print("list_q :", list_q)
# list_q : [4, 500, 1, 5]


##########################################
# list concatenation : we can add two list values and create new list without updating original list

list_n = [5, 6, 8, 22]
list_m = ['a', 'b', 'c', 'd']
list_v = [4.5, 6.7, 88.7, 22.3]
list_o = list_n + list_m + list_v
print("list output :", list_o)
# [5, 6, 8, 22, 'a', 'b', 'c', 'd', 4.5, 6.7, 88.7, 22.3]


##################### Remove data from list########################
print("_"*50)
# remove method : this method remove any specific value from list
#                 -> if the same value repeated multiple times, them it will first occurence
#                 -> remove method does not return anything, default return none
#                 -> in remove method if specified value is not
list_k = [4, 7, 9, 2, 6, 7, 11]
list_k.remove(6)

print("list_k:", list_k)
# [4, 7, 9, 2, 7, 11]
val = list_k.remove(7)
print(val)
print("list_k :", list_k)

print("_"*50)
##########################
# pop method : ->pop method remove value from list and return it
#              -> pop method remove value from specific index position, default index position is -1
#              -> if pop method is specified index is not available then it will  given
list_g = [44, 66, 88, 22, 55, 6]
# remove value from default index -1
val = list_g.pop()
print("remove value :", val)  # remove value : 6
print("list_g :", list_g)  # [44, 66, 88, 22, 55]


# remove value from specific index
val2 = list_g.pop(2)
print("removed value :", val2)  # removed value : 88
print("list_g :", list_g)  # [44, 66, 22, 55]

list_h = [44, 66, 88, 88, 22, 55, 6]
list_h.pop(2)
print("list_h :", list_h) # [44, 66, 88, 22, 55, 6]

print("_"*50)
####################
# remove daata with help del keyword : del keyword remove the object from memory
# del can any type of variable from memory. int, float, string, list,tuple
list_j = [4, 6, 8, 9, 12]
# remove the list object from memory
del list_j
# print(list_j) # list_j removed from memory

# remove value with slicing using del keyword
list_y = [55, 66, 88, 22, 51]

del list_y[1:3]
print("list_y :", list_y) # [55, 22, 51]

del list_y[-1]
print("list_y :", list_y)  # [55,22]

list_Q= [5, 7, 8, 2, 6, 3, 6, 9, 22]
del list_Q[1::2]
print("list_Q :", list_Q)  # [5, 8, 6, 6, 22]


list_z = [5, 7, 99]
# list_z.remove(100)
# valueError : list.remove(x) : x not in list

# list_z.pop(5)
# IndexError: pop index out of range

print("_"*50)
##########################
# clear method : this method clear all the data from list and remain only blank list

list_aa =[5, 7, 22, 55, 88]
list_aa.clear()

print("list_aa :", list_aa)  # list_aa : []
print("_"*50)
###############List data manuplation ##############
# sort method : -> This method sort the list values in ascending and descending order
#               -> sort method modify the original list
#               -> sort method does not return anything
list_P = [4, 11, 1, 3, 5, 2, 55]

# sort the list in ascending order
list_P.sort()
print("list_P:", list_P)
#  [1, 2, 3, 4, 5, 11, 55]

list_Q = [4, 11, 1, 3, 5, 2, 55]
# sort the list in descending order
list_Q.sort(reverse=True)
print("list_Q:", list_Q)
#  [55, 11, 5, 4, 3, 2, 1]


##########################
# sorted function : This function accept list as parameter and return the list in ascending and descending
#                   -> Sorted function does not modify the original list
#                   -> this function return required result

list_aa = [4, 1, 6, 11, 77, 10, 22]

result2 = sorted(list_aa, reverse=True)
print("descending order list :", result2)
# descending order list : [77, 22, 11, 10, 6, 4, 1]

#list_bb = [4, 1, 6, 11, 'hello', 77, 10, 12]
#result3 = sorted(list_bb)
#print(result3)
# TypeError: '<' not supported between instances of 'str' and 'int'

list_cc = ['a', 'z', 'b','d', 'hello']
result4 = sorted(list_cc)
print(result4)
# ['a', 'b', 'd', 'hello', 'z']

print("_"*50)
##################################
# reverse () method : This method reverse the list values
#                    -> this method modify the original list and does not return anything

list_XX = [4, 7, 8, 11, 55, 22]
list_XX.reverse()

print("list_xx:", list_XX)
#  [22, 55, 11, 8, 7, 4]

############################
# reversed function : This function reverse the list values and return the required start
#                     -> This function does not modify original list
#                     -> this function return the reverse interator object that we can convert into list
list_yy =[1, 7, 2, 40, 32, 34]
result1 = list(reversed(list_yy))
print("result :", result1)
# [34, 32, 40, 2, 7, 1]

list_vv = [11, 17, 12, 40, 22, 34, 25]
result2 = reversed(list_vv)
print(result2) # <list_reverseiterator object at 0x000001AC09C046A0>
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
#################################
# count method : This method count the numbers of occureneces of any variable
list_ee = [4, 6, 8, 4, 7, 22, 33, 7, 6, 4]
print("count of 4 :", list_ee.count(4))
# count of 4 : 3
print("count of 7 :", list_ee.count(7))
# count of 7 : 2
print("_"*50)
#################################
# index method
list_nn = [4, 6, 8, 22, 55, 66]
print("index of 8 :", list_nn.index(8))  # 2
print("index of 55 :", list_nn.index(55))  # 4

print("_"*50)
#############################################
# copy method :


# shallow copy : In shallow copy concept when we assign one list to another list ,then it does not copy the content
#                It pass the reference of one list to another, and if we modify anyone of the list,then changes will
#                 reflect in both list.

list_mm = [5, 7, 9, 2, 66, 7]
list_pp = list_mm
list_pp.append(100)

print("list_pp :", list_pp)  # [5, 7, 9, 2, 66, 7, 100]
print("list_mm :", list_mm)  # [5, 7, 9, 2, 66, 7, 100]

# deep copy : in deep copy, when we copy data from one list to another list then it create the new list with all value
#             of first list, If we do change in any of list, then it will reflect in another list

list_jj = [4, 6, 8, 11,55, 77]
list_kk = list_jj.copy()

list_kk.append(100)
list_jj.append(200)
print("list_kk :", list_kk)
# list_kk : [4, 6, 8, 11, 55, 77, 100]

print("list_jj :", list_jj)
# list_jj : [4, 6, 8, 11, 55, 77, 200]

#########################################
# get sum of list value, max and min number from list

list_rr = [44, 6, 77, 22, 55, 88, 12]
print("sum od all values :", sum(list_rr)) # 304

print("max value from list :", max(list_rr)) # 88

print("min value from list :", min(list_rr)) # 6

print("total number of value :", len(list_rr)) # 7

##########################################

# write a python program to return the output list this
list1 = [55, 77, 88, 11, 23, 56]
# output = [(55, 'odd'),(77, 'odd'), (88, 'even') (11, 'odd)

output = []
for val in list1:
    if val%2 == 0:
        output.append((val,'even'))
    else:
        output.append((val, 'odd'))
print("output :", output)
# [(55, 'odd'), (77, 'odd'), (88, 'even'), (11, 'odd'), (23, 'odd'), (56, 'even')]
