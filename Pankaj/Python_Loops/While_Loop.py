"""
# While Loop:
while cond:
      code
"""
print("_" * 70)
n1 = 1
while n1 <= 5:
    print(n1)
    # n1 += 1
    n1 = n1 + 1

print("_" * 70)
# While loop with multiple condition
n2 = 10
while 10 <= n2 <= 15:  # n2 >=10 and n2 <=15
    print(n2)
    n2 = n2 + 1

print("_" * 70)
# Continue and break statement

# continue : continue statement, help to move on next interation without executing the remaining
#            after continue statement
for i in range(1, 10):
    if 3 < i < 7:
        continue
    print(i)

print("_" * 70)
for j in range(1, 10):
    if 5 < j < 7:
        break
    print(j)

# infinite loop
""" 
num = 1
while True:
    print(num)
    num += 1
    num = num + 1
    if num == 1000:
        break
"""

"""
# For Loop
--> A for loop iterates over a sequence of elements, such as a range of numbers, items in a list, or characters in a 
    string. 
--> It is an entry-controlled loop, meaning the condition is checked before entering the loop body.

# While Loop
--> A while loop continues to execute a block of code as long as a specified condition is true. 
--> It is also an entry-controlled loop.

"""

# write a python program to reverse the given number
num = 121
reverse = 0
original_num = num # store the original value of num
while num != 0:
    temp = num % 10 # 1, 2, 1
    reverse = reverse * 10 + temp, # 1, 12, 121
    num = num // 10 # 12, 1, 0

print("Reverse Value", reverse)
if original_num == reverse: # stored original value of num, and use for comparison
    print("This number is palindrome: ", reverse)
else:
    print("This number is not palindrome: ", reverse)


