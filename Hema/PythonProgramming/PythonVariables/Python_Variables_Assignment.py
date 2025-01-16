########### HOME WORK ################

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
print("*"*50)
print("TASK 1: (a+b)^3 = a^3 + b^3 + 3ab(a+b)")
a = 3
b = 4
print("a value is: ", a)
print("b value is: ", b)
lhs = (a+b) ** 3
rhs = a ** 3 + b ** 3 + 3 * a * b * (a+b)
print("lhs value is: ", lhs)
print("rhs value is: ", rhs)

print("Checking whether the value of lhs is equal to rhs: ", lhs == rhs)
print("="*50)

print("TASK 2: (a-b)(a+b)= a^2 - b^2")
a = 10
b = 5
print("a: ", a)
print("b: ", b)
lhs = (a-b) * (a+b)
rhs = a ** 2 - b ** 2
print("lhs value: ", lhs)
print("rhs value: ", rhs)
print("Checking whether the lhs is equal is rhs: ", lhs == rhs)
print("#" * 50)

print("TASK 3: a3-b3= (a-b)^3 + 3ab(a-b)")
a1 = 6
b1 = 3
print("a1 value is: ", a1)
print("b1 value is: ", b1)
lhs = a1 ** 3 - b1 ** 3
rhs = (a1 - b1) ** 3 + 3 *a1 *b1 * (a1-b1)
print("lhs value: ", lhs)
print("rhs value: ", rhs)
print("checking whether lhs is equal to rhs: " , lhs == rhs)
print("#" * 50)

print("TASK 4: h2 = l2 + b2")
'''
In a right angled triangle:
the square of the hypotenuse is equal to
the sum of the squares of the other two sides.
'''
h = 5 # or 26
l = 3 # or 10
b = 4 # or 24

lhs = h ** 2
rhs = l ** 2 + b ** 2
print("h value: ", h)
print("l valuw: ", l)
print("b value: ", b)
print("lhs value is: ", lhs)
print("rhs value is: ", rhs)
print("checking whether lhs is equal to rhs: ", lhs == rhs)
print("#" * 50)

print("TASK 5: calculating the area of circle : PI*R^2")
PI = 3.14
R = 4
area_of_circle = PI * R ** 2

print("PI value is: ", PI)
print("R value is: ", R)
print("Area of circle: ", area_of_circle)
print("#" * 50)

print("TASK 6: Calculate simple interest: (P x T x R)/ 100")
'''
Formula = (P x T x R)/ 100 
P = Principle Amount
r = Anual interest rate
t = time
'''

P = 5000
r = 5
t = 2

print(" P value: ", P, "\n", "r value: ", r, "\n", "t value: ",t)
simple_interest = (P * t * r) / 100
print("Simple interest value is: ", simple_interest)
print("#" * 50)

print("TASK 7: Calculate compound interest: A = P(1+(r/n))^t")

'''
A	=	final amount
P	=	initial principal balance
r	=	interest rate
n	=	number of times interest applied per time period
t	=	number of time periods elapsed
'''

P = 12000
r = 5
n = 100
t = 3

print(" P value: ", P , "\n", "r value: ", r, "\n", "n value: ", n , "\n", "t value: ", t)
A = P * (1+(r/n)) ** t
print("Compound interest value is: ", A)
print("#" * 50)