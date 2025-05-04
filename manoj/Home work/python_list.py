
# 1) write a python program Problem to get the square of all numbers In the python list
list2 = [2,4,6,9]
count = 0
while count < len(list2):
  print(list2[count],":",list2[count]**2)
  count += 1
# 2 : 4
# 4 : 16
# 6 : 36
# 9 : 81


# 2) write a program Problem to add elements from list1 to list2.
list1 = [1,2,3,4,5]
list3 = [4,5,6,7,8]
output = list1 + list3
print(output)
# [1, 2, 3, 4, 5, 4, 5, 6, 7, 8]

# 3) write a program Problem to find minimum and maximum elements from a list
list12 = [11, 45, 88, 23]
list12.sort()
print("smallest number:", list12[0]) # 11
print("largest number:", list12[-1]) # 88

#4) write a program Problem to remove all the duplicate elements from a list
listA = [1,2,5,2,6,5,7,9,6]
listB = []
for value in listA:
  if value not in listB:
    listB.append(value)
print(listB)
# [1, 2, 5, 6, 7, 9]

# 5) write a program Problem to print list in reverse order using index slicing
list_a = [1, 2, 3, 4]
list_b = list_a[::-1]
print(list_b)
# [4, 3, 2, 1]

#6) write a program Problem to print true if common elements between lists.
list11 = [2, 4, 6, 8]
list22 = [4, 6, 9]
for value in list11:
  if value in list22:
    print("True") #True

# 7) write a program Problem to print false if common elements between lists.
list11 = [2, 4, 6, 8]
list22 = [4, 6, 9]
for value in list11:
  if value in list22:
    print("False") # false

# 8) Problem to remove negative elements from the list
list3 = [-2, 4, -6, 99, 20]
for value in list3:
  if value>= 0:
    print(value, end=" ") # 4, 99, 20
print("_"*50)

# 9) Problem to remove positive elements from the list
list32 = [-2, 4, -6, 99, 20]
for value in list32:
  if value <= 0:
    print(value, end=" ") # 4 99 20 -2 -6
print("_"*50)

# 10) write a program Problem to add two lists using extend method

list23 = [2, 4, 3, 5, 7, 88]
list32 = [ 1, 4, 5, 7]
list23.extend(list32)
print(list23) # [2, 4, 3, 5, 7, 88, 1, 4, 5, 7]

print("_"*50)
# 11) write a program Problem to sort a list using the sort and sorted method.
list44 = [44, 66, 23, 55]
list44.sort()
print("sort:", list44) # sort: [23, 44, 55, 66]

# 12) write a python program to find the largest number from the list
list55 = [11, 22, 56, 88, 90]
list55.sort()
print("largest number:", list55[-1])
# 90

# 13) write a python program to find the smallest number from the list
list56 = [11, 22, 56, 88, 90]
list56.sort()
print("smallest number:", list56[0])
# 11



# 14) write a python program to find the 2nd largest number from the list
list57 = [12, 34, 77, 999, 123]
list57.sort()
print("2nd largest:", list57[-2])
# 123

#15) write a python program to find the 2nd smallest number from the list
list58 = [1, 2, 4, 56, 77]
list58.sort()
print("2nd smallest:", list58[0])
# 1

#16) write a python Problem to get the difference between two lists.

list13 = [44, 36, 71, 87]
for value in list12:
  if value not in list13:
    print(value, end=" ")
# 1, 32, 35, 85



# 17) write a python problem to get all the unique numbers in the list.
list14 = [33, 77, 98, 45, 78, 188]
print(list(set(list14)))
# [33, 98, 45, 77, 78, 188]

#18) write a python program to Convert a string into a list

string = "i am manoj kumar"
list2 = string.split(" ")
print(list2)
# ['i', 'am', 'manoj', 'kumar']



#19) write a python program Problem to convert multiple numbers into a single number.

list13 = [12, 45, 78]
for value in list13:
  print(value, end="")
# 124578



#20) write a python program Problem to add two lists using extend method

list15 = [9, 8, 0, 7, 5]
list16 = [7, 5, 3, 5, 3]
list15.extend(list16)
print(list15)
# [9, 8, 0, 7, 5, 7, 5, 3, 5, 3]





































































