# write a python program to create a calculator

def add(v1, v2):
    print("addition :", v1 + v2)


def multiplication(v1, v2):
    print("multiplication :", v1 * v2)


def subtraction(v1, v2):
    print("subtraction :", v1 - v2)


def divide(v1, v2):
    print("division :", v1 // v2)


def calculator(operation, var1, var2):
    if operation == 1:
        add(var1, var2)
    elif operation == 2:
        multiplication(var1, var2)
    elif operation == 3:
        subtraction(var1, var2)
    elif operation == 4:
        divide(var1, var2)
    else:
        print("Invalid input")


calculator(1, 50, 60)
calculator(2, 2000, 60)
