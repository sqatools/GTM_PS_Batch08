print("_"*60)
# 1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")

print("_"*60)
# 2). Python Loops program to construct the following pattern, using a nested for loops.
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
for q in range(6):
    print(q*"*")
for w in range(4, -1, -1):
    print(w*"*")

print("_"*60)
#3). Python Loops program that will add the word from the user to the empty string using python.
word = str(input("Enter the word: "))
str1 = " "
for i in range(len(word)):
    str1 += word[i]
print(str1)

print("_"*60)

# 4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
# Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for a in numbers:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Count of even numbers are: {even}")
print(f"Count of odd numbers are: {odd}")

# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for i in range(0, 11):
    if i != 3 and i != 6:
        print(i, end=" ")

# 6). Write a program to get the Fibonacci series between 0 and 20 using python.
a, b = 0, 1
for _ in range(20):
    print(a, end=' ')
    a, b = b, a+b



