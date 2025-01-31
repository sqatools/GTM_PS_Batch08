################################################################################################
# Home : Write a python program to create a calculator
"""
Take three input user, num1, num2, decision
if decision ==1 : add num1, num2
if decision ==2 : sub num1, num2
if decision ==3 : multi num1, num2
if decision ==4 : division num1, num2
if decision > 4 : invalid input

"""
decision = int(input("Enter the value from 1 to 4: "))
num1 = float(input("Enter the value of num1: "))
num2 = float(input("Enter the value of num1: "))

if decision == 1:
    print("1. Addition", num1+num2)
elif decision == 2:
    print("2. Subtraction", num1 - num2)
elif decision == 3:
    print("3. Multiplication", num1 * num2)
elif decision == 4:
    print("1. Division", num1 / num2)
else:
    print("Invalid Input")

