"""
if condition:
    code
else:
    code
"""
print("_"*50)
# check given numbers are equal or not
a = 40
b = 60


if a == b :
    # if condition is True
    print("Number are equal :", a , b)
else:
    # if condition is False
    print("Number are not equal :", a, b)


print("Condition output:", a == b)

print("_"*50)
# write a program to check given number is even or odd
# if any number can be divisible by 2 than it is even or odd number
#
"""
Note : input function accepts the values in string format, we have to convert as per requirements
"""
"""
num1 = int(input("Please  Enter the Value:"))
var1 = 2
print("Condition output: ",num1%var1)

if (num1 % 2) == 0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)
"""
"""
Home Work.

#1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the
number

"""

##### -----24-01-2025 ---------
"""
Logical Operators
 > : greater than
 < :  Less than
 >= : greater than equal
 <= : less than equal
 != : not equal
 == : equal to operator
 in : in operator
 is : is operator
 is not : is operator

 AND Logic
 True and False : False
 False and True : False
 False and False : False
 True and True : True

 OR Logic
 True or False : True
 False or True : True
 True or True : True
 False or False : False

"""

"""
if cond1 :
    code
elif cond2:
    code
elif cond3:
    code
else:
    code
"""
"""
# write a python program to check greater number among three values

a = 200
b = 200
c = 20

if a > b and a > c:
    print("A has greater value :", a)
elif b > a and b > c:
    print("B has greater value :", b)
elif c > a and c >  b:
    print("C has greate value :", c)
elif a == b == c:
    print("A, B, C has equal values")
elif a == b != c:
    print("A, B has equal values")
else:
    print("No one has greater value")



print("_" * 50)
# write a python program to provide the grade to the students as per marks obtained.
marks = 45

if 35 < marks <= 50:
    print("Passed with C grade")
elif marks > 50 and marks <= 70:
    print("Passed with B Grade")
elif marks > 70 and marks <= 90:
    print("Passed with A grade")
elif marks > 90 and marks <= 100:
    print("Password Excellent Grade A++")
elif marks > 100:
    print("Invalid value, marks can not be more than 100")
elif marks < 0:
    print("invalid marks, value should be positive")
else:
    print("Failed in Exam, better luck next time")

print("_" * 50)
# write a python program to check the given number is divisible by 3 or 7
A = 30
if (A % 3 == 0 or A % 7 == 0) and A % 5 == 0:
    print("A is divisible by 3 or 7")
else:
    print("A is not divisible by 3 or 7")

# Home : Write a python program to create a calculator


Take three input user, num1, num2, decision
if decision ==1 : add num1, num2
if decision ==2 : sub num1, num2
if decision ==3 : multi num1, num2
if decision ==4 : division num1, num2
if decision > 4 : invalid input

"""
"""
"""

print("_____calculator_____")
num1 = float(input("please enter 1st Number : "))
num2 = float(input("please enter 2nd Number : "))
decision = int(input("Please enter your choice 1: Add, 2: Subtract, 3: Multiply, 4: Divide " ))

if decision == 1:
    result = num1 + num2
    print("Addition is:", result)
elif decision == 2:
    result = num1 - num2
    print("Subtraction is:", result)
elif decision == 3:
    result = num1 * num2
    print("Multiplication is:", result)
elif decision == 4:
    result = num1 / num2
    print("Division is:", result)
else:
    print("Invalid Choice, Please Enter valid Selection from 1 to 4")




