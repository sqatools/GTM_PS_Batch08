"""

print("*"*50)
#lets check if the given numbers are even or odd

a1 = 11
b1 = a1%2

if b1==0:
    print("This is an even number :", b1)
else:
    print("This is an odd number :", b1)


print("#"*50)

#1). write a python program to check given number is divisible by 3 or not

num1 = int(input("Please enter any number :"))
num2 = num1%3

print("division output :", num2)

if num2 == 0:
    print("the number entered is divisible by 3", num1)
else:
    print("the number entered is not divisible by 3", num2)



#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
print("#"*50)

n = int(input("please enter any number :"))
Sq = n**2
Cu = n**3
n4 = n % 2

if n4 == 0:
    print("This is an even number :", n)
    print("The square of the number is :", Sq)
else:
    print("This is an odd number :", n)
    print("The cube of the number is :", Cu)

print("_"*50)

#3). write a python program to check given number is positive or negative.

V1 = float(input("enter any number :"))

if V1 > 0:
    print("This is a postive number:", int(V1))
else:
    print("This is a negative number:", int(V1))



#4).  Check given number is divisible by 7 then add 50 in the number else subtract 50 from the number

Num1 = int(input("Please enter any number:"))
Num2 = Num1 % 7
Num3 = Num1 + 50
Num4 = Num1 - 50
print("divison output:", Num2)

if Num2 == 0:

    print("This is divisible  by number 7")
    print("the new number is :", Num3)
else:

    print("This is not divisible  by number 7")
    print("the new number is :", Num4)


#5 If else program to get all the numbers divided by 3 from 1 to 30.

for a in range (0, 31):
    if a % 3 == 0:
        print(a, end=" ")

#6 If else program to assign grades as per total marks.
#marks > 40: Fail
#marks 40 – 50: grade C
#marks 50 – 60: grade B
#marks 60 – 70: grade A
#marks 70 – 80: grade A+
#marks 80 – 90: grade A++
#marks 90 – 100: grade Excellent
#marks > 100: Invalid marks

marks = int(input("Please enter your marks :"))
if marks < 40:
    print("Fail")
elif marks >= 40 and marks < 50:
    print("Grade C")
elif marks >= 50 and marks < 60:
    print("Grade B")
elif marks >= 60 and marks < 70:
    print("Grade A")
elif marks >= 70 and marks < 80:
    print("Grade A+")
elif marks >= 80 and marks < 90:
    print("Grade A++")
elif marks >= 90 and marks <= 100:
    print("Excellent marks")
else:
    print("Invalid marks")



#7 Python program to check the given number divided by 3 and 5.

Num = int(input("Enter any number of your choice : "))

if Num % 3 == 0:
    print("The number if divided by 3")
elif Num % 5 == 0:
    print("The number is divided by 5")
else:
    print("The number is not devided by 3 and 5")



#8 Python program to print the square of the number if it is divided by 11.

New = int(input("type any number : "))

if New % 11 == 0:
    print("The number if divided by 11 and its square root is", New ** 2)
else:
    print("Dont proceed as the number is not divided by 11")

"""

#9 Python program to check given number is a prime number or not.

Num1 = int(input("type any number : "))

if Num1 %%






