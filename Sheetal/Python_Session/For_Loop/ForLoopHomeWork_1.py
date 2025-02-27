from colorama import *

#Program 1
print(Fore.GREEN +"Python Loops program to construct the one side diamond pattern, using a nested for loops."+ Style.RESET_ALL)
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

num = int(input('Enter number of rows for pattern number: '))

for i in range(0,num):
    for k in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(0, num):
    for j in range(i,num):
         print("*",end=" ")
    print()



"""print("_"*40)
for i in range(num-1,0):
    for j in range(0,i+1):
         print("*",end=" ")
    print()
for i in range(0,num):  ##rows
    for k in range(i,num//2):  ##column
        print("*",end=" ")
    print()
"""

#Program 2
print(Fore.BLUE +"WAP to print Full Diamond pattern"+ Style.RESET_ALL)

print("_"*40)
num = int(input("Enter number of rows for the pattern: "))

for i in range(1, num + 1):
    print(" " * (num - i) + "* " * i)

for i in range(num - 1, 0, -1):
    print(" " * (num - i) + "* " * i)

print("_"*40)
#Program 3
print(Fore.GREEN +"Python for loop program to print the alphabet pattern 0 using python."+ Style.RESET_ALL)
# """Output:
#   ***
# *       *
# *       *
# *       *
# *       *
# *       *
#    ***
# """
for i in range(0,13):
    for j in range(0,13):
        if (i==0 or i==12) and (1< j <11):
            print("*",end=" ")
        elif(0< i <=11) and (j==1 or j==11):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("_"*40)
#Program 4
print(Fore.GREEN +"Print the following small alphabet letter pattern using Python Loops."+ Style.RESET_ALL)
# Output =
#            a
#        b c d
#      e f g h i
#    j k l m n o p
#      q r s t u
#        v w x
#           y
start_pt = ord('a')
for i in range(1,8):
    print(" " * (8-i), end="")
    for j in range(i):
        print(chr(start_pt), end=" ")
        start_pt += 1
    print()


start_pt = ord("a")

for i in range(1,9):
    print(" " * (8 - i) + chr(start_pt))
    start_pt +=1


print("_"*40)
#Program 5
print(Fore.GREEN +"Write a program to find the maximum number from the list using Python Loops"+ Style.RESET_ALL)
# Input : [12,14,45,88,63,97,88]
# Output : Maximum number: 97
Input = [12,14,45,88,63,97,88]
print(len(Input))
max_value=0

for i in Input:
    if max_value < i:
        max_value = i
    else:
        max_value = max_value
print("The maximum value is : ", max_value)


print("_"*40)
#Program 6
print(Fore.GREEN +"Write a program to sort a list using for loop in Python Loops.")
Input = [6,8,2,3,1,0,5]
# Output = [0,1,2,3,5,6,8]

for i in range(len(Input)):
    for j in range(0,len(Input)):
        if Input[i] > Input[j]:
            temp = Input[i]
            Input[i]=Input[j]
            Input[j] = temp
print(Input)

print("_"*40)
#Program 7
print(Fore.GREEN +"Python Loops program that will add the word from the user to the empty string using python."+ Style.RESET_ALL)
str1 = ""
str2 = str(input("Enter a string: "))

for i in range(len(str2)):
    str1 += str2[i]
print("The input string was: ", str1)

print("_"*40)
#Program 8
print(Fore.GREEN +"Python Loops program to count the number of even and odd numbers from a series of numbers using python."+ Style.RESET_ALL)
Input = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count1 = 0
count2 = 0
for i in range(len(Input)):
    if Input[i]%2==0:
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print("The count of even numbers in the Input is: ", count1)
print("The count of odd numbers in the Input is: ", count2)

print("_"*40)

#Program 9
print(Fore.GREEN +"Write a program to find the sum of the first and last digits of a number using python."+ Style.RESET_ALL)
Input = int(input("Enter the number: "))
result = str(Input)
# for i in range(0,len(result)):
first_digit= result[0]
last_digit = result[-1]
final = int(first_digit) + int(last_digit)
print("The first digit is :", first_digit)
print("The last digit is :",last_digit)
print("The sum of first and last digit is: ", final)

print("_"*40)
#Program 10
print(Fore.GREEN +"Write a program to count the number of digits in a number using python."+ Style.RESET_ALL)
Input = int(input("Enter the number: "))
result = str(Input)
print("The length of the number is :", len(result))


print("_"*40)
#Program 11
print(Fore.GREEN +"Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python."+ Style.RESET_ALL)
for i in range (7):
    if i!= 3 or i != 6:
        print(i,end="")


print("_"*40)
#Program 12
print(Fore.GREEN +"""Write a program that iterates the integers from 1 to 30 using python.
 For multiples of three print 'Fizz' instead of the number and for multiples of five print 'Buzz'.
  For numbers that are multiples of both three and five print 'FizzBuzz'"""+ Style.RESET_ALL)

for i in range(1,31):
    if i%3 ==0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i% 5 == 0:
        print("Buzz")
    else:
        print(i)


print("_"*40)
#Program 13
print(Fore.GREEN +"Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python."+ Style.RESET_ALL)
Input = "SqaTOOlS"

print(Input.lower())

print("_"*40)
# Program 14
print(Fore.GREEN +"Python loops program that accepts a string and calculates the number of digits and letters using python."+ Style.RESET_ALL)
Input = "python1234"
count1 =0
count2 = 0
list1 = []
for i in Input:
    list1.append(i)
for j in range(0,len(list1)):
    if list1[j].isnumeric():
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print(list1)
print("Count of Alphabet: ",count2)
print("Count of Number: ",count1)


print("_"*40)
# Program 15
print(Fore.GREEN +"Python Loops program to print all alphabets from a to z using for loop"+ Style.RESET_ALL)
#         Take chr method help to print characters with ASCII values
#         chr(65) = ‘A’

for i in range(97, 123):
    print(chr(i),end=" ")

print()
print("_"*40)
#Program 16
print(Fore.GREEN +"Python Loops program to print all even numbers between 1 and 100 in python."+ Style.RESET_ALL)
for i in range(0,101):
    if i%2 == 0:
        print(i, end =" ")

print()
print("_"*40)
#Program 17
print(Fore.GREEN +"Python Loops program to find the sum of all natural numbers between 1 to n using python."+ Style.RESET_ALL)
sum1= 0
for i in range(0,100):
    sum1 = sum1 +i

print("The sum of first 100 numbers are: ", sum1)

print("_"*40)
#Program 18
print(Fore.GREEN +"Python program to find the sum of all even numbers between 1 to n using python."+ Style.RESET_ALL)

sum2 = 0
for i in range(0,101):
    if i%2 == 0:
        sum2 = sum2 + i

print("Sum of even numbers upto 100", sum2)

print("_"*40)
# Program 19
print(Fore.GREEN +"Write a program to remove repeated characters in a string and replace it with a single letter using python."+ Style.RESET_ALL)
#Split() is used for splitting by spaces, but string "aabbccdd" has no spaces.
Input = "aabbccdd"
# Output = ‘cabd’
str12 =[]

for i in Input:
    if i not in str12:
        str12.append(i)

print("".join(str12))

print("_"*40)
#Program 20
print(Fore.GREEN +"Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)."+ Style.RESET_ALL)
Input1 = 1500
Input2 = 2700
list_display =[]

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        list_display.append(i)
print("The number is divisible by 7 and is multiple of 5", list_display)



print("_"*40)
#Program 21
print(Fore.GREEN +"Program to find the frequency of each digit in a given integer using Python Loops"+ Style.RESET_ALL)
Input = "Hello12 Python14 is2 a1 greate1 program2"
# digit_frequency = [0]*10
#
# for i in Input:
#     if i.isdigit():
#         digit_frequency[int(i)] += 1
#
# for digit in range(10):
#     if digit_frequency[digit] > 0:
#         print(f"Digit {digit}: {digit_frequency[digit]} times")

# Input = "Hello12 Python14 is2 a1 greate1 program2"
#
# for digit in range(1,10):
#     count = Input.count(str(digit))
#     if count > 0:
#         print(f"Digit {digit}: {count} times")

print("_"*40)
#Program 22
print(Fore.GREEN +"Python loops program to enter a number and print it in words."+ Style.RESET_ALL)
number = int(input("Enter a single digit number: "))
str1 = ""

for i in str(number):
    if i == "1":
        str1 += "One"
    elif i == "2":
        str1 += "Two"
    elif i == "3":
        str1 += "Three"
    elif i == "4":
        str1 += "Four"
    elif i == "5":
        str1 += "Five"
    elif i == "6":
        str1 += "Six"
    elif i == "7":
        str1 += "Seven"
    elif i == "8":
        str1 += "Eight"
    elif i == "9":
        str1 += "Nine"

print(str1)
print("_"*40)
#Python 23
print(Fore.GREEN +"Write a program to count the total numbers of odd numbers between 1-100 using Python Loops."+ Style.RESET_ALL)
count1 = 0
for i in range(0,101):
    if i%2 != 0:
        # print(i,end=" ")
        count1 = count1 +1

print("The total count of odd number between 0 and 100 is: ",count1)

print("_"*40)
#Program 24
print(Fore.GREEN+ "Write a program to get input from the user if it is a number insert it into an empty list using Python Loops."+ Style.RESET_ALL)
Input = input("Enter the value: ")
list11 =[]

if Input.isdigit():
    list11.append(Input)
    print("The entered value is : ", list11)
else:
    print("The entered string is: ",Input)

print("_"*40)
#Program 25
print(Fore.GREEN +"Write a program to get input from the user if it is a string insert it into an empty list using Python Loops."+ Style.RESET_ALL)
Input = "sqatools007"
list1 = []
for i in Input:
    if i.isalpha():
        list1.append(i)
print("".join(list1))

print("_"*40)
#Program 26
print(Fore.GREEN +"Write a program to accept the kilometers covered and calculate the bill according to the following using Python Loops"+ Style.RESET_ALL)
# First 5 km- 15rs/km
# Next 20 km- 12rs/km
# After that- 10rs/km


print("_"*40)
#Program 27
print(Fore.GREEN +"Write a program to construct the following pattern, using a nested for loop in Python."+ Style.RESET_ALL)

print("_"*40)
#Program 28
print(Fore.GREEN +"Write a program to check the validity of password input by users using Python Loops"+ Style.RESET_ALL)

print("""At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 5 characters.
Maximum length 15 characters.""")

Input = "Abcd@1234"
# Input = "A@1"
# Output = Valid password
import string
from colorama import *
Output = ""

count_lower = count_upper = count_special = count_number = 0
if 5 <= len(Input) <=15:
    for char in Input:
        if char.isalpha() or char.isnumeric() or char in ("$#@"):
            if char.isalpha() and char in (string.ascii_lowercase):
                Output += char
                count_lower +=1
            if char.isalpha() and char in (string.ascii_uppercase):
                Output += char
                count_upper +=1
            if char.isnumeric() and char in string.digits:
                Output +=char
                count_number +=1
            if char in ("@#$"):
                Output += char
                count_special +=1

    if count_lower >0 and count_special > 0 and count_upper >0 and count_number >0:
        print(f"The output of the string {Fore.BLUE }{Output} {Style.RESET_ALL}is a valid password")
    else:
        print(f"The password entered {Fore.BLUE}{Output} {Style.RESET_ALL} is wrong. It must contain given parameter")
else:
    Output = Input
    print(f"Please check the length of your entered password {Fore.BLUE }{Output} {Style.RESET_ALL} which should be between 5 to 15")

print("_"*40)
#Program 29
print(Fore.GREEN +"Write a program to check whether a string contains an integer or not using Python Loops"+ Style.RESET_ALL)
Input = "Hello657 Python1234"
list1 =[]

for i in Input:
    if i.isnumeric():
        print(True, end="")
        break
        # list1.append(i)

print()
# print(list1)

print("_"*40)
#Program 30
print(Fore.GREEN +"Write a program to display numbers from a list using Python Loops"+ Style.RESET_ALL)
Input = [1,5,8,0,4]
for i in Input:
    print(i, end =" ")


print("_"*40)
#Program 31
print(Fore.BLUE+ "Write a program to find the first repeated character in a string and its index."+Style.RESET_ALL)
str11 = "sqltools"
seen_string = []

for i in range(len(str11)):
    if str11[i] in seen_string:
        print(f"First repeated character: '{str11[i]}' at index {i}")
        # print((str11[i],i))
        break

    seen_string.append(str11[i])
else:
    print("No repeated character found")

print("_"*40)
#Program 32
