a = 5
b = 6
lhs = (a + b) ** 3
rhs = a ** 3 + b ** 3 + 3 * a * b * (a + b)
print(lhs == rhs)

# (a-b)(a+b)=a^2-b^2

lhs = (a - b) * (a + b)
rhs = a ** 2 - b ** 2
print(lhs == rhs)

# 3. a^3-b^3=(a-b)^3 +3ab(a-b)
lhs = a ** 3 - b ** 3
rhs = (a - b) ** 3 + 3 * a * b * (a - b)
print(lhs == rhs)

# 4 H^2=P^2+B^2

H = 5
P = 3
B = 4
lhs = H ** 2
rhs = P ** 2 + B ** 2
print(lhs == rhs)
# 5. area of circle


print("area of circle is: ", 3.14 * P ** 2)


# 6. simple interest
R = 10
T = 5
print("simple interest is:", P * R * T / 100)


# 7 compound interest
lhs=a
rhs
