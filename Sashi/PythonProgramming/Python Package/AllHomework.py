##1) (a+b)^3 = a^3 + b^3 + 3ab(a+b)
"""
a = int(input("Please Enter a Value:"))
b = int(input("Please Enter b Value:"))

LHS = (a+b)**3
RHS = a**3 + b**3 + 3*a*b*(a+b)

print("The Value of LHS is :", LHS)
print ("The Value of RHS is:", RHS)
print(LHS==RHS)

if LHS == RHS:
    print ("LHS is equal to RHS")
else:
    print("LHS is not equal to RHS")

"""

##2) (a-b) (a+b) = a^2 - b^2
""""
a = int(input("Please Enter a Value:"))
b = int(input("Please Enter b Value:"))
LHS = (a-b)*(a+b)
RHS = a**2 - b**2

print("The value of LHS:", LHS)
print("The Value of RHS:", RHS)
print (LHS==RHS)

if LHS == RHS:
    print("LHS is equal to RHS")
else:
    print("LHS is not equal to RHS")
"""

##3) a^3 - b^3 = (a-b)^3 + 3ab(a-b)
"""
a = int(input("Please Enter a Value:"))
b = int(input("Please Enter b Value:"))
LHS = a**3 - b**3
RHS = (a-b)**3 + 3*a*b*(a-b)

print("The Value of LHS:", LHS)
print("The Value of RHS:", RHS)

if LHS==RHS:
    print("LHS is equal to RHS")
else:
    print("LHS is not equal to RHS")
"""
##4) h^2 = l^2 + b^2
"""
l = int(input("Please Enter l Value:"))
b = int(input("Please Enter b Value:"))
h = (l**2 + b**2) ** 0.5

print("The Value of h:", h)
"""

##5) Square root of number
"""
a = int(input("Please Enter a Value:"))
squareroot = a**0.5

print("The Squareroot of a:", squareroot)
"""

##6) Cube root of number
"""
a = int(input("Please Enter a Value:"))
Cuberoot = a**(1/3)

print("The Cuberoot of a:", Cuberoot)
"""
##7) Area of cricle : PIR^2
"""
PI = 3.14
R = int(input("Please Enter a Value:"))
Area = PI * R**2

print("The area of Circle is:", Area)
"""

##8) Simple Interest calculation : SI =PRT/100
"""
P = int(input("Please Enter P Value:"))
R = int(input("Please Enter R Value:"))
T = int(input("Please Enter T Value:"))
SI = (P*R*T)//100

print("The Value of SI is", SI)
"""

##9) Compound Interest calculation : A = P(1+r/n)^nt (doubt)
"""
A= Final amount
P=initial principal balance
r=interest rate
n=number of times interest applied per time period
t=number of time periods elapsed
"""
"""
P = int(input("Please Enter P Value:"))
R = int(input("Please Enter R Value:"))
N = int(input("Please Enter N Value:"))
T = int(input("Please Enter T Value:"))

A = P*(1+R//N)**N*T

print("The Value of A:", A)
"""

#10). write a python program to check given number is divisible by 3 or not
"""
Num1= int(input("Please Enter Num1 Value:"))

if Num1%3==0:
    print(Num1,":is divisible by 3")
else:
    print ("The entered number is not divisible by 3")
"""
#11). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
"""
Num1= int(input("Please Enter Num1 Value:"))

if Num1%2==0:
    print("The Entered number is even and the square of number is:", Num1**2)
else:
    print("The entered number is ODD and the Cube of the number is:", Num1**3)
"""
#12). write a python program to check given positive or negative.
"""
Num1= int(input("Please Enter Num1 Value:"))

if Num1>=0:
   print("The Entered number is positive:", Num1)
else:
    print("The entered number is negative:", Num1)
"""

#13).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the number
"""
Num1= int(input("Please Enter Num1 Value:"))

if Num1%7==0:
   print("The Entered number is divisible by 7 so addition value is:", Num1+50)
else:
    print("The entered number is not divisible by 7 so substraction value is:", Num1-50)
"""

##Calculator Program
###1)WAP to create a calculator, Take 3 input where
#Number1 is input 1 and Number2 is input 2 and Descision for operation
#Descision 1 is for addition
#Descision 2 is for substraction
#Descision 3 is for multiplication
#Descision 4 is for division
#Descision 5 is for invalid descision value
"""

Num1 = int(input("Please Enter Num1 Value:"))
Num2 = int(input("Please Enter Num2 Value:"))
Descision = int(input("Please Enter Descision Value:"))

if Descision==1:
   print("The addition of Num1 and Num2 is:", Num1+Num2)
elif Descision==2:
   print("The Substraction of Num1 and Num2 is:", Num1-Num2)
elif Descision==3:
   print("The Multiplication of Num1 and Num2 is:",Num1*Num2)
elif Descision==4:
   print("The Division of Num1 by Num2 is:", Num1//Num2)
elif Descision==5:
   print("The Entered descision Value is incorrect,Please Enter Correct descision Value")
"""