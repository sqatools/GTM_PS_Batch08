# decorator :  decorator enhance the functionality of the code without
#              changing the existing feature.
#              ->  decorator is the external function that we have call with any function
#                  using @.
#              ->  When we call any function which is associated with decorator, will initiate the
#                  decorator function first.

def decorator_function(func):
    def inner(param):
        print("*"*50)
        var1 = func(param)
        print(var1)
        print("*"*50)
    return inner

# calling the decorator function with existing code
@decorator_function
def greeting(msg):
    return msg


greeting("Good Morning")



@decorator_function
def show_greeting_msg(msg):
    return msg

show_greeting_msg("Very good evening")



def fun_decor(func):
    def inner(param):
        param_val = 50 if param >= 50 else param
        func(param_val)
    return inner


@fun_decor
def show_all_even_value(range_num):
    for i in range(range_num):
        if i%2 == 0:
            print(i)

show_all_even_value(60)
