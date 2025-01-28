#1.Write a program to create a calculator#

num1 = int(input("please enter a number1:"))
num2 = int(input("please enter a number2:"))
add = num1+num2
sub = num1-num2
mul = num1* num2
div = num1/ num2
decision = int(input("please enter a decision number:"))
if decision == 1:
    print("Add two numbers num1 and num2:", add)
elif decision == 2:
    print("substract two numbers num1 and num2:", sub)
elif decision == 3:
    print("Multiply two numbers num1 and num2:", mul)
elif decision == 4:
    print("Divide num1 and num2:", div)
else:
    print ("Invalid Decision")