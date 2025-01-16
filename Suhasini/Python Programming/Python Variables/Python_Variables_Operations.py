######## Python Mathematical Operations ############

# 1. Addition Operation :

var1 = 20
var2 = 40
print("Addition of 2 numbers is: ",var1+var2)   # Addition of 2 numbers is:  60
print(var1+var2)  # 60

sum = var1 + var2
print("Sum of 2 numbers is :",sum)  # Sum of 2 numbers is : 60

print("-"*80)


# 2. Subtraction Operation :

var1 = 50
var2 = 23

print("Value after Subtraction is: ",var1-var2) # Value after Subtraction is:  27

print("-"*80)  #Hyphen will be printed 80 times

# 3. Multiplication Operation :

c1 = 16
c2 = 36

print("Multiplication of 2 numbers is :", c1*c2)  # Multiplication of 2 numbers is : 576

# Consider this:
c1= 'Hello'
c2 = 5

# If we multiply the string with number then it will repeat the string that number of times

print(c1*c2)   # HelloHelloHelloHelloHello

print("-"*80)

# Division Operation :
d1 = 40
d2 = 3

print("Division with single / :", d1/d2)  # Division with single / : 13.333333333333334
print("Division with double // :", d1//d2)  # Division with double // : 13

# Division with single / returns float or pointer value. Division with double // returns whole number.
print("-"*80)


# Power Operator **

h1 = 5

print("h1 = 5")
print("Square of h1 : ",h1**2)
print("Cube of h1 :",h1**3)

# Solve below equation
#(a+b)2 = a2 + b2 + 2ab

print("Solving the equation - (a+b)2 = a2 + b2 + 2ab ")
a = 10
b = 20
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b

print("LHS of the equation is: ", lhs)
print("RHS of the equation is: ", rhs)

print("Verify if LHS = RHS")
print("LHS = RHS is: ",lhs==rhs)   # Using == Operator  ==> True

print("-"*80)


#Remainder Operator %

print("Remainder Operator %")
f1 = 17
f2 = 3

print("Remainder of 17 % 3 is: ",f1%f2)

print("\n",("-"*80))


