# # write a python program to create a calculator
#
# def add(v1, v2):
#     print("addition :", v1 + v2)
#
#
# def multiplication(v1, v2):
#     print("multiplication :", v1 * v2)
#
#
# def subtraction(v1, v2):
#     print("subtraction :", v1 - v2)
#
#
# def divide(v1, v2):
#     print("division :", v1 // v2)
#
#
# def calculator(operation, var1, var2):
#     if operation == 1:
#         add(var1, var2)
#     elif operation == 2:
#         multiplication(var1, var2)
#     elif operation == 3:
#         subtraction(var1, var2)
#     elif operation == 4:
#         divide(var1, var2)
#     else:
#         print("Invalid input")
#
#
# calculator(1, 50, 60)
# calculator(2, 2000, 60)
# # write a python check odd or even value from given number of values
#
# def get_even_odd(*args):
#     for val in args:
#         if val % 2 == 0:
#             print(val, ": even")
#         else:
#             print(val, ": odd")
#
#
# # get_even_odd(4, 6, 8, 2, 18, 23)
# # get_even_odd(1, 6, 3, 7, 8)
#
#
# def add(n1, n2):
#     print("addition :", n1 + n2)
#
#
# # write a python program to n number employee in employee list using **kwargs.
# emp_list = []
#
#
# def get_employee_details(**kwargs):
#     emp_list.append(kwargs)
#
#
# def add_employee_details():
#     for i in range(3):
#         user_name = input("enter name :")
#         user_email = input("enter email :")
#         user_phone = input("enter phone :")
#         get_employee_details(name=user_name, email=user_email, phone=user_phone)
#
# add_employee_details()
#
# print(emp_list)
# """
# def function_name():
#     code
#
# """
#
#
# def greeting():
#     print("Hello Good Morning")
#
#
# # call the function
# greeting()
#
# print("_" * 50)
#
#
# ############################################
# # function with parameters
# def addition(n1, n2):
#     print("value of n1 :", n1)
#     print("value of n2 :", n2)
#     print("addition of number :", n1 + n2)
#
#
# # There are 2 ways to pass value to the function
# # 1. PASS BY VALUE
# addition(50, 60)
# # _____________________
# print("_" * 50)
# addition(n1=70, n2=80)
# print("_" * 50)
# # _____________________
# # if we are using parameter name, then can change the order of value as well with the help
# # param names.
# addition(n2=100, n1=90)
#
# # _____________________
# print("_" * 50)
# addition([4, 6, 7], [8, 1, 4])  # [4, 6, 7, 8, 1, 4]
# addition('Hello', 'Python')  # HelloPython
#
# # addition(n2=200)
# # TypeError: addition() missing 1 required positional argument: 'n1'
#
# # #_____________________
# # 2. PASS BY REFERENCE :  when we pass difference variables in function calling instead of value, then
# #                         it is called pass by reference.
#
# x = 500
# y = 600
# addition(x, y)  # 1100
#
# l1 = [4, 5, 7]
# l2 = [6, 9, 10]
# addition(l1, l2)  # [4, 5, 7, 6, 9, 10]
#
# id(list)
#
# print("_" * 50)
#
#
# ##################### function parameters with data type ##############
#
# def multiplication(v1: int, v2: int):
#     """
#     This function help to multiply integer values and print it.
#     :param v1: first parameter value
#     :param v2: second parameter value
#     :return : None
#     """
#     print("multiplication  :", v1 * v2)
#
#
# # program will execute without any issue
# multiplication(50, 5)
# # multiplication  : 250
#
# # program will execute with warning in program file.
# multiplication('Python', 5)  # PythonPythonPythonPythonPython
#
# print("_" * 40)
#
#
# ########### function with return data ################
#
# # # function with single return value
# def greeting_msg(name):
#     return f"Hello {name}, good morning"
#
#
# val1 = greeting_msg('Rahul')
# print("return val :", val1)  # Hello Rahul, good morning
#
#
# # function with multiple return value
# def math_operation(n1, n2):
#     add = n1 + n2
#     multi = n1 * n2
#     sub = n1 - n2
#     div = n1 // n2
#     return add, multi, sub, div
#
#
# # store multiple return value in one variable
# result = math_operation(10, 5)
# print("return values :", result)
# # return values : (15, 50, 5, 2)
#
# # store multiple return value in different variable
# a, b, c, d = math_operation(40, 15)
# print("addition output :", a, a ** 2)
# print("multiplication output :", b, b ** 3)
# print("subtraction output :", c, c ** 4)
# print("division output :", d, d ** 5)
#
# print("_" * 50)
# print(math_operation(50, 10))
#
# """
# # Home work
# 1. write a python function to get max value from list
# 2. write a python function to return factorial value of number number
# 5 = 120 : 5*4*3*2*1
# 3. Write a python function to calculate the number of consonants in given string.
# str1= "Hello We are Learning Python" # output = 16
# """
# print("_" * 50)
#
#
# # write a python function get square of each value in the list
# # list1 = [4, 7, 9, 12, 34]
# # output = [16, 49, 81, 144, 34..]
#
# def get_square_value(l1):
#     output = []
#     for val in l1:
#         output.append(val ** 2)
#
#     return output
#
#
# list1 = [4, 7, 9, 12, 34]
# result = get_square_value([4, 7, 9, 12, 34])  #
# print(result)  # [16, 49, 81, 144, 1156]
#
# print(get_square_value(list1))  # [16, 49, 81, 144, 1156]
#
# list2 = [2, 5, 7, 9]
# result2 = get_square_value(list2)
# print(result2)  # [4, 25, 49, 81]
#
# print("_" * 50)
#
#
# ################### Function with default parameter value ######################
# # As per rule default parameter should follow non default parameter,
# # it means default parameter always comes at end of param list.
# def addition_multiple_value(n1, n2, n3=50):
#     print("value of n1:", n1)
#     print("value of n2:", n2)
#     print("value of n3:", n3)
#     add = n1 + n2 + n3
#     print("addition  :", add)
#     return add
#
#
# # if we don't provide value default param, thn it will consider default value
# addition_multiple_value(20, 30)
#
# print("_" * 50)
# # overwrite default value of parameter, then assign new value
# r1 = addition_multiple_value(200, 300, 400)
# print("result1 :", r1)
#
# #####################################################
# print("_" * 50)
#
#
# # specific return type of the function
#
# def add_words(w1, w2) -> int:
#     return int(w1) + int(w2)
#
#
# # v1 = add_words('Hello', 'Programing')
# # print("result :", v1)
#
#
# v2 = add_words(20, 30)
# print("result2 :", v2)
#
# print("_" * 50)
#
#
# #######################################
# # function with *args parameter.
# # *args parameter accept n number of values while calling the function.
# # it accepts the values in form of tuple
#
# def get_sum_values(var1, *args):
#     print("var1 :", var1)
#     print("args :", args)
#     sum = 0
#     for val in args:
#         sum += val
#
#     print("sum of all values :", sum)
#
#
# get_sum_values(4, 5)
# get_sum_values(10, 40, 50, 60, 70, 80)
# # get_sum_values(10, 40, [4, 6,7], 'Hello', 70, {'a':123, 'b' : 345})
#
#
# print("_" * 50)
# #######################################
# # function with **kwargs parameter.
# # -> kwargs store the data in key value format or dictionary format
# # -> User has to pass the param name as key and any value we can assign
# # -> Any, number or tuple can not be key while calling the function, it has to be valid variable name.
#
# def get_user_details(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k, ":", v)
#
#
# get_user_details(name='rahul', surname='gupta', email='rahul@gmail.com', phone=654645645, age=40.5)
#
#
# def user_login(**kwargs):
#     """
#     This function accepts two input value as username and password
#
#     :param kwargs:
#     :return:
#     """
#     db_user = 'user1'
#     db_password = 'user@12345'
#     if kwargs['username'] == db_user and kwargs['password'] == db_password:
#         print("Login Successful")
#     else:
#         print("invalid credentials")
#
#
# print("_"*50)
# user_login(username='user1', password='user@12345')
# user_login(username='user2', password='user@12345')
#
#
# """
# write a python program update the user entry in the data base using *kwargs
# ->  we have company data, here we have to add 10 new member details in database
# ->  create a function which accept the users details using kwargs
# ->  add kwargs values to list
# ->  accept all the values using input
# """
#
# list1 = []
#
# list1 = [
#     {'name':'rohit', 'surname': 'verma', 'age':20, 'email':'rohit@gmail.com'},
#     {'name':'dharmendra', 'surname': 'sahu', 'age':25, 'email':'dharmendra@gmail.com'},
#     {'name':'shilpi', 'surname': 'sharma', 'age':30, 'email':'shilpi@gmail.com'}
# ]
#
# print(list1)
# """
# local variable :   ->  When we defined any variable inside the function, then it is known
#                        as local variable
#                    -> The scope of local variable is limited to the function only.
# global variable :  ->  when we define any variable outside the function, then it is known
#                        as global variable
#                    -> global variable is accessible to any function inside the module or
#                       outside the module as well
#
#                     -> If we want to change the value of global variable inside the function
#                        then we have to use global keyword. e.g. global var_p
#
# non local variable :  When we defined a variable inside the outer function and outside of the
#                       inner function, then it is called non local variable.
#
#                       ->  If we want to update non local variable value inside the inner the function
#                           then we have to nonlocal keyword e.g. nonlocal var_y
# """
# # global variable
# var_p = 500
#
#
# def function1():
#     print("____function1____\n")
#     global var_r
#     var_q = 400  # local variable
#     var_p = 600
#     print("global variable var_p:", var_p)
#     print("local variable var_q:", var_q)
#
#
# def function2():
#     print("____function2____\n")
#     var_r = 300  # local variable
#     print("global variable var_p:", var_p)
#     print("local variable var_r:", var_r)
#
# """
# function2()
# function1()
# print("_"*50)
# function2()
# """


############################### Non local variable ###################
var_x = 800 # global variable

def outer_function():
    var_y = 700 # non local variable

    def inner_func1():
        print("-----------inner fun1 ------------")
        # nonlocal var_y
        global var_y
        global var_x
        # nonlocal var_x
        var_z = 600  # local variable
        var_x = 1100
        var_y = 1000
        print("global var_x :", var_x)
        print("non local var_y :", var_y)
        print("local var_z :", var_z)

    def inner_func2():
        print("-----------inner fun2 ------------")
        var_w = 500  # local variable
        print("global var_x :", var_x)
        print("non local var_y :", var_y)
        print("local var_z :", var_w)

    inner_func2()
    inner_func1()
    inner_func2()


outer_function()

# import specific function
# from python_function2 import get_even_odd
# import all available variable/method/function/class
# from python_function2 import *
#
# get_even_odd(5, 7, 9, 11, 5, 23, 22)
# add(50, 70)
