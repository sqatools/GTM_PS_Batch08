def greeting():
    return "Good Morning"
    print("Hello world")  # code is un-reachable

# when we call function with return statement, then we loose the control over the function
# can not access the function anymore, any code will write after return
# statement will be unreachable.

var = greeting()
print(var)  # Good Morning


def get_grade(marks):
    if 50 < marks < 60:
        return "B grade"
    elif 60 > marks < 80:
        return "A grade"

result = get_grade(55)
print("result :", result)



# function with generator
def msg_list():
    yield "Good Morning"
    yield "Good Evening"
    yield "Hope you are doing good"
    yield "Learning Python"


data = msg_list()
print(data) # <generator object msg_list at 0x000001E9CF014880>

"""
print(next(data)) # Good Morning
print(next(data)) # Good Evening
print(next(data)) # Hope you are doing good
print(next(data)) # Learning Python
# print(next(data)) # StopIteration
"""

# get all values one by one using for loop
for val in data:
    print(val)

"""
Good Morning
Good Evening
Hope you are doing good
Learning Python

"""

def get_all_list_values(list_values):
    for val in list_values:
        yield val


list1 = [5, 7, 9, 1, 'a', [4, 6, 7], (4, 7, 8)]*100
print(list1)
data = get_all_list_values(list1)
print(data)

for n in data:
    print(n)
