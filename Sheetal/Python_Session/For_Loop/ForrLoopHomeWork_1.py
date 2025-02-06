##Program 1
## Python Loops program to construct the following pattern, using a nested for loops.
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
num = int(input("Enter number of rows for pattern number"))

for i in range(0,num):  ##rows
    for k in range(0,i+1):  ##column
        print("*",end=" ")
    print()
for i in range(0, num):
    for j in range(i,num):
         print("*",end=" ")
    print()



"""print("_"*40)
for i in range(num-1,0):
    for j in range(0,i+1):
         print("*",end=" ")
    print()
for i in range(0,num):  ##rows
    for k in range(i,num//2):  ##column
        print("*",end=" ")
    print()
"""

#Program 2
## Full Diamond

print("_"*40)
num = int(input("Enter number of rows for the pattern: "))

# Upper part of the diamond
for i in range(1, num + 1):
    print(" " * (num - i) + "* " * i)


# Lower part of the diamond
for i in range(num - 1, 0, -1):
    print(" " * (num - i) + "* " * i)

print("_"*40)
##Python for loop program to print the alphabet pattern 0 using python.
"""Output:
  ***  
*       *
*       *
*       *
*       *
*       *
   ***  
"""
for i in range(0,13):
    for j in range(0,13):
        if (i==0 or i==12) and (1< j <11):
            print("*",end=" ")
        elif(0< i <=11) and (j==1 or j==11):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("_"*40)
#Program 3
# Print the following small alphabet letter pattern using Python Loops.
# Output =
#            a
#        b c d
#      e f g h i
#    j k l m n o p
#      q r s t u
#        v w x
#           y

print("_"*40)
#Program 4
# Write a program to find the maximum number from the list using Python Loops
# Input : [12,14,45,88,63,97,88]
# Output : Maximum number: 97




print("_"*40)
#Program 5
# Write a program to sort a list using for loop in Python Loops.
# Input = [6,8,2,3,1,0,5]
# Output = [0,1,2,3,5,6,8]



print("_"*40)
#Program 6
# Python Loops program that will add the word from the user to the empty string using python.




print("_"*40)
#Program 7
# Python Loops program to count the number of even and odd numbers from a series of numbers using python.
# Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)


print("_"*40)
#Program 8
# Write a program to find the sum of the first and last digits of a number using python.


print("_"*40)
#Program 9
# Write a program to count the number of digits in a number using python.



print("_"*40)
#Program 10
# Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.


print("_"*40)
#Program 11
# Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers that are multiples of both three and five print “FizzBuzz”.


print("_"*40)
#Program 12
# Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
# Input : “SqaTOOlS”



print("_"*40)
#Program 13
# Python loops program that accepts a string and calculates the number of digits and letters using python.
# Input : “python1234”

print("_"*40)
#Program 14
# Python Loops program to print all alphabets from a to z using for loop
#         Take chr method help to print characters with ASCII values
#         chr(65) = ‘A’


print("_"*40)
#Program 15
# Python Loops program to print all even numbers between 1 to 100 in python.


print("_"*40)
#Program 16
# Python Loops program to find the sum of all natural numbers between 1 to n using python.



print("_"*40)
#Program 17
# Python program to find the sum of all even numbers between 1 to n using python.



print("_"*40)
#Program 18
# Write a program to count the number of digits in a number using python.


print("_"*40)
#Program 19
# Write a program to find the sum of the first and last digits of a number using python.




print("_"*40)
#Program 20
# Program to find the frequency of each digit in a given integer using Python Loops



print("_"*40)
#Program 21
# Python loops program to enter a number and print it in words.