# 1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and
# 2700 (both included).
for num in range( 1500, 2701 ):
    if num % 7 == 0 and num % 5 == 0:
        print( num, end=" " )

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
for i in range( 1, 6 ):
    print( i * "*" )
for j in range( 4, 0, -1 ):
    print( j * "*" )

# 3). Python Loops program that will add the word from the user to the empty string using Python
str3 = input( "enter the word:" )
em_str = []
for i in range( len( str3 ) ):
    em_str += str3[i]
print( "".join( em_str ) )

# 4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
even_count = 0
odd_count = 0
num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in num:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print( f"total even number: {even_count} and total odd number are: {odd_count}" )

# 5). Write a program to get the Fibonacci series between 0 to 20 using python.
n1 = 0
n2 = 1
count = 0
while count < 20:
    print( n1, end=" " )
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1
print( n1 )

#  6). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for num in range(7):
    if num % 3 ==0 and num!=0:
        continue
    else:)
        print(num)

# 7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz”
# instead of the number and for multiples of five print “Buzz”. For numbers that are multiples of both three and five
# print “FizzBuzz”.
for i in range( 1, 31 ):
    if i % 3 == 0 and i % 5 == 0:
        print( "FizzBuzz" )
    elif i % 3 == 0:
        print( "Fizz" )
    elif i % 5 == 0:
        print( "Buzz" )
    else:
        print( i )

# 8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using
# python. Input : “SqaTOOlS”
str8 = "SqaTOOlS"
for char in str8:
    if char.islower():
        print(char.upper(),end="")  # Convert only the character to uppercase
    else:
        print(char.lower(),end="")

# 9). Python loops program that accepts a string and calculates the number of digits and letters using python.
#Input : “python1234”
str9 = "python1234"
count_val = 0
count_digit = 0
for val in str9:
    if val.isalpha():
     count_val += 1
    elif val.isdigit():
     count_digit += 1
print( f"count_val: {count_val}" )
print( f"count_digit:{count_digit}" )

# 10). Python for loop program to print the alphabet pattern ‘O’ using python.

for i in range(0,7):
    for j in range(0,7):
        if (i==0 or i==5) and (1< j <5):
            print("O",end='')

        elif(0< i <5) and (j==1 or j==5):
            print("O",end='')
        else:
            print(" ",end="")
    print()

# 11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
num = int(input("Enter the last number: "))
count =1
while count <=num:
    print(count)
    count+=1

# 12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
num = int(input("Enter the last number:"))
count=num
while count != 0:
    print(count,end=' ')
    count-=1

# 13). Python Loops program to print all alphabets from a to z using for loop Take chr method help to print characters with ASCII values
"""
        chr(65) = ‘A’
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122
"""
print("Alphabet from a to z:")
for i in range(26):
    print(chr(97+i),end=' ')
print("\nAlphabet from A to Z:")
for j in range(26):
    print(chr(65+j),end=" ")

# 14). Python Loops program to print all even numbers between 1 to 100 in python.
for i in range(1,101):
    if i % 2 ==0:
         print(i,end =" ")

# 15). Python Loops program to print all odd numbers between 1 to 100 using python.
for i in range(1,101):
    if i % 2 !=0:
        print(i,end=' ')

# 16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
num =int(input("Enter the last number:"))
count=0
for i in range(1,num+1):
 count +=i
print(count)

# 17). Python program to find the sum of all even numbers between 1 to n using python.
num =int(input("Enter the num: "))
count =0
for i in range(1,num+1):
    if i % 2 ==0:
      count +=i
print(count)

# 18). Python program to find the sum of all odd numbers between 1 to n using python.
num =int(input("Enter the num: "))
count =0
for i in range(1,num+1):
    if i % 2 !=0:
      count +=i
print(count)

# 19). Write a program to count the number of digits in a number using python.
num = '125678'
count =0
for word in range(len(num)):
 #count += 1
 total_digit=word+1
print(total_digit,end=' ')

 #  20). Write a program to find the first and last digits of a number using python.
num = 12345
num1 = str( num )
for i in range( len( num1 ) ):
    if i == 0:
        print( f"first digit is:{num1[i]}" )
    elif i == len(num1)-1 :
        print(f"last digit is:{num1[i]}")






