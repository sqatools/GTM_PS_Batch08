
# handle exception error msg
def basic_exception_handling():
    try:
        num1 = 50
        num2 = "hello"
        print(num1+num2)
    except Exception as e:
        print(e)
        print("can not add string with integer")

    print("good evening")

basic_exception_handling()

# raise explicit exception : when user wants to fail the program  to explicity  with the exception error
#                          -> This kind of condition occur when core application feature  are not avaialblle
#                          -> it has to fix as soon as possible
#

def raise_explicit_exception():
    try:
        num1 = 50
        num2 = "hello"
        print(num1 + num2)
    except Exception as e:
        print(e)
        print("can not add string with integer")
        raise

    print("good evening")

#raise_explicit_exception()

#######################
# try-except-else block.
# finally : finally block of code will execute anyway,
def try_except_else_block_handling(num1, num2):
    try:
       x = num1
       y = num2
       print("addition :", x+y)
    except Exception as e:
       print(e)
       print("can not add string with integer")
    else:
        # this block will only execute, when there is no exeception
       print("good evening")
##############################
def try_except_else_block_handling(num1, num2):
    try:
            x = num1
            y = num2
            print("addition :", x + y)
    except Exception as e:
            print(e)
            print("can not add string with integer")
    else:
            # this block will only execute, when there is no exeception
            print("good evening")

    finally:
        # this section will always execute
        for i in range(1, 11):
            print(i, "*", num1, ":", i*num1)

# correct values
# try_except_else_Finally_block)handling(5, 6_)

# in correct values
try_except_else_block_handling(7, 'hello')


#################################3
# handle multiple exception: user can define different error msg for different exception
def handle_multiple_exception(num1, num2, num3, filepath):
    try:
        addition = num1+num2
        print("addition :", addition)

        #multiplication
        mul = num1*num2
        print("multiplication :", mul)

        # division
        divide = num2//num3
        print("division error :", divide)

        # read file
        with open(filepath) as file:
            data = file.read()
            print(data)
    except TypeError:
        print("both the values should be integer")
    except ZeroDivisionError:
        print("can not divide number with zero")
    except FileNotFoundError:
        print("Can not find the file path specified")
    except Exception as e:
        print("Raising gene")
        raise e


handle_multiple_exception(5, 6, 10.,  'read_data.txt')

