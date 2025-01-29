"""
if condition
   code
else
   code
"""
print("_" * 50)

# Ques: check given numbers are equal or not
a = 30
b = 50
if a == b:
    print("Values of a and b are equal", a, b)
else:
    print("Values of a and b are not equal", a, b)

print("Condition output:", a == b)

# Ques: write a program to check given number is even or odd
# num1 = int(input("Enter the value for which you want to check odd and even: "))
a1 = 3
if a1 % 2 == 0:
    print("a1 is Even number")
else:
    print("a1 is odd number")

################################# Logical Operator #################################
"""
Logical Operator
> : greater than
< : Less than
>= : greater than equal to
<= : less than equal to
== : equal to
!= : Not equal to
in : in operator
is : is operator
is not : is not operator

 AND Logic
 True and False : False
 False and True : False
 False and False : False
 True and True : True

 OR Logic
 True or False : True
 False or True : True
 True or True : True
 False or False : False
"""

"""
if cond1:
   code
elif cond2:
   code
elif cond3:
   code
else:
   code

"""
print("_" * 60)
# write a python program to check greater number among three values

a = 30
b = 30
c = 30
if a > b and a > c:
    print("A is greater", a)
elif b > a and b > c:
    print("B is greater", b)
elif c > a and c > b:
    print("C is grater", c)
elif a == b == c:
    print("All values are equal")
elif a == b != c:
    print("A and B has equal values")
else:
    print("No one has greater value")

print("_" * 50)
# write a python program to provide the grade to the students as per marks obtained.
marks = 50
if 35 < marks <= 50:
    print("Passed with C grade")
elif 50 < marks <= 70:
    print("Passed with B Grade")
elif 70 < marks <= 90:
    print("Passed with A grade")
elif 90 < marks <= 100:
    print("Password Excellent Grade A++")
elif marks > 100:
    print("Invalid value, marks can not be more than 100")
elif marks < 0:
    print("invalid marks, value should be positive")
else:
    print("Failed in Exam, better luck next time")

print("_" * 50)
# write a python program to check the given number is divisible by 3 or 7
A = 20
if (A % 3 == 0 or A % 7 == 0) and A % 5 == 0:
    print("A is divisible by 3 or 7")
else:
    print("A is not divisible by 3 or 7")
