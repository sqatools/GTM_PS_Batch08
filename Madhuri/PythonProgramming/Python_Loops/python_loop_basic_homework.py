"""
1. Write a python program to print value which are divisible 5 and 7 between 1500 and 2700 (both included).



for i in range (1500,2700):
    if i%5 == 0 and i%7==0:
        print(i, end=" ")
# 1505 1540 1575 1610 1645 1680 1715 1750 1785 1820 1855 1890 1925 1960 1995 2030 2065 2100 2135 2170 2205 2240 2275 2310 2345 2380 2415 2450 2485 2520 2555 2590 2625 2660 2695

"""
"""
# 2. Write a python program to print square of even number and cube of odd number from 1 to 20.

for j in range(1, 21):

    if (j % 2) == 0:
        print(":Square of even number is:",j,j ** 2)
    else:
        print(":cube of odd number is:",j,j ** 3)
"""

"""
2). Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*


for i in range(1,10):
    #print("*", end =" ")
    for j in range(1,6):
     # print("*", end=" ")
        if (i==1 and j==1):
            print("*", end=" ")
        elif (i==1 and j==2) or (i==2 and j==2):
            print("*", end=" ")
        else:
            print("@", end=" ")
    print()

No Output
"""
"""
3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”

word = input("Enter the String: ")
str1 = ""
for i in range (len(word)): 
    str1=str1+word[i] #python

print(str1)

##python
"""

"""
#4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
#Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)

#Number of even numbers: 4
#Number of odd numbers: 5

number=(1,2,3,4,5,6,7,8,9)
even= 0
odd = 0
for i in number:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Even Number: ", even)
print("Odd Number: ", odd)

#Output:
#Even Number:  4
#Odd Number:  5
"""

"""
# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
#number=(1,2,3,4,5,6)
for i in range(0,7):
    if i!= 3 and i!=6:
        print(i, end=" ") #0 1 2 4 5 
    else:
        continue
print()

"""

"""
#6). Write a program to get the Fibonacci series between 0 to 20 using python.
# Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

fib1 = 0
fib2 = 1
count =0
while count<20:
    print(fib1,end=" ")
    Fib = fib1+fib2
    fib1 = fib2
    fib2 = Fib
    count= count+1
## Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

"""
"""
7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the 
number and for multiples of five print “Buzz”.For numbers that are multiples of both three and five print “FizzBuzz”. 


for i in range (1,31):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
Output:     
Fizz
Buzz
Fizz
Fizz
Buzz
Fizz
FizzBuzz
Fizz
Buzz
Fizz
Fizz
Buzz
Fizz
FizzBuzz

"""
"""
8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
Input : “SqaTOOlS”
Output : “sqatools”
"""
"""
word = input("Enter the string:")
for i in word:
    if i.isupper():
        print(i.lower(),end="")
    elif:
        print(i,end="")


word = input("Enter the string:")
for i in word:
    if i.isupper():
        print(i.lower(),end="")
    elif i.islower():
        print(i.upper(),end="") #sQAtooLs
"""
"""
9). Python loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4

word ="python1234"
digit = 0
charactor =0
for i in word:
    if i.isnumeric():
        digit=digit+1
    elif i.isalpha():
       charactor=charactor+1
print("digits:",digit)
print("charactor:",charactor)

Output:
digits: 4
charactor: 6
"""
"""
10). Python for loop program to print the alphabet pattern ‘O’ using python.
Output:
  ***  
*       *
*       *
*       *
*       *
*       *
   ***  

for row in range(0,7):
    for column in range  (0,7):
        if (row==0 and column==2) or (row==0 and column==3) or (row==0 and column==4):
            print("*",end=" ")
        elif (row == 1 and column==1) or (row ==1 and column==5):
            print("*", end=" ")
        elif (row == 2 and column == 1) or (row == 2 and column == 5):
            print("*", end=" ")
        elif (row == 3 and column==1) or (row ==3 and column==5):
            print("*", end=" ")
        elif (row == 4 and column == 1) or (row == 4 and column == 5):
            print("*", end=" ")
        elif (row == 5 and column == 1) or (row == 5 and column == 5):
            print("*", end=" ")
        elif (row == 6 and column == 2) or (row == 6 and column == 3) or (row == 6 and column == 4):
            print("*", end=" ")
        else:
            print(" ",end=" ")

    print()
Output:
    * * *     
  *       *   
  *       *   
  *       *   
  *       *   
  *       *   
    * * *     
 
"""
"""
#11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
n= int(input("Enter the Number: "))
count = 1
while count <= n:
    print(count,end=" ")
    count = count+1
    
#Enter the Number: 30
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
"""
"""
#12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
n1= int(input("Enter the Number: "))
count1 = n1
while count1 != 0:
    print(count1,end=" ")
    count1 = count1 - 1
    
    Output:
    Enter
    the
    Number: 5
    5
    4
    3
    2
    1
    """
"""
13). Python Loops program to print all alphabets from a to z using for loop
        Take chr method help to print characters with ASCII values
        chr(65) = ‘A’
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122


import string
print("Alphabates from a-z:")
for letter in string.ascii_lowercase:
    print(letter, end=" ")
print("\nAlphabates from A-Z")
for letter in string.ascii_uppercase:
    print(letter, end=" ")
    
Output:
Alphabates from a-z:
a b c d e f g h i j k l m n o p q r s t u v w x y z 
Alphabates from A-Z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
Process finished with exit code 0
"""
"""
#14). Python Loops program to print all even numbers between 1 to 100 in python.

for i in range(1,101):
    if i%2 == 0:
        print(i,end=" ")
Output:
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 
"""
"""
#15). Python Loops program to print all odd numbers between 1 to 100 using python.


for i in range(1,101):
    if i%2 != 0:
        print(i,end=" ")


Output:1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 
"""
"""
#16). Python Loops program to find the sum of all natural numbers between 1 to n using python.

num = int(input("Enter the number: "))
total=0

for i in range(1,num+1):
    total=total+i
print(total)

Output:
Enter the number: 4
10
"""
"""
#17). Python program to find the sum of all even numbers between 1 to n using python.

total = 0
no2 =int(input("Enter the number:"))
for i in range (1,no2+1):
    if i%2==0:
        total = total + i
    print(total)

"""
"""
#18). Python Loops program to find the sum of all odd numbers between 1 to n using python.


no2 =int(input("Enter the number:"))
total = 0
for i in range(1,no2+1):
    if i%2!=0:
        total = total + i
    print(total)
"""
"""
#19). Write a program to count the number of digits in a number using python.

number ="123455678"
count =0
for i in number:
   count=count+1
print("Total digit:", count)
#Total digit: 9
"""
"""
#20). Write a program to find the first and last digits of a number using python.
#21). Write a program to find the sum of the first and last digits of a number using python.

#22). Write a program to calculate the sum of digits of a number using python.
#23). Write a program to calculate the product of digits of a number using python.
#24).Python loops program to enter a number and print its reverse using python.


#25). Write a program to check whether a number is a palindrome or not using python loops.

#27). Python loops program to enter a number and print it in words.

num = int(input("Enter a number: "))
str1 = ""
for i in str(num):
    if i == "1":
        str1 += "One"
    elif i == "2":
        str1 += "Two"
    elif i == "3":
        str1 += "Three"
    elif i == "4":
        str1 += "Four"
    elif i == "5":
        str1 += "Five"
    elif i == "6":
        str1 += "Six"
    elif i == "7":
        str1 += "Seven"
    elif i == "8":
        str1 += "Eight"
    elif i == "9":
        str1 += "Nine"

print(str1)
"""