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
print("return value: ", val2)  # (300, 20000, -100, 2), multiple value will be return in form of tuple

# store multiple value in different variable
a, b, c, d = math_function(40, 50)
print("Addition: ", a)
print("Multiplication: ", b)
print("Subtraction: ", c)
print("Division: ", d)

print("_" * 70)
print(math_function(70, 40))

"""
# Home Work
1. Write python function to get max value from list.
2. write python function to return factorial value of number
   5=120: 5*4*3*2*1
3. Write python function to calculate the number of constants in given string.
str1 = "Hello we are learning python" # output = 16

"""
print("_" * 70)
# write a python program to get square of each value in list.

list1 = [4, 5, 6, 7, 8, 9]


def get_square(li):
    output = []
    for val in li:
        output.append(val ** 2)
    return output


final_square_value = get_square(list1)
print(final_square_value)

print(get_square(list1))

list2 = [9, 8, 7]
print(get_square(list2))

print("_" * 70)


######################## Function with default parameter value ################################
# Note *:  default value will always comes at last position
def addition_multiple_value(n1, n2, n3=40):
    add = n1 + n2 + n3
    print("Addition: ", add)
    return add


# if we dont provide value in method it will take default value
addition_multiple_value(20, 30)
# if we provide value inside method it will override the default value
addition_multiple_value(10, 20, 30)

print("_" * 70)


######################## specific return type of the function ######################
def add_words(w1, w2) -> str:
    return int(w1) + int(w2)


# value = add_words("pankaj", "prasad")
# print(value)
value1 = add_words(20, 70)
print(value1)

print("_" * 70)


##########################
# 1. function with *args parameter
# *args parameter accept n number of value while calling the function
# it accepts value in form of tuple

def get_sum_of_values(var1, *args):
    sum1 = 0
    for val in args:
        sum1 += val
    print("Sum of all values: ", sum1)


get_sum_of_values(4, 5)
get_sum_of_values(10, 20, 30, 40)

print("_" * 70)


def add_numbers(*args):
    return sum(args)


# Example usage
result = add_numbers(1, 2, 3, 4, 5)
print("The sum is:", result)

print("_" * 70)


##################################
# 1. function with **kwargs parameter.
# -> kwargs store the data in key value format or dictionary format.
# -> user has to pass param name as key and any value we can assign
# -> Any number of tuple can not be key while calling the function, it has to be valid variable name.

def get_user_details(**kwargs):
    return kwargs


value4 = get_user_details(name='pankaj', sarname='prasad', age=38, location='Bangalore', state='Karnataka')
print(value4)

print("_" * 70)


def get_user2(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, ":", v)


get_user2(name='pankaj', sarname='prasad', age=38, location='Bangalore', state='Karnataka')

print("_" * 70)


def user_login(**kwargs):
    """
    This function accepts two input as username and password

    :param kwargs:
    :return:
    """
    db_user = 'user1'
    db_password = 'user@1234'
    if kwargs['username'] == db_user and kwargs['password'] == db_password:
        print("Login successful")
    else:
        print("Login details are not valid")


user_login(username='user1', password='user@1234')
# user_login(username='user2', password='user@1234')
