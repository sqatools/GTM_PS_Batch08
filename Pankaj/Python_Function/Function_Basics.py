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
addition(n1=300, n2=900) # this way we can change the order of value
print("_" * 70)
addition([1, 2, 3, 4], [2, 3, 4, 5])#[1, 2, 3, 4, 2, 3, 4, 5]
addition("pankaj", "prasad") # pankajprasad

# 2. PASS BY REFERENCE
x = 400
y = 500
addition(x, y)

############################### function parameter with data type ##############################
