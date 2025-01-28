#1). Python program to check given number is divided by 3 or not.

no1=12
if no1 %2 ==0:
    print("Number is divisible by 3",no1)
else:
    print("Number is not divisible by 3",no1)

"""
#2) If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks 

marks= float(input("Enter the marks:"))

if marks < 40:
    print("Fail", marks) #Fail 23.0
elif marks >=40 and marks <=50:
    print("Grade C", marks) #Grade C 41.0
elif marks >50 and marks <=60:
    print("grade B", marks) #grade B 55.0
elif marks >60 and marks <=70:
    print("Grade A", marks) #Grade A 70.0
elif marks >70 and marks <=80:
    print("Grade A+", marks) #Grade A+ 74.0
elif marks >80 and marks <=90:
    print("Grade A++", marks) #Grade A++ 89.0
elif marks >90 and marks <=100:
    print("grade Excellent", marks) #grade Excellent 99.0
else:
    print("Invalid marks",marks) #Invalid marks 455.0

"""

"""
#3) Python program to check the given number divided by 3 and 5.

no = float(input("Enter the Number"))
if no % 3 == 0 and no % 5 == 0:
    print("Number is divisble by 3 and 5")
else:
    print("NUmber is not divisible by 3 nor 5")
"""
"""
# 5). Python program to print the square of the number if it is divided by 11.
num = float(input("Enter the Number: "))
if num % 11 ==0:
    print("Number is divisible by 11", num**2,num) #Number is divisible by 11 1089.0 33.0
else:
    print("Number is not divisible by 11",num) #Number is not divisible by 11 23.0
"""

"""
# 6). Python program to check given number is a prime number or not.
"""
"""
#7). Python program to check given number is odd or even.

num1 = int(input("Enter a number: "))
if num1 % 2 == 0:
# Print output
    print("It is a even Number",num1) #It is a even Number 54
else:
    print("It is an odd number",num1) #It is an odd number 7
"""

"""
#8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [0, 1, 1, 2, 3, 5, 8]
num1 = int(input("Enter a number: "))

if num1 in fib:
    print("Given number is part of the Fibonacci series") #Given number is part of the Fibbonacci series 8
else:
    print("Given number is not part of the Fibonacci series") #Given number is not part of the Fibonacci series 133
"""

# 9). Python program to check authentication with the given username and password. ?????







"""
#10) Python program to validate user_id in the list of user_ids.

id_list = [1,2,3,5,6,7,8,9,10,11,12]
id = int(input("Enter ID number: "))
# Check whether input id is in list of ids
if id in id_list:
    print("It is Valid ID") #It is Valid ID 11
else:
    print("It is Invalid ID") #It is Invalid ID 13
"""

"""
# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

#num2 = 6
num2 = int(input("Enter the number:"))

if num2 % 2 == 0 : #6%2
    print(num2**2, num2)  #16 4
elif num2 % 3 == 0:
    print(num2**3,num2) #729 9
else:
    print("Number is not divisible by 2 nor 3",num2) #Number is not divisible by 2 nor 3 7
"""
"""
#12). Python program to describe the interview process.


round1 = "pass"
round2 = "pass"
round3 = "pass"
round4 = "HR Discussion Done"

if round1 == "pass":
    print("congrats first round is cleared")

    if round2 == "pass":
        print("congrats second round is cleared")
        if round3 == "pass":
            print("congrats you are selected")
            if round4 == "HR Discussion Done":
                print("Congratulations You Will get Offer letter Soon!!!!")
            else:
                print("Not ready for the given Offer")
        else:
            print("Failed in last round, try next time")
    else:
        print("Failed in second round, try next time")

else:
    print("Failed in first round, try next time")
"""

"""
#13) Python program to determine whether a given number is available in the list of numbers or not.

list1 = [22,33,49,34,65,67,12,25]
num = int(input("Enter the number:"))

if num in list1:
    print("Num is available in the list", num) #Num is available in the list 12
else:
    print("Num is not available in the list",num) #Num is not available in the list 35

"""

#14). Python program to find the largest number among three numbers.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))



"""
#15)Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible

age = int(input("Enter the Number:"))
if age >= 18:
    print("Eligible",age) #Eligible 23
else:
    print("Not Eligible",age) #Not Eligible 12
"""

