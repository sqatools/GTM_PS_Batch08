"""
def function_name():
    code

function_name()  #call function to pass values
"""
# Homework


print("1. WAPF to get max value from list")
def maximum_fun(l1):
    max_num =l1[0]
    for num in l1:
        if num > max_num:
            max_num = num
    return max_num

max_value = maximum_fun([57,88,43,22,1])
print(f"The maximum number from the list is {max_value}")

print("_"*40)
print("2. WAPF to return factorial value of number number")
# 5 = 120 : 5*4*3*2*1
def fact_num(num):
    fact_n = 1
    while num >0:
        fact_n = fact_n * num
        num = num-1
    return fact_n,num

fact_of_num = fact_num(5)

print(f"The Factorial of number is {fact_of_num} and the data type of", type(fact_of_num))


print("_"*40)
print("3. WAPF to calculate the number of consonants in given string.")
str1= "Hello We are Learning Python" # output = 15

def const_alp(str2,count_c):
    vowel = ("aeiouAEIOU")
    str3 = ""
    # count_const = 0
    for string1 in str2:
        print(string1)
        if string1 not in vowel and string1.isalpha():
            str3 += string1
            count_c +=1

    return str3,count_c
# HllWrLrnngPythn

const_print, count_const = const_alp(str1, 0)
print(f"The final string is {const_print} and the count of the consonants are {count_const}")


# print("Python function program to get a valid mobile number.")

print("_"*40)
"""
write a python program update the user entry in the data base using *kwargs
->  we have company data, here we have to add 10 new member details in database
->  create a function which accept the users details using kwargs
->  add kwargs values to list
->  accept all the values using input
"""

list1 = []
def emp_detail(**kargs):
    emp = {}
    emp['name'] = input("Enter emp first name: ")
    emp['surname'] = input("Enter emp last name: ")
    emp['age'] = input("Enter age of emp: ")
    emp['email'] = input("Enter email of emp: ")

    list1.append(emp)

for i in range(3):
    print(f"\nEnter details for Employee {i+1}:")
    emp_detail()

print("\nUpdated Employee Database:")
for emp in list1:
    print(emp,"\n")


# list1 = [
#     {'name':'rohit', 'surname': 'verma', 'age':20, 'email':'rohit@gmail.com'},
#     {'name':'dharmendra', 'surname': 'sahu', 'age':25, 'email':'dharmendra@gmail.com'},
#     {'name':'shilpi', 'surname': 'sharma', 'age':30, 'email':'shilpi@gmail.com'}
# ]
import re
# print(list1)
list1= []
def emp_detail(**kargs):
    list1.append(kargs)

for i in range(3):
    print(f"\nEnter details for Employee {i + 1}:")
    while True:
        name = input("Enter emp first name: ")
        if name == "" or name[0].isnumeric():
            print("First Name can't be blank or name can't start with number")
        else:
            break
    surname = input("Enter emp last name: ")
    while True:
        age = input("Enter age of emp: ")
        if age.isnumeric() and len(age) <= 2:
            break
        else:
            print("Please enter correct age of length 2 or less and age shud accept number only")
    while True:
        email = input("Enter email of emp: ")
        if ('@' in email and '.' in email and email.index('@') < email.rindex('.')
            and re.search(r'[A-Za-z]', email) and
        re.search(r'[0-9]', email)):
            break
        else:
            print("Please enter correct email id -> It shud contain 'alp, number ,@ , . ' as a valid id")
    emp_detail(name=name,lastname=surname,age=age,email=email)

# print(list1,"\n")
print("_"*40)
print("\nUpdated Employee Database: [")

for emp in list1:
    print(emp)

print("]")
