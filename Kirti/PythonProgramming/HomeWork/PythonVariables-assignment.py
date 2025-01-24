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

#1. (a+b)^3 = a^3 + b^3 + 3ab(a+b)
a=5
b=6
print("value of a = ", a)
print("value of b = ", b)

lhs = (a+b) ** 3
print("lhs = ", lhs)
rhs = a**3 + b**3 + 3*a*b*(a+b)
print("rhs = ", rhs)

print(lhs==rhs)



print("----"*50)
#2. (a-b)(a+b)= a^2 - b^2
a=5
b=6
print("value of a = ", a)
print("value of b = ", b)

lhs= (a-b)*(a+b)
print("lhs = ", lhs)
rhs= a**2 - b**2
print("rhs = ",rhs)

print(lhs==rhs)


print("----"*50)
#3. a3-b3= (a-b)^3 + 3ab(a-b)
a=5
b=6
print("value of a = ", a)
print("value of b = ", b)

lhs=a**3-b**3
print("lhs = ", lhs)
rhs= (a-b)**3 + 3*a*b*(a-b)
print("rhs = ",rhs)

print(lhs==rhs)



print("----"*50)
#4. h2 = l2 + b2
l=3
b=4
h=5
print("values of l, b, h are as : ", l, b, h)

lhs=h**2
print("lhs= ",lhs)
rhs=l**2+b**2
print("rhs= ", rhs)

print(lhs==rhs)



print("----"*50)
'''5. calculate the area of circle : PI*R^2
PI = 3.14
R = 4'''
PI = 3.14
R = 4
print("Area o Circle = ", 2*PI*R)




print("----"*50)
#6.  Calculate simple interest
# SI = PNR/100
P=2000
N=2
R=5.6
print("values of P, N, R as ", P, N, R)

print("Simple Interest = ", P*N*R/100)



print("----"*50)
#7.  Calculate compound interest
# CI = Principal × (1 + Rate)Time − Principal    i.e. (CI = P*(1+R/100)**N-P)

P=2000
N=2
R=5.6
print("values of P, N, R as ", P, N, R)

print("Compound Interest = ", P*(1+R/100)**N-P)