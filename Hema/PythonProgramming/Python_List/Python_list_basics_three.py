#12th Feb 2025


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
