"""
math operation
+ : plus operator
_ : subtraction
* : multiplication
/ : divide with single /
// : divide with double //
% : remainder operator
** : power operator
== : equal to operator
!= : not equal to operator
"""

# plus operator
m1 = 20
m2 = 30
print("addition :", m1+m2)
m3 = m1 + m2
print("addition of values :", m3)

#subtraction

n1 = 500
n2 = 301
print("subtraction :", n1-n2)
n3 = n1 - n2
print("subtraction of values :", n3)

# add two strings with plus operator #

var1 = 'Hello'
var2 = 'good evening'
print(var1 + " "+var2) # Hello good evening

### multiplication#####
k1 = 20
k2 = 5
print("multiplication :", k1*k2)
# multiplication : 100

# multiply string with integer
c1 = 'Hi'
c2 = 3

# if we multiply the string with number/ then it will repeat the string
print("string with int multiply :", c1*c2)
# string with int multiply : hihihihi

# draw a line
print("_"*50)

#####division ######
d1 = 40
d2 = 3
# division with single /return float or pointer output
print("division with single / :", d1/d2)
# division with single / : 13.333333333333334

# division with double // return integer output or whole number
print("division with double // :", d1/d2)
# division with double // : 13.333333333333334

###### remainder operator #####
f1 = 15
f2 = 4

print("remainder output :", f1%f2)
# remainder output : 3

#### power operator #####
h1 = 7
print("square of h1 :", h1**2)
# square of h1 : 49

print("cube of h1 :", h1**3)
# cube of h1 : 343

# solve the below equation
# (a+b)^2 = a^2 +b^2 + 2ab
a = 22
b = 34
lhs = (a+b)**2
rhs = a**2 + b**2 +2*a*b
print("lhs output :", lhs)# lhs output : 3136
print("rhs output :", rhs)# rhs output : 3136

# use == operator two compare 2 values
print(lhs == rhs)

# homework #
""""
1.(a+b)^3 = a^3 + b^3 + 3ab(a+b)
2. (a-b)(a+b) = a^2 - b^2
3. a3-b3 = (a-b)^3 + 3ab(a-b)
4.  h2 = l2 + b2
5. calculate the area of circle : PI*R^2
PI = 3.14
R = 4
6. calculate simple interest
7. calculate compound interest
"""