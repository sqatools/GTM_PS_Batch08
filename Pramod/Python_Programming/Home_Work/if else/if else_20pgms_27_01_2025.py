'''
#1)Python program to check given number is divided by 3 or not.
n=2
if n%3==0:
    print("the given number is divisible by 3")
else:
    print("the given number is not divisible by 3")
print ("_"*50)


#2)If else program to get all the numbers divided by 3 from 1 to 30.
for i in(1,30,1):
    if i%3==0:
        print (i)
print ("_"*50)

#3)else program to assign grades as per total marks.
marks=int(input("Enter the value:"))
a,b,c,d,e=0,35,60,85,100

if 0 > marks < 35:
    print("the grade is C")
elif 35 > marks and marks < 60:   # 35>10<60
    print("the grade is B")
elif  60 > marks and marks < 85:
    print("the grade is A")
elif  100 > marks<0:
    print("the grade is Fail")
else:
    print("the grade is invalid")
print("_"*50)

# 4) Python program to check the given number divided by 3 and 5.
a=int((input("Enter the number:")))
if a%3==0  and a%5==0:
    print("the given number is divisible by 3 and 5")
else:
    print("the given number is not divisible by 3 and 5")

"""
Home Work.
#1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the
number
"""

# 5). write a python program to check given number is divisible by 3 or not
n = 2
if n % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

# The number is not divisible by 3

# 6). write a python print square(n**2) if number is even or print cube(n**3) if number is odd

a = 4
if a % 2 == 0:
    print("the number is even", a ** 2)
else:
    print("the number is odd", a ** 3)

# 7). write a python program to check given positive or negative.

b = -3
if b >= 0:
    print("the number is positive", b)
else:
    print("the number is negative", b)

# the number is negative -3

# 8).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the

c = 4
if c % 7 == 0:
    print("The number is divisible by 7, so adding 50", c + 50)
else:
    print("The number is not divisible by 7, so substract 50. ", "=", c - 50)
# The number is not divisible by 7, so substract 50.  = -46
'''
# 9) Program to check whether the number is a prime number.
num=int(input("Enter the number:"))
count=0
for i in range(2,num):
    if num%i==0:
        count+=1
        if count>0:
            print("It is  a prime number")
        else:
            print("It is  not a prime number")

#10 Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
num=int(input("Enter the fb number"))
if num in fib:
    print("the number comes under fib series ")
else:
    print("the number does not comes under fib series ")







