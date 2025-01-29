# 1). Python program to check given number is divided by 3 or not.
num1 = int(input("Enter the integer value : "))
if num1 % 3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by three")

# 2). If else program to get all the numbers divided by 3 from 1 to 30.
for i in range(1, 31, 1):
    if i % 3 == 0:
        print(f"{i} is divisible")

print("_" * 60)
"""
3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""
marks = int(input("Enter your marks : "))
if marks < 40:
    print("Fail")
elif 40 <= marks < 50:
    print("Grade C")
elif 51 < marks <= 60:
    print("Grade B")
elif 61 < marks <= 70:
    print("Grade A")
elif 71 < marks <= 80:
    print("Grade A+")
elif 81 < marks <= 90:
    print("Grade A++")
else:
    91 < marks <= 100
    print("Excellent")

print("_" * 60)
# 4). Python program to check the given number divided by 3 and 5.
num2 = int(input("Enter your number : "))

if num2 % 3 == 0 and num2 % 5 == 0:
    print(f"{num2} --> is divided by 3 and 5")
else:
    print(" Number is not divided by 3 and 5")

print("_" * 60)
# 5). Python program to print the square of the number if it is divided by 11.
num3 = int(input("Enter your number : "))
if num3 % 11 == 0:
    print(f"{num3} is divisible by 11 and square of {num3} is:", num3 ** 2)
else:
    print("Number is not divisible by 11")

print("_" * 60)
# 6). Python program to check given number is a prime number or not.
num4 = int(input("Enter your number: "))
print("Prime" if num4 % 2 == 0 else "Odd")

print("_" * 60)
# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
num5 = int(input(" 8. Enter your number to check if it's a part of series or not : "))
if num5 in fib:
    print(f"Number is a part of series: {num5}")
else:
    print(f"Number is not a part of series: {num5}")

print("_" * 60)
# 9). Python program to check authentication with the given username and password.
username = "pankajprasad30@gmail.com"
password = "password_nahi_milega"
user_name = str(input("Enter your user-name: "))
if user_name == username:
    print("User name is correct ")
    password_ = str(input("Enter your password: "))
    if password_ == password:
        print("User name & password both are correct")
    else:
        print("password is wrong")
else:
    print("User name is not valid")

print("_" * 60)
# 10). Python program to validate user_id in the list of user_ids.
userID_list = [20, 30, 40, 50, 70, 90]
userID = int(input("Enter your user id : "))
if userID in userID_list:
    print("User id is present")
else:
    print("user id is not present")

print("_" * 60)
# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
num6 = int(input("Enter your number : "))
if num6 % 2 == 0:
    print("Square of your number is :", num6 ** 2)
elif num6 % 3 == 0:
    print("Qube of your number is :", num6 ** 3)
else:
    print("Number is not divisible by 2 or 3")

print("_" * 60)
# 12). Python program to describe the interview process.

first_round = str(input("Enter your first round result: "))
if first_round == "pass":
    print("Congratulations! your first round is clear ")
    second_round = str(input("Enter your second round result: "))
    if second_round == "pass":
        print("Congratulations! your final round is clear and you got select in our company ")
    else:
        print("Sorry! your final round is not cleared")
else:
    print("Sorry! your first round is not clear")

# 13). Python program to determine whether a given number is available in the list of numbers or not.
list1 = [33, 44, 55, 66, 77, 88, 99]
num7 = int(input("Enter your number :"))
if num7 in list1:
    print(f"{num7} is present in list")
else:
    print(f"{num7} is not present in list")

# 14). Python program to find the largest number among three numbers.
num8 = int(input("Enter your 1st number: "))
num9 = int(input("Enter your 2nd number: "))
num10 = int(input("Enter your 3rd number: "))
if num8 > num9 and num8 > num10:
    print(f"{num8} is largest number")
elif num9 > num10 and num9 > num8:
    print(f"{num9} is largest number")
else:
    print(f"{num10} is the largest number")

# 15). Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

# 16). Python program to check whether any given number is a palindrome.
palindrome_number = 12321
palindrome_check = str(palindrome_number)
if palindrome_number == int(palindrome_check[::-1]):
    print("Its a palindrome number")
else:
    print("not a palindrome")

# 17). Python program to check if any given string is palindrome or not.
string_in = str(input("Enter your string to check its palindrome or not"))
if string_in == str(string_in[::-1]):
    print("palindrome")
else:
    print("not palindrome")

# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have
# passed the exam.

marks = int(input("Enter your marks to check pass or fail"))
if marks >= 45:
    print("pass")
else:
    print("fail")

# 19). Python program to check whether the given number is positive or not.
num11 = int(input("Enter your number: "))
if num11 > 0:
    print("its positive")
elif num11 == 0:
    print("number is neutral")
else:
    print("number is negative")

# 20). Python program to check whether the given number is negative or not.
num12 = int(input("Enter your number: "))
if num12 < 0:
    print("Number is negative")
else:
    print("Number is positive")