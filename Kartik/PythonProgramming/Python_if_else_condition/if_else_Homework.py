"""
Home Work.

#1). write a python program to check given number is divisible by 3 or not.
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd.
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the number.

"""
print("_"*100)
"""
#1). write a python program to check given number is divisible by 3 or not

num1 = int(input("Enter the number:"))

if (num1%3) == 0:
    print("This number is divisible by 3 :" , num1)
else:
    print("This number is  not divisible by 3 :", num1)

"""
print("_"*100)
"""

#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd

num2 = int(input("Enter the number:"))

if (num1%2) == 0:
    print("The number is even so square of this number is :" , num2**2 )
else:
    print("The number is odd so qube of this number is :", num2 ** 3)
    
"""
print("_"*100)
"""

#3). write a python program to check given  number is positive or negative.

num1 = float(input("Please Enter the Number"))

if num1 > 0:
    print("This is a postive number:", int(num1))
else:
    print("This is a Negative number:", int(num1))
    
"""
print("_"*100)
"""
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the number.

val1 = int(input("Please enter any number:"))
val2 = val1 % 7
val3 = val1 + 50
val4 = val1 - 50

print("divison output:", val2)

if val2 == 0:

    print("This is divisible  by number 7")
    print("the new number is :", val3)
else:

    print("This is not divisible  by number 7")
    print("the new number is :", val4)
"""
print("_"*100)
"""
# 5). Home : Write a python program to create a calculator

Take three input user, num1, num2, decision
if decision ==1 : add num1, num2
if decision ==2 : sub num1, num2
if decision ==3 : multi num1, num2
if decision ==4 : division num1, num2
if decision > 4 : invalid input
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



