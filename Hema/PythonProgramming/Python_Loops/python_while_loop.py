# 30th Jan'2025

"""
#  while loop ###

while cond:
    code

"""

print("_" * 50)
# while loop with one condition
n1 = 1
while n1 <= 10:
    print(n1)
    n1 += 1

# while loop with multiple condition
print("_" * 50)
num1 = 10
while 10 <= num1 <= 15:
    print(num1)
    num1 += 1

print("_" * 40)
# Continue and break statement

# continue : continue statement, help to move on next interation without executing the remaining
#            after continue statement
for i in range(1, 11):
    if i > 3 and i < 8:
        continue

    print(i)

print("_" * 40)
# break
for j in range(1, 11):
    if j > 5 and j < 8:
        break
    print(j)

# infinite loop
"""
num = 1
while True:
    print(num)
    num += 1
    num = num + 1
    if num == 100000:
        break
"""
"""
# For Loop

A for loop iterates over a sequence of elements, such as a range of numbers,
 items in a list, or characters in a string. It is an entry-controlled loop,
  meaning the condition is checked before entering the loop body.

# While Loop

A while loop continues to execute a block of code as long as a specified condition
 is true. It is also an entry-controlled loop.

"""

# write a python program to reverse the given number
num = 122
var1 = num
reverse = 0  # 3

while num > 0:  # 123 > 0 | 12 > 0 | 1 > 0 | 0 > 0
    temp = num % 10  # 3, 2, 1
    reverse = reverse * 10 + temp  # 3 | 3*10 + 2 = 32 | 32*10 + 1 = 321
    num = num // 10  # 12 | 1 | 0

print("reveres value :", reverse)

if var1 == reverse:
    print("This is palindrome number :", reverse)
else:
    print("This is not palindrome number :", reverse)








