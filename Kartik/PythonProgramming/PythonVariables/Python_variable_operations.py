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

# draw a line
print("_"*50)

###################
# Plus operator
print("_"*50)
print("Plus operator")
n1 = 10
n2 = 20
print ("addiotion :", n1+n2)
n3= n1+n2
print("addition :", n3)
print(n1+n2)
print("_"*50)

# add two strings with plus operator

print("add two strings with plus operator")
s1 = 'Hello'
s2 = 'very Good morning'
print(s1 +" "+s2)

# can not add Sting with integer
v1='hello'
v2=40
# print(v1 +v2)
# TypeError: can only concatenate str (not "int") to str
print("_"*50)

############## Subtraction ###########
print("Subtraction")
a1 = 200
a2 = 500
print("Subtraction :", a2-a1)

print("_"*50)

############## multiplication###########
print("multiplication")
b1 = 40
b2 = 5
print("Multiplication:", b1*b2)

############## multiplication string with integer ###########
c1 = 'Hello'
c2 = 5
print("String with integer multiply :", c1*c2)

# Note : if we multiply the string with number, then it will repeat the string, that number of times

print("_"*50)
############## Division ###########
print("division")
d1 = 40
d2 = 5


# division with single / return float pointer output
print("Division with single / :", d1/d2)

# division with double // return integer output or whole number
print("Division with double // :", d1//d2)

print("_"*50)
############## Remainder Operator ###########
print("Remainder Operator")
f1=19
f2=3
print("remainder output :", f1 % f2)

print("_"*50)
############## Power Operator ###########
print("Power Operator")
h1=5
print ("Square of h1 :", h1**2)

print ("cube of h1 :", h1**3)

print("_"*50)

############## Equation  ###########
print("Equation")
# (a+b)^2 = a^2 + b^2 + 2ab
a=2
b=3
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print ("lhs output :", lhs)
print("rhs output :", rhs)

print("_"*25)
############## compare operator  ###########
print("compare operator == ")

print("compare operator output :", rhs == lhs)












