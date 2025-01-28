"""
2). If else program to get all the numbers divided by 3 from 1 to 30.
"""
final_list = []

for i in range(1, 31):
    if i % 3 == 0:
        final_list.append(i)
    else:
        continue
print(final_list)

print("-" * 50)

"""
3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""
marks = int(input("Please enter your total marks out of 100: "))

if marks < 40:
    print("Grade: Fail")
elif 40 <= marks < 50:
    print("Grade: C")
elif 50 <= marks < 60:
    print("Grade: B")
elif 60 <= marks < 70:
    print("Grade: A")
elif 70 <= marks < 80:
    print("Grade: A+")
elif 80 <= marks < 90:
    print("Grade: A++")
elif 90 <= marks <= 100:
    print("Grade: Excellent")
else:
    print("Invalid Marks")

print("-" * 50)

"""
4). Python program to check the given number divided by 3 and 5.
"""

num1 = int(input("Please enter a number:"))

if num1 % 3 == 0:
    if num1 % 5 == 0:
        print("The given number is divisible by both 3 and 5")
    else:
        print("The given number is only divisible by 3")
else:
    print("The given numver is neither divisible by 3 nor 5")

print("-" * 50)

"""
5). Python program to print the square of the number if it is divided by 11.
"""

num2 = int(input("Please enter a number:"))

if num2 % 11 == 0:
    print(num2 ** 2)
else:
    print(num2)

print("-" * 50)

