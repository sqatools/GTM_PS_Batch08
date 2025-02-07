# Python Programs

#Program 1
#Python program to check given number is divided by 3 or not.

num = int(input("Enter a number: "))
var = 3
if num%var == 0:
	print(f"Number", num , " is divisible by 3 ", )
else:
	print(f"Number", num , " is not divisible by 3")


# Program 2
print("_"*50)
#If else program to get all the numbers divided by 3 from 1 to 30.
num = 3
print("The table of 3 ")
for i in range(1,31):
    if i%3 == 0:
        print(num,  "*",i//3 , "=", i)

#print(len("String"))

#Program 3
print("_"*40)
#If-else program to assign grades as per total marks
marks = int(input("Enter the Marks:  "))
if marks > 80:
    print("Student has scored Grade A")
elif 60 <= marks >70:
    print("Student has scored Grade B")
elif 50 <=marks >60:
    print("Student has scored Grade C")
else:
    print("Student has scored Grade D")

print("_"*40)

#Program 4
## Python program to check the given number divided by 3 and 5.
num = int(input("Enter a number: "))
if num%3 == 0 and num%5 == 0:
    print("The number is divisible by both 3 and 5: ",num )
else:
    print("The number is not divisible by 3 and 5: ", num)

print("_"*40)

#Program 5
##Python program to print the square of the number if it is divided by 11.
num = int(input("Enter a number: "))
if num%11 == 0:
    print("The given number", num, " is divisible by 11")
else:
    print(f"The given number {num} not divisible by 11")

print("_"*40)

#Program 6
##Python program to check given number is a prime number or not.
num =  int(input("Enter a number: "))
count = 0

for i in range(2,num):
    if num%i == 0:
        count += 1
if count > 0:
    print("It is not a prime number")
else:
    print("It is a prime number")

print("_"*40)

#Program 7
##Python program to check given number is odd or even.
num = int(input("Enter a number: "))
if num%2 == 0:
    print("The given number", num, " is even")
else:
    print("The given number", num, " is odd")

print("_"*40)

#Program 8
##Python program to check a given number is part of the Fibonacci series from 1 to 10.

num = int(input("Enter a number (1 to 10): "))

if num in [1, 1, 2, 3, 5, 8]:
    print(f"{num} is part of the Fibonacci series from 1 to 10.")
else:
    print(f"{num} is NOT part of the Fibonacci series from 1 to 10.")

print("_"*40)

#Program 9
##Python program to check authentication with the given username and password.
# Take username and password as input through the user
UserName = "admin"
PassWord = "admin@123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == UserName and password == PassWord:
    print("You are a valid user")
    print("Authentication successful")
else:
    print("You are not allowed to Login")
    print("Authentication failed!")

print("_"*40)

#a given character is uppercase or not.

char = input("Enter a character: ")
if char.isupper():
    print("True")
else:
    print("False")