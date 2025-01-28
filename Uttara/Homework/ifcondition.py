# 1.Write a python program to check given number is divisible by 3 or not.#
print("Divisible by 3 or not output")
numb1= int(input("please enter value:"))
var1 = 553
print("Condition Output:", numb1 % var1)
if numb1 % var1 == 0:
    print("This number is divisible by 3")
else:
    print("This number is not divisible by 3")
#output:This number is not divisible by 3
print("_"*100)


# 2.Write a python program to print Square (num**2) if number is even or cube(num**3)if number is odd.#
print("Square and cube value output")
n = int(input("please enter value:"))
var2 = 2
print("Condition output for further:", n % var2)
if n % var2 == 50:
    print("Value is even so print Square", n**2)
else:
    print("Value is odd so print Cube:", n**3)

print("_"*100)

# 3.Write a python program to check whether the given number is positive or not#
print("positive or negative output")
num1 = int(input("please enter a number:"))
if num1 > 0:
    print("Number is positive", num1)
else:
    print("Number is negative:", num1)


#4.Write a program check given number is divisible by 7 then add 50 in number else substract 50 from number#

print("Add 50 else subtract 50 program output")
num2 = int(input("please enter a number:"))
valu1 = 7
if num2 % valu1 == 0:
    print("Number is divisibleby 7 so add 50 in given number", num2+50)
else:
    print("Number is not divisible by 7 so subtract 50 from number", num2-50)