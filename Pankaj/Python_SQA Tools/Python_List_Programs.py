# 1. Problem to get the square of all numbers In the python list
list1 = [1, 2, 3, 4, 5]
for value in list1:
    print(f"Square of {value} is: ", value ** 2)

# 2. Problem to add elements from list1 to list2.
list2 = [3, 4, 5, 6, 7]
list3 = [7, 8, 8, 9, 6]
print(list2 + list3)

# 3). Python program to calculate the sum of all elements from a list.
list4 = [2, 3, 4, 5]
summ = 0
for val in list4:
    summ += val
print(summ)

# 4). Python program to find a product of all elements from a given list.
list5 = [4, 4, 4, 4]
product = 1
for val in list5:
    product *= val
print(product)

# 5). Python program to find the minimum and maximum elements from the list.
list6 = [2, 33, 77, 99, 1, 100, 300]
sorted(list6)
print(list6)
print("Minimum Number : ", list6[0])
print("Maximum Number : ", list6[-1])

# 6). Python program to differentiate even and odd elements from the given list.
list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for value in list7:
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)
print("Even Num: ", even)
print("Odd Num: ", odd)

print("_"*50)
# 7). Python program to remove all duplicate elements from the list.
list8 = [2, 3, 4, 4, 3, 1]
list8_1 = []
for value in list8:
    if value not in list8_1:
        list8_1.append(value)
print(list8_1)

# 8). Python program to print squares of all even numbers in a list.
list9 = [1, 2, 3, 4, 5, 6]
for value in list9:
    if value % 2 == 0:
        print(value, "-->", value**2)

# 9. Python program to split the list into two-part, the left side all odd values and the right side all even values.
list10 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
even_no = []
odd_no = []
for value in list10:
    if value %2 == 0:
        even_no.append(value)
    else:
        odd_no.append(value)

odd_no.extend(even_no)
print(odd_no)

# 10).  Python program to get common elements from two lists.

list11 = [4, 5, 7, 9, 2, 1]
list12 = [2, 5, 8, 3, 4, 7]
common_list = []
for value in list11:
    if value in list12:
        common_list.append(value)
print(common_list)

# 11. Python program to reverse a list with for loop.
list13 = [1, 2, 3, 4, 5, 6, 7]
for value in list13[::-1]:
    print(value, end=" ")
print()

# 12.  Python program to reverse a list with a while loop.

list14 = [1, 2, 3, 4, 5, 6, 7]
while list14:
    print(list14.pop(), end=" ")
print()

# 13). Python program to reverse a list using index slicing.
list15 = [1, 2, 3, 4, 5, 6, 7]
list15_1 = list15[::-1]
print(list15_1)

# 14) Python program to reverse a list with reversed and reverse methods.

list16 = [1, 2, 3, 4, 5, 6]
# print(list(reversed(list16)))
#           or
list16.reverse()
print(list16)

# 15) Problem to copy the list to another list.

list17 = [1, 2, 3, 4, 5]
emp_list = []
for value in list17:
    emp_list.append(value)
print(emp_list)

# 16)Problem to print true if common elements between lists.
list18_1 = [1, 2, 3]
list18_2 = [3, 4]
for value in list18_1:
    if value in list18_2:
        print("True")

# 17)Problem to remove negative elements from the list
list19 = [1, 2, 3, 4, 5, 6, 7, 8, -9, -8]
for value in list19:
    if value >= 0:
        print(value, end=" ")
print()
print("_"*60)
# 18) . Python program to get a list of all elements which are divided by 3 and 7.
list20 = [22, 33, 44, 55, 66, 77, 23, 54, 70, 90, 9, 21]
list20_1 = []
for value in list20:
    if value % 3 == 3 or value % 7 == 0:
        list20_1.append(value)
print(list20_1)

# 19. Problem to check whether the list is palindrome or not.
list21 = [1, 2, 3, 2, 1]
list_reverse = list21[::-1]
if list_reverse == list21:
    print("Palindrome")
else:
    print("Not palindrome")

# 20) Problem to add two lists using extend method.
list22 = [22, 33, 44, 55, 66, 77, 23, 54, 70, 90, 9, 21, 99]
list23 = [1, 2, 10, 3, 4, 5, 6, 7]
list22.extend(list23)
print(list22)



