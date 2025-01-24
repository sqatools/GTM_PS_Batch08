"""
Variabke: Math Operation
+ : plus operator
- :  subtraction'
* : multiplication
/ :  divide with single /
// : divide with double // (floor division)
% :  remainder operator (Modulus operator)
** :  power operator
== :  equal to operator
!= :  not equal to operator
"""

# plus operator (Addition)
n1 = 40
n2 = 50
print("addition :", n1+n2)
n3 = n1 + n2
print("addition of values :", n3)
print(n1+n2)


# add two strings with plus operator #

var1 = 'Hello'
var2 = 'Good Morning'
print(var1 +" "+var2)  # Hello Good Morning

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


################### Multiplication ##########
b1 = 60
b2 = 4
print("multiplication :", b1*b2)
# multiplication : 240

# multiply string with integer
c1 = 'Hello'
c2 = 5

# if we multiply the string with number, then it will repeat the string, that number of times
print("string with int multiply :", c1*c2)
# string with int multiply : HelloHelloHelloHelloHello

# draw a line
print("_"*50)
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
############## remainder operator #########
f1 = 17
f2 = 3

print(" remainder output :", f1%f2)
# remainder output : 2

print("_"*50)
############## power operator #########

h1 = 5
print("square of h1 :", h1**2)
# square of h1 : 25

print("cube of h1 :", h1**3)
# cube of h1 : 125

print("_"*50)
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

# Home work
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

