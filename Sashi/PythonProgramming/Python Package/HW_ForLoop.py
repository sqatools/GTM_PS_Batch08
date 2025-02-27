"""""""""
#Write a Python loops program to find those numbers which are divisible by 7 ")
print("and multiple of 5, between 1500 and 2700(both included)")
print("Input1:1500")
print("Input2:2700")

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
    
""""""""

print("_" * 50)

#Python Loops program to construct the following pattern, using a nested for loops.
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

""""""
import string

a=4
for i in range(1,10):
    if i<=5:
        for j in range(0,i):
            print("* "*i)
            break
    else:
        print("* "*a)
        a=a-1
        continue
"""""""""""""
print("_" * 50)


a = 5
d = 5 // 2 + 1
for i in range(1, 6):  # 1
    for j in range(1, 6):
        if i == 1 and j == 3:
            print("*", end=" ")
        elif i == 2 and (j == 2 or j == 4):
            print("*", end=" ")
        elif i == 3 and (j == 1 or j == 5):
            print("*", end=" ")
        elif i == 4 and (j == 2 or j == 4):
            print("*", end=" ")
        elif i == 5 and (j == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
""""""""""""""


print("_" * 50)

#Python Loops program that will add the word from the user to the empty string using python.")
word = input("Enter word : ")
o = ""
for i in word:
    o = o + i

print("Output :", o)

""""""""""""
print("_" * 50)

# Python Loops program to count the number of even and odd numbers from a series of numbers using python.")
num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
e = 0
o = 0
for i in num:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
print("Number of even numbers :", e)
print("Number of odd numbers :", o)
"""""""""""""

print("_" * 50)

# Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python")
for x in range(0, 7, 1):
    if x == 3 or x == 6:
        continue
    else:
        print(x, end=" ")
print()
""""""""
print("_" * 50)

# Write a program to get the Fibonacci series between 0 to 20 using python.")
a = 0
b = 1
c = 0
print(a, end=" ")
for x in range(0, 19):
    c = b + a
    a = b
    b = c

    print(a, end=" ")
print()

""""""""
print("_" * 50)

# Write a program that iterates the integers from 1 to 30 using python")
print("For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.")
print("For numbers that are multiples of both three and five print “FizzBuzz”. ")

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
""""""""""""
print("_" * 50)


# Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.")
print('Input : “SqaTOOlS”')
print('Output : “sqatools”')

word = input("Enter word: ")
word = word.casefold()
print("Output: ", word)

"""""""

print("_" * 50)

#Python loops program that accepts a string and calculates the number of digits and letters using python.")
print('Input : “python1234”')
print("Output :")
print("Letters 6")
print("Digits 4")

str1 = input("Enter your string: ")
letters = 0
digits = 0
for letter in str1:
    if letter.isalpha():
        letters += 1
    else:
        digits += 1
print(f"Letters {letters}")
print(f"Digits {digits}")

""""""""
print("_"*50)


# Python for loop program to print the alphabet pattern ‘O’ using python.")

for i in range(1,8):
    for j in range(1,6):
        if (i==1 or i==7) and 1<j<5:
            print("*", end=" ")
        elif 1<i<7 and (j==1 or j==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
"""""""    
print("_"*50)

# Python Loops program to print all natural numbers from 1 to n using a while loop in python.")
n=int(input("Enter number: "))
i=1
while i<=n:
    print(i,end=" ")
    i+=1
print()

""""""
print("_"*50)

#Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.")
n=int(input("Enter number: "))
while n>=1:
    print(n,end=" ")
    n=n-1
print()

""""""
print("_"*50)

# Python Loops program to print all alphabets from a to z using for loop \n Take chr method help to print characters with ASCII values \n chr(65) = ‘A’ \n    A-Z ASCII Range  65-90 \n     a-z ASCII Range  97-122")

for n in string.ascii_lowercase:
    print(n,end=" ")
print()
for i in string.ascii_uppercase:
    print(i, end=" ")
print()

"""""""
print("_"*50)

for n in range(65,91):
    print(chr(n),end=" ")
print()
for i in range(97,123):
    print(chr(i),end=" ")
print()

""""""
print("_"*50)

#Python Loops program to print all even numbers between 1 to 100 in python.")
for x in range(2,101,2):
    print(x,end= " ")
print()
""""""
print("_"*50)

#Python Loops program to print all odd numbers between 1 to 100 using python.")
for x in range(1,101,2):
    print(x,end=" ")
print()

""""""
print("_"*50)

#Python Loops program to find the sum of all natural numbers between 1 to n using python.")
n=int(input("Enter number : "))
num1=0
for x in range(1,n+1):
    num1+=x
print("The sum of all natural numbers from 1 to",n, "is",num1)

""""""
print("_"*50)

#Python program to find the sum of all even numbers between 1 to n using python.")
n= int(input("Enter number : "))
num1=0
for i in range(2,n,2):
    num1+=i
if n%2==0:
    num1=num1+n

print(f"The sum of all even numbers between 1 and {n} is {num1}")

""""""
print("_"*50)

# Python Loops program to find the sum of all odd numbers between 1 to n using python.")
n=int(input("Enter number : "))
num1=0
for i in range(1,n,2):
    num1+=i
if n%2!=0:
    num1=num1+n
print(f"The sum of all odd numbers between 1 and {n} is {num1}")
print()

""""""
print("_"*50)
# Write a program to count the number of digits in a number using python.")
num2=input("Number: ")
digits=0
for i in num2:
    digits+=1
print(f"The number of digits in the number {num2} is {digits}")

"""""""""""""""""""
print("_"*50)

# Write a program to find the first and last digits of a number using python.")
num3=input("Enter number: ")

for x in range(0,len(num3)):
    if x==0:
        print(f"The first digit is {num3[x]}")
    elif x==len(num3)-1:
        print(f"The last digit is {num3[-1]}")
        
"""""""""""""""""""""""""""

