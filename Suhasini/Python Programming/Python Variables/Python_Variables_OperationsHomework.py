# 1. (a+b)3 = a3 + b3 + 3ab(a+b)

print("Solving the equation : (a+b)3 = a3 + b3 + 3ab(a+b)")

a = 15
b = 10
lhs = (a+b)**3
rhs = a**3 + b**3 + 3*a*b*(a+b)

print("LHS of the equation is :", lhs)
print("RHS of the equation is :", rhs)

print("Verifying if LHS = RHS ==> ", lhs==rhs)

print("_"*90)

# 2. (a-b)(a+b) = a2 - b2
print("Solving the equation : (a-b)(a+b) = a2 - b2")
lhs = (a-b)*(a+b)
rhs = a**2 - b**2

print("LHS of the equation is :", lhs)
print("RHS of the equation is :", rhs)

print("Verifying if LHS = RHS ==> ", lhs==rhs)
print("_"*90)


# 3. a3 - b3 = (a-b)3 + 3ab(a-b)

print("Solving the equation : a3 - b3 = (a-b)3 + 3ab(a-b)")
lhs = a**3 - b**3
rhs = (a-b)**3 + 3*a*b*(a-b)
print("LHS of the equation is :", lhs)
print("RHS of the equation is :", rhs)

print("Verifying if LHS = RHS ==> ", lhs==rhs)
print("_"*90)


# 4. h2 = l2 + b2 Pythagoras Theorem
print("Solving Pythagoras Theorem : c2 = a2 + b2")
l = 4
b = 6

pt = l**2 + b**2
print("Value of h2 when l=4 and b=6 is : ",pt)

print("_"*100)


# 5. Calculate Area of Circle : PI*r2
print("Calculating Area of Circle")

PI = 3.142
r = 4
area = PI* (r**2)
print ("Area of circle when r=4 is :", area)

print("_"*100)


# 6. Calculate Simple Interest

print("Calculating Simple Interest when p=13000, t=23, r=8")
p = 13000
t = 36
r = 8
SI = (p * t * r) / 100

print("Simple Interest is :", SI)

print("_"*100)


# Calculate Compound Interest CI = P (1 + r/n)t - P

print("Calculating Compound Interest when p=13000, t=3, r=8")
P = 13000
t = 3
r = 8
n = 2
ci = P * (1+ (r/n))**t

print("Compound Interest is :", ci)

print("_"*100)