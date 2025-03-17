def try_except_else_finally_block_handling(num1, num2):
    try:
        x = num1
        y = num2
        print("addition :", x+y)
    except Exception as e:
        print(e)
        print("Can not add string with integer")
        raise
    else:
        # This block will only execute, when there is no exception
        print("Good Morning")

    finally:
        # This section will always execute
        for i in range(1, 6):
            print(i, "*", num1, ":", i*num1)


# correct values
#try_except_else_finally_block_handling(5, 6)

# in-correct values
try_except_else_finally_block_handling(7, 'Hello')