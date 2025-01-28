"""
Math Operation
+ : plus operator
- :  subtraction'
* : multiplication
/ :  divide with single /
// : divide with double //
% :  remainder operator
** :  power operator
== :  equal to operator
!= :  not equal to operator
"""


# plus operator
num1 = 10
num2 = 30
plus1 = num1 + num2
print("Addition is:", plus1)
#Addition is: 40#
########################## operator ###########################################
# add two strings with plus operator #

str1 = 'Hello'
str2 = 'World'
print(str1 +" "+str2)  # Hello World

# can not add string with integer
v1 = 50
v2 = 'Hello'

# print(v1 + v2)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Subtraction Operator #
a1 = 500
a2 = 400
print("subtraction :", a2-a1)
# subtraction : -100
########################## operator ###########################################

# Multiplication operator #
b1 = 30
b2 = 2
print("multiplication :", b1*b2)
# multiplication : 60


# multiply string with integer
s1 = 'WelCome '
s2 = 5

# if we multiply the string with number, then it will repeat the string, that number of times
print("string with int multiply :", s1*s2)
# string with int multiply : WelCome WelCome WelCome WelCome WelCome

########################## operator ###########################################
# draw a line
print("_"*100)


########################## operator ###########################################
#division Program#
d1 = 20
d2 = 4
# division with single / return float or pointer output.
print("division with single / :", d1/d2)
# division with single / : 5.0

# division with double // return integer output or whole number
print("division with double // :", d1//d2)
# division with double // : 5

print("_"*50)

# remainder operator #
r1 = 28
r2 =5

print(" remainder output :", r1 % r2)
# remainder output : 3

print("_"*50)
# power operator #

p1 = 8
print("square of p1 :", p1**2)
# square of p1 : 64

print("cube of p1 :", p1**3)
#cube of p1 : 512#

# solve the below equation
# (a+b)^2 = a^2 + b^2 + 2ab
a = 20
b = 10
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print("output for lhs :", lhs)
print("output for rhs :", rhs)
# use == operator to compare 2 values
print(lhs == rhs)
