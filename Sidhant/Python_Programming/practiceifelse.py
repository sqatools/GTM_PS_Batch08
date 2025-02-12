# 1) Python program to check given number is divided by 3 or n  ot.

num1 = 9
if num1 % 3 == 0:
    print( "num1 is divisible" )
else:
    print( "num1 is not divisible" )

# 2)  If else program to get all the numbers divided by 3 from 1 to 30.
for i in range( 1, 31 ):
    if i % 3 == 0:
        print( i, end=" " )
    # 3) If-else program to assign grades as per total marks
    marks = int( input( "Enter the mark: " ) )
    if marks < 40:
        print( "Fail" )
    elif 40 <= marks <= 50:
        print( "Grade C" )
    elif 51 <= marks <= 60:
        print( "grade B" )
    elif 61 <= marks <= 70:
        print( "Grade A" )
    elif 71 <= marks <= 80:
        print( "grade A+" )
    elif 81 <= marks <= 90:
        print( "grade A++" )
    elif 91 <= marks <= 100:
        print( "grade A+++" )
    else:
        print( "Invalid data" )
    # 4) Python program to check the given number divided by 3 and 5.
    Num = int( input( "Enter the Number:" ) )
    if Num % 3 == 0 and Num % 5 == 0:
        print( "Divisible" )
    else:
        print( "not Divisible" )
    # 5). Python program to print the square of the number if it is divided by 11.
    Num1 = int( input( "Enter the Number:" ) )
    if Num1 % 11 == 0:
        print( "number is:", Num1 ** 2 )
    else:
        print("not divisible by 11 so no square")
    # 6). Python program to check given number is a prime number or not.
sid = int( input( "Enter the number:" ) )
Count = 0
for i in range( 2, sid ):
    if sid % i == 0:
        Count += 1
if Count > 0:
    print( "not prime" )
else:
    print( "prime number" )
# 7. Python program to check given number is odd or even.
Num7 = int( input( "enter the number:" ) )
if Num7 % 2 == 0:
    print( "even number" )
else:
    print( "odd number" )
# 8. Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Num8 = int( input( "check for number:" ) )
if Num8 in fib:
    print( "Fibonacci part" )
else:
    print( "Not part of Fibonacci" )
# 9). Python program to check authentication with the given username and password.

Username = input( "Username:" )
password = input( "password:" )
if Username == password:
    print( " login verified" )
else:
    print( "Invalid Username or password" )
# 10). Python program to validate user_id in the list of user_ids.
user_ids = [2, 1, 4, 8, 9, 23, 44, 45]
user_id = int( input( "Enter the user id:" ) )
if user_id in user_ids:
    print( "user id match " )
else:
    print( "user id not found" )
# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively
Num11 = int( input( "Enter the Number:" ) )
if Num11 % 2 == 0:
    print( "Square:", Num11 ** 2 )
elif Num11 % 3 == 0:
    print( "Cube:", Num11 ** 3 )
# 13). Python program to determine whether a given number is available in the list of numbers or not.
list1 = [23, 244, 34, 22, 55, 66]
num13 = int( input( "Enter the number:" ) )
if num13 in list1:
    print( f" number:{num13} is available in list1 " )

else:
    print( f"number:{num13} not found in list" )

# 14). Python program to find the largest number among three numbers.
num1 = int( input( "enter the first number:" ) )
num2 = int( input( "enter the second number:" ) )
num3 = int( input( "enter the third number:" ) )

if num1 > num2 and num1 > num3:
    print( f"{num1} is largest number" )
elif num2 > num1 and num2 > num3:
    print( f"{num2} is largest number" )
elif num3 > num1 and num3 > num2:
    print( f"{num3} is largest number" )
else:
    print( "invalid number" )

# 15). Python program to check any person eligible to vote or not
age1 = int( input( "Enter the age :" ) )
if age1 > 18:
    print( "you are eligible to vote" )

else:
    print( "you are not eligible to vote" )
# 16). Python program to check whether any given number is a palindrome.
num16 = int( input( "enter the number for palindrome check:" ) )
new_num = num16
result = 0
while num16 > 0:
    last_digit = num16 % 10
    result = result * 10 + last_digit
    num16 //= 10
print( f"{result} is the reverse form" )
if new_num == result:
    print( f"{new_num} is palindrome number" )
# 17). Python program to check if any given string is palindrome or not.
str1 = 'jaj'
str2 = str1[::-1]

if str1 == str2:
    print( "It is a palindrome string" )
else:
    print( "It is not a palindrome string" )

# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have
# passed the exam.
marks = int( input( "Enter the marks:" ) )
if marks > 35:
    print( "You are pass" )
else:
    print( "fail" )

# 19). Python program to check whether the given number is positive or not.
num19 = int( input( "Enter the number:" ) )
if num19 > 0:
    print( "positive number" )
else:
    print( "negative number" )
# 20 Python program to check whether the given number is negative or not.
num = int( input( "Enter a number: " ) )

if num < 0:
    print( "True" )
else:
    print( "False" )
