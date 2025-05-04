"""
if cond1:
    code
    if cond2:
        code
        if cond3:
            code
        else:
            code
    else:
        code
else:
    code



"""

# write a python code to simulate the interview process with the help nested if condition

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

"""
if cond1:
   code
   if cond2:
       code
   elif cond3:
       code
   else:
       code
      
else:
   code
   if cond_x:
      code
   else:
      code


"""

# write a program to check given positive or negative
"""


"""
num1 = 50

if num1 > 0:
    print(num1 ** 3)
    if num1 > 10 and num1 < 20:
        print(num1 // 2)
    elif num1 > 20 and num1 < 30:
        print(num1 // 4)
    else:
        print(num1 // 5)

else:
    print(num1 ** 2)
    if num1 > -10 and num1 < -50:
        print(num1 * 2)
    elif num1 > -50 and num1 < -100:
        print(num1 * 4)
    else:
        print(num1 * 5)

print("_" * 40)
# write if condition in one single line
# check for odd and even
num2 = 52
result = 'even' if num2 % 2 == 0 else 'odd'
print("output :", result)

print("even" if num2 % 2 == 0 else "odd")

print("_" * 50)
# write a program to check any person can give vote or not.
age = 15
result = "He can vote" if age >= 18 else "He can't vote"
print("result :", result)

# write a python program to calculate the bill amount on the basic unit consumption.
units = 155
total_bill = 0

if units <= 100:
    total_bill = units * 15
elif 100 < units <= 200:
    total_bill = units * 18
elif 200 < units <= 300:
    total_bill = units * 20
else:
    total_bill = units * 25

print("Total bill amount :", total_bill)

print("_"*50)
# check any given number in the list or not
val = 51
list1 = [50, 7, 9, 2, 7]

result = "True" if val in list1 else "False"
print("result :", result)


if val in list1:
    print("Value in available in list :", val, list1)
else:
    print("Value is not available in list:", val, list1)



str1 = "Hello"
char = "l"
if char in str1:
    print("char is available in the string")
else:
    print("char is not available in the string")
