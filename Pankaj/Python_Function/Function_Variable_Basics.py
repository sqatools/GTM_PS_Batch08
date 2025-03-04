"""
Local Variable:
     -> When we define any variable inside the function is called as local variable.
     -> Scope of local variable is limited to the function only
Global Variable:
     -> When we define any variable outside the function, is known as global variable.
     -> global variable is accessible to any function inside the module or outside the module as well.
     -> If we want to change the value of global variable inside the function then we have to use keyword global.
       e.g. global variable_name

Non-local: -> When we define variable inside the outer function and outside the inner function, is called as not local
              variable.
           -> If we want to update non local variable value inside the inner function then we have to use
              nonlocal keyword. eg. nonlocal variable_name.

"""
# global variable
var_1 = 500


def function1():
    print("________function1__________\n")
    var_2 = 400  # local variable
    global var_1  # if we mention this value the updated value will be assigned to both function
    var_1 = 600
    print("Global variable: ", var_1)
    print("Local Variable :", var_2)


def function2():
    print("________function2__________\n")
    var_3 = 300  # local variable
    print("Global variable: ", var_1)
    print("Local Variable :", var_3)  # for var_2 will giver error , cox of local variable


function2()
function1()
print("_" * 70)
function2()

######################### Non local ###########################
# when we define function inside a function

var_a = 500  # global variable


def outer_function():
    var_b = 700  # non local variable

    def inner_function11():
        print("___________Inner function 11___________")
        var_c = 100  # local variable
        global var_a
        var_a = 5000
        nonlocal var_b
        var_b = 7000
        print("Global variable: ", var_a)
        print("Non Local Variable: ", var_b)
        print("Local Variable: ", var_c)

    def inner_function22():
        print("___________Inner function 22___________")
        var_c = 200  # local variable
        print("Global variable: ", var_a)
        print("Non Local Variable: ", var_b)
        print("Local Variable: ", var_c)

    inner_function22()
    inner_function11()
    inner_function22()


outer_function()
