"""
Home Work.

#1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the
number

"""
#1). write a python program to check given number is divisible by 3 or not
Var1 = int(input("Please Enter Value:"))
Var2 = 3

if Var1%Var2 == 0:
    print(Var1, ":is divisible by 3")
else:
    print(Var1, ":is not divisible by 3")



"""
#Please Enter Value:10
10 :is not divisible by 3
# Please Enter Value:12
12 :is divisible by 3
"""

#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd

Var3 = int(input("Please Enter Value:"))
Var4 = 2


if Var3%Var4==0:
    print("The Square of Even Number:", Var3**2)
    ##Please Enter Value:2
    ##The Square of Even Number: 4
else:
    print("The Cube of ODD Number is:", Var3**3) 
    ##Please Enter Value:3
    ##The Cube of ODD Number is: 27


#3). write a python program to check given positive or negative.
Var5 = int(input("Please Enter Value:"))
Var6 = 0

if Var5 >= Var6:
    print(Var5, "is a Positive number")
    ##Please Enter Value:0
    ##0 is a Positive number
    ##Please Enter Value:1
    ##1 is a Positive number
else:
    print(Var5, "is a Negative number")
    ##Please Enter Value:-1
    ##-1 is a Negative number


##4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the number
Var7 = int(input("Please Enter Value:"))
Var8 = 7

if Var7%Var8==0:
    print("The Number is divisible by 7 so addition value is :", Var7+50)
    ##Please Enter Value:70
    ##The Number is divisible by 7 so addition value is : 120
else:
    print("The Number is not divisible by 7 so substraction value is :", Var7-50)
    ##Please Enter Value:69
    ##The Number is not divisible by 7 so substraction value is : 19
















