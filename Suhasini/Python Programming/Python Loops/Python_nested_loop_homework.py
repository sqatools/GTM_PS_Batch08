########################### Homework and Practice questions #############################
"""
# 1. Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included)

print("Python program to print those numbers that are divisible by 7 and multiple of 5, between 1500 and 2700")

for i in range (1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=(","))

print()
print("_"*80)
"""
import string

"""
# 2. Python Loops program to construct the following pattern, using a nested for loops.
# Output :
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

print("Python program to print a pattern:")
for i in range (1, 6):
    print(i*"*")
for i in range (4, -1, -1):
    print(i*"*")
print("_"*80)
"""

"""
#3. Python Loops program that will add the word from the user to the empty string using python.
print("Python Loops program that will add the word from the user to the empty string using python")

str1 = ""
word = input("Enter a word")

for i in range (len(word)):
    str1 += word[i]
print("Str1: ",str1)
print("_"*80)
"""

"""
#4. Python Loops program to count the number of even and odd numbers from a series of numbers using python.
#Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)

oddcount = 0
evencount = 0
print("4. Python Loops program to count the number of even and odd numbers from a series of numbers using python")

for i in range (1, 10):
    if i%2 == 0:
        evencount += 1
    else:
        oddcount += 1
print("Number of even numbers is: ",evencount)
print("Number of odd numbers is: ",oddcount)
print("_"*80)

#5. Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
print("5. Program that prints all the numbers from 0 to 6 except 3 and 6 using python.")

for i in range (0, 11):
    if i != 3 or i != 6:
        print(i, end=",")
print()
print("_"*80)

#6. Write a program to get the Fibonacci series between 0 to 20 using python
print("6. Write a program to get the Fibonacci series between 0 to 20 using python")

num1 = 0
num2 = 1
count = 0

while count < 20:
    print(num1,end=" ")
    n2 = num1 + num2
    num1 = num2
    num2 = n2
    count += 1
print("_"*80)
"""

"""
#7. Write a program that iterates the integers from 1 to 30 using python. For multiples of three
# print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers that are multiples of both three and five print “FizzBuzz”.

print("Printing numbers as mentioned: ")
for i in range (1, 31):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print("_"*80)
"""

"""
# 8. Write a program that accepts a word from the user and
# converts all uppercases in the word to lowercase using python

print("Program to convert uppercase to lower case and vice versa in a string")
str1 = input("Enter a string")

for i in range (0, len(str1)):
    if str1[i].islower():
        print(str1[i].upper(),end="")
    elif str1[i].isupper():
        print(str1[i].lower(),end="")
print()
print("_"*80)
"""

"""
# 9. Python loops program that accepts a string and calculates the number
# of digits and letters using python
print("Program that accepts a string and calculates the number of digits and letters using python")
str1 = input("Enter a string")
countnum = 0
countalpha = 0
for i in range (0, len(str1)):
    if str1[i].isnumeric():
        countnum += 1
    elif str1[i].isalpha():
        countalpha += 1
print("Count of numbers is: ",countnum)
print("Count of alphabets is: ",countalpha)
"""

"""
# 10. Write a program to print the pattern of O
print("10. Write a program to print the pattern of O")

for i in range (0, 7):
    if i == 0 or i == 6:
        print("  *** ")
    else:
        print("*     *")
print("_"*80)
"""

"""
# 11. Python Loops program to print all alphabets from a to z using for loop
# A-Z ASCII Range  65-90
# a-z ASCII Range  97-122

print("Alphabets from a-z:")
for i in string.ascii_lowercase:
    print(i, end=" ")

print()
print("Alphabets from A-Z :")
for i in string.ascii_uppercase:
    print(i, end=" ")
print()
print("_"*80)
"""

"""
# 12. Python Loops program to print all even numbers between 1 to 100 in python
print("Python Loops program to print all even numbers between 1 to 100 in python")

for i in range (1, 101):
    if i %2 == 0:
        print(i, end=",")

print()
print("_"*80)
"""

"""
#13. Python Loops program to print all odd numbers between 1 to 100 using python
print("Python Loops program to print all odd numbers between 1 to 100 in python")

for i in range (1, 101):
    if i %2 != 0:
        print(i, end=",")

print()
print("_"*80)
"""

"""
# 14. Python Loops program to find the sum of all natural numbers between 1 to n using python
print("Python Loops program to find the sum of all natural numbers between 1 to n using python")

total = 0
n = int(input("Enter the last number"))
for i in range (1, n+1):
    total += i

print("Total of the numbers is: ",total)
print("_"*80)
"""

"""
# 15. Python program to find the sum of all even numbers between 1 to n using python
print("Python program to find the sum of all even numbers between 1 to n using python")

total = 0
n = int(input("Enter the last number"))
for i in range (1, n+1):
    if i % 2 == 0:
        total += i

print("Total of the numbers is: ",total)
print("_"*80)
"""

"""
#16. Python Loops program to find the sum of all odd numbers between 1 to n using python
print("Python Loops program to find the sum of all odd numbers between 1 to n using python")

total = 0
n = int(input("Enter the last number"))
for i in range (1, n+1):
    if i % 2 != 0:
        total += i

print("Total of the numbers is: ",total)
print("_"*80)
"""

"""
# 17. Write a program to count the number of digits in a number using python.
print("17. Program to count the number of digits in a number using python")

count = 0
num = int(input("Enter a number"))
str1 = str(num)
# length = len(num)
for i in str1:
    count += 1

print("Number of digits in the entered number is: ",count)
"""

"""
# 18. Write a program to find the first and last digits of a number using python
print("Program to find the first and last digits of a number using python")

num = input("Enter a number")
length = len(num)
print("First digit of the number is: ",num[0])
print("Last digit of the number is: ",num[length-1])
print("_"*80)
"""

"""
# 19. Write a program to find the sum of the first and last digits of a number using python
print("Program to find the sum of the first and last digits of a number using python")

num = int(input("Enter a number"))
str1 = str(num)
total= 0

for i in range(len(str1)):
    if i == 0:
        print("First digit of the number is: ", str1[i])
        total += int(str1[i])
    elif i == len(str1)-1:
        print("Last digit of the number is: ", str1[i])
        total += int(str1[i])

print("Sum of first and last number: ",total)
print("_"*80)
"""


# 20. Write a program to calculate the sum of digits of a number using python
print("Program to calculate the sum of digits of a number using python")

num = int(input("Enter a number"))
str1 = str(num)
total= 0

for i in range(len(str1)):
    total = total + int(str1[i])

print("Sum of the digits is:",total)
print("_"*80)



# While loop : 11, 12