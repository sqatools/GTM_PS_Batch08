#5). Python program to find area of cube
"""
for i in range(1,31,1):
    if i%3==0:
        print(i, end=" ")

"""



##WAP to find the reverse of a number and check if its palindrome or not

num1 = 1221
var1 = num1
Reverse = 0

while num1 > 0:
    Temp = num1 % 10
    Reverse = Reverse*10 + Temp
    num1 = num1//10
print("The Reverse of the number is:", Reverse)

if var1 == Reverse:
    print("The Entered number is Palindrome")
else:
    print("The Entered number is not Palindrome")