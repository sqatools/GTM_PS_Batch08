"""
def function_name():
    code

def: This keyword is used to define a function.
function_name: This is the name of the function, which follows standard naming conventions.
parameters: These are optional inputs that the function can accept. You can have zero or more parameters.
return: The return statement is optional. It defines the value that the function will return to the caller.

"""

print("_" * 70)


def greet():
    print("Hello all ! welcome to python coding.")


greet()  # below is way to call function

print("_" * 70)


############################ Function with parameter ############################################
def addition(n1, n2):
    print("Value of n1: ", n1)
    print("Value of n2: ", n2)
    print(n1 + n2)


addition(100, 200)

############################ Two way to pass the value ############################################
# 1. PASS BY VALUE
addition(300, 400)

print("_" * 70)
addition(n1=300, n2=900)  # this way we can change the order of value
print("_" * 70)
addition([1, 2, 3, 4], [2, 3, 4, 5])  # [1, 2, 3, 4, 2, 3, 4, 5]
addition("pankaj", "prasad")  # pankajprasad

# 2. PASS BY REFERENCE
x = 400
y = 500
addition(x, y)

print("_" * 70)


############################### function parameter with data type ##############################
# 1. function with single return value
def name_print(name):
    return f"hello {name}, good morning"


val1 = name_print("pankaj prasad")
print(val1)


# function with multiple return value
def math_function(n1, n2):
    add = n1 + n2
    mul = n1 * n2
    sub = n2 - n1
    div = n1 // n2
    return add, mul, sub, div


val2 = math_function(200, 100)
print("return value: ", val2) # (300, 20000, -100, 2), multiple value will be return in form of tuple

# store multiple value in different variable
a, b, c, d = math_function(40, 50)
print("Addition: ", a)
print("Multiplication: ", b)
print("Subtraction: ", c)
print("Division: ", d)

print("_"*70)
print(math_function(70, 40))

"""
# Home Work
1. Write python function to get max value from list.
2. write python function to return factorial value of number
   5=120: 5*4*3*2*1
3. Write python function to calculate the number of constants in given string.
str1 = "Hello we are learning python" # output = 16

"""
