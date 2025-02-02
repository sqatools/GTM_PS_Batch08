# SQA 20 Programs
# 1.Write a python program to check whether person eligible for voting or not#
age = int(input("Enter a age: "))
if age >= 18:
    print("Person is eligible for voting")
else:
    print("Person is not eligible for voting")

"""Enter a age: 20
Person is eligible for voting 
Enter a age: 11
Person is not eligible for voting"""
print("*" * 100)

# 2.Write a Python program to print the square of the number if it is divided by 11.

num = int(input("Enter a number: "))
if num % 11 == 0:
    print("Square of the number", num * 2)
else:
    print("Number is not divisible by 11")

"""Enter a number: 80
Number is not divisible by 11"""
print("*" * 100)

#P3.if else program to assi5gn grade as per total marks:
"""Mark> 40:fail
mark 40-50:Grade C
mark 50-60:Grade B
mark 60-70:Grade A
mark 70-80:Grade A+
mark 80-90:Grade A++
mark 90-100:Grade Excellent
mark>100:Invalid Marks """

marks = int(input("Enter a Marks: "))
if marks < 40:
    print("You are Fail")
elif marks >= 40 and marks <= 50:
    print("Having Grade C")
elif marks >= 50 and marks <= 60:
    print("Having Grade B")
elif marks >= 60 and marks <= 70:
    print("Having Grade A")
elif marks >= 70 and marks <= 80:
    print("Having Grade A+")
elif marks >= 80 and marks <= 90:
    print("Having Grade A++")
elif marks >=  90 and marks <= 100:
    print("Excellent")
elif marks > 100:
    print("Invalid marks")
else:
    print("Invalid value")
print("*"*100)

#4.To check Authantication with the given Username and password

username = input("Enter a Username: ")
password = input("Enter a Password: ")
if username == "1abc" and password == "Hello":
    print("Login Authenticate")
else:
    print("Invalid username or password")
print("*"*100)
"""Enter a Username: dfr
Enter a Password: rrrrrr
Invalid username or password"""

#5.program to determine whether a given number is available in the list of numbers or not.

lis = [10,20,30,40,50,60,70]
numbr = int(input("Enter a number: "))

if numbr in lis:
    print("Number is available in the list")
else:
    print("Number is not available in the list")

"""Enter a number: 33
Number is not available in the list"""
print("*"*100)

#6.find the largest number among three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2:
    if num1 > num3:
        print("Number is the greatest")
    else:
        print("Number is the greatest")
else:
    if num2 > num3:
        print("Number is the greatest")
    else:
        print("number is the greatest")

print("*"*100)

#7. Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.

marks = int(input("Enter marks of a student: "))
if marks >= 45:
    print("Pass")
else:
    print("Fail")

print("*"*100)

#8.Write a python program to print the largest number from two numbers.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 > num2:
    print("Number is Larger")
else:
    print(" No negetive number allowed")

#9.Python program to check whether a given character is uppercase or not.
char = input("Enter a character: ")
if char.isupper():
    print("Uppercase character")
else:
    print("Not in Uppercase")

print("*"*100)

#10.Python program to check whether the given character is lowercase or not.
char = input("Enter a character: ")

if char.islower():
    print("Lowercase")
else:
    print("Not in Lowercase")

print("*"*100)

#11.WAP to print all numbers from 10-15 except 13
for i in range(10 ,16):
    if i!=13:
        print(i)
print("*"*100)

