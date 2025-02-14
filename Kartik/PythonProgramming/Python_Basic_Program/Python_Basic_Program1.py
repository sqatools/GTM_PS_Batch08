print('_'*50)
# 1). Python Program to add two integer values.
num1 = 10
num2 = 20

Addition  = num1 + num2
print("Addition of two num :", Addition)

print('_'*50)
# 2). Python Program to subtract two integer values.

num1 = 10
num2 = 20

subtract  = num2 - num1
print("subtraction of two num :", subtract)

print('_'*50)
# 3). Python Program to multiply two integer values.

num1 = 20
num2 = 80

Multiplication  = num2 * num1
print("Multiplication of two num :", Multiplication)

print('_'*50)
# 4). Python Program to repeat a given string 5 times.
str = "Python"
n = 5

print("Repeat String is :", str*n)

print('_'*50)
# 5). Python Program to get the Average of given numbers.
num1 = 10
num2 = 20
num3 = 30

Avg = ((num1 + num2 + num3)/3)

print ("Average of given number: ",Avg)

print('_'*50)
# 6). Python Program to get the median of given numbers.
value = [10,80,60,40,50]

value.sort()
n=len(value)

if n%2 == 1:
    median_value = value[n//2]
else:
    median_value = (value[n//2 -1] + value[n//2])/2

print(f"the Median is :{median_value}")

print('_'*50)
# 7). Python Print the square and cube of a given number.
n = 3

square_1 = n**2
cube_1 = n**3

print("square of number is:", square_1)
print("cube of number is:", cube_1)

print('_'*50)
# 8). Python Program to interchange values between variables.

a = 10
b = 20
a, b = b, a

print("value of a :", a)
print("value of b :", b)

print('_'*50)
# 9). Python program to solve this Pythagoras theorem.
# Theorem : (a2 + b2 = c2)
a= 2
b = 3
c = 4
lhs = (a**2 + b**2)
rhs = c**2
print(lhs)
print(rhs)

print("your result is :", lhs  , rhs)






