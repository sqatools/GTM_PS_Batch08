"""
Decorator: Decorator enhances functionality of code without changing the existing feature
            --> Decorator is an external function that we can call with any function using @

            --> When we call any function which is associated with decorator,
                then decorator function will be initiated first

"""

def decorator_func(func):
    def inner(param):
        print("*"*50)
        var1 = func(param)
        print(var1)
        print("*"*50)
    return inner

# calling decorator function with existing code
@decorator_func
def greeting_msg(msg):
    return msg

greeting_msg("Hello Good morning")

@decorator_func
def show_greeting_msg(msg):
    return msg

show_greeting_msg("Very good evening")

print("#"*70)
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

