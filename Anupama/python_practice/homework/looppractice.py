for i in range(1,11,1):
#range(start,stop, step/diffrence)
    print(i, end="")
print()
print("-"*50)
for j in range(-10,0,1):
    print(j, end="")
    print()
print("-"*50)
#apply if condition in loop
#write a prog to get all the numbers devisible by 7 till 50
for i in range(1,51,1):
    if i%7==0:
        print(i, " ", end="")
        print()
print("-"*50)
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

#**** Python for loop program to print the alphabet pattern ‘O’ using python.")

for i in range(1,8):
    for j in range(1,6):
        if (i==1 or i==7) and 1<j<5:
            print("*", end=" ")
        elif 1<i<7 and (j==1 or j==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("_"*100)

#**Python Loops program to print all natural numbers from 1 to n using a while loop in python.")
n=int(input("Enter number: "))
i=1
while i<=n:
    print(i,end=" ")
    i+=1
print()
print("_"*100)

#**Python Loops program to print all alphabets from a to z using for loop \n Take chr method help to print characters with ASCII values \n chr(65) = ‘A’ \n    A-Z ASCII Range  65-90 \n     a-z ASCII Range  97-122")

for n in string.ascii_lowercase:
    print(n,end=" ")
print()
for i in string.ascii_uppercase:
    print(i, end=" ")
print()
print("_"*100)

for n in range(65,91):
    print(chr(n),end=" ")
print()
for i in range(97,123):
    print(chr(i),end=" ")
print()
print("_"*100)

#**Python Loops program to print all odd numbers between 1 to 100 using python.")
for x in range(1,101,2):
    print(x,end=" ")
print()
print("_"*100)

#**Python Loops program to print all even numbers between 1 to 100 in python.")
for x in range(2,101,2):
    print(x,end= " ")
print()
print("_"*100)

#**Python Loops program to find the sum of all natural numbers between 1 to n using python.")
n=int(input("Enter number : "))
num1=0
for x in range(1,n+1):
    num1+=x
print("The sum of all natural numbers from 1 to",n, "is",num1)
print("_"*100)

#**Python program to find the sum of all even numbers between 1 to n using python.")
n= int(input("Enter number : "))
num1=0
for i in range(2,n,2):
    num1+=i
if n%2==0:
    num1=num1+n
print("-"*100)


