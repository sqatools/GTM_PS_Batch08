
# Assignment


# 1. print 1 (a+b)^3 = a^3 + b^3 + 3ab(a+b)
c=3
d=2
lhs=(c+d)**3
rhs=c**3 + d**3 + 3*c*d*(c+d)
print("lhs output :", lhs) #125
print("rhs output :", rhs) #125

print(lhs==rhs) # True



# 2. (a-b)(a+b)= a^2 - b^2

a = 6
b = 4
lhs = (a-b) * (a+b)
rhs = a**2 - b**2
print("lhs output :", lhs) #20
print("rhs output :", rhs) #20

print(lhs == rhs) # True




#3. a3 - b3 = (a - b) (a2 + ab + b2).
p=6
q=7
lhs = p**3 - q**3
rhs = (p-q) * (p**2 + p*q + q**2)
print("lhs output :", lhs) #-127
print("rhs output :", rhs) #-127

print(lhs == rhs) #True


#4. h1^2 = l1^2 + b1^2
h1 = 8
l1 = 5
b1 = 4
lhs = h1**2
rhs = l1**2 + b1**2
print("lhs output :", lhs) #64
print("rhs output :", rhs) #41

print(lhs == rhs) #False


# 5. calculate the area of circle : PI*R^2 where PI = 3.14

PI= 3.14
R=7
print ("Area off  Circle is:", PI * R**2)  # Area off  Circle is: 153.86


# 6. Calculate simple interest
"""
# S.I. = (P × R × T)/100 
where P = Principal, 
R = Rate of Interest in % per annum, and 
T = Time """

P = 500000
R = 10.5
T = 12
print("Simple Intrest:", (P * R * T)/100) #Simple Intrest: 630000.0


# 7.  Calculate compound interest
"""
A = P(1 + r/n)^(nt)
where A	=	final amount
P	=	initial principal balance
r	=	interest rate
n	=	number of times interest applied per time period
t	=	number of time periods elapsed """

P =50000
R=2.5
N=2
T=1
CI= P * (1 + (R/N)) ** (N*T)
print("Compound Interest:", CI) #Compound Interest: 253125.0





