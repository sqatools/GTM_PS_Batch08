# 1. Python program to calculate the square of each number from the given list.
print("1. Python program to calculate the square of each number from the given list.")

list1 = [2, 3, 6, 9, 13, 46, 78, 34, 21, 10]
# print(len(list1))
sqr = 0
for i in range (len(list1)):
    sqr = list1[i]**2
    print("Square if ",list1[i]," is: ",sqr)

print("_"*50)


# 2. Python program to combine two lists.
print("2. Python program to combine two lists.")

listA = ['a', 'b', 'c', 1, 4, 7, 9, ['x', 'y', 'z'] ]
listB = [4.5, 6.7, 88.9, 22.3]

listRes = listA + listB
print("List after combining 2 lists is: ",listRes)
print("_"*50)


# 3. Python program to calculate the sum of all elements from a list.
print("3. Python program to calculate the sum of all elements from a list.")

list3 = [2, 5, 3, 8, 4, 0, 23, 56, 67, 12]
sum = sum(list3)
print("Sum of elements of list is: ",sum)
print("_"*50)


# 4. Python program to find a product of all elements from a given list
print("4. Python program to find a product of all elements from a given list")

list4 = [2, 5, 3, 8, 4, 0, 23, 56, 67, 12]
a = 0
b = 0

for i in range (len(list4)):
    for j in range (i+1, len(list4)):
        a = list4[i]
        b = list4[j]
        mul = a * b

print("Product of the numbers of list is: ",mul)
print("_"*50)


# 5. Python program to find the minimum and maximum elements from the list.
print("5. Python program to find the minimum and maximum elements from the list.")

list5 = [2, 5, 3, 8, 4, 0, 23, 56, 67, 12]
print("Maximum of all the elements of list is: ",max(list5))
print("Minimum of the elements of list is: ",min(list5))
print("_"*50)


# 6. Python program to differentiate even and odd elements from the given list.
print("6. Program to differentiate even and odd elements from the given list")
list6 = [23, 12, 10, 67, 45, 89, 100, 76, 39, 26]
listA = []
listB = []

for val in list6:
    if val % 2 == 0:
        listA.append(val)
    else:
        listB.append(val)

print("Even numbers are: ",listA)
print("Odd numbers are: ",listB)
print("_"*70)


# 7. Python program to remove all duplicate elements from the list.
print("7. Program to remove all duplicate elements from the list")
list7 = [12, 67, 34, 12, 'Hello', 'hello',34, 100, 10, 'hello', 37]
listA = []

for val in list7:
    if val  in listA:
        continue
    else:
        listA.append(val)

print("List after eliminating duplicates is: ",listA)
print("_"*70)


# 8. Python program to print a combination of 2 elements from the list whose sum is 10.
print("8. Program to print a combination of 2 elements from the list whose sum is 10")
list8 = [2, 8, 4, 6, 5, 5, 8, 4, 10, 9, 1, 0]

print("Combination of 2 elements from the list whose sum is 10 is: ")
for i in range (len(list8)):
    for j in range (i+1, len(list8)):
        if list8[i] + list8[j] == 10:
            print(list8[i],",",list8[j])
print("_"*70)


# 9. Python program to get common elements from two lists.
print("9. Common elements from both lists are: ")
listA = [4, 5, 7, 9, 2, 1]
listB = [2, 5, 8, 3, 4, 7]
output = []

for i in range (len(listA)):
    for j in range (len(listB)):
        if listA[i] == listB[j]:
            output.append(listA[i])

print(output)
print("_"*70)


# 10. Python program to reverse a list with for loop.
print("10. Reversing list using for loop")
list10 = [2, 8, 4, 6, 5, 5, 8, 4, 10, 9, 1, 0]
listA = []
for i in range (-1, -len(list10)-1, -1):
    listA.append(list10[i])

print(listA)
print("_"*70)


# 11. Python program to reverse a list with a while loop.
print("11. Reverse a list with a while loop")

list11 = [2, 8, 4, 6, 5, 5, 8, 4, 10, 9, 1, 0]
length = len(list11) - 1
listA = []

while length >= 0:
    listA.append(list11[length])
    length = length - 1
print(listA)
print("_"*70)


# 12. Python program to reverse a list using index slicing.
print("12. Reverse a list using index slicing")

list12 = [2, 8, 4, 'Hello', 5, 5, 8, 4, 10, 9, 1, 0]
print(list12[-1:-len(list12)-1:-1])
print("_"*70)


# 13. Python program to reverse a list with reversed and reverse methods
print("13. Reverse a list with reversed and reverse methods")

list13 = [2, 8, 4, 'Hello', 5, 5, 8, 4, 10, 9, 1, 0]
listA = [2, 8, 4, 'hello', 5, 5, 8, 4, 10, 9, 1, 0]
listB = []

print("Using reverse() :")
listA.reverse()
print(listA)

print("Using reversed() :")
listB = list(reversed(list13))
print(listB)
print("_"*70)


# 14. Python program to copy or clone one list to another list.
print("14. Program to copy or clone one list to another list")

list14 = [2, 8, 4, 'Hello', 5, 5, 8, 4, 10, 9, 1, 0]
list15 = [0, 1, 9, 10, 4, 8, 5, 5, 'Hello', 4, 8, 2]
listA = list14

print("original list is: ")
print(list14)
print("After copying list14 to listA using '=', contents of listA are: ")
print(listA)

print("Original list is: ")
print(list15)
print("Contents of listA after copying using copy() is :")
listA = list15.copy()
print(listA)
print("_"*70)


# 15. Python program to return True if two lists have any common member.
print("15. Python program to return True if two lists have any common member.")

listA = [2, 8, 4, 'Hello', 5, 5, 8, 4, 10, 9, 1, 0]
listB = [12, 10, 5, 100, 'Hello', 10, 76, 26, 4,]
output = []

for value in listA:
    if value in listB:
        print("True")
        break
#print(output)
print("_"*70)


# 16. Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
print("16. Print the list after removing the 1st, 3rd, and 6th elements from the list")

list16 = [0, 1, 9, 10, 4, 8, 5, 5, 'Hello', 4, 8, 2]
# list16.pop(1)
# list16.pop(3)
# list16.pop(6)

for i in range (len(list16)):
    if i == 1 or i == 3 or i == 6:
        list16.pop(i)
print(list16)
print("_"*70)


# 17. Python program to check whether the given list is palindrome or not
print("17. Program to check whether the given list is palindrome or not")

list17 = [2,4,6,6,4,2]
print("Given list is: ")
print(list17)

listA = list(reversed(list17))
print("Reversed list is: ")
print(listA)

if list17 == listA:
    print("Given list is a Palindrome")
else:
    print("Given list is not Palindrome")
print("_"*70)


# 18. Python Program to get a list of words which has vowels in the given string.
# Input: “www Student ppp are qqqq learning Python vvv”
# Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]

print("18.Program to get a list of words which has vowels in the given string")
str1 = "www Students ppp are qqqq learning Python vvv"
str2 = str1.split()
print("Original string is: ")
print(str2)
list18 = []

for words in str2:
    for char in words:
        if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'
        or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
            list18.append(words)
            break
print("List of words containing vowels is:")
print(list18)
print("_"*70)


# 19. Python program to add 2 lists with extend method.
print("19. Program to add 2 lists with extend method")

list1 = [1, 3, 5, 7, 9]
list2 = ['a', 'b', 'c', 'd', 'e']
list1.extend(list2)
print("List after using extend method: ")
print(list1)
print("_"*70)


# 20. Python program to sort list data, with the sort and sorted method.
print("20. Program to sort list data, with the sort and sorted method")

print("Original list is:")
list20 = [4, 11, 1, 3, 5, 2, 55, 34, 10, 21, 12]
print(list20)
listA = listB = listC = list20

print("\ni. Sorting using sort()")
list20.sort()
print("Ascending order is:")
print(list20)

print("Descending order is: ")
listA.sort(reverse=True)
print(listA)

print("\nii. Sorting using sorted()")
result1 = sorted(listB)
print("Ascending order is:")
print(result1)

result2 = sorted(listC, reverse=True)
print("Descending order is:")
print(result2)
print("_"*70)















"""
#Program 1:
list5 = [2, 5, 3, 8, 4, 0, 23, 56, 67, 12]
sum = 0

for val in list5:
    sum = sum + val

print("Average = ", sum/len(list5))


# Program 2:
list1 = [9, 42, 33, 21, 28, 25]

listA = []
for val in list1:
    if val % 3 == 0 and val % 7 == 0:
        listA.append(val)

print(listA)
"""