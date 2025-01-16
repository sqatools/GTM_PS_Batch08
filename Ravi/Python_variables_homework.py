a = 3
b = 4
c = 5

# 1.(a+b)^3 = a^3 + b^3 + 3ab(a+b)
lhs_1 = (a+b) ** 3
rhs_1 = a ** 3 + b ** 3 + 3*a*b*(a+b)
print(lhs_1 == rhs_1)
print("-"*50)

# 2. (a-b)(a+b) = a^2 - b^2
lhs_2 = (a-b) * (a+b)
rhs_2 = a ** 2 - b ** 2
print(lhs_2 == rhs_2)
print("-"*50)

# 3. a3-b3 = (a-b)^3 + 3ab(a-b)
lhs_3 = (a ** 3) - (b ** 3)
rhs_3 = (a-b) ** 3 + 3 * a * b * (a-b)
print(lhs_3 == rhs_3)
print("-"*50)

# 4.  h2 = l2 + b2
lhs_4 = c ** 2
rhs_4 = a ** 2 + b ** 2
print(lhs_4 == rhs_4)
print("-"*50)

# 5. calculate the area of circle : PI*R^2
PI = 3.14
R = 4
area = PI * R ** 2
print(area)
print("-"*50)

# 6. calculate simple interest
principle = a
time = b
rate_of_interest = c

simple_interest = (principle * time * rate_of_interest) / 100

print(simple_interest)
print("-"*50)

# 7. calculate compound interest
compound_interest = principle * (1 + rate_of_interest) ** time - principle
print(compound_interest)
print("-"*50)
