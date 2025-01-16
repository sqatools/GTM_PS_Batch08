# homework #
""""
1.(a+b)^3 = a^3 + b^3 + 3ab(a+b)
2. (a-b)(a+b) = a^2 - b^2
3. a3-b3 = (a-b)^3 + 3ab(a-b)
4.  h2 = l2 + b2
5. calculate the area of circle : PI*R^2
PI = 3.14
R = 4
6. calculate simple interest
7. calculate compound interest
"""

1.
a = 22
b = 33

lhs = (a+b)**3
rhs = a**3 + b**3 + 3*a*b*(a+b)

print("lhs output (a+b)^3:", lhs)   # lhs output (a+b)^3:  166375
print("rhs output a^3 + b^3 + 3ab(a+b):", rhs)   # rhs output a^3 + b^3 + 3ab(a+b): 166375
print(lhs == rhs)   # True
#####################

2.
a = 7
b = 3
lhs = (a-b)*(a+b)
rhs = a**2 - b**2
print("lhs output (a-b)(a+b):", lhs)   # lhs output (a-b)(a+b): 40
print("rhs output a^2 - b^2:", rhs)  # rhs output a^2 - b^2: 40
print(lhs == rhs)   # True

########################
3.
a = 6
b = 7

lhs = a**3-b**3
rhs = (a-b)**3 + 3*a*b*(a-b)
print("lhs output a3-b3:", lhs)   # lhs output a3-b3: -127
print("rhs output (a-b)^3 + 3ab(a-b):", rhs)   # rhs output (a-b)^3 + 3ab(a-b): -127
print(lhs == rhs)   # True

#############
4.  # h2 = l2 + b2
l = 3
b = 4
h = 5
lhs = h**2
rhs = l**2 + b**2
print("lhs output h2:", lhs)   # lhs output h2: 25
print("rhs output l2+ b2:", rhs)  # rhs output l2+ b2: 25
print(lhs == rhs)  # true


###########
5.  # calculate the area of circle : PI*R^2
PI = 3.14
R = 4
Area = PI*R**2
print("area of circle :", Area)   # area of circle : 50.24

########
6.  #calculate simple interest  (P × R × T)/100

P = 10
R = 11
T = 5
SI = (P*R*T)/100
print("Simple Interest :", SI)  # Simple Interest : 5.5

####################333

7.  #calculate compound interest  ((P*(1+i)^n) - P),

P = 100000
i = 1.5
n = 24

CI = ((P*(1+i)**n) - P)
print("Compound interest :", CI)  # Compound interest : 355271367780050.06


