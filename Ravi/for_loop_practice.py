"""
1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
between 1500 and 2700 (both included).
Input1:1500
Input2:2700
"""

Input1 = 1500
Input2 = 2700
outlist = []

for i in range(Input1, Input2 + 1):
    if i % 7 == 0 and i % 5 == 0:
        outlist.append(i)
    else:
        continue

print(outlist)

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

len_2 = int(input(" Please enter the length of the design:"))

for i in range(1, len_2 + 1):
    print("*" * i)

for j in range(len_2 - 1, 0, -1):
    print("*" * j)

print("-" * 50)

"""
3). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
"""

series = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_count = 0
odd_count = 0

for i in series:
    if i % 2:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers present are:", str(even_count))
print("Number of odd numbers present are:", str(odd_count))

print("-" * 50)

"""
4). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
"""

for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    else:
        print(i)

print("-" * 50)

"""
5). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz”
instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”.
"""

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        continue

print("-" * 50)

"""
6). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
"""

input_6 = input("Enter your word:")
output_6 = ""

for i in input_6:
    if i.islower():
        output_6 += i.upper()
    else:
        output_6 += i.lower()

print(output_6)
print("-" * 50)

"""
7). Python loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4
"""

input_7 = input("Enter your input:")
num_str = '1234567890'
alpha_count = 0
digit_count = 0

for i in input_7:
    if i in num_str:
        digit_count += 1
    elif i.isalpha():
        alpha_count += 1
    else:
        print("There is a special character present:", i)

print("Number of alphabets:", alpha_count)
print("Number of digits:", digit_count)

print("-" * 50)

"""
8). Python for loop program to print the alphabet pattern ‘O’ using python.
Output:
  ***
*       *
*       *
*       *
*       *
*       *
   ***
"""

input_8 = int(input("Enter your preferable size:"))
print("Your output")
print(" "+"*"*(input_8-2)+" ")
for i in range(1,input_8):
    print("*"+" "*(input_8-2)+"*")
print(" "+"*"*(input_8-2)+" ")
print("-" * 50)

"""
9). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
"""

input_9 = int(input("Enter the input range:"))
i = 1

while i < input_9+1:
    print(i)
    i += 1
print("-" * 50)

"""
9). Python Loops program to print all alphabets from a to z using for loop
        Take chr method help to print characters with ASCII values
        chr(65) = ‘A’
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122
"""
print("Alphabet from a-z")
for i in range(26):
    print(chr(97 + i), end=' ')

print("\nAlphabet from A-Z")
for i in range(26):
    print(chr(65 + i), end=' ')

print("-" * 50)

"""
10). Python Loops program to print all even and odd numbers between 1 to 100 in python.
"""
even_list = []
odd_list = []

for i in range(1,101):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

print("-" * 50)

"""
11). Python Loops program to find the sum of all natural numbers between
1 to n using python.
"""
input_11 = int(input("Enter the end range:"))
sum_11 = 0
for i in range(1,input_11+1):
    sum += i

print("The sum of the numbers till the provided range is:", sum_11)

print("-"*50)

"""
12). Write a program to calculate the sum
of digits of a number using python.
"""
input_12 = int(input("Enter the number:"))
sum_12 = 0

while input_12 > 0:
    rem = input_12 % 10
    sum_12 += rem
    input_12 = input_12 // 10

print("Sum of the digits: ", sum_12)

print("-"*50)

"""
13). Write a program to calculate the product of digits of a number using python.
"""
input_13 = int(input("Enter the number:"))
product_13 = 1

while input_13 > 0:
    rem = input_13 % 10
    product_13 *= rem
    input_13 = input_13 // 10

print("The product of the digits of the given number is:", product_13)

print("-"*50)

"""
14). Write a program to check whether a number is a palindrome or not using python loops.
"""
num = int(input("Enter a number: "))
rev = 0
original_num = num
while num > 0:
    rem = num % 10
    rev = (rev*10) + rem
    num = num//10

print("Reverse number: ", rev)
print("Original number:", num)

if original_num == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

print("-"*50)

"""
15). Program to find the frequency of each digit in a given integer using Python Loops.
"""
num = input("Enter your number:")
str1 = str(num)
dicti = {}

for val in str1:
    if val in dicti:
        dicti[val] += 1
    else:
        dicti[val] = 1

print(dicti)
print("-"*50)

"""
16).  Python loops program to print the pattern T using Python Loops.

       Output :

       * * * * * * * * *
       * * * * * * * * *
             * * *
             * * *
             * * *
             * * *
             * * *
"""
input_16 = int(input("Enter the size:"))

for i in range(2):
    print("*"*input_16)

for j in range(4):
    print(" "+"*"*(input_16-2)+"")

print("-"*50)
"""
17). Write a program to print the pyramid structure using Python Loops.

    Output:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
input_17 = int(input("Enter the number of rows:"))

for i in range(1, input_17+1):
    print("_"*(input_17-i)+"*"*(i*2-1)+"_"*(input_17-i))

print("-"*50)

"""
18). Write a program to get input from the user if it is a number insert it into an empty list using Python Loops.
Input :
L=[]
125python
Output = [1,2,5]
"""

input_18 = input("Please provide your string:")
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
num_list = []

for i in input_18:
    if i in num:
        num_list.append(i)
    else:
        continue

print(num_list)

print("-"*50)

"""
19). Write a program to construct the following pattern, using a for loop in Python.
Output :
*
* *
* * *
* * * *
* * * * *
"""

input_19 = int(input("Enter the number of rows:"))

for i in range(1,input_19+1):
    print("*"*i)

print("-"*50)

"""
20). Write a program to print the following pattern using Python Loops.
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
input_20 = int(input("Enter the maximum number of stars required:"))

for i in range(1, input_20+1):
    if i == input_20:
        for j in range(input_20, 0, -1):
            print("*"*j)
    else:
        print("*"*i)

