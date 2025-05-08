""""
def function_name();
    code

"""


def greeting():
    print("hello")


# call the function
greeting()


# function with parameters
def addition(n1, n2):
    print("value of n1 :", n1)
    print("value of n2 :", n2)
    print("addition of num :", n1 + n2)


# There are 2 ways to pass value to the function
# 1) pass by value
addition(50, 60)
print("_" * 50)

addition(n1=52, n2=65)
print("_" * 50)

# if we are using parameter name, then can change the order of the value as well the help
# param names

addition(n2=100, n1=90)

# 2) pass by reference: when we pass difference in function calling instead of the value
#                       then it is called pass by reference

X = 101
y = 123
addition(X, y)  # 224

l1 = [4, 6, 8]
l2 = [5, 9, 8]
addition(l1, l2)  # [4, 6, 8, 5, 9, 8]

id(list)

print("_" * 40)


#################### function parameter with data type #########

def multiplication(v1: int, v2: int):
    """
    This function help to multiply integer values and print it
    :param v1: first parameter value
    :param v2: second parameter value
    :return: none
    """
    print("multiplication :", v1 * v2)


# program will execute without any issue
multiplication(50, 5)
# multiplication : 250

# program will execute with warning in program file
multiplication('Manoj', 3)  # ManojManojManoj

print("_" * 40)


################# function with return data###########

# function with single return value
def greeting_msg(name):
    return f"Hello {name}, good evening"


val1 = greeting_msg('manoj')
print("return val :", val1)  # Hello manoj, good evening


# function with multiple return value
def math_operation(n1, n2):
    add = n1 + n2
    mul = n1 * n2
    sub = n1 - n2
    divide = n1//n2
    return add,mul,sub,divide

# store multiple return value in one variable
result = math_operation(10, 20)
print("return values :", result)
# return values :  # (30, 200, -10, 0)

# store multiple return value in one multiple
a, b, c, d = math_operation(10, 20)
print("addition output :", a)
print("multiplication output :", b)
print("subtraction output :", c)
print("division output :", d)