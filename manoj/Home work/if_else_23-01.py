# homework

# write a python program to check given number is divisible by 3 or not
num1 = 83
var1 = 3
if num1%var1 == 0:
    print("number is divisible :", num1)
else:
    print("number is not divisible :", num1)  # number is not divisible : 83



# write a python print square(n**2) if number is even or print cube(n**) if number is odd

num1 = 4
var1 = 2
print("condition output :", num1%var1)

if num1%var1 == 0:
    print("output :", num1**2)
else:
    print("output :", num1**3)

# write a python program to check given positive or negative
num3 = 0
var3 = 0
if num3 > 0 :
    print("given number is positive :", num3)
else:
    print("given number is negative :", num3)


# write a python program Check whether the number is divisible by 3
num = 3
if num%3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")
# Number is divisible by 3


# write a Program to get all numbers divided by 3 between 1 to 30
for i in range(1,31):
    if i%3 == 0:
        print(i,end=" ")  # 3 6 9 12 15 18 21 24 27 30



# write a Program to get all numbers divided by 3 between 10 to 35
for i in range(10,37):
    if i%3 == 0:
        print(i,end=" ")  # 3 6 9 12 15 18 21 24 27 30 12 15 18 21 24 27 30 33 36


#  write a Python program to check the given number divided by 3 and 5.

num = 16
# Check for division
if num%3 == 0  and num%5 == 0:
    print("Given number can divide by both 3 and 5")

else:
    print("Given number can not divide by 3 and 5")  # Given number can not divide by 3 and 5

# write a python program to print the square of the number if it is divided by 11.

num = 22
# Check for division
if num%11 == 0:
    print(num**2)
else:
    print("Number is not divisible by 11")

# 484

# write a Program to check whether the number is a prime number
num = 56
count = 0

for i in range(2,num):

    if num%i == 0:
        count += 1

if count > 0:
    print("It is not a prime number")
else:
    print("It is a prime number")
# It is not a prime number


# write a Python program to check given number is odd or even
num = 7
if num%2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")
# It is an odd number

# write a Python program to check authentication with the given username and password
name = 124
password = 123456
if name == password:
    print("It is valid")
else:
    print("It is not valid")
# It is not valid


# Find the largest number among three numbers
num1 = 12
num2 = 13
num3 = 14

if num1>num2:
    if num1>num3:
        print(f"{num1} is the greatest")
    else:
        print(f"{num3} is the greatest")
else:
    if num2>num3:
        print(f"{num2} is the greatest")
    else:
        print(f"{num3} is the greatest")  # 14 is the greatest

# Find the smallest number among three numbers

num1 = 12
num2 = 13
num3 = 14

if num1<num2:
    if num1<num3:
        print(f"{num1} is the smallest") # 12 is the smallest
    else:
        print(f"{num3} is the smallest")
else:
    if num2>num3:
        print(f"{num2} is the smallest")
    else:
        print(f"{num3} is the smallest")


#  Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible

age = 30

if age >= 18:
    print("You are eligible") # You are eligible
else:
    print("You are not eligible")

#  Python program to check whether a student has passed the exam. If marks are greater than 35 students
#  have passed the exam.

marks = 50
if marks>=45:
    print("Pass")  # pass
else:
    print("Fail")

# Python program to check whether the given number is positive or not.
num = 28

if num>0:
    print("True") # true
else:
    print("False")


# Python program to check whether the given number is negative or not
num = 38

if num<0:
    print("True")
else:
    print("False") # false


# Print the largest number from two numbers.
num1 = 66
num2 = 65
if num1>num2:
    print(f"{num1} is greatest") # 65
else:
    print(f"{num2} is greatest")


# # Print the smallest number from two numbers.

num1 = 66
num2 = 65
if num1<num2:
     print(f"{num1} is smallest") # 65
else:
     print(f"{num2} is smallest")

#  Python program to check whether the given character is lowercase or not.
char = 'c'
if char.islower():
    print("True")  # True
else:
    print("False")
