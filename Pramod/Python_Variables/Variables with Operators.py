"""
Math Operation
+ : plus operator
- :  subtraction'
* : multiplication
/ :  divide with single /
// : divide with double //
% :  remainder operator
** :  power operator
== :  equal to operator
!= :  not equal to operator
"""


a=20
b=40
print("addition :", a+b)

print("Multiplication :", "A=", 3*5)

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










