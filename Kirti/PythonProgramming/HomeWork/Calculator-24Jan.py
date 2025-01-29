# Home : Write a python program to create a calculator
"""
Take three input user, num1, num2, decision
if decision ==1 : add num1, num2
if decision ==2 : sub num1, num2
if decision ==3 : multi num1, num2
if decision ==4 : division num1, num2
if decision > 4 : invalid input

"""

num1= int(input("Enter number1:  "))
num2= int(input("Enter number2:  "))
decision= int(input("Enter decision:  "))
result=0

if decision == 1:
    result = num1+num2
elif decision == 2:
    result = num1 - num2
elif decision == 3:
    result = num1 * num2
elif decision == 4:
    result = num1 / num2
elif decision > 4:
    print("invalid input, please enter decision less than equal to 4")
else:
    print("invalid input, please enter decision between 1 to 4")
print("Result is : ", result)