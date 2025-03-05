"""
local variable :   ->  When we defined any variable inside the function, then it is known
                       as local variable
                   -> The scope of local variable is limited to the function only.
global variable :  ->  when we define any variable outside the function, then it is known
                       as global variable
                   -> global variable is accessible to any function inside the module or
                      outside the module as well

                    -> If we want to change the value of global variable inside the function
                       then we have to use global keyword. e.g. global var_p

non local variable :  When we defined a variable inside the outer function and outside of the
                      inner function, then it is called non local variable.

                      ->  If we want to update non local variable value inside the inner the function
                          then we have to nonlocal keyword e.g. nonlocal var_y
"""
# global variable
var_p = 500


def function1():
    print("____function1____\n")
    global var_p
    var_q = 400  # local variable
    var_p = 600
    print("global variable var_p:", var_p)
    print("local variable var_q:", var_q)


def function2():
    print("____function2____\n")
    var_r = 300  # local variable
    print("global variable var_p:", var_p)
    print("local variable var_r:", var_r)

"""
function2()
function1()
print("_"*50)
function2()
"""


############################### Non local variable ###################
var_x = 800 # global variable

def outer_function():
    var_y = 700 # non local variable

    def inner_func1():
        print("-----------inner fun1 ------------")
        nonlocal var_y
        global var_x
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
