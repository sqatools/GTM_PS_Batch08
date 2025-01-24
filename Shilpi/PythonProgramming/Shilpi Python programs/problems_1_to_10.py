print("1). Python Program to add two integer values.")

a = 20
b = 10
print(a, "+", b, "=", a + b)
print("_" * 100)

print("2). Python Program to subtract two integer values.")

a = 20
b = 10
print(a, "-", b, "=", a - b)
print("_" * 100)

print("3). Python program to multiply two numbers.")
a = 45
b = 25
print(a, "*", b, "=", a * b)
print("_" * 100)

print("4). Python program to repeat a given string 5 times.")
str1 = "SQATools"
print(str1 * 5)
print("_" * 100)

print("5). Python program to get the Average of given numbers.")
a = 40
b = 50
c = 30
avg = (a + b + c) / 3
print("The average of the numbers is: ", avg)
print("_" * 100)

print("6). Python program to get the median of given numbers.")
import statistics
numbers = [60, 45, 61, 70, 66, 77, 80, 100,50]
numbers.sort()
print(numbers)
m=statistics.median(numbers)
print(m)
print("_" * 100)

print("7). Python program to print the square and cube of a given number.")
num1=9
sq=num1**2
cube=num1**3
print(sq)
print(cube)
print("_" * 100)

print("8). Python program to interchange values between variables.")
a=10
b=20
a,b=b,a # since we are interchanging value, this has to be done in the same line
print("The new value of a is: ",a)
print("The new value of b is: ",b)
print("_" * 100)

print("9). Python program to solve this Pythagorous theorem.Theorem : (a2 + b2 = c2)")
a=3
b=4
c=5
lhs=(a**2)+(b**2)
rhs=c**2
print(lhs)
print(rhs)

if lhs==rhs:
    print("The triangle is a right angle triangle")
else:
    print("The triangle is not a right angle triangle")
print("_" * 100)

print("10). Python program to solve the given math formula.")
print("Formula : (a + b)^2 = a^2 + b^2 + 2ab")
a=5
b=4
lhs=(a+b)**2
rhs=(a**2)+(b**2)+(2*a*b)
print(lhs)
print(rhs)
print(lhs==rhs)
print("_" * 100)


