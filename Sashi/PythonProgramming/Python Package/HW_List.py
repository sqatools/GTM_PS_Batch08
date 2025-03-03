"""""""""

1. Python program to calculate the square of each number from the given list.")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list1:
    print(i, ":", i ** 2)

print("_" * 50)

2.Python program to combine two lists.")
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = list1 + list2
print("List using concatenation:", list3)
list1.extend(list2)
print("List using extend: ", list1)
print("_" * 50)

3.Python program to calculate the sum of all elements from a list.")
list3 = [3, 7, 9, 12, 6]
sum = 0
for x in list3:
    sum += x
print(sum)
print("_" * 50)

4.Python program to find a product of all elements from a given list.")
list4 = [3, 4, 5]
product = 1
for x in list4:
    product = product * x
print(product)
print("_" * 50)

5.Python program to find the minimum and maximum elements from the list.")
list5 = [34, 89, 2, 7, 90]
print("The maximum number is: ", max(list5))
print("The minimum number is: ", min(list5))


6.Python program to differentiate even and odd elements from the given list.")
list6 = [3, 5, 6, 8, 90, 23, 34, 9]
for x in list6:
    if x % 2 == 0:
        print(x, ": Even")
    else:
        print(x, ": Odd")
print("_" * 50)

7.Python program to remove all duplicate elements from the list.")
List7 = ["Sita", "Ram", "Laxman", "Hanuman", "Sita", "Sita", "Hanuman", "Ram", "Laxman"]
list8 = []
for x in List7:
    if x not in list8:
        list8.append(x)
    else:
        continue
print(list8)
print("_" * 50)

8.Python program to print a combination of 2 elements from the list whose sum is 10.")
# Did not understand the solution on website using itertools. Check if this program is ok
# List8=[0,1,2,3,4,5,6,7,8,9,10]
List8 = [2, 5, 8, 5, 1, 9]
print("The 10s partner are as follows: ")
for x in range(0, len(List8)):
    for y in range(x + 1, len(List8)):
        if List8[x] + List8[y] == 10:
            print(List8[x], "+", List8[y], "=", List8[x] + List8[y])
        else:
            continue
print("_" * 50)

9. Python program to print squares of all even numbers in a list.")
list9 = [7, 2, 34, 6, 8, 57]
for x in list9:
    if x % 2 == 0:
        print(x, "^ 2 =", x ** 2)
print("_" * 50)

10.Python program to split the list into two-part, the left side all odd values and the right side all even values.")
# Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
# Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
list10 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
outputeven = []
outputodd = []
for x in list10:
    if x % 2 == 0:
        outputeven.append(x)
    else:
        outputodd.append(x)
# concatenating
print(outputodd + outputeven)
# using extend
outputodd.extend(outputeven)
print(outputodd)
print("_" * 50)

11.Python program to get common elements from two lists.")
# Input =
# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]
# Output : [4, 5, 7, 2]
list11 = [4, 5, 7, 9, 2, 1]
list12 = [2, 5, 8, 3, 4, 7]
output = []
for x in range(0, len(list11)):
    if list11[x] in list12:
        output.append(list11[x])
print(output)
print("_" * 50)

12.Python program to reverse a list with for loop.")
list12 = [8, 5, 6, 34, 98, 0, 3]
print("Original: ", list12)
rev = []
for x in range(-1, -len(list12) - 1, -1):
    rev.append(list12[x])
print("Reverse: ", rev)
print("_" * 50)

13.Python program to reverse a list with a while loop.")
# Did not understand website solution
list12 = [9, 3, 6, 34, 12, 15, 80, 2]
print("Original list: ", list12)
list121 = []
x = 0
y = -1
while x < len(list12):
    list121.append(list12[y])
    y = y - 1
    x = x + 1
print("Reverse: ", list121)
print("_" * 50)



14. Python program to reverse a list using index slicing.")
list14 = [6, 4, 8, 9, 2, 12, 3, 5, 15]
print(list14)
list141 = list14[-1:-len(list14) - 1:-1]
print(list141)
print("_" * 50)

15. Python program to reverse a list with reversed and reverse methods.")
List15 = [2, 8, 3, 4, 1, 90, 34]
List15.reverse()
print("Using reverse", List15)  # This will modify the list
list16 = [2, 8, 3, 4, 1, 90, 34]
result1 = list(reversed(list16))  # converts to iterator object so converted to list
print("Using reversed", result1)
print("_" * 50)

16.Python program to copy or clone one list to another list.")
list17 = [2, 4, 6, 76, 45, 90, 9]
list18 = list17.copy()
print("Deep copy", list18)
list17.append(100)
list18.append(200)
print((list17))
print(list18)
print("_" * 50)

"""""""""""""""






