"""
Home Work.

#1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the
number

"""

#1). write a python program to check given number is divisible by 3 or not

num1=9
#num1= int(input("Enter the number:", ))

if(num1%3 == 0):
    print("Given number is divisible by 3",num1) #Number is divisible by 3 9
else:
    print("Given number is not divisible by 3", num1) #NUmber is not divisible by 3 7


print("-"*50)
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd

num2 =12
#num2= int(input("Enter the number:",num2 ))

if(num2%2 == 0):
    print("Given number is Even and its Square is:",num2**2,num2) #Number is Even and its Square is: 144 12
else:
    print("Given number is odd and its square root is:", num2**3,num2) #Number is odd and its square root is: 343 7


print("-"*50)
#3). write a python program to check given positive or negative.

Num3=-6
# Num3 = int(input("Enter the number:"))

if(Num3 >= 0):
    print("Given number is Positive",Num3) #Given number is Positive 8
    """Enter the number:-0
Given number is Positive 0 """
else:
    print("Given number is Negative",Num3) #Given number is Negative -6


#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the

Num4 = int(input("Enter the Number:"))

if(Num4 % 7 == 0):
    print(Num4, "is divisible by 7:", "Num4+50 is:", Num4+50) #Num4 is divisible by 7: 14 Num4+50 is: 64
else:
    print(Num4, "is not divisible by 7", "Num4+50 is:", Num4-50) #3 is not divisible by 7 Num4+50 is: -47
