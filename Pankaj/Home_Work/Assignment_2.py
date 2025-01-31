################# Homework ########################
print("_" * 60)
# 1). write a python program to check given number is divisible by 3 or not
print("Answer 1: ")
num1 = int(input("Enter you number: "))
if num1 % 3 == 0:
    print(num1, "Number is divisible by 3")
else:
    print(num1, "Number is not divisible by 3")

print("_" * 60)
# 2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
print("Answer 2: ")
if num1 % 2 == 0:
    print(f"{num1} is even & ", f"Square of {num1} is: ", num1 ** 2)
else:
    print(f"{num1} is odd & ", f"Qube of {num1} is: ", num1 ** 3)

print("_" * 60)
# 3). write a python program to check given number is positive or negative.
print("Answer 3: ")
if num1 < 0:
    print(f"Number is negative number: {num1}")
elif num1 == 0:
    print(f"Number is neutral Number: {num1}")
else:
    print(f"Number is positive number: {num1}")

print("_" * 60)
# 4). Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the number.
if num1 % 7 == 0:
    print(f"{num1} is divisible by 7, ", f"adding {num1} with 50: ", num1 + 50)
else:
    print(f"{num1} is not divisible by 7, ", f"subtracting {num1} with 50: ", num1 - 50)