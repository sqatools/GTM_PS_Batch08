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

# 1. lhs1 = (a+b)^3
# rhs1 = a^3 + b^3 + 3ab(a+b)
a=3
b=4
lhs1=(a+b)**3
rhs1=(a**3)+(b**3)+(3*a*b*(a+b))
print(lhs1)
print(rhs1)
print(lhs1==rhs1)


#2. (a-b)(a+b)= a^2 - b^2
# lhs2 = (a-b)*(a+b)
# rhs2 = a^2 - b^2

a=7
b=8
lhs2 = (a-b)*(a+b)
rhs2 = a**2 - b**2
print(lhs2)
print(rhs2)
print(lhs2==rhs2)

#3.  a3-b3= (a-b)^3 + 3ab(a-b)
# lhs3= a^3 - b^3
# rhs3 = (a-b)^3 + 3ab(a-b)

a=10
b=11
lhs3 = (a**3)-(b**3)
rhs3 = (a-b)**3 + (3*a*b*(a-b))
print(lhs3)
print(rhs3)
print(lhs3==rhs3)

#4. h^2 = l^2 + b^2

h=10
l=8
b=9
lhs4=h**2
rhs4=(l**2) + (b**2)
print(lhs4)
print(rhs4)
print(lhs4==rhs4)


#5. calculate the area of circle : PI*R^2
PI=3.14
R=4
Area_of_circle = PI*(R**2)
print(Area_of_circle)


#6.  Calculate simple interest
# Simple_interest =(Principal*Rate_of_interest*time_in_years)/100
Principal = 10000
Rate_of_interest=10
time_in_years = 5
Simple_interest = (Principal*Rate_of_interest*time_in_years)/100
print(Simple_interest)


#7.  Calculate compound interest
# Compound Interest= A=Principal(1+Rate_of_interest/n)^n*Time_in_years
Principal = 5000
Rate_of_interest = 10
n = 4  # n is the number of times interest is compounded per year. quarterly in this case.
Time_in_years= 10  # number of years for which the amount is invested
Amount = Principal * (1 + Rate_of_interest / n) ** (n * Time_in_years)
print(Amount)

