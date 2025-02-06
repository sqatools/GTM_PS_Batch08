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
print("4. Program to add 50 to the number if it is divisible by 7 else subtract 50 from the number")

num4 = int(input("Please enter a number"))

if num4 % 7 == 0:
    print("Entered number is divisible by 7 so adding 50 to it :", num4+50)
else:
    print("Entered number is not divisible by 7 so subtracting 50 from it: ",num4-50)

print("_"*80)

##################### Homework - Date : 24/01/2025  ####################

# 5. Write a python program to create a calculator

# Take three input from user: num1, num2, decision
# if decision ==1 : add num1, num2
# if decision ==2 : sub num1, num2
# if decision ==3 : multi num1, num2
# if decision ==4 : division num1, num2
# if decision > 4 : invalid input

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


################### Practice Programs #########################

# 6. Python program to check the given number divided by 3 and 5

print("Program to check the given number divided by 3 and 5")
num = int(input("Enter a number"))

if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by 3 and 5")
print("_"*80)


# 7. Python program to print the square of the number if it is divided by 11

print("Program to print the square of the number if it is divided by 11")
num = int(input("Enter a number"))

if num % 11 == 0:
    print("Number is divisible by 11")
    print("Square of the number is: ",num**2)
else:
    print("Number is not divisible by 11")
print("_"*80)


# 8. Python program to check given number is a prime number or not

print("Program to authenticate if user name and password are correct")
uname1 = "suhasini@gmail.com"
password1 = "123456"
uname = input("Enter your name")
password = input("Enter your password")

if uname1 == uname and password1 == password:
    print("Entered username and password are valid")
else:
    print("Entered username and password are invalid")
print("_"*80)


# 9. Python program to validate user_id in the list of user_ids
print("Python program to validate user_id in the list of user_ids")

userid_ls = ["suhasini", "sanusha", "gia", "pooja", "junnu", "bujji", "guru"]
userid = input("Enter a user id that you want to check if it exists")

if userid in userid_ls:
    print("Entered user id is present in list")
else:
    print("Entered user id is not present in the list")

print("_"*80)


# 10. Python program to accept two numbers and mathematical operations from users and
# perform mathematical operations according to it.

print("Python program to accept two numbers and mathematical operations from users and perform mathematical operations according to it.")

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
ope = input("Enter the operator based on what operation you would like to perform on numbers")

if ope == '+':
    print("Addition of 2 numbers is: ",num1+num2)
elif ope == '-':
    print("Subtraction of 2 numbers is: ",num1-num2)
elif ope == '*':
    print("Multiplication of 2 numbers is: ",num1*num2)
elif ope == '/':
    print("Division of 2 numbers is: ",num1/num2)
else:
    print("Invalid operator! Enter any operator from 1.+ 2.- 3.* 4./ ")
print("_"*80)


# 11. Python program to accept the temperature in Fahrenheit and check whether the
# water is boiling or not.
# Hint: The boiling temperature of water in Fahrenheit is 212 degrees

print("program to accept the temperature in Fahrenheit and check whether the water is boiling or not")

temp = int(input("Enter temperature in Fahrenheit"))

if temp > 212:
    print("Water is boiling")
else:
    print("Water is not boiling")

print("_"*80)


# 12. Python program to check whether a given year is a leap or not

print("Python program to check whether a given year is a leap or not")

year = int(input("Enter the year to check if it is leap or not"))

if (year%100 != 0 or year%400 == 0) and year%4 == 0:
    print(year," is leap year")
else:
    print(year," is not leap year")
print("_"*80)


# 13. Python program to print all the numbers from 10-15 except 13

print("Python program to print all the numbers from 10-15 except 13")

print("The numbers are: ")
for i in range(10,16):
    if i != 13:
        print(i)
print("_"*80)


# 14. Python program to check whether the given input is a string or not.
print("Python program to check whether the given input is a string or not")

str1 = "Python"
if type(str1) == str:
    print("String is entered")
else:
    print("String is not entered")
print("_"*80)


# 15. Python program to check whether the given character is lowercase or not
print("Python program to check whether the given character is lowercase or not")

char1 = input("Enter a character")

if char1.islower():
    print("Entered character is lowercase")
else:
    print("Entered character is not lowercase")
print("_"*80)


# 16. Python program to print the largest number from two numbers.
print("Python program to print the largest number from two numbers.")
num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

if num1>num2:
    print(num1," is greater number")
else:
    print(num2," is greater number")
print("_"*80)


# 17. Python program to check a given number is part of the Fibonacci series from 1 to 10
print("Python program to check a given number is part of the Fibonacci series from 1 to 10")

fib = [0, 1, 1, 2, 3, 5, 8]
num = int(input("Enter a number between 1-10"))

if num in fib:
    print("Entered number is in Fibonacci series")
else:
    print("Entered number is not in the Fibonacci series")

print("_"*80)


# 18. Python program to accept marks from the user allot the stream based on the following criteria.
# Marks>85: Science
# Marks>70: Commerce
# 35<Marks<70: Arts
# Marks<35: Fail

print("Program to accept marks and accordingly allot a stream")
marks= int(input("Enter the marks"))

if marks > 85 and marks <= 100:
    print("Marks is:", marks)
    print("Stream allocated is : SCIENCE")
elif marks <= 85 and marks > 70:
    print("Marks is:", marks)
    print("Stream allocated is : COMMERCE")
elif marks >= 35 and marks <= 70:
    print("Marks is:", marks)
    print("Stream allocated is : ARTS")
elif marks < 35 and marks >= 0:
    print("Marks is:", marks)
    print("Student has failed! Better luck next time")
else:
    print("Invalid marks")
print("_"*80)


# 19. Python program to determine whether a given number is available in the list of numbers or not

print("Python program to determine whether a given number is available in the list of numbers or not")

num_ls = [23, 34, 434, 67, 87, 23, 87, 89]
num = int(input("Enter a number that you want to check if it exists"))

if num in num_ls:
    print("Entered number is present in list")
else:
    print("Entered number is not present in the list")
print("_"*80)


# 20. Python program to check if a number is prime
print("Program to check if a number is prime")
num = int(input("Enter a number"))
count = 0

for i in range(2,num):
    if num % i == 0:
        count+= 1
 
if count > 0:
    print("Number is not prime")
else:
    print("Number is prime")
print("_"*80)
