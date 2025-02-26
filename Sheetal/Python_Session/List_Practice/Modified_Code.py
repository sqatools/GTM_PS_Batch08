from colorama import Fore, Style

# Program 1: Calculate square of each number in a list
print(Fore.GREEN + "Python program to calculate the square of each number from the given list." + Style.RESET_ALL)
Input1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
for i in Input1:
    print(f"Square of {i} is: {i * i}")

print("_" * 40)

# Program 2: Combine two lists
print(Fore.GREEN + "Python program to combine two lists." + Style.RESET_ALL)
Input2 = [56, 17, 21, 18, 61]

Final_list = Input1 + Input2  # Fixed list appending issue
print(Final_list)

print("_" * 40)

# Program 3: Sum of all elements in a list
print(Fore.GREEN + "Python program to calculate the sum of all elements from a list." + Style.RESET_ALL)
print(f"Sum of elements: {sum(Input1)}")

print("_" * 40)

# Program 4: Product of all elements in a list
print(Fore.GREEN + "Python program to find the product of all elements from a given list." + Style.RESET_ALL)
product = 1
for i in Input1:
    product *= i
print(f"Product of elements: {product}")

print("_" * 40)

# Program 5: Find min and max in a list
print(Fore.GREEN + "Python program to find the minimum and maximum elements from the list." + Style.RESET_ALL)
print(f"The max number from the list is: {max(Input1)}")
print(f"The min number from the list is: {min(Input1)}")

print("_" * 40)

# Program 6: Differentiate even and odd numbers
print(Fore.GREEN + "Python program to differentiate even and odd elements from the given list." + Style.RESET_ALL)
for i in Input1:
    print(f"{i} is {'even' if i % 2 == 0 else 'odd'}")

print("_" * 40)

# Program 7: Remove duplicates from a list
print(Fore.GREEN + "Python program to remove all duplicate elements from the list." + Style.RESET_ALL)
Input3 = [5, 7, 2, 8, 11, 12, 12, 19, 2]
Rem_dup = list(set(Input3))  # Using set() to remove duplicates
print(Rem_dup)

print("_" * 40)

# Program 8: Find pairs whose sum is 10
print(Fore.GREEN + "Python program to print a combination of 2 elements from the list whose sum is 10." + Style.RESET_ALL)
Input4 = [5, 7, 2, 8, 3, 11, 5, 12, 17, 19, 22]
pairs = set()

for i in range(len(Input4)):
    for j in range(i + 1, len(Input4)):
        if Input4[i] + Input4[j] == 10 and (Input4[j], Input4[i]) not in pairs:
            print(f"{Input4[i]} + {Input4[j]} = 10")
            pairs.add((Input4[i], Input4[j]))

print("_" * 40)

# Program 9: Print squares of even numbers
print(Fore.GREEN + "Python program to print squares of all even numbers in a list." + Style.RESET_ALL)
Org_list = [5, 7, 2, 8, 3, 11, 5, 12, 17, 19, 22]

new_list = [i for i in Org_list if i % 2 == 0]  # Even numbers
new_list_sq = [i * i for i in new_list]  # Squared values

print(f"The Original List: {Org_list}\nNew List (Evens): {new_list}\nSquared List: {new_list_sq}")

print("_" * 40)

# Program 10: Split list into odds and evens
print(Fore.GREEN + "Python program to split the list into two parts: odd values on the left, even values on the right." + Style.RESET_ALL)
odd_list = [i for i in Org_list if i % 2 != 0]
even_list = [i for i in Org_list if i % 2 == 0]

print(odd_list + even_list)

print("_" * 40)

# Program 11: Get common elements from two lists
print(Fore.GREEN + "Python program to get common elements from two lists." + Style.RESET_ALL)
List1 = [4, 5, 9, 2, 1]
List2 = [2, 5, 8, 3, 4, 7]

common_elements = list(set(List1) & set(List2))  # Using set intersection
print(common_elements)




