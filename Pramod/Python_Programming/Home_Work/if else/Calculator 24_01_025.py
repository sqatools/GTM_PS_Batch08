# Home : Write a python program to create a calculator
"""
Take three input user, num1, num2, decision
if decision ==1 : add num1, num2
if decision ==2 : sub num1, num2
if decision ==3 : multi num1, num2
if decision ==4 : division num1, num2
if decision > 4 : invalid input

"""
"""
num1 =10
num2 =20
decision=2
"""
num1=int(input("Enter the num1 value"))
num2=int(input("Enter the num2 value"))
decision= int(input("Enter the value"))


if decision ==1:
    print ("adding two numbers 10+20=", num1+num2)
elif decision ==2:
    print("subtraction two numbers 10-20=", num1-num2)

elif decision ==3:
    print("Multiplication two numbers 10*20=", num1*num2)
elif decision ==4:
    print("Division two numbers 10%20=", num1%num2)
else:
    decision >4
    print("invalid output")

## Output: subtraction two numbers 10-20= -10
