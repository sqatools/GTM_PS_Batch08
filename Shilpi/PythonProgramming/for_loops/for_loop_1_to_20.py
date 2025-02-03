print("1). Write a Python loops program to find those numbers which are divisible by 7 ")
print("and multiple of 5, between 1500 and 2700(both included)")
print("Input1:1500")
print("Input2:2700")

for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i)
    else:
        continue
print("_"*100)

'''2). Python Loops program to construct the following pattern, using a nested for loops.
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
'''
"""
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
print("_"*100)
"""

a=5
d=5//2+1
for i in range(1,6):#1
    for j in range(1,6):
        if i==1 and j==3:
            print("*", end=" ")
        elif i==2 and (j==2 or j==4):
            print("*",end=" ")
        elif i==3 and (j==1 or j==5):
            print("*",end=" ")
        elif i==4 and (j==2 or j==4):
            print("*",end=" ")
        elif i==5 and (j==3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("_"*100)

stars=int(input("Enter an odd number: "))
a=stars//2+1
b=a
c=a
d=stars-1
e=2

for i in range(1,stars+1):
    for j in range(1,stars+1):
        if (i==1 or i==stars) and j==a:
            print("*", end=" ")
        elif 1<i<=a and (j==b or j==c):
            print("*",end=" ")
        elif i>a and i!=stars and (j==d or j==e):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()
    if i>2 or i<=a:
        b=b-1
        c=c+1
    if i>a:
        d=d-1
        e=e+1
        continue
print("_"*100)

print("3). Python Loops program that will add the word from the user to the empty string using python.")
word=input("Enter word : ")
o=""
for i in word:
    o=o+i

print("Output :",o)
print("_"*100)

print("4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.")
num=(1,2,3,4,5,6,7,8,9)
e=0
o=0
for i in num:
    if i%2==0:
        e +=1
    else:
        o +=1
print("Number of even numbers :",e)
print("Number of odd numbers :",o)
print("_"*100)

print("5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python")
for x in range(0,7,1):
    if x==3 or x==6:
        continue
    else:
        print(x, end=" ")
print()
print("_"*100)

print("6). Write a program to get the Fibonacci series between 0 to 20 using python.")
a=0
b=1
c=0
print(a, end=" ")
for x in range(0,19):
    c=b+a
    a=b
    b=c

    print(a,end=" ")
print()
print("_"*100)

print("7). Write a program that iterates the integers from 1 to 30 using python")
print("For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.")
print("For numbers that are multiples of both three and five print “FizzBuzz”. ")

for i in range(1,31):
    if i%3==0 and i%5==0:
            print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
print("_"*100)

print("8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.")
print('Input : “SqaTOOlS”')
print('Output : “sqatools”')

word=input("Enter word: ")
word=word.casefold()
print("Output: ",word)

print("_"*100)

print("9). Python loops program that accepts a string and calculates the number of digits and letters using python.")
print('Input : “python1234”')
print("Output :")
print("Letters 6")
print("Digits 4")

str1=input("Enter your string: ")
for letter in str1:





































