##1). Python program to check given number is divided by 3 or not.
"""""""""
num1=int(input("Please Enter a Valid Number:"))

if num1%3==0:
    print(num1,"is divisible by 3")
else:
    print("Please enter another value")
"""""""""""
"""
#Please Enter a Valid Number:9
9 is divisible by 3

#Please Enter a Valid Number:10
Please enter another value
"""
##2). If else program to assign grades as per total marks.
"""
marks < 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""""
"""""""""
marks=int(input("Please enter Marks:"))

if marks<40:
    print ("Fail")
#Please enter Marks:10
#Fail
elif 40<=marks<50:
    print ("grade C")
#Please enter Marks:40
#grade C
elif 50<= marks <60:
    print("grade B")
#Please enter Marks:50
#grade B
elif 60<= marks <70:
    print("grade A")
#Please enter Marks:60
#grade A
elif 70<= marks <80:
    print("grade A+")
#Please enter Marks:70
#grade A+
elif 80<= marks <90:
    print("grade A++")
#Please enter Marks:80
#grade A++
elif 90<= marks <=100:
    print("grade EXCELLENT")
#Please enter Marks:90
#grade EXCELLENT
elif marks>100:
    print("INVALID MARK")
#Please enter Marks:101
#INVALID MARK

""""""""""""
3). Python program to check the given number divided by 3 and 5.
""""""
num4=int(input("Please Enter Valid Number:"))

if num4 % 3 == 0 and num4 % 5 == 0:
    print(num4, "is divisible by 3 and 5")
else:
    print(num4, "is not divisible by 3 and 5")
#Please Enter Valid Number:15
##15 is divisible by 3 and 5

#Please Enter Valid Number:11
#11 is not divisible by 3 and 5

"""""""""
"""""""""
##4). Python program to print the square of the number if it is divided by 11.

num5=int(input("Please Enter Valid Number:"))

if num5%11==0:
   print("The Number is divisible by 11", num5**2)
else:
   print("The Number is not divisible by 11")
#Please Enter Valid Number:110
#The Number is divisible by 11 12100

#Please Enter Valid Number:10
#The Number is not divisible by 11

"""""""""""""""

##5). Python program to check given number is a odd number or even number.
"""""""""
num =  int(input("Please enter a Valid number: "))
if num%2 == 0:
   print("It is an even number")
else:
    print("It is an odd number")
#Please enter a Valid number: 3
#It is an odd number

#Please enter a Valid number: 10
#It is an even number


"""""""

#5).  If else program to get all the numbers divided by 3 from 1 to 30.
"""""""
for i in range(1,31,1):
    if i%3==0:
        print(i, end=" ")
"""



##WAP to find the reverse of a number and check if its palindrome or not
"""""""""
num1 = 1221
var1 = num1
Reverse = 0

while num1 > 0:
    Temp = num1 % 10
    Reverse = Reverse*10 + Temp
    num1 = num1//10
print("The Reverse of the number is:", Reverse)

if var1 == Reverse:
    print("The Entered number is Palindrome")
else:
    print("The Entered number is not Palindrome")
"""""""""""

##Python program to check a given number is part of the Fibonacci series from 1 to 10
"""""
fib= [0,1,1,2,3,5,8]

num=int(input("Please enter valid number:"))

if num in fib:
    print ("The enter number is a part of Fibonacci series:", num)
else:
    print("The enter number is not a part of Fibonacci series:", num)
"""""

##Python program to check authentication with the given username and password.
"""""""""
UserName = int(input("Please Input Valid Username:"))
Password = int(input("Please Input Valid Password:"))

if UserName == Password:
    print("Authentication is Successful, login accepted")
else:
    print("Authentication is not Successful, login failed")
"""""""""""""""""

##Python program to validate user_id in the list of user_ids.
"""""""""""
List_id=[1,2,3,4,5,6,7]
user_id=int(input("Please enter valid id:"))

if user_id in List_id:
    print("User Id validated:",user_id)
else:
    print("User Id not validated:", user_id)
"""""""""""""""""

##Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
"""""""""""
num3=int(input("Please enter valid number:"))

if num3%2==0:
    print("The Number is divisible by 2:",num3**2)
elif num3%3==0:
    print("The Number is divisible by 3:",num3**3)
"""""""""""""""""""""
##Python program to describe the interview process
""""""""""""""""""""""""""""
round1=input("Enter round1 Result:")
round2=input("Enter round2 Result:")

if round1=="passed":
    print("Your round1 is passed")
    if round2=="passed":
        print("You are selected")
    else:
        print("failed in second attempt")
else:
    print("failed in first attempt")
"""""""""""""""

#Python program to determine whether a given number is available in the list of numbers or not.
"""""""""""

list_a=[1,2,3,4,5,6,7,8,9]
num=int(input("Please enter valid number:"))

if num in list_a:
    print("the given number is available in the list", num)
else:
    print("the given number is not available in the list", num)
"""""""""""""""""""""""











