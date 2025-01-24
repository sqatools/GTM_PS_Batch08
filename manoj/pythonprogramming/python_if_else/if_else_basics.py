"""
if condition:
     code
else:
    code
"""

print("_"*50)
# check given numbers are equal or not
a = 40
b = 60

print("condition output :", a == b)

if a == b:
    # if condition is true
    print("Numbers are equal:", a, b)
else:
    # if condition is false
    print("Numbers are not equal :", a, b)



print("_"*50)
# write a program to check given number is even or odd
# if any number can be divisible by 2 than it is even or odd

num1 = 5
var1 = 2
print("condition output :", num1%var1)

if num1%var1 == 0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)

"""
home work :

# write a python program to check given number is divisible by 3 or not
# write a python print square(n**2) if number is even or print cube(n**) if number is odd
# write a python program to check given positive or negative
# check given number is divisible by 7 then add 50  in the number else subtraction 50 from the number

"""
# write a python program to check given number is divisible by 3 or not
num1 = 83
var1 = 3


if num1%var1 == 0:
    print("number is divisible :", num1)
else:
    print("number is not divisible :", num1)  # number is not divisible : 83



 # write a python print square(n**2) if number is even or print cube(n**) if number is odd

num1 = 4
var1 = 2
print("condition output :", num1%var1)

if num1%var1 == 0:
    print("output :", num1**2)
else:
    print("output :", num1**3)

# write a python program to check given positive or negative

num3 = 0
var3 = 0
if num3 > 0 :
    print("given number is positive :", num3)
else:
    print("given number is negative :", num3)
