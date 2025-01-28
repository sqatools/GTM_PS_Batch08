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

num =  int(input("Please enter a Valid number: "))
if num%2 == 0:
   print("It is an even number")
else:
    print("It is an odd number")
#Please enter a Valid number: 3
#It is an odd number

#Please enter a Valid number: 10
#It is an even number

