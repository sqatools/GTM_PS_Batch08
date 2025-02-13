"""
1). Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
Input1:1500
Input2:2700
"""
num1 = 1500
num2 = 2700
for i in range(num1, num2 + 1):
    factors_of_5 = []
    for j in range(num1, num2 + 1):
        if j % 5 == 0:
            factors_of_5.append(j)
    if (i % 7 == 0) and (i in factors_of_5):
        print(f"{i} is divisible by 7 and factor of 5")
    else:
        print(f"{i} is not divisible by 7 and factor of 5")
print("-" * 50)
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
"""
rows = 10

for i in range(1, rows + 1):
    if 0 < i <= (rows // 2):
        print(i * "* ")
    else:
        print((rows - i) * "* ")

# for j in range(1, rows):
#    print((rows-j) * "* ")

print("-" * 50)
"""
3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”
"""

print("-" * 50)
"""
4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5

print("-" * 50)
5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

print("-" * 50)

6). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

print("-" * 50)
7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”.

print("-" * 50)
8). Write a program that accepts a word from the user and converts all uppercase's in the word to lowercase using python.
Input : “SqaTOOlS”
Output : “sqatools”

print("-" * 50)
9). Python loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4

print("-" * 50)
10). Python for loop program to print the alphabet pattern ‘O’ using python.
Output:
  ***
*       *
*       *
*       *
*       *
*       *
   ***

print("-" * 50)

11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.

Solution
12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.

print("-" * 50)
13). Python Loops program to print all alphabets from a to z using for loop
        Take chr method help to print characters with ASCII values
        chr(65) = ‘A’
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122
print("-" * 50)
14). Python Loops program to print all even numbers between 1 to 100 in python.

print("-" * 50)
15). Python Loops program to print all odd numbers between 1 to 100 using python.

print("-" * 50)
16). Python Loops program to find the sum of all natural numbers between 1 to n using python.

print("-" * 50)
17). Python program to find the sum of all even numbers between 1 to n using python.

print("-" * 50)
18). Python Loops program to find the sum of all odd numbers between 1 to n using python.

print("-" * 50)

19). Write a program to count the number of digits in a number using  python.

print("-" * 50)
20). Write a program to find the first and last digits of a number using python.

print("-" * 50)
21). Write a program to find the sum of the first and last digits of a number using python.

print("-" * 50)
22). Write a program to calculate the sum of digits of a number using python.
"""

print("-" * 50)
