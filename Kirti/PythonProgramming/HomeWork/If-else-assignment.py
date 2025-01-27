"""
Home Work.

#1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the
number

"""

#1). write a python program to check given number is divisible by 3 or not

num1 = int(input("Enter a number num1 : "))

if num1 % 3 == 0:
    print("Number "+str(num1)+" is divisible by 3")
else:
    print("Number " + str(num1) + " is not divisible by 3")


print("-"*50)
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd

num2 = int(input("Enter a number num2 : "))

if num2 % 2 == 0:
    print("Result is : ", num2**2)
else:
    print("Result is : ", num2**3)



print("-" * 50)
#3). write a python program to check given positive or negative.

num3 = int(input("Enter a number num3 : "))

if num3 > 0:
    print("Number is Positive : ", num3)
else:
    print("Number is Negative : ", num3)


print("-" * 50)
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the number

num4 = int(input("Enter a number num4 : "))

if num4 % 7 == 0:
    print("Result is : ", num4+50)
else:
    print("Result is : ", num4-50)
