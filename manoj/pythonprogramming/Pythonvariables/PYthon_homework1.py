a = 2
b = 3

l = (a + b) ** 3
r = a ** 3 + b ** 3 + 3 * a * b * (a + b)
lh = (a - b) * (a + b)
rh = a ** 2 - b ** 2
lhs = a ** 3 - b ** 3
rhs = (a - b) ** 3 + 3 * a * b * (a - b)

print("lhs output (a+b)^3:", l)
print("rhs output a^3 + b^3 + 3ab(a+b):", r)
print("lhs output (a-b)(a+b):", lh)
print("rhs output a^2 - b^2:", rh)
print("lhs output a3-b3:", lhs)
print("rhs output (a-b)^3 + 3ab(a-b):", rhs)
