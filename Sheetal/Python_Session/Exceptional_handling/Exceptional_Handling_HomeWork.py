print("1.Python Program How to read a file in reading mode.")
def read_file(filepath):
    try:
        with open(filepath) as file:
            data = file.read()
            print(data)
    # except FileNotFoundError:
    #     print("Error: File not found.")
    except Exception as e:
        print(e)
        print("The file path does not exist")
    finally:
        print("This is the actual file content")

read_file("Exception_File1.txt")

print("_"*50)
print("2. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.")


print("_"*50)
print("3. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.")


print("_"*50)
print("3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.")


print("_"*50)
print("4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.")


print("_"*50)
print("5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.")


print("_"*50)
print("6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.")


print("_"*50)
print("7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.")


print("_"*50)
print("8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.")


print("_"*50)
print("9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.")


print("_"*50)
print("10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.")