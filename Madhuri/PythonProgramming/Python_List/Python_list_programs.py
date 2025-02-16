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
