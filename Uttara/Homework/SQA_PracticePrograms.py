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

#12. Python program to accept two numbers and mathematical operations from users and perform mathematical operations according to it.
"""Input:
A=30
B=45
Operation = +
Output = 75"""

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operation = input("Enter operation of your choice")

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "/":
    print(num1/num2)
elif operation == "*":
    print(num1*num2)
else:
    print("Invalid operation")

"""13.Python program to accept the temperature in Fahrenheit and check whether the water is boiling or not.
Hint: The boiling temperature of water in Fahrenheit is 212 degrees
Input = Enter temperature: 190
Output = Water is not boiling
code:"""

temp = int(input("Enter temperature of water in Fahrenheit: "))

if temp != 212:
    print("Water is not boiling")
else:
    print("Water is boiling")

"""14.Python program to accept the city name and display its monuments (take Pune and Mumbai as cities).
Input = Enter city name: Pune
Output:
Shaniwar vada
Lal mahal
Sinhgad fort
code:"""
city = input("Enter city name: ").lower()

if city == "pune":
    print("Shaniwar vada\nLal mahal\n")
    print("Sinhgad fort")
elif city == "mumbai":
    print("Getway of India\nGandhi statue\nAjanta cave")
else:
    print("Invalid city")


"""15.Python program to check the student’s eligibility to attend the exam based on his/her attendance. If attendance is greater than 75% eligible if less than 75% not eligible.
Input = Enter attendance: 78
Output = You are eligible"""

attendance = int(input("Enter attendance % of a student: "))
if attendance >= 75:
    print("Student is eligible")
else:
    print("Student is not eligible")

#16. A shop will give a 10% discount if the bill is more than 1000, and 20% if the bill is more than 2000. Using the python program Calculate the discount based on the bill.

bill = int(input("Enter bill amount: "))
discount = 0

if bill >= 2000:
    discount = 20*(bill/100)
elif 1000<= bill < 2000:
    discount = 10*(bill/100)

print("Discount amount: ",discount)

#17. Find the lowest number between three numbers.

num1 = 70
num2 = 23
num3 = 68

if num1<num2:
    if num1<num3:
        print("Lowest numbner: ",num1)
elif num2<num1:
    if num2<num3:
        print("Lowest numbner: ",num2)
else:
    print("Lowest number: ",num3)
