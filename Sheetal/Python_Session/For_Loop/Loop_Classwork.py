"""
for cond:
   code
"""
# Hello
# range(start, stop, difference)
# when we run loop with range, then it include the start value and exclude stop value

for i in range(1, 10, 1):
    print(i)

print("_"*50)
# range with 2 parameter range(start, stop), default difference value will be 1
for j in range(2, 8):
    print(j)


print("_"*50)
# print negative values in reverse order
for j in range(-10, -20, -1):
    print(j, end="")

# -10 -11 -12 -13 -14 -15 -16 -17 -18 -19


# class
# pass
# continue

print()
print("_"*50)
# range with one parameter, range(stop_value), default initial value will 0 and difference value 1
for k in range(15):
    print(k, end=" ")


"""
Range class rules
->  range accepts three parameters range(start, stop, step)
->  range output include start value and exclude stop value
->  if we don't define the initial value and step value then, 
    default initial value will be zero (0)
    default step value will be 1
    range(30) -> range(0, 30, 1) 
->  Range parameter only accept int value, float values are not allowed.
->  If we define two parameter in the range, then it will consider start value, stop value
    default step value will be 1
    range(2, 10) -> start=2, stop=10, step=1
"""
print()
print("_"*50)
####################
# apply if condition in the loop
# write a program to get all the numbers which are divisible by 7 from 1 to 50
for i in range(1, 51, 1):
    if i%7 == 0:
        print(i, end=" ")

print()
for i in range(7, 51, 7):
    print(i, end=" ")


print()
print("_"*50)
# write a python program to print table of any given number
num= 9
for i in range(1, 11):
    print(i, "*", num, "=", i*num)

"""
1 * 9 = 9
2 * 9 = 18
3 * 9 = 27
4 * 9 = 36
5 * 9 = 45
6 * 9 = 54
7 * 9 = 63
8 * 9 = 72
9 * 9 = 81
10 * 9 = 90
"""

print("_"*50)
###############Apply Loop on list ############
list1 = [5, 7, 8, 2, 88]
list2 = []
for val in list1:
    #print(val, val**2)
    list2.append(val+2)
    #print(list2)
print(list2)

print("_"*40)
list_len = len(list1)
for i in range(-list_len, 0, 1):
    print(i, list1[i])


#Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50
#Q2 write a python print square of even number and cube of odd from 1 to 20
"""
for cond1:
    for cond2:
        code

"""
for i in range(1, 5):  # outerloop
    print("address :", i)
    for j in range(1, 4):  # inner loop
        print("package :", j)

    print("_" * 30)


for a in range(1, 5):  # outerloop
    print("address :", a)
    for b in range(1, 4):  # inner loop
        print("package :", b)
    for c in ['HEllo','Goood','Morning']:
        print("Greeting :",c)

    print("_" * 30)

#Multi level loop
#Outerloop -->inner loops-->inner loop


for a in range(1, 5):  # outerloop
    print("address :", a)
    for b in range(1, 4):  # inner loop
        print("package :", b)
        for c in  ['HEllo','Goood','Morning']:
                print("Greeting :",c)

    print("_" * 30)

for a in range(1, 5):  # outerloop
    print("address :", a)
    for b in range(1, 4):  # inner loop
        print("package :", b)

        if a == 1 or a == 4:
         for c in  ['HEllo','Goood','Morning']:
                print("Greeting :",c)

    print("_" * 30)
print()
print("_"*50)
#write a python program to print below pattern
""" 
*
* *
* * * 
* * * * 
* * * * *
"""
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
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

"""
num = 345
#num = 7
reverse = 0

while num > 0: # 34 > 0 | 3 > 0 | 0> 0
    temp = num%10 # 5, 4, 3
    reverse = reverse*10 + temp #| 10*0 + 5 = 5 | 5*10 + 4 = 54| 54*10 = 3 = 543
    num = num//10 # 34 | 3 | 0


print("Reverse :", reverse)

print(-345%10)
"""


num = -345
reverse = 0

# while num < 0:
#     temp = num%10 # 5
#     reverse = reverse*10 + temp # 5
#     num = num//10 #

#print(-345//10)
# ASCII Values :
# A-Z : 65-90
# a-z : 97-122

# chr() : this function will return the character if we provide the ASCII value
print(chr(65))  # A

# ord() : This return the ASCII value of we provide the character.
print(ord("B")) # 66

for i in range(65, 91):
    print(chr(i), end=" ")
# A B C D E F G
# 6H I J K L M N O P Q R S T U V W X Y Z

print()

for i in range(97, 123):
    print(chr(i), end=" ")
# a b c d e f g h i j k l m n o p q r s t u v w x y z


print()
print("_"*50)

start_value = 65
for i in range(1, 8):
    for j in range(i):
        print(chr(start_value), end=" ")
        start_value += 1
    print()

# print(chr(91))

str1 = "Hello"
str1.upper()

print(chr(65).lower())
"""
# while loop:
while condition:
    code
"""
num1 = 1
while num1 <= 10:
    print(num1)
    num1 += 1

print("_"*50)
num1 = 10
while 10 <= num1 <= 15:
    print(num1)
    num1 += 1

print("_"*50)

# continue and break statement
# continue: continue statement, help to move on next interation without executing
# the remaining after continue
for i in range(1, 11):
    if i > 3 and i < 6:
        continue
    print(i)

print("_"*50)
print()
for j in range(1, 10):
    if j == 6:
        break
    print(j)

print("_"*50)
for i in range(1, 11):
    if i > 3 and i < 6:
        break
    print(i)

print("_"*50)
# infinite loop
num1 = 1
while True:
    print(num1)
    num1 += 1
    if num1 == 10000:
        break






