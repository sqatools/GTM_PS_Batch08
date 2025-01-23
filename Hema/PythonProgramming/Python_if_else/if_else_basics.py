"""
if condition:
    code
else:
    code
"""
#23rdJan2025
print("_"*50)
# check given numbers are equal or not
a = 40
b = 50

if a == b:
    # if condition is True
    print("Numbers are equal:", a, b)
else:
    # if condition is False
    print("Numbers are not equal :", a, b)


print("condition output:", a == b)



print("_"*50)
# write a program to check given number is even or odd
# if any number can be divisible by 2 than it is even or odd number
#
# input function accepts the values in string format, we have to convert as per requirements
num1 = int(input("Please enter value :"))
var1 = 2
print("condition output :", num1%var1)

if (num1%var1) == 0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)

"""
Home Work.

#1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the
number

"""
