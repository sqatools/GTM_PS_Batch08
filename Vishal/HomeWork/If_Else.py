
#program for calculator
"""
a = 10
b = 20
num1 = int(input("Enter value from 1 to 4:"))
if num1 == 1:
    print("Addition of a and b is", a+b)
elif num1 == 2:
    print("Subtraction of and b is", a-b)
elif num1 == 3:
    print("Multiplication of a and b is",a*b)
elif num1 == 4:
    print("Division of a and b is", a/b)
else:
    print("Incorrect choice")

"""
#Program 2

"""
num1 = 111

if num1%3==0:
    print("number is divisible by 3")
else:
    print("number is not divisible by 3")
"""

#Program 3

'''
for x in range(1, 31, 1):
    if x%3 == 0:
        print(x, end=' ')
'''
#Program 4

"""
x = 78
if x<40:
    print('You are failed')
elif 40<x<50:
    print('Grade C')
elif 50<x<60:
    print("Grade B")
elif 60<x<70:
    print("Grade A")
elif 70<x<100:
    print("Excellent")
elif x>100:
    print("invalid input")
"""

#Program 5
"""
x = int(input("Enter your number"))

if x%3 == 0 and x%5 == 0:
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")
"""
#Program 6

"""
x = int(input("Enter your number : "))

if x%11 == 0:
    print("Given number is divisible by 11 and its square is", x**2)
else:
    print("Given number is not divisible by 11")
"""

#Program 7
"""
x = int(input("Enter your number :"))
count = 0
for y in range (2, x//2):
    if x%y == 0:
        count = count + 1
        print(count, end=' ')
if count > 0:
    print("Number is not prime")
else:
    print("Number is prime")
"""

#Program 8

"""
x = int(input("Enter your number"))

list1 = [0, 1, 2, 3, 5, 8, 13]

if x in list1:
    print("Entered number is part of fibonacci series")
else:
    print("Entered number is not part of fibonacci series")

"""

#Program 9

"""
x = int(input("Enter your number: "))

if x%2 == 0:
    print("Square of given number is", x**2)
elif x%3 == 0:
    print("Cube of given number is", x**3)
else:
    print("Number is not divisible by 2 or 3")
"""

#Program 10
 """
x = int(input("Enter your 1st number :"))
y = int(input("Enter your 2nd number :"))

if x>y:
    print("the greater number is :", x)
else:
    print("the greater number is :", y)
"""
"""
print("__"*50)

for i in range(1, 7):
    for j in range(i):
        print("*", end=' ')

    print()

print("__"*50)

for i in range(7, 1, -1):
    for j in range(i-0):
        print("*", end=' ')

    print()

"""
