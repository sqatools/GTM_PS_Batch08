# PROBLEM 1 :(a+b)^3=a^3+b^3+3ab(a+b)
print("PROBLEM 1 : (a+b)^3=a^3+b^3+3ab(a+b)")
a = 3
b = 2
lhs1 = (a + b) ** 3
print("lhs is : ", lhs1)
rhs1 = a ** 3 + b ** 3 + (3 * a * b) * (a + b)
print("rhs is : ", rhs1)
print(lhs1 == rhs1)
print("-" * 100)

# PROBLEM 2 :(a-b)(a+b)=a^2-b^2
print("PROBLEM 2 : (a-b)(a+b)=a^2 - b^2")
a, b = 5, 3
lhs2 = (a - b) * (a + b)
print("lhs is : ", lhs2)
rhs2 = a ** 2 - b ** 2
print("rhs is : ", rhs2)
print(lhs2 == rhs2)
print("-" * 100)

# PROBLEM 3 : a3-b3 = (a-b)^3 + 3ab(a-b)
print("PROBLEM 3 : a3-b3 = (a-b)^3 + 3ab(a-b)")
a, b = 5, 2
lhs3 = (a ** 3) - (b ** 3)
print("lhs is : ", lhs3)
rhs3 = (a - b) ** 3 + (3 * a * b) * (a - b)
print("rhs is : ", rhs3)
print(lhs3 == rhs3)
print("-" * 100)

# PROBLEM 4 : Pythagoras Theorem h^2=l^2+b^2
print("PROBLEM 4: Pythagoras Theorem h^2=l^2+b^2")
hypotenuse = 5
l = 3
b = 4
lhs4 = hypotenuse ** 2
print("lhs is : ", lhs4)
rhs4 = l ** 2 + b ** 2
print("rhs is : ", rhs4)
print(lhs4 == rhs4)
print("-" * 100)

# PROBLEM 5 :Area of the circle: PI*r^2
print("PROBLEM 5: Area of the circle: PI*r^2")
import math

PI = math.pi
r = 4
area = PI * r ** 2
print("Area of the circle with radius ", r, "=", area)
area = round(area, 2)
print("Area of the circle with radius ", r, " rounded to two decimal places =", area)
print("-" * 100)

# PROBLEM 6 :Calculating Simple Interest P*R*T/100
print("PROBLEM 6: Calculating Simple Interest P*R*T/100")
principal = 1000
rate = 5  # 5 means 5%
time = 10
SI = (principal * rate * time) / 100
print("The Simple interest for Rs.", principal, "at the rate of", rate, "% for", time, "years is Rs.", SI)
print("-" * 100)

# PROBLEM 7 :Calculating Compound Interest A=P(1+r/n)^nt
print("PROBLEM 7: Calculating Compound Interest A=P(1+r/n)^nt")
principal1 = 5000
rate1 = 10
r = rate1 / 100
n = 4  # n is the number of times interest is compounded per year. quarterly in this case.
time1 = 20  # number of years for which the amount is invested
amount = principal1 * (1 + r / n) ** (n * time1)
amount = round(amount, 2)
print("The total amount for an investment of Rs.", principal1, "at an annual interest rate of", rate1, "% compunded", n,
      "times per year for", time1, "years is Rs.", amount)
print("The total compound interest =", round(amount - principal1, 2))
print("-" * 100)
