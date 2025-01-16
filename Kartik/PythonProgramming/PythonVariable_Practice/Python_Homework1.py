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

print("_" * 50)
############## Question 1  ###########
print("(a+b)^3 = a^3 + b^3 + 3ab(a+b)")
a = 2
b = 3
lhs = (a + b) ** 3
rhs = (a ** 3) + (b ** 3) + ((3 * a * b) + (a + b))
print(lhs)
print(rhs)
print("compare operator output :", rhs == lhs)

print("_" * 50)
############## Question 2  ###########
print("(a-b)(a+b)= a^2 - b^2")
a = 4
b = 5
lhs = (a - b) * (a + b)
rhs = (a ** 2) - (b ** 2)
print(lhs)
print(rhs)
print("compare operator output :", rhs == lhs)

print("_" * 50)
############## Question 3  ###########
print("(a3-b3= (a-b)^3 + 3ab(a-b)")
a = 10
b = 5
lhs = a ** 3 - b ** 3
rhs = (a ** 3) - (b ** 3) + ((3 * a * b) * (a - b))
print(lhs)
print(rhs)
print("compare operator output :", rhs == lhs)

print("_" * 50)
############## Question 4  ###########
print("h2 = l2 + b2")
height = 2
length = 2
breadth = 2
lhs = (height ** 2)
rhs = (length ** 2) +( breadth **2)
print(lhs)
print(rhs)

print("_" * 50)
############## Question 5 ###########
print("calculate the area of circle : PI*R^2")
PI = 3.14
R = 9
area = PI*(R**2)
print("Area of Circle:", area)

print("_" * 50)
############## Question 6 ###########
print("Calculate simple interest : A=P(1+rt)")

p=100000
r=1.5
t=1

A=(p * (1 + (r*t)))
print(A)

print("_" * 50)
############## Question 7 ###########


print("Calculate compound interest : A=P(1+(r/n)^nt)")

p=100000
r=1.5
t=1
n=2
A=(p * (1 + (r/n) ** (n*t)))
print(A)




