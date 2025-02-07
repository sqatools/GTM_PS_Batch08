#Program 1 To print the variable nae if you know the value of the variable

name = "Mohit"
num = 42
age = 30
salary = 42  # Another variable with the same value

value_to_find = "Mohit"  # The value you are looking for

for var_name, var_value in list(globals().items()):
    if var_value == value_to_find:
        print(f"Variable name: {var_name}, Value: {var_value}")



print("_"*40)
#Program 2
# Write a program to print the last element of a list using a while loop using Python Loops.
# Input :
# C=[s,q,a,t,o,o,l,s]
# Output = s





print("_"*40)
#Program 3
# Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.

print("The value")

str_y="PythonIsGreat"
print(str_y[-1:0:-1])