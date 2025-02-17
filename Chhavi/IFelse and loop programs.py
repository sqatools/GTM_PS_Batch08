# write a program to ask user his age and decide wheather you are eligible to vote or not?
"""
a = int(input("Please enter your age :"))
if a >= 18:
    print("You are eligible to vote")
else:
    print("you are too young to vote")

"""

# write a program to ask user his age and decide wheather you are eligible to vote or not? if you are above 18 ask the gender and direct them to the concerned room for voting
"""
a = int(input("Please enter your age :"))
if a >= 18:
    print("You are eligible to vote")
    b = str(input("whats your gender; type M for Male and F for Female " ))
    if b == "M":
        print("Please go to room no 1 for vote")
    elif b == "F":
        print("Please go to room no 2 for vote")
    else:
        print("please enter a valid input")
else:
    print("you are too young to vote")

"""

"""
#Write a program that takes a grade (a number between 0 and 100) and prints the corresponding letter grade:
90-100 = A
80-89 = B
70-79 = C
60-69 = D
Below 60 = F


marks = int(input("Please enter your marks : "))

if marks > 0 and marks < 100:
    print("Please enter a valid two digit number")
elif marks > 1 and marks <60:
    print("Your grade is F")
elif marks >= 60 and marks < 69:
    print("Your grade is D")
elif marks >= 70 and marks < 79:
    print("Your grade is C")
elif marks >= 80 and marks < 89:
    print("Your grade is B")
elif marks >= 90:
    print("Your grade is A")

"""
"""
#Write a program that asks the user to input their purchase amount and applies a discount based on the following conditions:
#Purchase amount over $1000: 20% discount
#Purchase amount between $500 and $1000: 10% discount
#Purchase amount less than $500: 5% discount

bill = int(input("Please enter your bill amount : "))

if bill > 500:
    print("You are eligible to get 5% discount on your next purchase"
elif bill >= 500 and bill < 1000:
    print("You are eligible to get 10% discount on your next purchase")
elif bill > 1000:
    print("You are eligible to get 20% discount on your next purchase"
"""


def reverse_negative(num):
    if num >= 0:
        return "Please enter a negative number."

    reversed_num = int(str(abs(num))[::-1])
    return -reversed_num


# Example usage
num = -56743
print(reverse_negative(num))  # Output: -54321