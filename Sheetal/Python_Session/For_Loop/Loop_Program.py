## Write a Python Program to print value which are divisible by 5 and 7 from 1 to 50
from selenium.webdriver.common.devtools.v85.fetch import continue_request

for i in range(1, 51):
    if i%5 == 0 and i%7 == 0:
     print(i, " is divisible by 5 as well as 7 ")

print("_"*40)

##Write a Python Program to print square of even no. and cub of odd no. from 1 to 20

for i in range(1,21):
    if i%2 ==0:
        num = i**2
        print(" The square of ", i , " is: ", num)
    else:
        num = i ** 3
        print(" The cube of ", i, " is: ", num)

print("_"*40)


## Print Right angled Triangle Pattern - Method 1

for i in range(1,6):
    for j in range(1, i+1):
        print("*", end = " ")
    print()

print("_"*40)

## Print Right angled Triangle Pattern - Method 2
for i in range(1,6):
    for j in range(i):
        print("*", end = " ")
    print()

print("_"*40)

## Print Reverse Right angled Triangle Pattern
for i in range(1,6):
    for j in range(6,i,-1):
        print("*", end = " ")
    print()

print("_"*40)

###WAP to get list of prime number ####
prime_list=[]
prime=True
num = int(input("Enter a number: "))

if num <2:
    prime = False

for i in range(2,num//2+1):
    if num%i == 0:
        prime = False
        break
if prime:
    print("This is a prime number: ",num)
else:
    print("This is not a prime number", num)
    prime_list.append(num)
print("The prime number list is : ", prime_list)

print("_"*40)
# WAP to get the Fibonacci series upto the number using swap method
num_terms = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:", end=" ")
for i in range(num_terms):
    print(a, end=" ")
    a, b = b, a + b  # Update values
