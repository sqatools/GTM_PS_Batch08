print("If Else condition Problems")
print("-" * 50)
"""
1). Python program to check given number is divided by 3 or not.
"""
number = 9

if number % 3 == 0:
    print("number is divided by 3 is", number)
else:
    print("number is not divided by 3")

print("-" * 50)
"""
2). If else program to get all the numbers divided by 3 from 1 to 30.
"""
for i in range(1, 31):
    if i % 3 == 0:
        print("numbers divided by 3 from 1 to 30 is", i)

print("-" * 50)
"""
3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""
marks = 188
if marks < 40:
    print("Fail")
elif 40 > marks <= 50:
    print("grade C")
elif 50 < marks <= 60:
    print("grade B")
elif 60 < marks <= 70:
    print("grade A")
elif 70 < marks <= 80:
    print("grade A+")
elif 80 < marks <= 90:
    print("grade A++")
elif 90 < marks <= 100:
    print("grade Excellent")
else:
    print("Invalid marks")

print("-" * 50)
"""
4). Python program to check the given number divided by 3 and 5.
"""
number = 20

if (number % 3 == 0) and (number % 5 == 0):
    print("number is divisible by 3 and 5")
else:
    print("number is not divisible by 3 and 5")

print("-" * 50)
"""
5). Python program to print the square of the number if it is divided by 11.
"""
number = 144

if number % 11 == 0:
    print(f"square of the {number} is ", (number ** 2))
else:
    print("number not divisible by 11")

print("-" * 50)

"""
6). Python program to check given number is a prime number or not.
A prime number is a natural number greater than 1 that has only two factors: 1 and itself.
"""
number = 18
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

print("-" * 50)
"""
7). Python program to check given number is odd or even.
"""
number = 11
if number % 2 == 0:
    print(f"given number {number} is even number")
else:
    print(f"given number {number} is odd number")

print("-" * 50)
"""
8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, 
starting from 0 and 1.
"""
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

print()
print("-" * 50)
"""
9). Python program to check authentication with the given username and password.

USERNAME = "admin"
PASSWORD = "password123"

entered_username = input("Enter username: ")
entered_password = input("Enter password: ")


if entered_username == USERNAME and entered_password == PASSWORD:
    print("Login successful!")
else:
    print("Authentication failed! Invalid username or password.")
"""
print("-" * 50)
"""
10). Python program to validate user_id in the list of user_ids.

USERID = "Sankar_123"

entered_userid = input("Enter user ID: ")
if entered_userid == USERID:
    print("User ID validation done successfully")
else:
    print("User ID validation not done successfully")

"""
print("-" * 50)

"""
11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

"""
number = 13

if (number % 2 or number % 3) == 0:
    print(f"{number} is divided by 2 or 3")
else:
    print(f"{number} is not divided by 2 or 3")

print("-" * 50)

"""
12). Python program to describe the interview process.
"""
round1 = "pass"
round2 = "pass"
final_round = "fail"

if round1 == "pass":

    if round2 == "pass":

        if final_round == "pass":
            print("Congratulation you are selected")
        else:
            print("Your failed in final round, Better luck next time")
    else:
        print("Your failed in round 2, Better luck next time")
else:
    print("Your failed in round 1, Better luck next time")

print("-" * 50)
"""
13). Python program to determine whether a given number is available in the list of numbers or not.
"""
number = -4
list_nums = [i for i in range(1, 100)]

if number in list_nums:
    print(f"{number} available in the list")
else:
    print(f"{number} not available in the list")

print("-" * 50)
"""
14). Python program to find the largest number among three numbers.
"""
number = "123"

for i in number:
    if int(i) == int(max(number)):
        print("largest number is: ", i)
    else:
        pass
print("-" * 50)
""" 
15). Python program to check any person eligible to vote or not
age > 18+ : eligible
age < 18: not eligible
"""
age = 12
if age >= 18:
    print("Your eligible for Vote")
else:
    print("Your not eligible for Vote")

print("-" * 50)
"""
16). Python program to check whether any given number is a palindrome.
Input: 121
Output: palindrome
"""
Input = 1221
reversed_num = 0
original_num = Input
while original_num > 0:
    last_digit = original_num % 10
    reversed_num = reversed_num * 10 + last_digit
    original_num = original_num // 10

if Input == reversed_num:
    print(f"Given {Input} a palindrome")
else:
    print(f"Given {Input} not a palindrome")


print("-" * 50)
"""
17). Python program to check if any given string is palindrome or not.
Input: ‘jaj’
output = palindrome
"""
word = "hello"
palindrome = word[::-1]

if word == palindrome:
    print("Given word is a palindrome:", word)
else:
    print("Given word is not a palindrome:", word)


print("-" * 50)

"""
Solution 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students 
have passed the exam. Input = Enter marks: 45 Output = Pass
"""
marks = 35

if marks > 35:
    print("Pass")
else:
    print("Fail")

print("-" * 50)
"""
19). Python program to check whether the given number is positive or not.
Input = 20
Output = True
"""
num = 30
if num > 0:
    print(f"Given {num} is positive number")
else:
    print(f"Given {num} is negative number")

print("-" * 50)
"""
20). Python program to check whether the given number is negative or not.
Input = -45
Output = True
"""
num = -30
if num > 0:
    print(f"Given {num} is positive number")
else:
    print(f"Given {num} is negative number")

print("-" * 50)
"""
21). Python program to check whether the given number is positive or negative and even or odd.
Input = 26
Output = The given number is positive and even
"""
num = 26
if num > 0:
    if num % 2 == 0:
        print(f"Given {num} is positive and even number")
    else:
        print(f"Given {num} is positive and odd number")

else:
    if num % 2 == 0:
        print(f"Given {num} is negative and even number")
    else:
        print(f"Given {num} is negative and odd number")

print("-" * 50)
"""
22). Python program to print the largest number from two numbers.
Input:
25, 63
Output = 63
"""
nums = 65, 120

if nums[0] > nums[1]:
    print(f"In the {nums}, the largest number is {nums[0]}")
else:
    print(f"In the {nums}, the largest number is {nums[1]}")


print("-" * 50)
"""
23). Python program to check whether a given character is uppercase or not.
Input = A
Output = The given character is an Uppercase
"""
character = "H"

if character == character.upper():
    print(f"Given {character} is in uppercase")
else:
    print(f"Given {character} is in lowercase")
print("-" * 50)

