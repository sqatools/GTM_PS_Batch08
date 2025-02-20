from colorama import *

# Program 1
print(Fore.GREEN + "Python program to calculate the square of each number from the given list." + Style.RESET_ALL)
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
for i in Input:
    print("Square of ", i, " is: ", i * i)

print("_" * 40)

#Program 2
print(Fore.GREEN + "Python program to combine two lists." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Input2 = [56, 17, 21, 18, 61]

Final_list = Input1 + Input2

print(Input1)

print("_" * 40)
#Program 3
print(Fore.GREEN + " Python program to calculate the sum of all elements from a list." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]

Sum_Num = 0

for i in Input1:
    Sum_Num = Sum_Num + i

print(Sum_Num)

print("_" * 40)

#Program 4
print(Fore.GREEN + "Python program to find a product of all elements from a given list." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Input1_prod = 1

for i in Input1:
    Input1_prod = Input1_prod * i
print(Input1_prod)

print("_" * 40)

#Program 5
print(Fore.GREEN + "Python program to get a list with n elements removed from the left and right." + Style.RESET_ALL)
Input = [2, 5, 7, 9, 3, 4]
print("Remove 1 element from left")
# [5, 7, 9, 3, 4]
print(Input[1:])
print("Remove 1 element from the right")
# [2, 5, 7, 9, 3]
print(Input[0:len(Input) - 1])
print("Remove 2 elements from left")
# [7, 9, 3, 4]
print(Input[2:])
print("Remove 2 elements from right")
# [2, 5, 7, 9]
print(Input[0:len(Input) - 2])

#Program 6
print("_" * 40)
print(Fore.GREEN + "Python program to get common elements from two lists." + Style.RESET_ALL)
#Output= [4, 5, 7, 2]
List1 = [4, 5, 9, 2, 1]
List2 = [2, 5, 8, 3, 4, 7]

new_list = []
for i in List1:
    for j in List2:
        if i == j and i not in new_list:
            new_list.append(i)
        else:
            break

# common_elements = list(set(List1) & set(List2))
print(new_list)

print("_"*40)
#Program 7
print(Fore.GREEN + "Python program to find the minimum and maximum elements from the list." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]

Input1_max = Input1[0]
Input1_min = Input1[0]

for i in Input1:
    if i > Input1_max:
        Input1_max = i
    elif i < Input1_max:
        Input1_min = i
print("The max number from the list is: ", Input1_max)
print("The min number from the list is: ", Input1_min)

print("_" * 40)
#Program 8
print(Fore.GREEN + " Python program to differentiate even and odd elements from the given list." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]

for i in Input1:
    if i % 2 == 0:
        print(i, " is an even number")
    else:
        print(i, " is an odd number")

print("_" * 40)

#Program 9
print(Fore.GREEN + "Python program to remove all duplicate elements from the list." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 11, 12, 12, 19, 2]

Rem_dup = []
for i in Input1:
    if i not in Rem_dup:
        Rem_dup.append(i)

print(Rem_dup)

print("_" * 40)

#Program 10
print(
    Fore.GREEN + "Python program to print a combination of 2 elements from the list whose sum is 10." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 3, 11, 5, 12, 17, 19, 22]
pairs = set()

for i in range(len(Input1)):
    for j in range(i + 1, len(Input1)):
        if Input1[i] + Input1[j] == 10 and (Input1[j], Input1[i]) not in pairs:
            print(Input1[i], "+", Input1[j], "=", 10)
            pairs.add((Input1[i], Input1[j]))

print()

print("_" * 40)

#Program 11
print(Fore.GREEN + "Python program to print squares of all even numbers in a list." + Style.RESET_ALL)
Org_list = [5, 7, 2, 8, 3, 11, 5, 12, 17, 19, 22]

new_list = []
new_list_sq = []

for i in Org_list:
    if i % 2 == 0:
        k = i * i
        new_list_sq.append(k)
        new_list.append(i)

# print("The Original List:", Input1, "\n", new_list, "\n", new_list_sq)
print(f"The Original List: {Input1}\nNew List: {new_list}\nSquared List: {new_list_sq}")

print("_" * 40)

#Program 12
print(
    Fore.GREEN + "Python program to split the list into two-part, the left side all odd values and the right side all even values." + Style.RESET_ALL)
Org_list = [5, 7, 2, 8, 11, 12, 17, 19, 22]
even_list = []
odd_list = []

for i in Org_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(odd_list + even_list)
print()

print("_"*40)
#Program 13
print(Fore.GREEN + "Python program to reverse a list with a while loop." + Style.RESET_ALL)
Org_list = [5, 7, 2, 8, 11, 12, 17, 19, 22]
reverse_list = []
i = len(Org_list) - 1

while i >= 0:
    reverse_list.append(Org_list[i])
    i -= 1

print(f"The original list {Org_list} and reverse list is {reverse_list}")

print("_" * 40)
#Program 14
print(Fore.GREEN + "Python program to calculate percentage from a given mark list, the max mark for each item is 100." + Style.RESET_ALL)

Marks_list = [80, 50, 70, 90, 95]
# Output: 77%
mark_per = []
sum_mark = 0
Total_mark = len(Marks_list) * 100

print(f"The Total numbers of marks of {len(Marks_list)} subjects is {Total_mark} ")

for i in Marks_list:
    sum_mark = sum_mark + i
print(f"The sum of all marks are : {sum_mark}")

result = (sum_mark / Total_mark) * 100
print(f"Overall Percentage: {result:.2f}%")

print("_"*40)

#Program 15
print(Fore.GREEN + "WAP" + Style.RESET_ALL)
list_b = [3, 6, 4, 12, 78, 34, 37]
print(f" The number {i} is {'even' if i % 2 == 0 else 'odd'}" for i in list_b)
# print(f"{i} is {'even' if i % 2 == 0 else 'odd'}")

print("\n".join(f"The number {i} is {'even' if i % 2 == 0 else 'odd'}" for i in list_b))

print("_"*40)

#Program 16
print(Fore.GREEN + "Python program to reverse a list using index slicing." + Style.RESET_ALL)
Org_list = [5, 7, 2, 8, 11, 12, 17, 19, 22]

reverse_list = Org_list[-1:-len(Org_list) - 1:-1]

print(f"The Original number was {Org_list} and the new reversed list is {reverse_list}")
print("_"*40)

#Program 17
print(Fore.GREEN + "Python program to calculate the bill per fruit purchased from a given fruits list." + Style.RESET_ALL)
"""Input = Fruit list with Price: [[‘apple’, 30], [‘mango’, 50], [‘banana’, 20], [‘lichi’, 50]]
Fruit with quantity: [[‘apple’, 2]]
Output = Fruit: Apple Bill: 60 Fruit: mango Bill: 500 """
Input = [["apple", 30], ["mango", 50], ["banana", 20], ["lichi", 50]]
Quantity = [["apple", 2], ["mango", 5], ["banana", 5]]

for fru in Input:
    for qty in Quantity:
        if fru[0] == qty[0]:
            bill = fru[1] * qty[1]  # price * quantity
            print(f"Fruit: {fru[0].capitalize()} | Bill: {bill}")


print("_"*40)
# Program 18
print("Python program to copy or clone one list to another list." + Style.RESET_ALL)
Org_list = [5, 7, 2, 8, 11, 12, 17, 19, 22]
New_list = Org_list.copy()

print(f"The two lists are {Org_list} and copied one is {New_list}")

print("_"*40)
#Program 19
print(Fore.GREEN + "Python program to create a dictionary with two lists." + Style.RESET_ALL)
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [234, 123, 456, 343, 223]
# Output: {'a': 234, 'b': 123, 'c': 456, 'd': 343, 'e': 223}

dictionary = dict(zip(list1, list2))

print("Generated Dictionary:", dictionary)

print("_"*40)
#Program 20
print(Fore.GREEN + "Python program to insert a sublist into the list at a specific index." + Style.RESET_ALL)
Input = [4, 6, 8, 2, 3, 5]
sublist = [5, 2, 6]
index = 3
# Output: [4, 6, 8, [5, 2, 6], 2, 3, 5]

Input.insert(index,sublist)

print(Input)
