"""
def function_name():
    code

"""


def greeting():
    print("Hello Good Morning")


# call the function
greeting()

print("_" * 50)


############################################
# function with parameters
def addition(n1, n2):
    print("value of n1 :", n1)
    print("value of n2 :", n2)
    print("addition of number :", n1 + n2)


# There are 2 ways to pass value to the function
# 1. PASS BY VALUE
addition(50, 60)
# _____________________
print("_" * 50)
addition(n1=70, n2=80)
print("_" * 50)
# _____________________
# if we are using parameter name, then can change the order of value as well with the help
# param names.
addition(n2=100, n1=90)

# _____________________
print("_" * 50)
addition([4, 6, 7], [8, 1, 4])  # [4, 6, 7, 8, 1, 4]
addition('Hello', 'Python')  # HelloPython

# addition(n2=200)
# TypeError: addition() missing 1 required positional argument: 'n1'

# #_____________________
# 2. PASS BY REFERENCE :  when we pass difference variables in function calling instead of value, then
#                         it is called pass by reference.

x = 500
y = 600
addition(x, y)  # 1100

l1 = [4, 5, 7]
l2 = [6, 9, 10]
addition(l1, l2)  # [4, 5, 7, 6, 9, 10]

id(list)

print("_" * 50)


##################### function parameters with data type ##############

def multiplication(v1: int, v2: int):
    """
    This function help to multiply integer values and print it.
    :param v1: first parameter value
    :param v2: second parameter value
    :return : None
    """
    print("multiplication  :", v1 * v2)


# program will execute without any issue
multiplication(50, 5)
# multiplication  : 250

# program will execute with warning in program file.
multiplication('Python', 5)  # PythonPythonPythonPythonPython

print("_" * 40)


########### function with return data ################

# # function with single return value
def greeting_msg(name):
    return f"Hello {name}, good morning"


val1 = greeting_msg('Rahul')
print("return val :", val1)  # Hello Rahul, good morning


# function with multiple return value
def math_operation(n1, n2):
    add = n1 + n2
    multi = n1 * n2
    sub = n1 - n2
    div = n1 // n2
    return add, multi, sub, div


# store multiple return value in one variable
result = math_operation(10, 5)
print("return values :", result)
# return values : (15, 50, 5, 2)

# store multiple return value in different variable
a, b, c, d = math_operation(40, 15)
print("addition output :", a, a**2)
print("multiplication output :", b, b**3)
print("subtraction output :", c, c**4)
print("division output :", d, d**5)


print("_"*50)
print(math_operation(50, 10))


"""
# Home work
1. write a python function to get max value from list
2. write a python function to return factorial value of number number
5 = 120 : 5*4*3*2*1
3. Write a python function to calculate the number of consonants in given string.
str1= "Hello We are Learning Python" # output = 16
"""
