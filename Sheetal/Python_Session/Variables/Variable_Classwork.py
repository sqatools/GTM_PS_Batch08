print("_" * 50)
print("??????????????????")

a1 = 121231545415454
print(a1,type(a1))
a = 10
# a : variable
# = : assignment operator
# 10 : value assign to the variable

print(a)  # 10
print(id(a))  # 140720823159512

b = 20
print(b, id(b))  # 20 140720823159832

# Note: every different variable holding different value will have different addresses.

########### two variable have same value ##########
# if two variable have same value, thn their address will same
x = 40
y = 40

print("x :", x, "address:", id(x))
# x : 40 address: 140720823160472
print("y :", y, "address:", id(y))
# y : 40 address: 140720823160472

################### Assign multiple value to multiple value at a time ############

p, q, r = 50, 60, 70
print("value p:", p)  # value p: 50
print("value q:", q)  # value q: 60
print("value r:", r)  # value r: 70
print("value of p, q, r :", p, q, r)
# value of p, q, r : 50 60 70

########### Assign same value to multiple variables ###########

A = B = C = 100
print("Value A :", A, id(A))  # Value A : 100 140720823162392
print("Value B :", B, id(B))  # Value B : 100 140720823162392
print("Value C :", C, id(C))  # Value C : 100 140720823162392
#############
L = 200
# print(l)
# NameError: name 'l' is not defined. Did you mean: 'L'?

############# Rules to declare variables #############
# 1. Variable name can not start with number
var123 = 500  # correct
# 2var = 500   # wrong

# 2. Variable name can not have space in the name
var_name_email = 'rahul jain'  # correct
# var name = 'john' # wrong name

# 3. There is no specific length for variable
var_name_has_no_limit_wrtrewereer = 50
print(var_name_has_no_limit_wrtrewereer)

# 4. Python is case-sensitive, variable names will treat differently with different case.

Name = 'Jai'
NAME = 'Rahul'
name = 'Mohit'
namE = 'Pramod'

print(Name, NAME, name, namE)

print(Name, "\n", NAME, "\n", name, "\n", namE)

# 5. Can not use special character in variable name except underscore('_')
# var_$_123 = 500 # wrong
# var-to-home = 600

# 6. Can not inbuilt keyword as variables
# True = 600 # wrong # SyntaxError: cannot assign to True
true = 700  # wrong
# class = 600 # wrong

###################################
import keyword

print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 
'async', 'await', 'break', 'class', 'continue', 'def', 
'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 
'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

"""

"""
# math operations




"""
########### two variable have same value ##########
# if two variable have same value, thn their address will same
x = 40
y = 40

print("x :", x, "address:", id(x))
# x : 40 address: 140720819097240
print("y :", y, "address:", id(y))
# y : 40 address: 140720823160472
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


print("_"*50)
# plus operator
n1 = 40
n2 = 50
print("addition :", n1+n2)
n3 = n1 + n2
print("addition of values :", n3)
print(n1+n2)

print("_"*50)

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



