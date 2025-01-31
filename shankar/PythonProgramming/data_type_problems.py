"""Python Basics Problems"""
import a

print("_" * 50)

# 1). Python Program to add two integer values.
int_1 = 30
int_2 = 40

result = int_1 + int_2
print(result)  # 70

print("_" * 50)

# 2). Python Program to subtract two integer values.
int_1 = 30
int_2 = 40

result = int_1 - int_2
print(result)  # -10

print("_" * 50)

# 3). Python program to multiply two numbers.
int_1 = 30
int_2 = 40

result = int_1 * int_2
print(result)  # 1200

print("_" * 50)

"""
4). Python program to repeat a given string 5 times.
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools”
"""

str1 = "SQATools"
result = str1 * 5
matched_str = "SQAToolsSQAToolsSQAToolsSQAToolsSQATools"
if result == matched_str:
    print("As per output code write")  # As per output code write

print("_" * 50)

"""
5). Python program to get the Average of given numbers.
Formula: sum of all the number/ total number
Input:
a = 40
b = 50
c = 30
Output :
Average = 40
"""
a = 40
b = 50
c = 30
sum_of_all_numbers = a + b + c
total_number = 3
average = sum_of_all_numbers // total_number

print("average : ", average)

print("_" * 50)

"""
6). Python program to get the median of given numbers.
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66
"""
Input_nums = [45, 60, 61, 66, 70, 77, 80]
sort_list = Input_nums.sort()
number_of_values = len(Input_nums)
median_value = 0
if number_of_values % 2 == 1:  # Odd number of values
    median_value += Input_nums[number_of_values // 2]
else:  # Even number of values
    median_value += (Input_nums[number_of_values // 2 - 1] + Input_nums[number_of_values // 2]) / 2
print("median value is :", median_value)

print("_" * 50)

"""
7). Python program to print the square and cube of a given number.
Input :
num1 = 9
Output :
Square = 81
Cube =   729
"""
num_1 = 9

square_num = num_1 ** 2
print(square_num)

cube_num = num_1 * num_1 * num_1
print(cube_num)

print("_" * 50)
"""
8). Python program to interchange values between variables.
Input :
a = 10
b = 20
Output :
a = 20
b = 10
"""
a = 10
b = 20
a, b = b, a

print(a, b)
print("_" * 50)

"""
9). Python program to solve this Pythagoras theorem.
Theorem : (a2 + b2 = c2)

"""
a = 3
b = 4

c_squared = (a ** 2) + (b ** 2)
c = c_squared ** 0.5

print("a^2 + b^2 = ", c_squared)
print("The value of c (√(a^2 + b^2)) = ", c)

# hypotenuse squared equals the sum of the sides squared.

print("_" * 50)
"""
10). Python program to solve the given math formula.
Formula : (a + b)2 = a^2 + b^2 + 2ab
"""
a = 2
b = 4
left_side = (a + b) ** 2
right_side = (a ** 2) + (b ** 2) + (2 * a * b)

if left_side == right_side:
    print("The formula is verified: (a + b)^2 = a^2 + b^2 + 2ab")
else:
    print("The formula is not satisfied.")

print("-" * 50)
"""
11). Python program to solve the given math formula.
Formula : (a – b)2 = a^2 + b^2 – 2ab
"""
a = 4  # int(input("Enter the value of a: "))
b = 5  # int(input("Enter the value of b: "))

left_side = (a - b) ** 2
right_side = (a ** 2) + (b ** 2) - (2 * a * b)

if left_side == right_side:
    print("The formula is verified: (a – b)2 = a^2 + b^2 – 2ab")
else:
    print("The formula is not satisfied.")

print("-" * 50)

"""
12). Python program to solve the given math formula.
Formula : a2 – b2 = (a-b)(a+b)
"""
a = 4
b = 5
left_side = (a ** 2) - (b ** 2)
right_side = (a - b) * (a + b)

if left_side == right_side:
    print("The formula is verified: a2 – b2 = (a-b)(a+b)")
else:
    print("The formula is not satisfied.")

print("-" * 50)

"""
13). Python program to solve the given math formula.
Formula : (a + b)3 = a3 + 3ab(a+b) + b3 
"""
a = 4
b = 5
left_side = (a + b) ** 3
right_side = (a ** 3) + (3 * a * b * (a + b)) + (b ** 3)

if left_side == right_side:
    print("The formula is verified: (a + b)3 = a3 + 3ab(a+b) + b3")
else:
    print("The formula is not satisfied.")

print("-" * 50)

"""
14). Python program to solve the given math formula.
Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
"""
x = 4
y = 5

left_side = (x - y) ** 3
right_side = (x ** 3) - (3 * (x ** 2) * y) + (3 * x * (y ** 2)) - (y ** 3)

if left_side == right_side:
    print("The formula is verified: (a + b)3 = a3 + 3ab(a+b) + b3")
else:
    print("The formula is not satisfied.")

print("-" * 50)
"""
15). Python program to calculate the area of the square.
Formula : area = a*a
"""
a = 40
area = a * a

print("The area of the square with side length: ", a, "is :", area)

print("-" * 50)

"""
16). Python program to calculate the area of a circle.
Formula = PI*r*r
r = radius
PI = 3.14
"""

r = 10
PI = 3.14

area = PI * r * r
print("The area of the circle with radius", r, "is area", area)
print("-" * 50)

"""
17). Python program to calculate the area of a cube.
Formula = 6*a*a
"""
a = 5
area_of_cube = 6 * a * a
print("Area of a cube is:", area_of_cube)

print("-" * 50)

"""
18). Python program to calculate the area of the cylinder.
Formula = 2*PI*r*h + 2*PI*r*r
"""
PI = 3.14
radius = 4
height = 20
area_of_cylinder = (2 * PI * radius * height) + (2 * PI * radius * height)
print("The area of the cylinder is:", round(area_of_cylinder, 1))

print("-" * 50)

"""
19). Python program to check whether the given number is an Armstrong number or not.
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
"""
num = 153
number_con = str(153)
armstrong_num = 0
for i in range(len(number_con)):
    armstrong_num += int(number_con[i]) * int(number_con[i]) * int(number_con[i])
if num == armstrong_num:
    print("Given number is Armstrong number", armstrong_num)
else:
    print("Given number is not Armstrong number")

print("-" * 50)

"""
20). Python program to calculate simple interest.
Formula = P+(P*r)*t
P = Principle Amount
r = Annual interest rate
t = time
"""
P = 12000
r = 5/100
t = 5

total_amount = P + (P * r) * t
interest = P * r * t
print(f"The total amount after {t} years is {total_amount}")
print(f"The simple interest for {t} years is {interest}")

print("-" * 50)




