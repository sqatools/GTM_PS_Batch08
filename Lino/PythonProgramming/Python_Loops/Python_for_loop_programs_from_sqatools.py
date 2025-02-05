#1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).

for i in range(1500,2701):
        if i%7 == 0 and i%5 == 0:
            print(i, end=" ")


#2). Python Loops program to construct the following pattern, using a nested for loops.
"""
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

for i in range(6):
    print(i*"*")
for i in range(4,-1,-1):
    print(i*"*")


#3). Python Loops program that will add the word from the user to the empty string using python.

word = input("Enter the word: ")
str1 = ""
for i in range(len(word)):
    str1 += word[i]

print(str1)


#4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0

for val in numbers:
    if val%2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)


#5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

for i in range(0,11):
        if i != 3 or i != 6:
            print(i,end=" ")



#6). Write a program to get the Fibonacci series between 0 to 20 using python.

num1 = 0
num2 = 1
count = 0

while count < 20:
    print(num1,end=" ")
    n2 = num1 + num2
    num1 = num2
    num2 = n2
    count += 1


#7). Write a program that iterates the integers from 1 to 30 using python.
# For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers that are multiples of both three and five print “FizzBuzz”.

for i in range(1,31):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")


#8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.

input1 = input("Enter word: ")
result = ''
for char in input1:
    if char.isupper():
        print(char.lower(),end="")
    else:
        print(char,end="")



#9). Python loops program that accepts a string and calculates the number of digits and letters using python.

word = "python1234"
digit = 0
character = 0

for ele in word:
    if ele.isalpha():
        character += 1
    elif ele.isnumeric():
        digit += 1

print("Digits :",digit)
print("Characters: ",character)


#10). Python for loop program to print the alphabet pattern ‘O’ using python.
"""
Output:
  ***  
*       *
*       *
*       *
*       *
*       *
   ***  
"""

for row in range(0, 7):
        for column in range(0, 7):
            # here in first and last row we want to three *
            if (row == 0 or row == 6) and (1 < column < 5) :
                print("*", end=' ')
            # here from 2 to 6 row, * will print on 1 and 5 index only.
            elif (0 < row <= 5) and (column ==1 or column ==5):
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()


#11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.

n = int(input("Enter the last number: "))
count = 1

while count <= n:
    print(count,end=" ")
    count += 1



#12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.

n = int(input("Enter the last number: "))
count = n

while count != 0:
    print(count,end=" ")
    count -= 1



#13). Python Loops program to print all alphabets from a to z using for loop

import string

print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
    print(letter, end =" ")

print("\nAlphabet from A-Z:")
for letter in string.ascii_uppercase:
    print(letter, end =" ")


#14). Python Loops program to print all even numbers between 1 to 100 in python.

for i in range(1,101):
    if i%2 == 0:
        print(i,end=" ")



#15). Python Loops program to print all odd numbers between 1 to 100 using python.

for i in range(1,101):
    if i%2 != 0:
        print(i,end=" ")



#16). Python Loops program to find the sum of all natural numbers between 1 to n using python.

n= int(input("Enter the last number: "))
total = 0

for i in range(1,n+1):
    total += i

print(total)


#17). Python program to find the sum of all even numbers between 1 to n using python.

n= int(input("Enter the last number: "))
total = 0

for i in range(1,n+1):
    if i%2 == 0:
        total += i

print(total)


#18). Python Loops program to find the sum of all odd numbers between 1 to n using python.

n= int(input("Enter the last number: "))
total = 0

for i in range(1,n+1):
    if i%2 != 0:
        total += i

print(total)


#19)Write a program to find the first and last digits of a number using python.

num = 2665
str1 = str(num)

for i in range(len(str1)):
    if i == 0:
        print("First number in the gievn number : ",str1[i])
    elif i == len(str1)-1:
        print("Last number in the gievn number : ",str1[i])



#20). Write a program to find the sum of the first and last digits of a number using python.

num = 2665
str1 = str(num)
total= 0

for i in range(len(str1)):
    if i == 0:
        total += int(str1[i])
    elif i == len(str1)-1:
        total += int(str1[i])

print("Sum of first and last number: ",total)



