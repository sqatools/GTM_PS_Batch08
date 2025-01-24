question = input("""Enter 1-to check given number is divisible by 3 or not
Enter 2-print square if number is even or print cube if number is odd
Enter 3-to check if a given number is positive or negative
Enter 4-to check if the given number is divisible by 7 then add 50 to the number else subtract 50 from the number\n""")

if question == "1":
    print("1). write a python program to check given number is divisible by 3 or not")
    num1 = int(input("Enter your number: "))

    if num1 % 3 == 0:
        print(num1, "is divisible by 3")
    else:
        print(num1, "is not divisible by 3")
    print("_" * 100)

elif question == "2":

    print("2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd")
    num2 = int(input("Enter your number: "))

    if num2 % 2 == 0:
        print("The square of", num2, "is", num2 ** 2)
    else:
        print("The cube of", num2, "is", num2 ** 3)
    print("_" * 100)

elif question == "3":
    print("#3). write a python program to check if a given number is positive or negative.")
    num3 = int(input("Enter your number: "))

    if num3 < 0:
        print(num3, "is a negative number")
    elif num3 == 0:
        print(num3, "a mirror from negativity to positivity")
    else:
        print(num3, "is a positive number")
    print("_" * 100)

elif question == "4":
    print("#4).Check if the given number is divisible by 7 then add 50 to the number else subtract 50 from the number")
    num4 = int(input("Enter your number: "))

    if num4 % 7 == 0:
        print(num4, "+ 50 =", num4 + 50)
    else:
        print(num4, " - 50 =", num4 - 50)
    print("_" * 100)

else:
    print("invalid choice")
