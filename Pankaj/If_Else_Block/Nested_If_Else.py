# Nested if else
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
round1 = "pass"
round2 = "fail"
round3 = "pass"
if round1 == "pass":
    print("First round is cleared")
    if round2 == "pass":
        print("Second round is cleared")
        if round3 == "pass":
            print("Third round is cleared")
        else:
            print("Third round is not cleared")
    else:
        print("Second round is not cleared")
else:
    print("First round is not cleared")

print("_" * 60)

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

print("_" * 60)

# write if condition in one single line
# check for odd and even
num5 = 21
result = 'even' if num5 % 2 == 0 else 'odd'
print("Output: ", result)
# or
print("even" if num5 % 2 == 0 else "odd")

print("_" * 50)
# write a program to check any person can give vote or not.
age = 17
print("can vote" if age >= 18 else "can not vote")

print("_" * 50)
# write a python program to calculate the bill amount on the basic unit consumption.
unit = 150
total_bill = 0
if unit <= 100:
    total_bill = unit * 15
elif 100 < unit <= 300:
    total_bill = unit * 18
elif 300 < unit <= 400:
    total_bill = unit * 20
else:
    total_bill = unit * 25

print("Total Bill Amount: ", total_bill)
################### in operator ##########################################
print("_"*50)
# check any given number in the list or not
value1 = 90
list1 = [20, 30, 40, 50, 60, 70, 80]
result_1 = "True" if value1 in list1 else "False"
print("Number is : ", result_1)

if value1 in list1:
    print("Number is present : ", value1, "List : ", list1)
else:
    print("Number is not present : ", value1, "List : ",  list1)

print("_"*50)
str1 = "Pankaj"
char1 = "a"
if char1 in str1:
    print("Character is present in string: ", char1)
else:
    print("Character is not present in string : ", char1)

# In one line
print("Character is present " if char1 in str1 else "Character is not present")



