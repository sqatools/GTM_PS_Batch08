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
num1 = 30
num2 = 40
print ("Addition is:", num1+num2)
num3 = num1 + num2
print(num3)



# add two strings with plus operator #

str1 = 'Hello'
str2 = 'My name is Madhuri'
print(str1 +" "+str2)  # Hello My name is Madhuri

# can not add string with integer
v1 = 50
v2 = 'Hello'

# print(v1 + v2)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


############### Subtraction ###########
a1 = 800
a2 = 400
print("subtraction :", a2-a1)
# subtraction : -400



################### Multiplication ##########
b1 = 40
b2 = 2
print("multiplication :", b1*b2)
# multiplication : 80


# multiply string with integer
c1 = 'WelCome '
c2 = 10

# if we multiply the string with number, then it will repeat the string, that number of times
print("string with int multiply :", c1*c2)
# string with int multiply : WelCome WelCome WelCome WelCome WelCome WelCome WelCome WelCome WelCome WelCome



# draw a line
print("*"*100)



############## division #########
d1 = 15
d2 = 4
# division with single / return float or pointer output.
print("division with single / :", d1/d2)
# division with single / : 3.75

# division with double // return integer output or whole number
print("division with double // :", d1//d2)
# division with double // : 3



# print("Hello" - "Morning")
# TypeError: unsupported operand type(s) for -: 'str' and 'str'




print("*"*50)
############## remainder operator #########
f1 = 29
f2 =5

print(" remainder output :", f1%f2)
# remainder output : 4

print("*"*50)


############## power operator #########

h1 = 6
print("square of h1 :", h1**2)
# square of h1 : 36

print("cube of h1 :", h1**3)
# cube of h1 : 216



print("*"*50)
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
