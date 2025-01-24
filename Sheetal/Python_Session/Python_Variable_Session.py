"""
Math Operation
+ : plus operator
- :  subtraction
* : multiplication
/ :  divide with single /
// : divide with double //
% :  remainder operator
** :  power operator
== :  equal to operator
!= :  not equal to operator
"""

# plus operator
n1 = 40
n2 = 50
print("addition :", n1+n2)
n3 = n1 + n2
print("addition of values :", n3)
print(n1+n2)
print("_"*50)
print("\n")

# add two strings with plus operator #

var1 = 'Hello'
var2 = 'Good Morning'
print(var1 +" "+var2)  # Hello Good Morning
print("_"*50)
print("\n")
# can not add string with integer
v1 = 40
v2 = 'Hello'

# print(v1 + v2)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


############### Subtraction ###########
a1 = 300
a2 = 500
print("subtraction :", a2-a1)
# subtraction : 200
print("_"*50)
print("\n")

################### Multiplication ##########
b1 = 60
b2 = 4
print("multiplication :", b1*b2)
# multiplication : 240
print("_"*50)
print("\n")
# multiply string with integer
c1 = 'Hello'
c2 = 5

# if we multiply the string with number, then it will repeat the string, that number of times
print("string with int multiply :", c1*c2)
# string with int multiply : HelloHelloHelloHelloHello

# draw a line
print("_"*50)
print("\n")
############## division #########
d1 = 40
d2 = 3
# division with single / return float or pointer output.
print("division with single / :", d1/d2)
# division with single / : 13.333333333333334

# division with double // return integer output or whole number
print("division with double // :", d1//d2)
# division with double // : 13


# print("Hello" - "Morning")
# TypeError: unsupported operand type(s) for -: 'str' and 'str'

print("_"*50)
print("\n")
############## remainder operator #########
f1 = 17
f2 = 3

print(" remainder output :", f1%f2)
# remainder output : 2

print("_"*50)
print("\n")
############## power operator #########

h1 = 5
print("square of h1 :", h1**2)
# square of h1 : 25

print("cube of h1 :", h1**3)
# cube of h1 : 125

print("_"*50)
print("\n")
# solve the below equation
# (a+b)^2 = a^2 + b^2 + 2ab
a = 10
b = 20
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print("lhs output :", lhs)
print("rhs output :", rhs)

# use == operator to compare 2 values
print(lhs == rhs)

# Home work ###
"""
1. (a+b)^3 = a^3 + b^3 + 3ab(a+b)
2. (a-b)(a+b)= a^2 - b^2
3. a3-b3= (a-b)^3 + 3ab(a-b)
4. h2 = l2 + b2
5. calculate the area of circle : PI*R^2
PI = 3.14
R = 4
6.  Calculate simple interest
7.  Calculate compound interest
"""
###### Question 1 ###########
###1. (a+b)^3 = a^3 + b^3 + 3ab(a+b) ###
a = 6
b = 8
lhs = (a + b) **3
rhs = a ** 3 + b ** 3 + 3 * a * b * (a+b)

print("LHS:", lhs)
print("RHS:", rhs)
print("Equality Check for (a+b)^3: ", lhs == rhs)

print("-"*50)
print("\n")

###### Question 2 ###########
###2. (a-b)(a+b)= a^2 - b^2 ###
a = 9
b = 5
lhs = (a - b) * (a + b)
rhs = a ** 2 - b ** 2

print("LHS:", lhs)
print("RHS:", rhs)
print("Equality Check for (a-b)(a+b): ", lhs == rhs)

print("-"*50)
print("\n")
###### Question 3 ###########
###3. a^3-b^3= (a - b) * (a**2 + a*b + b**2) ###
a = 12
b = 15

lhs = a**3-b**3
rhs = (a - b) * (a**2 + a*b + b**2)

##rhs = (a-b)**3 + 3**a**b**(a-b)

print("LHS:", lhs)
print("RHS:", rhs)
print("Equality Check for a^3-b^3: ", lhs == rhs)

print("-"*50)


print("\n")
###### Question 4 ###########
###4. h2 = l2 + b2 ###
h = 5
l = 3
b = 4

lhs = h ** 2
rhs = l ** 2 + b ** 2

print("Pythagoras' Theorem -> the value of hyp^2 = ", lhs)
print("Pythagoras' Theorem -> the value of base^2 + side^2 = ", rhs)

print("Pythagoras' Theorem -> to present it is a right angled triangle", lhs == rhs)

print("-"*50)
print("\n")
###### Question 5 ###########
###5. calculate the area of circle : PI*R^2 ###
PI = 3.14
R = 4
print("Area of Circle is =  ", PI*R**2)

print("-"*50)
print("\n")
###### Question 6 ###########
###6.  Calculate simple interest ###

"SI = (P * R * T) / 100"
"R = 20 %  and T = 2 years"

P = 1000
R = 20
T = 2
SI = (P * R * T) / 100

print("Simple Interest of the Principle amount " + str(P) + " is = ", SI)
print("-"*50)
print("\n")
###### Question 7 ###########
###7.  Calculate compound interest ###

"CI = P (1 + (R / 100)^T - P "
"R = 20 %  and T = 2 years"

P = 1000
R = 20
T = 2
CI = P * (1 + (R/100)) **T - P

print("Compound Interest for " + str(T) + " years is  = ", CI)

print("-"*50)


p2 = 3.4 + 4.5j
p3 = "Hello **Hello*#*"
print(p3)


