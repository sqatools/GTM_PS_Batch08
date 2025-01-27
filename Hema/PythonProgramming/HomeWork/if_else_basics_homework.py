"""
Home Work.

#1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the
number

"""
print("="*50)
print("1. To check given number is divisible by 3 or not")
num1 = 27
print("Given number is: ", num1)
print("checking the number is divisible by 3: ", num1%3==0)

if num1%3 == 0:
    print("The given number is divisible by 3")
else:
    print("The given number is not divisible by 3")

print("="*50)

print("2. To print square(n**2) if number is even or print cube(n**3) if number is odd")

#num2 = int(input("Enter the number: "))
num2 = 3
print("Given number is: ", num2)
print("checking the boolean value of given number is even: ", num2%2==0)
if num2%2 == 0:
    print("The number is even: ", num2)
    print("Square of the even number is: ", num2**2)
else:
    print("The number is odd: ", num2)
    print("Cube of the odd number is: ", num2**3)
print("="*50)

print("3. To check the given number is positive or negative")
num3 = -10
print("Given number is: ", num3)
print("checking the boolean value of given number is positive: ", num3>0)

if num3<0:
    print("The number is negative: ", num3)
else:
    print("The number is positive: ", num3)

print("="*50)
print("4. To Check given number is divisible by 7 then add 50 in the number,\n if given number is not divisble by 7 then subtract 50 from the number")
print("~"*50)
#num4 = 35
num4 = int(input("Please enter any number: "))
print("Given number is: ", num4)
print("checking the boolean value of given number is divisible by 7: ", num4%7==0)

if num4%7 != 0:
    sub = num4 - 50
    print("Since the number is not divisible by 7, subtract 50 from the number: ", num4, "-" ,50, "=", sub)
else:
    add = num4 + 50
    print("Since the number is divisible by 7, add 50 to the number: ", num4, "+", 50, "=", add)

print("="*50)