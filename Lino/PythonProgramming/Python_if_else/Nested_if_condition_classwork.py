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
