
print("*"*15,"check if given number is divisible by 3", "*"*15)
a = int(input("Integer value of a: "))
if (a%3)==0:
    print(a,"is divisible by 3")
else:
    print(a,"is not divisible by 3")
"""**********************************************************************************"""

print("*"*15,"print square of even number and cube of odd number", "*"*15)
a = int(input("Integer value of a: "))
if(a%2)==00:
    print("square of", a,"is",a**2)
else:
    print("Cube of",a, "is", a**3)
"""**********************************************************************************"""


print("*"*15,"check  if given number is positive or negative", "*"*15)
a = int(input("Integer value of a: "))
print("Given number is: ", a)
if a<0:
    print("The number is negative: ", a)
else:
    print("The number is positive: ", a)

"""**********************************************************************************"""

print("*"*10,"check  if given number is divisible by 7 then add 50, else subtract 50 from number", "*"*10)
a = int(input("Integer value of a: "))
if(a%7)==0:
    print("Final value of",a ,"is: ",a+50)
else:
    print("Final value of",a,"is:", a-50)

"""**********************************************************************************"""

print("*"*15,"simple calculator", "*"*15)
a = int(input("Integer value of a: "))
b = int(input("Integer value of b: "))
c = int(input("choose the operation 1 for '+' , 2 for '-', 3 for '*', 4 for '/' :"))
if c==1:
    print("The sum of a and b = ", a+b)
elif c==2:
    print("The difference of a and b = ", a - b)
elif c==3:
    print("The multiplied value of a and b = ", a * b)
elif c==4:
    print("A divided by b = ", a % b)
else:
    print("Invalid operation")
print("-"*50)

#**write a python code to simulate the interview process with the help nested if condition**

round1 = "fail"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("congrats first round is cleared")

    if round2 == "pass":
        print("congrats second round is cleared")
        if round3 == "pass":
            print("congrats you are selected")
        else:
            print("Failed in last round, try next time")
    else:
        print("Failed in second round, try next time")

else:
    print("Failed in first round, try next time")
print("-"*50)

#**python program to find number of strings and numbers**
str1 = input("Enter your string: ")
letters = 0
digits = 0
for letter in str1:
    if letter.isalpha():
        letters += 1
    else:
        digits += 1
print(f"Letters {letters}")
print(f"Digits {digits}")
print("_"*100)
