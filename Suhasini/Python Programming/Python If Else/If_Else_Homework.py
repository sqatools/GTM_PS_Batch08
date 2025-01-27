
# Date : 23/ 01/ 2025

#1). write a python program to check given number is divisible by 3 or not
print("1. Program to check if a number is divisible by 3")

num1 = int(input("Enter a number"))
if num1 % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

print("_"*80)

#2). write a python program to print square(n**2) if number is even or print
# cube(n**3) if number is odd
print("2. Program to print square of the number if that number is even else print cube of the number")

num2 = int(input("Please enter a number"))

if num1 % 2 == 0:
    print("The number is even")
    print("Square of the number is:", num2**2)
else:
    print("The number is odd")
    print("Cube of the number is: ", num2**3)

print("_"*80)

#3). write a python program to check if a given number is positive or negative.
print("3. Program to check if a number is positive or negative")

num3 = int(input("Please enter a number"))

if num3 > 0:
    print("The number is Positive")
elif num3 < 0:
    print("The number is Negative")
else:
    print("Enter a value other than 0")

print("_"*80)

#4).  Check given number is divisible by 7 then add 50 to the number else subtract 50 from the
#number
print("4. Program to add 50 to the number if its divisible by 7 else subtract 50 from the number")

num4 = int(input("Please enter a number"))

if num4 % 7 == 0:
    print("Entered number is divisible by 7 so adding 50 to it :", num4+50)
else:
    print("Entered number is not divisible by 7 so subtracting 50 from it: ",num4-50)

print("_"*80)

##################### Home work - Date : 24/01/2025  ####################

# Home : Write a python program to create a calculator
"""
Take three input from user: num1, num2, decision
if decision ==1 : add num1, num2
if decision ==2 : sub num1, num2
if decision ==3 : multi num1, num2
if decision ==4 : division num1, num2
if decision > 4 : invalid input
"""

num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
dec = float(input("Enter your decision: 1.Add 2.Subtract 3.Multiply 4.Divide"))

if dec == 1:
    result = num1+num2
    print("Value after adding 2 numbers is: ", result)
elif dec == 2:
    result = num1 - num2
    print("Value after subtracting numbers is: ", result)
elif dec == 3:
    result = num1 * num2
    print("Value after multiplying the numbers is: ", result)
elif dec == 4:
    result = num1 / num2
    print("Value after dividing the numbers is: ", result)
else:
    print("Decision value should be raging from 1-4 only")
