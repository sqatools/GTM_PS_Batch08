# Homework
# 1)write a python program to print value which be divisible by 5 and 7 from 1 to 50

for i in range(1,51, 1):
    if i%5 == 0 and i%7 == 0:
        print(i)
        # 35

# 2) Python Loops program that will add the word from the user to the empty string using python.

word = 'hello'
str1 = ""
for i in range(len(word)):
    str1 += word[i]

print(str1)
# hello

# 3) Python Loops program to count the number of even and odd numbers from a series of numbers using python.

numbers = (11, 12, 13, 14, 15, 16, 17, 18, 19)
even = 0
odd = 0

for val in numbers:
    if val%2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even numbers: ",even)  # 4
print("Number of odd numbers: ",odd)  # 5

# 4) Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for i in range(0,13):
        if i != 3 or i != 6:
            print(i,end=" ")  # 0 1 2 3 4 5 6 7 8 9 10 11 12


# 5)Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
input1 = 'MANOJ'
result = ''
for char in input1:
    if char.isupper():
        print(char.lower(),end="")
    else:
        print(char,end="")  # manoj

# 6) Python Loops program to print all natural numbers from 1 to n using a while loop in python.
n = 5
count = 1

while count <= n:
    print(count,end=" ")
    count += 1
# 1 2 3 4 5

# 7) Python Loops program to print all even numbers between 1 to 10 in python.
for i in range(1,11):
    if i%2 == 0:
        print(i,end=" ")
# 2 4 6 8 10


# 7) Python Loops program to print all odd numbers between 1 to 20 in python.
for i in range(1,19):
    if i%2 != 0:
        print(i,end=" ")

# 1 3 5 7 9 11 13 15 17

#8) Find the sum of even numbers between 1 to n
n= 23
total = 0

for i in range(1,n+1):
    if i%2 == 0:
        total += i

print(total) # 132

#9) Count the number of digits in a number
num = '12345'
count = 0

for ele in num:
    count += 1

print(f"Total digits in {num}: ",count) # 5

# 10) Write a program to find the first and last digits of a number using python.
num = 2665
str1 = str(num)

for i in range(len(str1)):
    if i == 0:
        print("First number in the given number : ",str1[i]) # 2
    elif i == len(str1)-1:
        print("Last number in the given number : ",str1[i]) # 5

# 11) Total numbers of even numbers between 1-100

count = 0

for i in range(1, 101):

  if i % 2 == 0:

    count += 1

print("Total numbers of even number: ", count) # 50



# 12) Total numbers of odd numbers between 1-100

count = 0

for i in range(1, 101):

  if i % 2 != 0:

    count += 1

print("Total numbers of odd number: ", count) # 50



# 13) Program to insert a number into an empty list

data = "125python"

List = []

for char in data:

  if char.isnumeric():

    List.append(int(char))

print(List)

# [1, 2, 5]



# 14) Program to calculate the factorial of a number

num=5

fact = 1

while num>0:

  fact = fact*num

  num = num-1

print(f"factorial of {num} is: ",fact)

# 120 Program to calculate the factorial of a number



# 15) Write a program to calculate the sum of all odd numbers between 1-100 using Python

total = 2500

for i in range(1,101):
    if i%2 != 0:
        total += i

print("Sum of odd numbers: ",total)
# 5000

# 16) Find the numbers which are divisible by 5 in 0-100 using Python Loops.
for i in range(1,101):
    if i%5 == 0:
        print(i,end=" ")
# 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100

# 17) write a Program to display numbers from a list

list1 = [1, 5, 8, 0, 4]

for val in list1:
    print(val)


#1
#5
#8
#0
#4

# 18)Write a program to print each word in a string on a new line using Python Loops.
str1 = "Sqatools"

for char in str1:
    print(char,end="\n")


# S
# q
# a
# t
# o
# o
# l
# s

# 19) Find the sum of the first 10 natural numbers using the while loop in Python Loops.
count = 1
total = 0

while count<11:
    total += count
    count += 1

print("Total: ",total)

# 55

# 20) Write a program to sort a list using for loop in Python Loops.
l = [6, 8, 2, 3, 1, 0, 5]

for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)

# [0, 1, 2, 3, 5, 6, 8]














