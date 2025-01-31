## Write a Python Program to print value which are divisible by 5 and 7 from 1 to 50

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

