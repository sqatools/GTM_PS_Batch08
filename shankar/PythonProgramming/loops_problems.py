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
word = "python"
empty_str = ""
for i in word:
    empty_str += i
print(empty_str)

print("-" * 50)
"""
4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_nums_count = 0
odd_nums_count = 0
for i in numbers:
    if i % 2 == 0:
        even_nums_count += 1
    else:
        odd_nums_count += 1
print(f"Number of even numbers: {even_nums_count}")
print(f"Number of odd numbers: {odd_nums_count}")

print("-" * 50)

"""
5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
"""
for i in range(7):
    if i == 3 or i == 6:
        pass
    else:
        print(i, end=" ")
print()
print("-" * 50)
"""
6). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
"""
limit = 20
a, b = 0, 1  # first 2 number in series
for i in range(limit):
    if i > limit:
        break
    for j in range(1):
        a, b = b, a + b
    print(a, end=" ")

print()
print("-" * 50)
"""
7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” 
instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”.
"""
for i in range(1, 31):
    if (i % 3 == 0) and (i % 5 == 0):
        print(f"{i} multiple of 3 and 5, So 'FizzBuzz'")
    elif i % 3 == 0:
        print(f"{i} multiple of 3, So 'Fizz'")
    elif i % 5 == 0:
        print(f"{i} multiple of 5, So 'Buzz'")
    else:
        continue

print("-" * 50)
# Using List Comprehension

FizzBuzz = ["FizzBuzz" if (num % 3 == 0) and (num % 5 == 0)
            else "Fizz" if (num % 3 == 0)
else "Buzz" if (num % 5 == 0)
else num for num in range(1, 31)]
print(FizzBuzz)

print("-" * 50)
"""
8). Write a program that accepts a word from the user and converts all uppercase's in the word to lowercase using python.
Input : “SqaTOOlS”
Output : “sqatools”
"""
word = "SqaTOOlS"
lowercase_word = ""
for i in word:
    lowercase_word += i.lower()
print(lowercase_word)

print("-" * 50)
# used list comprehension
lowercase_list = [i.lower() for i in word]
print("".join(lowercase_list))

print("-" * 50)
"""
9). Python loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4
"""
n = "python1234"
letters = 0
digits = 0
for char in n:
    if char.isalpha():
        letters += 1
    else:
        digits += 1

print(f"Given string count of Letters : {letters}")
print(f"Given string count of Digits : {digits}")

print("-" * 50)
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
"""
n = 10
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n)
    else:
        print("* " + " " * (n-2) + "*")

print("-" * 50)
"""
11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
"""
n = 10
natural_nums = []
count = 1
while count <= n:
    natural_nums.append(count)
    count += 1
print(natural_nums)

# using list comprehension
natural_nums = [i for i in range(1,n+1)]
print(natural_nums)


print("-" * 50)
"""
12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
"""
natural_nums = [i for i in range(n,0,-1)]
print(natural_nums)

n = 10
natural_nums = []
count = n
while count > 0:
    natural_nums.append(count)
    count -= 1
print(natural_nums)


print("-" * 50)
"""
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
n = 2345
convert_to_str = str(n)
sum_n_digits = 0
for i in convert_to_str:
    sum_n_digits += int(i)
print(f"total sum of {n} digits is {sum_n_digits}")

digits_sum = sum(int(dig) for dig in str(n))
print(f"total sum of {n} digits is {digits_sum}")
print("-" * 50)

# Write python program to get values in a list are divided by 3 and 7.

list_1 = [9, 42, 33, 21, 28, 25]

result = [num for num in list_1 if num % 3 == 0 and num % 7 == 0]
print(f"Numbers are divided by 3 and 7 are {result}")

print("-" * 50)

# Write python program to get average of a list.

total = sum([num for num in list_1])
count = len([num for num in list_1])

average = total // count
print(f"average of a list is {average}")
