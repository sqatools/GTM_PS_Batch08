# write a python program to check greater number among three values

"""
a = int(input("Please enter value of a :"))
b = int(input("Please enter value of b :"))
c = int(input("Please enter value of c :"))


if a > b and a > c:
    print("A is greatest among all,", a)
elif b > c and b > a:
    print("B is greatest among all,", b)
elif c > a and c > a:
    print ("C is the greatest among all,",c)
"""


# write a python program to provide the grade to the students as per the marks obtained.

""" 
marks = int(input("please enter your marks:"))

if marks >= 35 and marks < 50:
    print(" Congratulations you have passed the exam with grade C")
elif marks >= 50 and marks < 75:
    print("Congratulations you have passed the exam with grade B")
elif marks >= 75 and marks < 90:
    print(" Congratulations you have passed the exam with grade A")
elif marks >= 90 and marks <= 100:
    print(" Congratulations you have passed the exam with grade A+")
elif marks < 35:
    print("Better luck next time")


"""

# Home : Write a python program to create a calculator
"""
Take three input user, num1, num2, decision
if decision ==1 : add num1, num2
if decision ==2 : sub num1, num2
if decision ==3 : multi num1, num2
if decision ==4 : division num1, num2
if decision > 4 : invalid input


num1 = float(input("please enter 1st Number"))
num2 = float(input("please enter 2nd Number:"))
decision = int(input("Please enter your choice 1: Add, 2: Subtract, 3: Multiply, 4: Divide))

if decision == 1:
print("Addition:", int(num1 + num2))
