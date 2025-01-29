'''
Program 1:

64)Python program to accept marks from the user allot the stream based on the following criteria.
Marks>85: Science
Marks>70: Commerce
35<Marks<70: Arts
Marks<35: Fail
Input = Marks: 88
Output = Science

'''

print("#"*50)
print("Program 1")
ch = input("Do you want to proceed to check stream allocation based on marks, please type (Yes/No): ")

if ch == 'y' or ch =='yes' or ch == 'Y' or ch == 'Yes' or ch == 'YES':
    print("To check stream allocation can be done based on the criteria")
    marks = int(input("Please enter the mark: "))
    print("Your mark is: ", marks)
    if marks >= 85 and marks <= 100:
        print("Congratulations!!! based on your mark criteria, you are allocated to Science stream")
    elif marks >= 70:
        print("Congratulations!!! based on your mark criteria, you are allocated to Commerce stream")
    elif marks >= 35 and marks < 70:
        print("Congratulations!!! based on your mark criteria, you are allocated to Art stream")
    elif marks>=0 and marks < 35:
        print("Fail, Better luck next time!!!")
    else:
        print("Please enter valid marks")
else:
    print("Thank you for visiting")

'''
Program 2:

58). Using a python program take input from the user between 1 to 7 and print the day according to the number. 
1 for Sunday 2 for Monday so on.
Input = Enter number: 7
Output = Saturday

'''
print("="*50)
print("Program 2")
print("To check which day according to the given number")
user_input_2 = int(input("Please enter any number between 1 to 7: "))
print("The number is: ", user_input_2)

if user_input_2 == 1:
    print("Based on the given number its Sunday")
elif user_input_2 == 2:
    print("Based on the given number its Monday")
elif user_input_2 == 3:
    print("Based on the given number its Tuesday")
elif user_input_2 == 4:
    print("Based on the given number its Wednesday")
elif user_input_2 == 5:
    print("Based on the given number its Thursday")
elif user_input_2 == 6:
    print("Based on the given number its Friday")
elif user_input_2 == 7:
    print("Based on the given number its Saturday")
else:
    print("Its Invalid number")

'''
Program 3:

56). Python program to display 1/0 if the user gives Hello/Bye as output.
Input = Enter your choice: Hello
Output = 1
Input = Enter your choice: Bye
Output = 0

'''
print("="*50)
print("Program 3")
print("Program to display 1/0, if the user gives Hello/Bye as output")

user_input_3 = input("Enter your choice (Hello or Bye): ")
print("Your choice is: ", user_input_3)
if user_input_3 == 'Hello' or user_input_3 == 'hello' or user_input_3 == 'HELLO':
    print("The choice is Hello, hence value is: ", 1)
elif user_input_3 == 'Bye' or user_input_3 == 'bye' or user_input_3 == 'BYE':
    print("The choice is Bye, hence value is: ", 0)
else:
    print("Invalid choice entered")

'''
Program 4:

52). A shop will give a 10% discount if the bill is more than 1000, and 
20% if the bill is more than 2000. 
Using the python program Calculate the discount based on the bill.
Input = 1500
Output = Discount amount: 150

'''
print("="*50)
print("Program 4")
print("Program to calculate the discount based on bill")

bill_amt = int(input("Enter the bill amount: "))
print("The bill amount is: ", bill_amt)

if bill_amt >= 1000 and bill_amt < 2000:
    discount = 10
    discount_amt = bill_amt * 10/100
    print("Since the amount is greater than 1000 to less than 2000, shop will give 10% discount")
    print("Discount amount is: ", discount_amt)
elif bill_amt>=2000:
    discount = 20
    discount_amt = bill_amt * 20/100
    print("Since the amount is greater than 2000, shop will give 20% discount")
    print("Discount amount is: ", discount_amt)
else:
    print("Invalid value entered, kindly enter valid amount")
'''
Program 5:

50). Python program to find employees eligible for bonus. 
A company decided to give a bonus of 10% to employees. 
If the employee has served more than 4 years. 
Ask the user for years served and check whether an employee is eligible for a bonus or not.
Input = Enter Years served: 5
Output = You are eligible for a bonus

'''
print("="*50)
print("Program 5")
print("To check employees eligible for bonus")

years_served = int(input("Enter the years served by the employee in the company: "))
print("The employee has served ", years_served, " years")

if years_served >= 4 and years_served <80:
    print("Congratulations!!!, You are eligible for the 10% bonus")
elif years_served > 0 and years_served < 4:
    print("Better luck next time, Since you are served ", years_served , "which is not eligible for bonus")
elif years_served < 0:
    print('Since there is no experience, there is No bonus')
else:
    print("Invalid served experience is entered")

'''
Program 6:
49). Python program to create 10 groups of numbers between 1-100 and 
find out given input belongs to which group using python nested if else statements.
Input= 36
Output = The given number belongs to 4th group
'''
print("="*50)
print("Program 6")
print("To create 10 groups of number between 1 to 100")
group_num = int(input("Please Enter any number from 1-100: "))
print("The number is: ", group_num)
if group_num > 0:
    print("To check which group it belong")
    if group_num >=1 and group_num <=10:
        print("The given number is between 1-10, which belongs to 1st group")
    elif group_num >=11 and group_num <=20:
        print("The given number is between 11-20, which belongs to 2nd group")
    elif group_num >=21 and group_num <=30:
        print("The given number is between 21-30, which belongs to 3rd group")
    elif group_num >=31 and group_num <=40:
        print("The given number is between 31-40, which belongs to 4th group")
    elif group_num >=41 and group_num <=50:
        print("The given number is between 41-50, which belongs to 5th group")
    elif group_num >=51 and group_num <=60:
        print("The given number is between 51-60, which belongs to 6th group")
    elif group_num >=61 and group_num <=70:
        print("The given number is between 61-70, which belongs to 7th group")
    elif group_num >=71 and group_num <=80:
        print("The given number is between 71-80, which belongs to 8th group")
    elif group_num >=81 and group_num <=90:
        print("The given number is between 81-90, which belongs to 9th group")
    elif group_num >=91 and group_num <=100:
        print("The given number is between 91-100, which belongs to 10th group")
    else:
        print("The number is out of range")
else:
    print("Invalid number")


'''
Program 7:
47). Python program to check whether the given input is a dictionary or not.
Input:
A={‘name’:’Virat’,’sport’:’cricket’}
Output = True
'''
print("="*50)
print("Program 7")
print("To check whether given input is dictionary")
A={'name':'Virat','sport':'cricket'}
print("The given input is: ", type(A))

if type(A) == dict:
    print("The given input is dictionary", type(A)==dict)
else:
    print("The given input is not a dictionary")

'''
Program 8:
37). Python program to check whether a triangle is isosceles or not. 
An isosceles triangle is a triangle with (at least) two equal sides.
Input:
Enter the length of the sides of the triangle
A=10
B=15
C=10
Output = True
'''
print("="*50)
print("Program 8")
print("To check whether a triangle is isosceles or not")

num1 = int(input("Enter the first length of the side of the triangle: "))
num2 = int(input("Enter the second length of the side of the triangle: "))
num3 = int(input("Enter the third length of the side of the triangle: "))

if num1 > 0 and num2 >0 and num3 >0:
    print("The first length of the side is: ", num1)
    print("The second length of the side is: ", num2)
    print("The third length of the side is: ", num3)

    if num1 == num2 or num1 ==num3 or num2 == num3:
        print("The triangle is isosceles triangle with (at least) two equal sides.")
    else:
        print("Its not an isosceles triangle, two sides are not equal")
else:
    print("Invalid number, Please enter valid length")

'''
Program 9:
31). Python Python program to check whether the input number 
if a multiple of two print “Fizz” instead of the number and 
for the multiples of three print “Buzz”. 
For numbers that are multiples of both two and three print “FizzBuzz”.
Input = 14
Output = Fizz
Input = 9
Output = Buzz
Input = 6
Output = FizzBuzz
'''
print("="*50)
print("Program 9")
print("To check whether the i/p number is multiples of 2 (or) multiples of 3 (or) multiples of 3 and 2")
num4 = int(input("Enter the input number: "))
print("The input number is: ", num4)

if num4 > 0:
    print("Checking whether input number is multiple of 2 or 3 or both")
    if num4 %2 ==0 and num4 %3 ==0:
        output = "FizzBuzz"
        print("The number is multiple of 2 and 3 ", output)
    elif num4 % 2 == 0:
        output = "Fizz"
        print("The number is multiple of 2, hence output is: ", output)
    elif num4 % 3 == 0:
        output = "Buzz"
        print("The number is multiple of 3, hence output is: ", output)
    else:
        print("Not multiple by 3 or 2")
else:
    print("Invalid number")

'''
Program 10:

30). Python program to check whether a given year is a leap or not.
Input = 2000
Output = The given year is a leap year
HINT:
conditions to check whether a year is a leap or not. a)year%100 != 0 or year%400 == 0, b) year%4 == 0.
'''
print("="*50)
print("Program 10")
print("To check whether given year is leap or not")

year = int(input("Enter the year: "))

if year > 0:
    print("The year is: ", year)
    if (year%100 != 0 or year%400 == 0) and year%4 ==0:
        print("Its the leap year")
    else:
        print("Its not a leap year")
else:
    print("Invalid year")


'''
Program 11:

17). Python program to check if any given string is palindrome or not.
Input: ‘jaj’
output = palindrome
'''
print("="*50)
print("Program 11")
print("To check whether given string is palindrome")
input_value = input("Enter the string to check palindrome: ")
reverse_string= input_value[::-1]
print("input value: ", input_value)
print("reverse string: ", reverse_string)
if input_value == reverse_string:
    print("palindrome", input_value == reverse_string)
else:
    print("not a palindrome", input_value != reverse_string)

'''
Program 12:

8). Python program to check a given number is part of the Fibonacci series from 1 to 10.

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''
print("="*50)
print("Program 12")
print("To check number is part of Fibonacci series 1 to 10")
fib = [0,1,1,2,3,5,8,13,21,34]
print("The fibonacci series are: ", fib)
for k in range(0, 10):
    if k in fib:
        print("The number is part of Fibonacci series: ", k)

'''
Program 13: 

10). Python program to validate user_id in the list of user_ids.
'''
print("="*50)
print("Program 13")
user_ids = [10,20,30,40,50,60,70]
print("To validate user id in the list of user ids: ", user_ids)
#for l in range(10, 100):
user_id = int(input("Enter any user_id from 10 to 70: "))
if user_id in user_ids:
    print("user_id available in user_ids list: ", user_id)
else:
    print("Invalid user_id is entered")

'''
Program 14:

57). Python program to accept the car price of a car and display the road tax to be paid according to the
following criteria:
Cost price<500000 –> tax:15000
Cost price<1000000 –> tax:50000
Cost price<1500000 –> tax:80000
Input = Car Price: 1200000
Output = Tax payable: 50000

'''
print("="*50)
print("Program 14")
print("Program to display road tax based on car price")
car_price = int(input("Enter the car price: "))

print("The car price is: ", car_price)

if car_price <= 500000:
    tax = 15000
    print("Tax payable is: ", tax)
elif car_price>500000 and car_price <=1000000:
    tax = 50000
    print("Tax payable is: ", tax)
elif car_price>1000000 and car_price <=1500000:
    tax = 80000
    print("Tax payable is: ", tax)
elif car_price<0:
    print("Invalid amount")
else:
    print("Tax is not available for this ", car_price, " amount")

'''
Program 15:

32). Python program to check whether an alphabet is a vowel.
Input = A
Output = True
'''
print("="*50)
print("Program 15")
print("Program to check whether entered alphabet is a vowel")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

user_in_vowel = input("Please enter an alphabet: ")
print("The entered alphabet is: ", user_in_vowel)
if user_in_vowel in vowels:
    print(user_in_vowel, "is a vowel")
else:
    print(user_in_vowel, "is not a vowel")

'''
Program 16:

34).  Python program to convert the month name to the number of days.
Input = February
Output = 28/29 days
'''
print("="*50)
print("Program 16")
print("To convert the month name to number of days")
month_name = input("Enter any month name: ")
print("The month name is: ", month_name)

if month_name == 'january' or month_name == 'January' or month_name == 'jan' or month_name == 'JAN':
    jan_days = 31
    print("The number of days in ", month_name, ": ",jan_days)
elif month_name == 'february' or month_name == 'February' or month_name == 'feb' or month_name == 'FEB':
    feb_days = 28/29
    print("The number of days in ", month_name, ": ",feb_days)
elif month_name == 'march' or month_name == 'March' or month_name == 'mar' or month_name == 'MAR':
    mar_days = 31
    print("The number of days in ", month_name, ": ",mar_days)
elif month_name == 'april' or month_name == 'APRIL' or month_name == 'apr' or month_name == 'APR':
    apr_days = 30
    print("The number of days in ", month_name, ": ",apr_days)
elif month_name == 'may' or month_name == 'May' or month_name == 'MAY':
    may_days = 31
    print("The number of days in ", month_name, ": ",may_days)
elif month_name == 'june' or month_name == 'June' or month_name == 'jun' or month_name == 'JUN':
    june_days = 30
    print("The number of days in ", month_name, ": ",june_days)
elif month_name == 'july' or month_name == 'July' or month_name == 'jul' or month_name == 'JUL':
    jul_days = 31
    print("The number of days in ", month_name, ": ",jul_days)
elif month_name == 'august' or month_name == 'August' or month_name == 'aug' or month_name == 'AUG':
    aug_days = 31
    print("The number of days in ", month_name, ": ",aug_days)
elif month_name == 'september' or month_name == 'September' or month_name == 'sep' or month_name == 'SEP':
    sep_days = 30
    print("The number of days in ", month_name, ": ",sep_days)
elif month_name == 'october' or month_name == 'October' or month_name == 'oct' or month_name == 'OCT':
    oct_days = 31
    print("The number of days in ", month_name, ": ",oct_days)
elif month_name == 'november' or month_name == 'November' or month_name == 'nov' or month_name == 'NOV':
    nov_days = 30
    print("The number of days in ", month_name, ": ",nov_days)
elif month_name == 'december' or month_name == 'December' or month_name == 'dec' or month_name == 'DEC':
    dec_days = 31
    print("The number of days in ", month_name, ": ",dec_days)
else:
    print("Please enter valid month name")

'''
Program 17:

48). Python program to check the eligibility of a person to sit on a roller coaster ride or not. Eligible 
when age is greater than 12.
Input = 15
Output = You are eligible
'''
print("=" * 50)
print("Program 17")
print("To check the eligibility of a person to sit on a roller coaster ride")
age = int(input("Enter your age: "))
print("Your age is: ", age)
if age >=12 and age < 100:
    print("You age is greater than and equal to 12, \n hence you are eligible person to sit on a roller coaster ride")
elif 0<= age <12:
    print("Your age is not greater than 12, \n hence you are not eligible person to sit on a roller coaster ride")
else:
    print("Due to the health safety, you are not eligible to sit on a roller coaster ride")
'''
Program 18:

54). Python program to check the student’s eligibility to attend the exam based on his/her attendance. 
If attendance is greater than 75% eligible if less than 75% not eligible.
Input = Enter attendance: 78
Output = You are eligible
'''
print("="*50)
print("Program 18")
print("To check student eligibilty to attend exam based on attendance")

attendance = input("Enter the student attendance: ")
print("Your attendance is: ", attendance, "%")

if int(attendance) >= 75 and int(attendance) <= 100:
    print("Congrats, you are eligible to attend the exam")
elif 0<= int(attendance) < 75:
    print("Better luck next time, since your attendance is less than 75% \n you are not eligible to attend the exam")
else:
    print("Invalid value entered, please enter valid attendance number")
'''
Program 19:

61). Python program to find the lowest number between three numbers.
Input:
A=45
B=23
C=68
Output = 23
'''
print("="*50)
print("Program 19")
print("To find the lowest number between three numbers")
A = 45
B = 23
C = 68
print("The value of A: ", A, end=";")
print("The value of B: ", B, end=";")
print("The value of C: ", C)
if A < B and A < C:
    print("Output: A is the lowest number", A)
elif B < A and B < C:
    print("Output: B is the lowest number", B)
elif C < A and C < B:
    print("Output: C is the lowest number", C)
else:
    print("None of the number is lowest")
'''
Program 20:
6). Python program to check given number is a prime number or not.
o/p: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.

'''
print("="*50)
print("Program 20")
print("Check whether given number is prime number or not")
num = int(input("Enter any number: "))
n = 2

if num <= 1:
    print(num, "Its an Invalid number and not a prime number")
elif num == 2:
    print(num, "It is a prime number")
elif num%n != 0:
    print("It is a Prime number", num%n)
else:
    print("Its Not a prime number", num%n)

'''
Program 21:

29). Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill
Input = 350
Output = 438.75

'''
print("="*50)
print("Program 21")
print("Program to find Electricity bill")
ch = input("Do you want to view Rupees for each units, type (yes/no): ")
charge = 0
if ch == 'y' or ch == 'yes' or ch == 'Y' or ch == 'Yes' or ch =='YES':
    print("Following are the rate for different units")
    print("1.Up to 50 units rs 0.50/unit")
    print("2.Up to 100 units rs 0.75/unit")
    print("3.Up to 250 units rs 1.25/unit")
    print("4.above 250 rs 1.50/unit")
    print("An additional surcharge of 17% is added to the bill")
    units = int(input("Please enter the units spemd: "))

    if units <=50:
        bill = units * 0.50
    elif units >=51 and units <=100:
        bill = (50 * 0.50) + (units-50) * 0.75
    elif units >=101 and units <=250:
        bill = (50 * 0.50) + (50 * 0.75) + (units-100) * 1.25
    elif units >=251:
        bill = (50 * 0.50) + (50 * 0.75) + (150 * 1.25) + (units-250) * 1.50
    else:
        print("invalid input")

    surcharge = bill * (17/100)
    total_bill = bill + surcharge
    print("The total bill for, ", units, " units is Rs ", total_bill)
elif ch == 'n' or ch == 'no' or ch == 'N' or ch == 'No' or ch == 'No':
    print("Since you typed 'No' the Rate for different units is not displayed")
else:
    print("Thank you")
