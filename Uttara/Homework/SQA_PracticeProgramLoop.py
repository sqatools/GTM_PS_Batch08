# Loop 20 Programs
"""P1. Write a Python loops program to find those numbers which are
 divisible by 7 and multiple of 5, between 1500 and 2700 (both included)."""

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print("Numbers is Divisible by 7 and multiple by 5 are:",i, end=" ")

print(" ")
print("*"*100)

#2.Python Loops program that will add the word from the user to the empty string using

S1 = input("Enter the word: ")
str1 = ""
for i in range(len(S1)):
    str1 += S1[i]

print(str1)
print(" ")
print("_"*100)

#3. Write a program to get the Fibonacci series between 0 to 20 using python.
#Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

num1 = int(input("Enter a starting of series:"))
num2 = 1
count = 0

while count < 20:
    print(num1,end=" ")
    n2 = num1 + num2
    num1 = num2
    num2 = n2
    count += 1

print(" ")
print("_"*100)

#4.Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.

word = input("Enter word: ")

for char in word:
    if char.isupper():
        print(char.lower(),end="")
    else:
        print(char,end="")

print(" ")
print("_"*100)
#5.Python Loops program to print all natural numbers from 1 to n using a while loop in python

n = int(input("Enter the last number: "))
count = 1

while count <= n:
    print(count,end=" ")
    count += 1

print(" ")
print("_"*100)

#6.Python Loops program to print all even numbers between 1 to 100 in python.

for i in range(1,101):
    if i % 2 == 0:
        print(i, end=" ")

print(" ")
print("_"*100)

#7.Python Loops program to print all odd numbers between 1 to 100 using python.
for i in range(1,101):
    if i%2 != 0:
        print(i,end=" ")

print(" ")
print("_"*100)

#8.Python program to find the sum of all even numbers between 1 to n using python.
n= int(input("Enter the number for sum: "))
sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum += i
print("sum of all even numbers Are:",sum)
print(" ")
print("_"*100)

#9.Write a program to count the number of digits in a number using python.

num = (input("Enter the  number: "))
count = 0

for n in num:
    count += 1

print("Total digits in number: ",count)
print(" ")
print("_"*100)

"""10.Write a program to print the pyramid structure using Python Loops.
Output:
*
* * *
* * * * *
* * * * * * *
* * * * * * * * *"""

for i in range(1, 10):
    for j in range(0, i, 1):
        print("*", end=" ")

    print()

print("_"*100)
"""11.Write a program to accept the kilometers covered and calculate the bill according to the following using Python Loops.
First 5 km- 5rs/km
Next 20 km- 12rs/km
After that- 10rs/km"""

km = int(input("Enter the KM covered: "))
bill = 0
a=b=c=0
for i in range(1,km+1):
    if i<6:
        a += 1
    elif i > 5 and i < 26:
        b += 1
    elif i> 25:
        c += 1

bill = a*5 + b*12 + c*10
print("Total bill: ", bill)
print()

print("_"*100)
#12.Find the numbers which are divisible by 5 in 0-100 using Python Loops.

for i in range(1,101):
    if i % 5 == 0:
        print(i, end=" ") #5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100

print()
print("_"*100)
"""13.Write a program to construct the following pattern, using a for loop in Python.
Output :
* * * * *
* * * *
* * *
* *
*"""
for i in range(6,0,-1):
    print(i*"*")
print()

print("_"*100)

"""14.Write a program to construct the following pattern, using a nested for loop in Python.
Output :
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5"""

for i in range(1,6):
        for j in range(i):
            print(i,end=" ")
        print()

"""15Write a program to print a table of 5 using for loop using Python Loops.
Output :
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50"""

num = 5
table1 = 0
for i in range(1,11):
    table1 = i*num
    print(i,"*",num,"=",table1)