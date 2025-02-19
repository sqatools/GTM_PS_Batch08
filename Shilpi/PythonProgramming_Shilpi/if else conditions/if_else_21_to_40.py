"""
print("21). Python program to check whether the given number is positive or negative and even or odd.")
# Input = 26
# Output = The given number is positive and even
num1=int(input("Enter number: "))
if num1>0:
    if num1%2==0:
        print(num1,"is positive and even")
    else:
        print(num1,"is positive and odd")
else:
    if num1%2==0:
        print(num1,"is negative and even")
    else:
        print(num1,"is negative and odd")
print("_"*100)

print("22). Python program to print the largest number from two numbers.")
# Input:25, 63
# Output = 63
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
if num1>num2:
    print(num1,"is the greater of the two numbers")
elif num2>num1:
    print(num2,"is the greater of the two numbers")
else:
    print("The two numbers are equal")
print("_"*100)
"""
print("23). Python program to check whether a given character is uppercase or not.")
# Input = A
# Output = The given character is an Uppercase
char1=input("Enter alphabet: ")
if char1.isupper():
    print("The given character is in the uppercase")
else:
    print("The given character is lowercase")
print("_"*100)