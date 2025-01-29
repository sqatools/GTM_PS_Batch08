#1). Python program to check given number is divided by 3 or not

num1=33
result=True if num1%3==0 else False
print(result)
print("_"*100)

#2). If else program to get all the numbers divided by 3 from 1 to 30.
for x in range(1,31):
    if x%3==0:
        print(x,"is divisible by","3")
print("_"*100)

#3). If else program to assign grades as per total marks.
#marks > 40: Fail
#marks 40 – 50: grade C
#marks 50 – 60: grade B
#marks 60 – 70: grade A
#marks 70 – 80: grade A+
#marks 80 – 90: grade A++
#marks 90 – 100: grade Excellent
#marks > 100: Invalid marks

total_marks=59
if total_marks>100:
    print("Invalid marks")
elif 90<=total_marks<=100:
    print("Grade Excellent")
elif 80<=total_marks<=89:
    print("Grade A++")
elif 70<=total_marks<=79:
    print("Grade A+")
elif 60<=total_marks<=69:
    print("Grade A")
elif 50<=total_marks<=59:
    print("Grade B")
elif 40<=total_marks<=49:
    print("Grade C")
else:
    print("Fail")
print("_"*100)

#4). Python program to check the given number divided by 3 and 5.
num2=67
if num2%3==0 and num2%5==0:
    print(num2,"is divisible by 3 and 5")
else:
    print(num2,"is not divisible by 3 and 5")
print("_"*100)

#5). Python program to print the square of the number if it is divided by 11.
num3=22
if num3%11==0:
    print(num3**2)
else:
    print(num3,"is not divisible by 11")
print("_"*100)

#6). Python program to check given number is a prime number or not.
num4=5
a=0
for i in range(2,num4+1):
    if num4%i==0:
        a=a+1

if a==1:
    print(num4,"is a prime number")
else:
    print(num4,"is not a prime number")
print("_"*100)

#7). Python program to check given number is odd or even.
num5=47
if num5%2==0:
    print(num5,"is an even number")
else:
    print(num5, "is an odd number")

print("_"*100)

print("8). Python program to check a given number is part of the Fibonacci series from 1 to 10.")
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

"""
print("9). Python program to check authentication with the given username and password.")
un=input("Username: ")
pw=input("Password: ")
if un==pw:
    print("The Username password in valid")
else:
    print("The Username Password in not valid")
print("_"*100)

print("10). Python program to validate user_id in the list of user_ids")
useridlist=[1,2,3,4,5,6,7,8,9,10]
userid=int(input("Enter your user ID: "))
if userid in useridlist:
    print("Userid",userid,"is valid")
else:
    print("Invalid UserID")
print("_"*100)
"""
print("11). Python program to print the square or cube if the given number is divided by 2 or 3 respectively.")
num6=11
if num6%2==0:
    print("The square of",num6,"is",num6**2)
if num6%3==0:
    print("The cube of",num6,"is",num6**3)
if num6%2!=0 and num6%3!=0:
    print("The number is not divisible by 2 or 3 ")
print("_"*100)

print("12). Python program to describe the interview process.")










