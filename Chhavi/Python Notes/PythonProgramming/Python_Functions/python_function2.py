# write a python check odd or even value from given number of values

def get_even_odd(*args):
    for val in args:
        if val % 2 == 0:
            print(val, ": even")
        else:
            print(val, ": odd")


# get_even_odd(4, 6, 8, 2, 18, 23)
# get_even_odd(1, 6, 3, 7, 8)


def add(n1, n2):
    print("addition :", n1 + n2)


# write a python program to n number employee in employee list using **kwargs.
emp_list = []


def get_employee_details(**kwargs):
    emp_list.append(kwargs)


def add_employee_details():
    for i in range(3):
        user_name = input("enter name :")
        user_email = input("enter email :")
        user_phone = input("enter phone :")
        get_employee_details(name=user_name, email=user_email, phone=user_phone)

add_employee_details()

print(emp_list)
