# Home : Write a python program to create a calculator
"""
Take three input user, num1, num2, decision
if decision ==1 : add num1, num2
if decision ==2 : sub num1, num2
if decision ==3 : multi num1, num2
if decision ==4 : division num1, num2
if decision > 4 : invalid input

"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
play = str(input("Do you want to perform operations on numbers answer in yes/no: "))
if play == "yes":
    print("""What type of operations do you want to perform"
      decision =1 is for addition
      decision =2 is for subtraction
      decision =3 is for multiplication
      decision =4 is for division""")
    decision = int(input("Enter the number to perform operation on numbers: "))

    if decision == 1:
        num3 = num1+num2
        print("The sum of ", {num1}, "and ", {num2}, "is equal to: ", num3)
    elif decision == 2:
        num3 = num1 - num2
        print("The subtraction of ", {num1}, "and ", {num2}, "is equal to: ", num3)
    elif decision == 3:
        num3 = num1 * num2
        print("The multiplication of ", {num1}, "and ", {num2}, "is equal to: ", num3)
    elif decision == 4:
        num3 = num1 % num2
        print("The division of ", {num1}, "and ", {num2}, "is equal to: ", num3)
    else:
        print("This is invalid entry")
else:
    print("You are out of the Calculation program.... Play again next time")