# decorator: Decorator enhance the functionality of the code without changing the existing feature

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


greeting("Hello buddy")

@decorator_function
def show_greeting_msg(msg):
    return msg

show_greeting_msg("heyy")


def show_all_even_value(range_num):
    for i in range(range_num):
        if i%2 ==0:
            print(i)

show_all_even_value(99)