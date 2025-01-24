"""
Home Work.

#1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the
number

"""
print("_"*50)
#1)write a python program to check given number is divisible by 3 or not
num1 = int(input("Please enter value :"))
var1 = 3
#print("condition output :", num1%var1)

if (num1%var1) == 0:
    print("Entered number is divisible by 3 :", num1)
else:
    print("Entered number is not divisible by 3  :", num1)

print("_"*50)

#2)write a python print square(n**2) if number is even or print cube(n**3) if number is odd
num2=int(input("Please enter value :"))
var1=2
if (num2%var1) == 0:
    print("Entered number is even :", num2**2)
else:
    print("Entered number is odd  :", num2**3)

print("_"*50)

#3)write a python program to check given positive or negative.

num3= int(input("Please enter value :"))
if num3>0:
    print("Entered number is positive")
elif num3<0:
    print("Entered number is negative")
else:
    print("Entered number is zero.")

print("_"*50)

#4)Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the
number

num4=int(input("Please enter value :"))
var1=7
if (num4%var1) == 0:
    print("Entered number is divisible by 7 :", num4+50)
else:
    print("Entered number is odd  :", num4-50)