# wap to check even and odd from given numbers of values

def even_odd(*args):
    for val in args:
        if val % 2 == 0:
            print(val, ": Even number")
        else:
            print(val, ": Odd number")


# even_odd(2, 3, 4, 5, 6, 19, 20)
even_odd(22, 23, 39, 40)


def add(n1, n2):
    print("addition: ", n1 + n2)


# wap to add number of employee in employee-list using kwargs
emp_list = []


def get_emp_list(**kwargs):
    emp_list.append(kwargs)


for i in range(3):
    user_name = input("Enter Name: ")
    user_email = input("Enter Email: ")
    user_age = input("Enter your age: ")
    get_emp_list(name=user_name, email=user_email, age=user_age)
print(emp_list)
