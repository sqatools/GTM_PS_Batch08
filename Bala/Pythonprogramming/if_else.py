# ########### 1. given number is divisible by 3 or not ###########

num=int(input("enter the number"))
if num %3==0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")
#
# ############ 2. Print square if the no is even or print cube if the no is odd #######
#
num=int(input("enter the number"))
if num %2==0:
    print("Number is even")
    print("output is:", num**2)
else:
    print("Number is odd")
    print("output is:", num**3)

# ########### 3. given number is positive or negative ##########
#
num=int(input("enter the number"))
if num>=0:
    print("Number is positive")
else:
    print("Number is negative")

####### 4. given no divisible by 7 and add 50 , else subtract 50
num=int(input("enter the number"))
if num %7==0:
    print("Number is divisible by 7")
    print("output is:", num+50)
else:
    print("Number is not divisible by 7")
    print("output is:", num-50)

####### 5. Pattern printing #############
for i in range(6):
    print(i*"*")
for i in range(4,-1,-1):
    print(i*"*")

###### 6. printing the given numbers##########
# for i in range(0,11):
#     if i !=3 or i !=6
#         print(i,end=" ")

######## 7. printing the text in between numbers#########
for i in range(3,9):
    if (i==3) or (i==5):
        print("hello")
    print(i)
######### example 8 ###########
for i in range(0,11):
        if i != 3 or i != 6:
            print(i,end=" ")

######### example 9 ######
a = int(input("enter the value"))
b = int(input("enter the value"))

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

######
for i in range(1,11,1):
#range(start,stop, step/diffrence)
    print(i, end="")
print()
print("-"*50)
for j in range(-10,0,1):
    print(j, end="")
    print()
print("-"*50)

#write a prog to get all the numbers devisible by 7 til 50
for i in range(1,51,1):
    if i%7==0:
        print(i, " ", end="")
        print()

#***python program to print a mltiplication table*****
num=8
for i in range(1,11):
    print(i, "*",num, "=", i*num)
print("-"*50)
#*****apply loop on list*********
l1=[2,4,6,8,0,11,33]
for val in l1:
    print(val, val**2)
    print()
print("-"*50)
#****** program to print * in inverted pyramid form****
for a in range(1,6,1):
    print(a*"*")
for a in range(4,0,-1):
    print(a*"*")
    print()
print("-"*50)
#****** program to print * in pyramid form****

print("*"*15,"Print * in a pyramid shape", "*"*15)
n = int(input("number of lines for pyramid: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
print()
print("-"*50)
#****** Program to find even and odd numbers form a given series****
print("*"*15,"Program to find even and odd numbers form a given series", "*"*15)
bucket = (1,3,2,4,6,7,8,9,12,54,31)
eve = 0
odd= 0

for i in bucket:
    if i%2==0:
        eve=eve+1
    else:
        odd=odd+1
print("No. of even:",eve)
print("No. of odd:", odd)
print()
print("-"*50)
#*****program to print a string 5 times*****
print("*"*15,"print a string five times", "*"*15)
a = str(input("String to print: "))
t=1
while t < 6:
    print(a)
    t=t+1
print()
print("-"*50)
#****check if the number is prime or not***
print("*"*15,"Check if the number is prime or not","*"*15)
num =  int(input("Enter a number: "))
count = 0
for i in range(2,num):
    if num%i == 0:
        count += 1
if count > 0:
    print("It is not a prime number")
else:
    print("It is a prime number")
    print()
print("-"*50)
#****** check if the given number is in the list*****
list1 = [44,77,56,97,45,65,67,64,31,23]
num = int(input("Enter a number: "))

if num in list1:
    print(f"{num} is available in the list")
else:
    print(f"{num} is not available in the list")
    print()
print("-"*50)

#*******program to findthe largest number***
print("*"*15,"Check the greatest number","*"*15)
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1>num2:
    if num1>num3:
        print(f"{num1} is the greatest")
    else:
        print(f"{num3} is the greatest")
else:
    if num2>num3:
        print(f"{num2} is the greatest")
    else:
        print(f"{num3} is the greatest")
print()
print("-"*50)

#*******program to print a half number pyramid*****
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
print("-"*50)

#*****program to authenticate username and password******
print("Python program to validate user_id in the list of user_ids")
useridlist=[1,2,3,4,5,6,7,8,9,10]
userid=int(input("Enter your user ID: "))
if userid in useridlist:
    print("Userid",userid,"is valid")
else:
    print("Invalid UserID")
print("_"*50)

#*********python program to check if the number is present in fibbonaci series***
print(" Python program to check if a given number is present in Fibonacci series from 1 to 10.")
num6=5
a,b=0,1
list1=[0]
for x in range(10):
    c=a+b
    a=b
    b=c
    if a>10:
        break
    else:
        list1.append(a)
print(list1)
if num6 in list1:
    print(num6, "is part of the fibonacci series from 1 to 10")
else:
    print(num6, "is not part of the fibonacci series from 1 to 10")
print("_"*100)


