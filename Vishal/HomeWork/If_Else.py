
#program for calculator

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
