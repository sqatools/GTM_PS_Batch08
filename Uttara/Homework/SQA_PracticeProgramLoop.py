# Loop 20 Programs
"""P1. Write a Python loops program to find those numbers which are
 divisible by 7 and multiple of 5, between 1500 and 2700 (both included)."""

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")

print(" ")
print("*"*100)
"""Output: 1505 1540 1575 1610 1645 1680 1715 1750 1785 1820 1855 1890 1925 1960 
           1995 2030 2065 2100 2135 2170 2205 2240 2275 2310 
            2345 2380 2415 2450 2485 2520 2555 2590 2625 2660 2695"""

#2.Python Loops program that will add the word from the user to the empty string using

S1 = input("Enter the word: ")
str1 = ""
for i in range(len(S1)):
    str1 += S1[i]

print(str1)
print(" ")
print("_"*100)
"""Output:Enter the word: Python
Python"""
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
"""output:Enter a starting of series:1
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 """
#4.Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.

word = input("Enter word: ")

for char in word:
    if char.isupper():
        print(char.lower(),end="")
    else:
        print(char,end="")

print(" ")
print("_"*100)
"""Enter word: UttaRa
uttara """
#5.Python Loops program to print all natural numbers from 1 to n using a while loop in python

n = int(input("Enter the last number: "))
count = 1

while count <= n:
    print(count,end=" ")
    count += 1

print(" ")
print("_"*100)
"""OUTPUT:Enter the last number: 15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"""
#6.Python Loops program to print all even numbers between 1 to 100 in python.

for i in range(1,101):
    if i % 2 == 0:
        print(i, end=" ")

print(" ")
print("_"*100)

"""2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58
60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100"""

#7.Python Loops program to print all odd numbers between 1 to 100 using python.
for i in range(1,101):
    if i%2 != 0:
        print(i,end=" ")

print(" ")
print("_"*100)
"""1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 
59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 """

#8.Python program to find the sum of all even numbers between 1 to n using python.
n= int(input("Enter the number for sum: "))
sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum += i
print("sum of all even numbers Are:",sum)
print(" ")
print("_"*100)
"""Enter the number for sum: 57
sum of all even numbers Are: 812"""

#9.Write a program to count the number of digits in a number using python.

num = (input("Enter the  number: "))
count = 0

for n in num:
    count += 1

print("Total digits in number: ",count)
print(" ")
print("_"*100)
"""Enter the  number: 5
Total digits in number:  1"""
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
"""Enter the KM covered: 40
Total bill:  415"""

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

###############################################################################################################
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
    print()

print("_" * 100)

###############################################################################################################
#16.Write a program to display numbers from a list using Python Loops.
"""Input = [1,5,8,0,4]
Output = 1,5,8,0,4
"""
list1 = [1,5,8,0,4]
for val in list1:
    print(val,end=" ")
print()

print("_" * 100)
#1 5 8 0 4
##############################################################################################################
#17.Write a program to print each word in a string on a new line using Python Loops.
str1 = "PythonProgram"

for char in str1:
    print(char,end="\n")
print()

print("_" * 100)
"""P
y
t
h
o
n
P
r
o
g
r
a
m"""
 #################################################################################################################
#18. Write a program to create an empty list and add even numbers from 1-10 in it including 10 using Python Loops.
"""Input = []
Output :
[2,4,6,8,10]"""

even = []
for i in range(1,11):
    if i%2 == 0:
        even.append(i)

print(even)
print()

print("_"*100)

###########################################################################################################
#19.Write a program to create an empty list and add odd numbers from 1-10 in it including 1 using Python.
"""Input = []
Output : [1,3,5,7,9]"""

odd = []
for i in range(1,11):
    if i%2 != 0:
        odd.append(i)

print(odd)
print()

print("_"*100)
#output: [1, 3, 5, 7, 9]
#############################################################################################################
#20.Write a program to print the values of the keys of a dictionary using Python.
"""Input = {name’:’virat’,’sports’:’cricket’}
Output :
Virat
Cricket"""

dict1 = {'name':'virat','sports':'cricket'}
for value in dict1.values():
    print(value)
print()

print("_"*100)
"""virat
cricket"""

##############################################################################################################
#21.Write a program to print the days in a week except Sunday using a while loop in Python.
"""Output :
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
"""
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

for day in days:
    if day != "Sunday":
        print(day, end=" ")

        print()

print("_"*100)
"""Monday 
Tuesday 
Wednesday 
Thursday 
Friday 
Saturday """