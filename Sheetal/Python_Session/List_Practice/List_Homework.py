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

for i in Input2:
    Final_list = Input1.append(i)

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
print(Fore.GREEN + "Python program to find the minimum and maximum elements from the list." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]

Input1_max = 0
Input1_min = []

for i in Input1:
    if i > Input1_max:
        Input1_max = i
    elif i < Input1_max:
        Input1_min = i
print("The max number from the list is: ", Input1_max)
print("The min number from the list is: ", Input1_min)

print("_" * 40)
#Program 6
print(Fore.GREEN + " Python program to differentiate even and odd elements from the given list." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]

for i in Input1:
    if i % 2 == 0:
        print(i, " is an even number")
    else:
        print(i, " is an odd number")

print("_" * 40)
#Program 7
print(Fore.GREEN + "Python program to remove all duplicate elements from the list." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 11, 12, 12, 19, 2]

Rem_dup = []
for i in Input1:
    if i not in Rem_dup:
        Rem_dup.append(i)

print(Rem_dup)

print("_" * 40)
#Program 8
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
#Program 9
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
#Program 10
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

# odd_list = [i for i in input_list if i % 2 != 0]
# even_list = [i for i in input_list if i % 2 == 0]


#Program 11
print("_" * 40)
print(Fore.GREEN + "Python program to get common elements from two lists." + Style.RESET_ALL)
#Outputt : [4, 5, 7, 2]
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


print("_" * 40)
#Program 12
print(Fore.GREEN+"Python program to reverse a list with a while loop."+Style.RESET_ALL)


print("_" * 40)
#Program 13
print(
    Fore.GREEN + "Python program to calculate percentage from a given mark list, the max mark for each item is 100." + Style.RESET_ALL)
Marks_list: [80, 50, 70, 90, 95]
# Output: 77%


print("_" * 40)
#Program 14
print(Fore.GREEN + "Python program to reverse a list using index slicing." + Style.RESET_ALL)

print("_" * 40)
#Program 15
print("Python program to copy or clone one list to another list." + Style.RESET_ALL)

print("_" * 40)
#Program 15
print(Fore.GREEN + "WAP" + Style.RESET_ALL)

print("_" * 40)
#Program 16
print(Fore.GREEN + "WAP" + Style.RESET_ALL)

print("_" * 40)
#Program 17
print(Fore.GREEN + "WAP" + Style.RESET_ALL)

print("_" * 40)
#Program 18
print(Fore.GREEN + "WAP" + Style.RESET_ALL)

print("_" * 40)
#Program 19
print(Fore.GREEN + "WAP" + Style.RESET_ALL)
