"""
1). If else program to get all the numbers divided by 3 from 1 to 30.
"""
final_list = []

for i in range(1, 31):
    if i % 3 == 0:
        final_list.append(i)
    else:
        continue
print(final_list)

print("-" * 50)

"""
2). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""
marks = int(input("Please enter your total marks out of 100: "))

if marks < 40:
    print("Grade: Fail")
elif 40 <= marks < 50:
    print("Grade: C")
elif 50 <= marks < 60:
    print("Grade: B")
elif 60 <= marks < 70:
    print("Grade: A")
elif 70 <= marks < 80:
    print("Grade: A+")
elif 80 <= marks < 90:
    print("Grade: A++")
elif 90 <= marks <= 100:
    print("Grade: Excellent")
else:
    print("Invalid Marks")

print("-" * 50)

"""
3). Python program to check the given number divided by 3 and 5.
"""

num1 = int(input("Please enter a number:"))

if num1 % 3 == 0:
    if num1 % 5 == 0:
        print("The given number is divisible by both 3 and 5")
    else:
        print("The given number is only divisible by 3")
else:
    print("The given numver is neither divisible by 3 nor 5")

print("-" * 50)

"""
4). Python program to print the square of the number if it is divided by 11.
"""

num2 = int(input("Please enter a number:"))

if num2 % 11 == 0:
    print(num2 ** 2)
else:
    print(num2)

print("-" * 50)

"""
5). Python program to check given number is a prime number or not.
"""

num3 = int(input("Please enter a number which you want to check:"))
prime_count = 0

for i in range(2,num3):
    if num3 % i == 0:
        prime_count += 1
    else:
        continue

if prime_count > 0:
    print("The provided number is not a prime number")
else:
    print("The provided number is a prime number")

print("-" * 50)

"""
6). Python program to check a given number is part of the Fibonacci series from 1 to 10.
First 20 Fibonaci numbers.
"""
Fibo_ten = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

num4 = int(input("Provide a number which you want to check whether if it is present in the first 10 Fibonacci series:"))

if num4 in Fibo_ten:
    print("The Provided number is one of the first 10 Fibonacci numbers")
else:
    print("The provided number is not one of the first 10 Fibonacci numbers")

print("-" * 50)

"""
7). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
"""
num5 = int(input("Provide you number:"))

if num5 % 2 == 0 or num5 % 3 == 0 :
    print("The provided number is divisible by 2 or 3")
    print("Square of the number is:"+str(num5**2))
else:
    print("The provided number is not divisible by 2 or 3")

print("-" * 50)

"""
8). Python program to check any person eligible to vote or not
age > 18+ : eligible
age < 18: not eligible
"""

age = int(input("Please enter your age:"))

if age >= 18 :
    print("Congrats you are eligible, vote responsibly")
elif age <= 0:
    print("You have provided an invalid age.")
else:
    print("You are not eligible yet, you will be eligible in "+str(18-age)+" years.")

print("-"*50)

"""
9). Python program to check whether any given number is a palindrome.
Input: 121
Output: palindrome
"""
palin_check = input("Enter the desired number which you wanted to check: ")

if len(palin_check) == 1:
    print("You have #entered a number with one digit")
else:
    if  int(palin_check) == int(palin_check[::-1]):
        print("The provided number is a palindrome number")
    else:
        print("The provided number is not a palindrome number")

print("-"*50)

"""
10). Python program to check if any given string is palindrome or not.
Input: ‘jaj’
output = palindrome
"""
palin_check_str = input("Enter the desired string which you wanted to check: ")

if len(palin_check_str) == 1:
    print("You have entered a string with one character")
else:
    if  palin_check_str == palin_check_str[::-1]:
        print("The provided string is a palindrome.")
    else:
        print("The provided string is not a palindrome.")

print("-"*50)

"""
11). Python program to check whether the given number is positive or negative and even or odd.
Input = 26
Output = The given number is positive and even
"""

num6 = int(input("Provide your number:"))

if num6 > 0:
    if num6 % 2 == 0:
        print("The provided number is a positive and Even number")
    else:
        print("The provided number is a positive and Odd number")
elif num6 < 0:
    if num6 % 2 == 0:
        print("The provided number is a negative and Even number")
    else:
        print("The provided number is a negative and Odd number")
else:
    print("You have provided 0 as input")

print("-"*50)
"""
12). Python program to check whether a given character is uppercase or not.
Input = A
Output = The given character is an Uppercase
"""
letter = input("Please provide your letter:")

if letter.islower():
    print("The provided letter is in lowercase")
else:
    print("The provided letter is in uppercase")

print("-"*50)
"""
13). Python program to check whether the input number if a multiple of two print “Fizz” instead of the number and for
     the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.
Input = 14
Output = Fizz
Input = 9
Output = Buzz
Input = 6
Output = FizzBuzz
"""
num7 = int(input("Enter the number:"))

if num7 == 0 or num7 < 0:
    print("You have either provided 0 or a negative number")
elif num7 % 2 == 0:
    if num7 % 3 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    print("Buzz")

print("-"*50)
"""
14). Python program to check whether an alphabet is a vowel.
Input = A
Output = True
"""
vowels = ['a', 'e', 'i', 'o', 'u']

vow_in = input("Provide the alphabet:")

if vow_in.lower() in vowels:
    print("The provided alphabet is a vowel")
else:
    print("The provided alphabet is a consonant")

print("-"*50)
"""
15).  Python program to convert the month name to the number of days.
Input = February
Output = 28/29 days
"""
month_31 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
month_30 = ['april', 'june', 'september', 'november']

month_input = input("Please enter a month:")

if month_input.lower() == 'february':
    print("Provided month has 28/29 days")
elif month_input.lower() in month_31:
    print("Provided month has 31 days")
elif month_input.lower() in month_30:
    print("Provided month has 30 days")
else:
    print("You have provided an invalid month")
print("-"*50)

"""
16). Python program that reads month and returns season for that month.
Input = February
Output = Summer
"""
summer_seasons = ['february', 'march', 'april', 'may']
rainy_seasons = ['june', 'july', 'august', 'september']
winter_seasons = ['october', 'november', 'december', 'january']

input_season = input("Provide the season:")

if input_season.lower() in summer_seasons:
    print("Provided season is a Summer season")
elif input_season.lower() in rainy_seasons:
    print("Provided season is a Rainy season")
elif input_season.lower() in winter_seasons:
    print("Provided season is a Winter season")
else:
    print("You have provided an invalid season")

print("-"*50)
"""
17). Python program to check the type of triangle.
isosceles (Has 2 equal sides)
equilateral (all equal sides)
scalar (No equal sides)
"""

side1 = int(input("Enter the 1st side:"))
side2 = int(input("Enter the 2nd side:"))
side3 = int(input("Enter the 3rd side:"))

if side1 == side2 == side3:
    print("The given sides form an equilateral triangle")
elif (side1 == side2 != side3) or (side1 == side3 != side2) or (side2 == side3 != side1):
    print("The given sides form an isosceles triangle")
else:
    print("The given sides form an scalar triangle")

print("-"*50)

"""
18). Python program to display 1/0 if the user gives Hello/Bye as output.
Input = Enter your choice: Hello
Output = 1
Input = Enter your choice: Bye
Output = 0
"""

user_in = input("Enter Hello/Bye:")

if user_in == "Hello":
    print("1")
elif user_in == "Bye":
    print("0")
else:
    print('You have entered wrong input')

print("-"*50)

"""
19). Using a python program take input from the user between 1 to 7 and print the day according to the number.
1 for Sunday 2 for Monday so on.
Input = Enter number: 7
Output = Saturday
"""

week = {'1': 'Sunday', '2': 'Monday', '3': 'Tuesday', '4': 'Wednesday', '5': 'Thursday', '6': 'Friday', '7': 'Saturday'}

week_input = input('Enter the input from 1 to 7:')

print(week[week_input])

print("-"*50)

"""
20). Python program to accept the city name and display its monuments (take Pune and Mumbai as cities).
Input = Enter city name: Pune
Output:
Shaniwar vada
Lal mahal
Sinhgad fort
"""

monuments = {'Mumbai': ['Gateway of Indian', 'Gandhi statue', 'Ajanta cave'],
             'Pune': ['Shaniwar vada', 'Lal mahal', 'Sinhgad fort']}

city = input("Please enter the city:")

print(monuments[city.capitalize()])

print("-"*50)
