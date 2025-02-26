""""#*** program to calculate square of the values in list**
list1 = [3, 5, 7, 1, 8]

for val in list1:
    print(val, ":", val**2)
print("-"*50)

#**program to slice the values from the list**
list2=[2,4,6,7,8,46,67,84,85]
print(list2[3:7])
print(list2[-5:-1])
print(list2[1:8:2])
print(list2[-2:-10:-2])
print(list2[-8:-1:2])
print("_"*50)

#**program to add 2 lists**
list1=[1,2,3,4,5,6,7,8]
list2=[9,10,11,12,13,14]
#output=list1+list2
output=list1.extend(list2)
#print(output)
print(list1)
print("_"*50)\

#program to reverse a list**
list_a=[2,9,75,65]
print(list_a[-1:-5:-1])
print("_"*50)

#**print the sum of all elements in a list****
list1 = [2,5,8,0,1]
var = 0
for value in list1:
    var += value
print(var)
print("_"*50)

#****list Methods Append,insert, extend***********
#print(dir(list))
list_c=[45,86,96,70,97,65,76]
list_c.append(400)
list_c.append("hello")
list_c.insert(2,[4,6,8]) #shifts to right
list_c.insert(3,"pyt") #to insert value at a specific position(3)
print(list_c)
print("_"*50)

#extend adds the data to end of the another list
lst1 = [a,g,f,d,t,u]
lst2 = [1,5,8]
lst2.extend(lst1)
print(lst2)
print("_"*50)

#replace a data in the list** we can replace data with the help of index pos
lst1 =[5,6,7,9,33,56]
lst1[3]= 100 #replace data at 3 index
print(lst1)
print("_"*50)

#** program to find the smallest and biggest number from list**

list1 = [9,7,6,4,32,41,22,12,65]
list1.sort()

print("Smallest number: ", list1[0])
print("Largest number: ", list1[-1])
print("_"*50)"""

#** program to sort and mearge 2 list**
list1=[45,76,84,384,756,846,378,345]
list2=[578,456,234,890,34,3,76,33,63]
list3= list1.extend(list2)
print(list1)
list1.sort()
print(list1[0::])
print("_"*50)

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

#Q1 write a python program to get average of all list value without using any function or method.
list_c = [55, 66, 33, 22, 12]
total=0
length = len(list_c)
for num in list_c:
    total=total+num
avg= total/length
print(avg)
print("_"*50)

#Q2 . write a python check value can be divide by 3 and 7
list_d = [9, 42, 33, 21, 28, 25]
# output : [42, 21]
# check if list values are divisible by 3and 7
for val in list_d:
    if val % 3==0 and val%7==0:
        print(val)
print("_"*50)