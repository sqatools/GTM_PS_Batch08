"""
1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the number
"""

num = int(input("Enter a number:"))

print("-"*50)
print("Check-1:Given number is divisible by 3 or not")
print("-"*50)
if num % 3 == 0:
    print("The provided number is divisible by 3")
else:
    print("The provided number is not divisible by 3")

print("-"*50)
print("Check-2:Square(n**2) if number is even or print cube(n**3) if number is odd")
print("-"*50)
if num % 2 == 0:
    print("The provided number is even")
    print("The square of the provided number is:"+str(num**2))
else:
    print("The provided number is odd")
    print("The cube of the provided number is:"+str(num**3))

print("-"*50)
print("Check-3:Positive or negative")
print("-"*50)
if num > 0:
    print("The provided number is positive")
else:
    print("The provided number is negative")

print("-"*50)
print("Check-4:divisible by 7 then add 50 in the number else subtraction 50 from the number")
print("-"*50)
if num % 7 == 0:
    print("The provided number is divisible by 7")
    print(num+50)
else:
    print("The provided number is not divisible by 7")
    print(num-50)