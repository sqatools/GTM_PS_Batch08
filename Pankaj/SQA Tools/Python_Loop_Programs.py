print("_"*60)
# 1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")

print("_"*60)
# 2). Python Loops program to construct the following pattern, using a nested for loops.
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
for q in range(6):
    print(q*"*")
for w in range(4, -1, -1):
    print(w*"*")

print("_"*60)
#3). Python Loops program that will add the word from the user to the empty string using python.
word = str(input("Enter the word: "))
str1 = " "
for i in range(len(word)):
    str1 += word[i]
print(str1)

print("_"*60)

# 4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
# Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for a in numbers:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Count of even numbers are: {even}")
print(f"Count of odd numbers are: {odd}")

# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for i in range(0, 11):
    if i != 3 and i != 6:
        print(i, end=" ")

# 6). Write a program to get the Fibonacci series between 0 and 20 using python.
a, b = 0, 1
for _ in range(20):
    print(a, end=' ')
    a, b = b, a+b

print("_" * 60)
# 7). Write a program that iterates the integers from 1 to 30 using python.
# For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers that are multiples of both three and five print “FizzBuzz”.

for i in range(0, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

# 8)Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
# Input : “SqaTOOlS”
# Output : “sqatools”

HumanInput = str(input("Enter words in upper and lower case: "))
result = " "
for char in HumanInput:
    if char.isupper():
        print(char.lower(), end=" ")
    else:
        print(char, end=" ")

# 9). Python loops program that accepts a string and calculates the number of digits and letters using python.
# Input : “python1234”
# Output :
# Letters 6
# Digits 4
HumInput = str(input("Enter your alphanumeric value: "))
digit = 0
character = 0
for char in HumInput:
    if char.isalpha():
        character += 1
    elif char.isnumeric():
        digit += 1

print("Digits :", digit)
print("Character :", character)

# 10). Python for loop program to print the alphabet pattern ‘O’ using python.
# Output:
#    ***
# *       *
# *       *
# *       *
# *       *
# *       *
#    ***

print("_" * 60)
for i in range(1, 8):
    for j in range(1, 8):
        if (i == 1 and j == 3) or (i == 1 and j == 4) or (i == 1 and j == 5):
            print("*", end=" ")
        elif (i == 2 and j == 1) or (i == 2 and j == 7):
            print("*", end=" ")
        elif (i == 3 and j == 1) or (i == 3 and j == 7):
            print("*", end=" ")
        elif (i == 4 and j == 1) or (i == 4 and j == 7):
            print("*", end=" ")
        elif (i == 5 and j == 1) or (i == 5 and j == 7):
            print("*", end=" ")
        elif (i == 6 and j == 1) or (i == 6 and j == 7):
            print("*", end=" ")
        elif (i == 7 and j == 3) or (i == 7 and j == 4) or (i == 7 and j == 5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.


