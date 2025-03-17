"""
#1). Python function program to add two numbers.

def add(a,b):
    sum = a+b
    print("Sum:", sum)

add(11,11) #Sum: 22
"""
#2). Python function program to print the input string 10 times.

"""
def String(str1):
    print(str1*10)
string = input ("Enter the String")

String(string) 

# Enter the String Hi
 # Hi Hi Hi Hi Hi Hi Hi Hi Hi Hi
 """

 #OR
"""
def String(str1):
    print(str1*10)

String("Hello") #HelloHelloHelloHelloHelloHelloHelloHelloHelloHello



#3). Python function program to print a table of a given number.

def Table(num):
    val=0
    for i in range(1,11):
        val= i*num
        print(i, "*" , num , "=", val)

Table(6)

1 * 6 = 6
2 * 6 = 12
3 * 6 = 18
4 * 6 = 24
5 * 6 = 30
6 * 6 = 36
7 * 6 = 42
8 * 6 = 48
9 * 6 = 54
10 * 6 = 60
"""
"""
#4). Python function program to find the maximum of three numbers.

#Input: 17, 21, -9
#Output: 21

def Greatest_val(num1,num2,num3):
    if num1 > num2:
        if num1 > num3 :
            print("num1 is greatest number")
    elif num2>num1:
        if num2>num3:
            print("num2 is greatest number")
    else:
        print("num3 is greatest number")

Greatest_val(17,21,-9) #num2 is greatest number


#5). Python function program to find the sum of all the numbers in a list.
#Input : [6,9,4,5,3]
#Output: 27

def Sum(list1):
    sum= 0
    for val in list1:
        sum= sum+val
    print("Sum:", sum)

Total = Sum([6,9,4,5,3]) #Sum: 27



#6). Python function program to multiply all the numbers in a list.
#Input : [-8, 6, 1, 9, 2]
#Output: -864

def Multiply(list1):
    Total =1
    for val in list1:
        Total= Total * val
    print("Total:", Total)

Multiply([-8, 6, 1, 9, 2]) #Total: -864
"""


"""
7). Python function program to reverse a string.
Input: Python1234
Output: 4321nohtyp


def rev(str1):
    Str7 = str1[::-1]
    print("Revers string is:", Str7)

rev("Python1234") #Revers string is: 4321nohtyP

"""

"""
8). Python function program to check whether a number is in a given range.
Input : num = 7, range = 2 to 20
Output: 7 is in the range


def check(num):
    if num in range (1,20):
        print("NUmber is in ranges")

    else:
        print("Number not in range")

num1 = int(input("Entert the Number"))
check(num1)

Entert the Number7
NUmber is in ranges


#Entert the Number45
#Number not in range
"""

"""
9). Python function program that takes a list and returns a new list with unique elements of the first list.
Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
Output : [2, 3, 1, 4, 6 ]


def unique(list1):
    print(list(set(list1)))

l = [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
unique(l) #[1, 2, 3, 4, 6]
"""

"""
10). Python function program that take a number as a parameter and checks whether the number is prime or not.
Input : 7
Output : True


def prime(num):
    count =0
    for i in range(2,num):
        if num%i == 0:
            count = count+1

        if count > 0:
          print("It is prime number")
        else:
            print("Not prime number")

prime(7)

"""

"""
11). Python function program to find the even numbers from a given list.
Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Output : [2, 4, 6, 8]


def Even_number(list1):
    even_list = []

    for val in list1:
        if val %2 == 0:
            even_list.append(val)
    print(even_list)

Even_number([1, 2, 3, 4, 5, 6, 7, 8, 9]) #[2, 4, 6, 8]
"""


"""
12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.
Input: 1 to 10
Output: 1, 4, 9, 16, 25, 36, 49, 64, 81


def square():
    for i in range(1,11):
        print(i,":",i**2)

square()
"""

#13). Python function program to execute a string containing Python code.


"""  
#14). Python function program to access a function inside a function.

def test(a):
    def add(b):
        nonlocal a
        a = a + 0
        return a + b

    return add


func = test(10)
print(func(10))

"""

"""
15). Python function program to calculate the sum of numbers from 0 to 10.
Output: 55


def Sum(num1):
    sum = 0
    for i in range (1,11):
        sum = sum + i
    print("Sum is:", sum)

Sum(10) #Sum is: 55

"""

"""
16). Python function program to create a function with *args as parameters.
Input: 5, 6, 8, 7
Output: 125 216 512 343

def func(*args):
    for num in args:
        print(num**3,end=" ")

func(1,2,3) #1 8 27 
"""

"""
17). Python function program to get the factorial of a given number.
Input: 5
Output: 120



def fact(n):
    fact = 1
    while n > 0:
        fact = fact * (n-1)
    print("Factorial of num:", fact)

fact(5)


"""

"""
18). Python function program to get the Fibonacci series up to the given number.
Input: 10
Output: 1 1 2 3 5 8 13 21 34


def fibo():
    num1 = 0
    num2 = 1
    count = 0
    while count < 10:
        print(num1, end=" ")
        n2 = num1 + num2
        num1 = num2
        num2 = n2
        count += 1


fibo() #0 1 1 2 3 5 8 13 21 34
"""
"""
19 ). Python function program to get unique values from the given list.
Input : [4, 6, 1, 7, 6, 1, 5]
Output : [4, 6, 1, 7, 5]


def unique(l):
    distinct = set(l)
    print(list(distinct))

unique([4, 6, 1, 7, 6, 1, 5]) #[1, 4, 5, 6, 7]
"""
"""
#20). Python function program to get the duplicate characters from the string.
#Input: Programming
#Output: {‘g’,’m’,’r’}
def dupli(string):
    list1 = []
    for char in string:
        if string.count(char) > 1:
            list1.append(char)
    print(set(list1))
dupli('Programming')
"""

"""
24). Python function program to get the square of all values in the given dictionary.
Input = {‘a’: 4, ‘b’ :3, ‘c’ : 12, ‘d’: 6}
Output = {‘a’: 16, ‘b’ : 9, ‘c’: 144, ‘d’, 36}


def square(d):
    a = {}
    for key,value in d.items():
        a[key] = value**2
    return a
square({'a':4,'b':3,'c':12,'d':6})

"""