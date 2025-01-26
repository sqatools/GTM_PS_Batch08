
# Home : Write a python program to create a calculator
"""
Take three input user, num1, num2, decision
if decision ==1 : add num1, num2
if decision ==2 : sub num1, num2
if decision ==3 : multi num1, num2
if decision ==4 : division num1, num2
if decision > 4 : invalid input

"""
#25Jan2025

print("="*50)

decision = int(input("Enter the valid decision number from 1 to 4 to perform calculator operation: "))

if decision >0 and decision <5:
    num1 = int(input("Enter any number num1: "))
    num2 = int(input("Enter any number num2: "))

    if decision == 1:
        print("Decision 1 is to perform addition")
        add = num1 + num2
        print("The addition result is: ",num1, "+",num2,"=", add)
    elif decision ==2:
        print("Decision 2 is to perform substraction")
        sub = num1 - num2
        print("The substraction result is: ",num1, "-",num2,"=", sub)
    elif decision ==3:
        print("Decision 3 is to perform multiplication")
        mul = num1 * num2
        print("The multiplication result is: ",num1, "*",num2,"=", mul)
    elif decision ==4:
        print("Decision 4 is to perform division")
        div = num1/num2
        print("The division result is: ",num1, "/",num2,"=", div)
    else:
        print("Happy coding")
elif decision < 1 or decision > 4:
    print("Invalid decision input, please enter the valid decision number from 1 to 4")
else:
    print("Happy calculation")


