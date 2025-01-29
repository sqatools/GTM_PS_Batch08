# Date: 15/01/2026
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

# 1. (a+b)^3 = a^3 + b^3 + 3ab(a+b)
a = 10
b = 20
lhs = (a+b)**3
rhs = a**3+b**3+3*a*b*(a+b)
print("Value of Left Hand Side: ", lhs)
print("Value of Right Hand Side: ", rhs)
print(lhs == rhs)
print("_"*50)

# 2. (a-b)(a+b)= a^2 - b^2
lhs = (a-b)*(a+b)
rhs = a**2-b**2
print("Value of Left Hand Side: ", lhs)
print("Value of Right Hand Side: ", rhs)
print(lhs == rhs)
print("_"*50)

# 3. a3-b3= (a-b)^3 + 3ab(a-b)
lhs = a**3-b**3
rhs = (a-b)**3+3*a*b*(a-b)
print("Value of Left Hand Side: ", lhs)
print("Value of Right Hand Side: ", rhs)
print(lhs == rhs)
print("_"*50)

# 4. h2 = l2 + b2 (Pythagorean theorem)
h = 13
l = 12
b = 5
lhs = h**2
rhs = l**2 + b**2
print("Value of Left Hand Side: ", lhs)
print("Value of Right Hand Side: ", rhs)
print(lhs == rhs)
print("_"*50)

# calculate the area of circle : PI*R^2
pi = 3.14
r = 5
Area_Of_Circle = pi*r**2
print("Area of circle : ", Area_Of_Circle)
print("_"*50)

# 6.  Calculate simple interest i=(p*r*t)/100
p = 2000
r = 17.7
t = 3
i = (p*r*t)/100
print("Simple Interest: ", i)

# 7.  Calculate compound interest ci = (p(1+r/n)**nt)-p
p = 10000
r = 9.1
n = 100
nt = 3
ci = (p*(1+r/n)**nt)-p
print("Compound Interest CI: ", ci)

