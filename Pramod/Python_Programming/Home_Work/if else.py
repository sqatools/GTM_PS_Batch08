"""
Home Work.
#1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the
number
"""

#1). write a python program to check given number is divisible by 3 or not
n = 2
if n%3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

#The number is not divisible by 3

#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd

a = 4
if a %2 ==0:
    print("the number is even", a**2)
else:
    print("the number is odd", a**3)

#3). write a python program to check given positive or negative.

b = -3
if b >=0:
    print("the number is positive", b)
else:
    print("the number is negative", b)
    
#the number is negative -3

#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the

c=4
if c%7==0:
    print ("The number is divisible by 7, so adding 50", c+50)
else:
    print("The number is not divisible by 7, so substract 50",c-50)

