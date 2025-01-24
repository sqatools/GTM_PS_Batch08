print("*"*50)
#lets check if the given numbers are even or odd

a1 = 11
b1 = a1%2

if b1==0:
    print("This is an even number :", b1)
else:
    print("This is an odd number :", b1)


print("#"*50)

#1). write a python program to check given number is divisible by 3 or not

num1 = int(input("Please enter any number :"))
num2 = num1%3

print("division output :", num2)

if num2 == 0:
    print("the number entered is divisible by 3", num1)
else:
    print("the number entered is not divisible by 3", num2)



#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
print("#"*50)

n = int(input("please enter any number :"))
Sq = n**2
Cu = n**3
n4 = n % 2

if n4 == 0:
    print("This is an even number :", n)
    print("The square of the number is :", Sq)
else:
    print("This is an odd number :", n)
    print("The cube of the number is :", Cu)

print("_"*50)

#3). write a python program to check given number is positive or negative.

V1 = float(input("enter any number :"))

if V1 > 0:
    print("This is a postive number:", int(V1))
else:
    print("This is a negative number:", int(V1))



#4).  Check given number is divisible by 7 then add 50 in the number else subtract 50 from the number

Num1 = int(input("Please enter any number:"))
Num2 = Num1 % 7
Num3 = add(Num1 + 50)
Num4 = sub(Num1 - 50)

print("condition output:", Num2)

if Num2 == 0:
    print("This is divisible  by number 7", Num1,)
    print("the new number is :", Num3)
else:
    print("This is not divisible  by number 7", Num1, )
    print("the new number is :", Num4)




