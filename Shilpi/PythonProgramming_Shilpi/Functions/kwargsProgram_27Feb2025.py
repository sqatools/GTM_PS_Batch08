def main():
    list1 = []
    for x in range(10):
        print("Employee", x + 1, "info")
        print("-" * 20)
        fn = input("First Name :")
        ln = input("Last Name : ")
        a = input("Age : ")
        e = input("E-mail : ")
        print()
        company_database(list1,FirstName=fn, LastName=ln, Age=a, Email=e)

    for y in range(len(list1)):
        print(list1[y])


def company_database(l1,**kwargs):
    """
    This function adds the values given in the argument by the user in the list
    :param l1: list created for adding employee information
    :param kwargs: information of employee
    :return: list with the dictionary of employee information
    """
    l1.append(kwargs)
    return l1


main()











# write a python program update the user entry in the data base using *kwargs
# ->  we have company data, here we have to add 10 new member details in database
# ->  create a function which accept the users details using kwargs
# ->  add kwargs values to list
# ->  accept all the values using input
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
