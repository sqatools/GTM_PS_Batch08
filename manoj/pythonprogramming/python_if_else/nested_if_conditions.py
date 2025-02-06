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

# write a python code to simulate the interview process with the help nested if

round1 = "pass"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("congratulations first round is cleared")
    if round2 == "pass":
         print("congratulations second round is cleared")
         if round3 == "pass":
            print("congratulations you are selected")
         else:
            print("failed in last round, try next time")
    else:
         print("rejected in second round , better luck next time")
else:
    print("failed in first round, try next time")


print("_"*40)
# write if condition in one single line
# check for odd and even
num2 = 52
result = 'even' if num2%2 == 0 else 'odd'
print("output :", result)

print('even' if num2%2 == 0 else 'odd')

print("_"*50)
# write a program to check any person can give vote or not

age = 15
result = " he can vote" if age>= 18 else " he cannot vote"
print("result :", result)

# write a python program to calculate the bill amount on the basis of unit consumption
units = 150
total_bill = 0

if units <= 100:
    total_bill = units * 15
elif 100 < units <= 200:
    total_bill = units * 18
elif 200 < units <= 300:
    total_bill = units * 20
else:
    total_bill = units * 25

print("total bill amount:", total_bill)

print("_"*50)

# check any given number in the list or not
val = 51
list1 = [50, 7, 9, 2, 7]

result = True if val in list1 else False
print("result :", result)

if val in list1:
    print("value in available in list :", val, list1)
else:
    print("value is not available in list:", val, list1)


str1 = "Hello"
char = "l"
if char in str1:
    print("char is available in the string")
else:
    print("char is not available in the string")
