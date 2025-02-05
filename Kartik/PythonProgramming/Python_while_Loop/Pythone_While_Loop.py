"""

While Loop
while cond:
    code
"""
print("_" * 50)

# while loop with one condition
num = 1
while num <= 10:
    print(num)
    num += 1

print("_" * 50)

# while loop with multiple  condition
num = 10
while 10 <= num <= 15:
    print(num)
    num += 1

#  continue and Break statement

print("_" * 50)

# Continue : Continue statement,help to move on next iteration without executing the remaining

for i in range(1, 11):
    if i > 3 and i < 8:
        continue
    print(i)

print("_" * 50)
# Break

for j in range(1, 11):
    if j > 5 and j < 8:
        break
    print(j)

print("_" * 50)
# infinite  Loop
num = 1
while True:
    print(num)
    num += 1
    if num == 50000:
        break
"""
For Loop
A for loop iterates over a sequence of elements, such as a range of numbers, items in a list, or characters in a string. 
It is an entry-controlled loop, meaning the condition is checked before entering the loop body.

While Loop
A while loop continues to execute a block of code as long as a specified condition is true. 
It is also an entry-controlled loop.

"""
print("_" * 50)
# write a Python program to reverse the given number
num1 = 123
reverse = 0

while num1 > 0:
    temp = num1 % 10
    reverse = reverse * 10 + temp
    num1 = num1 // 10

print("reverse value:", reverse)

if var1 == reverse:
    print("This is palindrome number:", reverse)
else:
    print("This is not palindrome number:", reverse)
