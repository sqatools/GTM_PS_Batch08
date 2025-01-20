'''
Math Operations
+: plus operator
-: subtraction
*: multiplication
/: divide with single
//: divide with double
**: power operator
==: equal to operator
!=: not equal to operator

'''

print("_" * 60)  # for drawing line

# plus operator
a = 20
b = 30
print("addition:", a + b)
c = a + b
print("value of c after adding a plus b :", c)

# add two string
a1 = "Pankaj"
a2 = "Prasad"
print("adding two string", a1 + " " + a2)

# adding of string with number
b1 = "Pankaj"
b2 = 20
# print(b1 + b2)
# TypeError: can only concatenate str (not "int") to str

############ Subtraction ############
c1 = 30
c2 = 40
print("subtraction:", c2-c1)

############ Multiplication ############
d1 = 30
d2 = 2
print("multiplication:", d1*d2)

# multiplication of string with number
e1 = 3
e2 = "Pankaj"
print(e1*e2)
# it will print string 3 times
print("_" * 60)

############ Division ############
# division with single /
f1 = 40
f2 = 3
print("division:", f1/f2)
# Note* output will be on float

# division with single //
print("division:", f1//f2)
# Note* output will be in integer and it will remove decimal values
print("_"*50)

############ Power Operator ############
h1 = 5
h2 = 2
print("square of 5: ", h1**2)
print("qube of 2: ", h2**3)
print("_"*50)

# Solve below equation
# (a+b)^2= a**2+b**2+2*a*b
a = 10
b = 20
lhs = (a+b)**2
rhs = a**2+b**2+2*a*b
print("Value of Left Hand Side: ", lhs)
print("Value of Right Hand Side: ", rhs)
# == Comparison operator, output will be in boolean
print(lhs == rhs)







