# Handle exeception erro msg
def basic_exception_handling():
    try:
        num1 = 50
        num2 = "Hello"
        print(num1 + num2)
    except Exception as e:
        print(e)
        print("Can not add string with integer")

    print("Good Morning")


# basic_exception_handling()


# raise explicit exception. : When user wants to fail the program to explicitly with the exception error
#                           ->  This kind of condition occur when core application feature are not working
#                                It has to fix as soon as possible.
#
def raise_explicit_exception():
    try:
        num1 = 50
        num2 = "Hello"
        print(num1 + num2)
    except Exception as e:
        print(e)
        print("Can not add string with integer")
        raise

    print("Good Morning")


# raise_explicit_exception()


#########################
# try-except-else block.
# else block only executes, when there is no exception in the code.


def try_except_else_block_handling(num1, num2):
    try:
        x = num1
        y = num2
        print("addition :", x + y)
    except Exception as e:
        print(e)
        print("Can not add string with integer")
    else:
        # This block will only execute, when there is no exception
        print("Good Morning")


# correct values
# try_except_else_block_handling(10, 20)
# incorrect values
# try_except_else_block_handling("Hello", 20)


#########################
# try-except-else-finally block.
# finally :  finally block of code will execute anyway, there is exception or not exception

def try_except_else_finally_block_handling(num1, num2):
    try:
        x = num1
        y = num2
        print("addition :", x + y)
    except Exception as e:
        print(e)
        print("Can not add string with integer")
        raise
    else:
        # This block will only execute, when there is no exception
        print("Good Morning")

    finally:
        # This section will always execute
        for i in range(1, 11):
            print(i, "*", num1, ":", i * num1)


# correct values
# try_except_else_finally_block_handling(5, 6)

# in-correct values
# try_except_else_finally_block_handling(7, 'Hello')


######################################
# handle multiple exception: Use can define different error msg for different exeception

def handle_multiple_exception(num1, num2, num3, filepath):
    try:
        addition = num1 + num2
        print("addition :", addition)

        # multiplication
        mul = num1 * num2
        print("multiplication :", mul)

        # division:
        divide = num2 // num3
        print("division error :", divide)

        # read file
        with open(filepath, "r") as file:
            data = file.read()
            print(data)

        # compare value
        assert num1 == num2
    except TypeError:
        print("both the values should be integer")
    except ZeroDivisionError:
        print("Can not divide number with zero")
    except FileNotFoundError:
        print("Can not find the file path specified")
    except AssertionError:
        print("Both values are not equal")
    except Exception as e:
        print("Raising generic message")
        raise e


# handle_multiple_exception(5, 10, 2, 'read_data.txt')

def handle_nested_level_exception(num1, num2, num3, filepath):
    try:
        addition = num1 + num2
        print("addition :", addition)

        # multiplication
        mul = num1 * num2
        print("multiplication :", mul)
        try:
            # division:
            divide = num2 // num3
            print("division error :", divide)

            # read file
            with open(filepath, "r") as file:
                data = file.read()
                print(data)

            # compare value
            assert num1 == num2
        except Exception as e:
            print("Inner exception :", e)
            #raise
        finally:
            print("Inner finally")

    except TypeError:
        print("Outer Exception : both the values should be integer")

    finally:
            print("outer finally")


#handle_nested_level_exception(20, 20, 30, "read_data2.txt")


##################################
# custom exception

class custom_exception(Exception):
    def __init__(self):
        print("Raising custom exception")


def use_custom_exception():
    for i in range(10):
        if i == 5:
            raise custom_exception
        else:
            continue


use_custom_exception()
