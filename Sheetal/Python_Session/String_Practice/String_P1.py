# Types of Python data types.
# 1. Numbers
#    i). Integer :  Immutable
#    ii). Float : Immutable
#    iii). Complex number  : Immutable
#
# 2. Sequential
#    i). String : Immutable
#    ii). List :  mutable
#    iii). Tuple : Immutable
#
# 3. Dictionary : mutable
# 4. Set : mutable
# 5. Boolean : Immutable
# """

import keyword

print("Trim left space and right space")

w=" Learn Python "
print(w.find("ea"))
print(w.index("ea"))

print(w.lstrip().rstrip())

print("_"*40)
print("Remove duplicates")
str3 = "Pramod Hema Kartik Bala Pramod Manoj Hema Kartik"

str3_split = str3.split()
list1 = []

for i in str3_split:
    if i not in list1:
        list1.append(i)
final_list = " ".join(list1)

print("_"*40)
print("")

# Convert list back to string
# result = " ".join(list1)
print(list1)
print(final_list)

print(keyword.kwlist)
print("*"*40)
#Program 1
from colorama import *

print(Fore.MAGENTA+"Write a program to get a list of all the mobile numbers from the given string using python."+Style.RESET_ALL)
Input_str = """ We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string.”””
Output = [‘8988858683’, ‘2312245566’, ‘4532892234’, ‘9999234355’]"""

total_num = 0
list_str = []
Input_str1 = Input_str.split()

for i in Input_str1:
    if i.isnumeric() and len(i) == 10:
        list_str.append(i)
        total_num +=1
print(total_num,list_str)

print("*"*40)
#Program 2
print(Fore.MAGENTA+"Write a program to get all the email id’s from given string using python."+Style.RESET_ALL)
Input_str = "We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string."
# Output = ['john@gmail.com', 'jay@lic.com', 'hari@facebook.com', 'mery@hotmail.com' ]

List_str1 =[]
Input_str1 = Input_str.split()
total = 0

for i in Input_str1:
    if i.__contains__('@') or i.__contains__('.'):
        total +=1
        List_str1.append(i)

print(total,List_str1)

print("*"*40)
#Program 3
print(Fore.MAGENTA+"Write a program to print each character on a new line using python."+Style.RESET_ALL)
Input = "python"

for i in Input:
    print(i)

print("*"*40)
#Program 4
print(Fore.MAGENTA+"Write a program to print a string 3 times using python."+Style.RESET_ALL)
Input = 'sqatools'

print(Input*3)

print("*"*40)
#Program 5
print(Fore.MAGENTA+"Write a program to remove repeated characters in a string and replace it with a single letter using python."+Style.RESET_ALL)
Input = "aabbccdd"

Output =""
for i in Input:
    if i not in Output:
        Output+=i

print(Output)

print("*"*40)
#Program 6
print(Fore.MAGENTA+"Write a program to swap cases of a given string using python."+Style.RESET_ALL)
Input = "Learning Python"

print(Input.swapcase())

print("*"*40)
#Program 7
print(Fore.GREEN+"Write a program to find the first repeated character in a string and its index."+Style.RESET_ALL)
Input = "sqatools"


print("*"*40)
#Program 8
print(Fore.GREEN+"Write a program to print the index of each character in a string."+Style.RESET_ALL)
Input =  "sqatools"



print("*"*40)
#Program 9
print(Fore.GREEN+"Write a program to reverse words in a string using python."+Style.RESET_ALL)
Input = "string problems"


print("*"*40)
#Program 10
print(Fore.GREEN+"Write a program to add ly at the end of the string if the given string ends with ing."+Style.RESET_ALL)
Input = "winning"



print("*"*40)
#Program 11
print(Fore.GREEN+"Write a program to add ‘ing’ at the end of the string using python."+Style.RESET_ALL)
Input = "xyz"


print("*"*40)
#Program 12
print(Fore.GREEN+"Write a program to check if a given string is binary or not."+Style.RESET_ALL)
# Hint: Binary numbers only contain 0 or 1.
Input = "01011100"
# Output = yes

Input = "sqatools 100"
# Output = ‘No’

print("*"*40)
#Program 13
print(Fore.GREEN+"Write a program to remove the kth element from the string"+Style.RESET_ALL)
# K=2
Input = "sqatools"


print("*"*40)
#Program 14
print(Fore.GREEN+"Write a program to accept a string that contains only vowels"+Style.RESET_ALL)
Input = "python"

print("*"*40)
#Program 15
print(Fore.GREEN+"Write a program to avoid spaces in string and get the total length"+Style.RESET_ALL)
Input = "sqatools is best for learning python"


print("*"*40)
#Program 15
print(Fore.GREEN+"Write a python program to find permutations of a given string using in built function."+Style.RESET_ALL)
Input  = "CDE"
# Output = [‘CDE’, ‘CED’ ‘EDC’, ‘ECD’, ‘DCE’, ‘DEC’]

