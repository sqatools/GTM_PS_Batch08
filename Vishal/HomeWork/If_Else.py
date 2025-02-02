
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


