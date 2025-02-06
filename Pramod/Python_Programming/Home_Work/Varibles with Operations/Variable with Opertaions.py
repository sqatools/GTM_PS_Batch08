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
print("_"*100)
#1) (a+b)^3 = a^3 + b^3 + 3ab(a+b)
a=20
b=10

#print((a+b)***3=, a***3 + b***3 + 3*a*b*(a+b))
LHS=(a+b)**3
RHS= a**3 + b**3 + 3*a*b*(a+b)
print("LHS :", LHS)
print("RHS :",RHS)

print("_"*100)

#2. (a-b)(a+b)= a^2 - b^2
print(((a-b)*(a+b)), "=", (a**2)-(b**2))

print("_"*100)
#3. a3-b3= (a-b)^3 + 3ab(a-b)
print((a**3)-(b**3),"=",((a-b)**3)+(3*a*b*(a-b)))

print("_"*100)
#4)h2 = l2 + b2
h=10
l=20
b=30
print((h**2),"=",((l**2)+(b**2)))

print("_"*100)
#5. calculate the area of circle : PI*R^2
PI = 3.14
R=2
print("Area of circle:", PI*R**2)
print("_"*100)

#6.  Calculate simple interest
P=10
T=20
R=30

print ("Simple interest =", (P*T*R)//(100))
print("_"*100)

#7. Calculate compound interest
'''
A=P(1+(R/n)**n*T
A = Total amount (Principal + Interest)
P = Principal amount (initial amount of money)
R = Annual interest rate (in decimal or percentage)
n = Number of times the interest is compounded per year
T = Time (in years)
To find the Compound Interest (CI):
CI=A−P
'''
A,P,R,n,T=100,10,2,12,25
print("A=", P*(1+(R//n)**(n*T)))
A=100
print("CI=", A-P)
print("_"*100)

