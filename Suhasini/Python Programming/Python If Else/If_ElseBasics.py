"""
if Condition:
    code
else:
    code
"""

print("If Else Basics")
print("-"*30)
#1. Check if the numbers are equal or not
print("1. Program to check if the numbers are equal")
a = 40
b = 55

if a == b:
    print("a and b are equal")
else:
    print("Numbers are not equal")

print("-"*80)

# write a program to check given number is even or odd
print("2. Program to check if a number is even or odd")

num1 = int(input("Please enter a number"))

if num1 % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

print("_"*80)

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

# write a python program to check greater number among three values

a = 25
b = 36
c = 12

if a > b and a > c:
    print("a is the greatest of all 3 numbers")
elif b > a and b > c:
    print("b is the greatest of all 3 numbers")
elif c > a and c >  b:
    print("C has greate value :", c)
elif a == b == c:
    print("A, B, C has equal values")
elif a == b != c:
    print("A, B has equal values")
else:
    print("No one has greater value")

print("_"*80)

# write a python program to provide the grade to the students as per marks obtained.

marks = int(input("Please enter marks"))

if 35 < marks <= 50:
    print("Passed with C grade")
elif marks >50 and marks <=70:
    print("Passed with B Grade")
elif marks > 70 and marks <=90:
    print("Passed with A grade")
elif marks > 90 and marks <= 100:
    print("Password Excellent Grade A++")
elif marks > 100:
    print("Invalid value, marks can not be more than 100")
elif marks < 0:
    print("invalid marks, value should be positive")
else:
    print("Failed in Exam, better luck next time")

print("_"*80)

# write a python program to check the given number is divisible by 3 or 7
A = 50
if A%3 == 0 or A%7 == 0:
    print("A is divisible by 3 or 7")
else:
    print("A is not divisible by 3 or 7")

print("_"*80)

