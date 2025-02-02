print("_"*50)
# check given numbers are equal or not
a = 40
b = 50

if a == b:
    # if condition is True
    print("Numbers are equal:", a, b)
else:
    # if condition is False
    print("Numbers are not equal :", a, b)


print("_"*50)
# write a program to check given number is even or odd

num1=int(input("Enter the first number: "))
var1 = 2
if (num1%var1) == 0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)


# write a python program to check greater number among three values

a = 30
b = 40
c = 50

if a > b and a > c:
    print("A has greater value :", a)
elif b > a and b > c:
    print("B has greater value :", b)
elif c > a and c >  b:
    print("C has greate value :", c)
else:
    print("No one has greater value")


print("_"*50)
# write a python program to provide the grade to the students as per marks obtained.
marks = -20

if 35 < marks <= 50:
    print("Passed with C grade")
elif marks >50 and marks <=70:
    print("Passed with B Grade")
elif marks > 70 and marks <=90:
    print("Passed with A grade")
elif marks > 90 and marks <= 100:
    print("Password Excellent Grade A++")
elif marks > 100:
    print("Invalid value, marks can not be more than 100")
elif marks < 0:
    print("invalid marks, value should be positive")
else:
    print("Failed in Exam, better luck next time")


print("_"*50)
# write a python program to check the given number is divisible by 3 or 7
A = 30
if (A%3 == 0 or A%7 == 0)
    print("A is divisible by 3 or 7")
else:
    print("A is not divisible by 3 or 7")