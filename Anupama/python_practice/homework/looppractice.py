for i in range(1,11,1):
#range(start,stop, step/diffrence)
    print(i, end="")
print()

for j in range(-10,0,1):
    print(j, end="")
    print()

#apply if condition in loop
#write a prog to get all the numbers devisible by 7 till 50
for i in range(1,51,1):
    if i%7==0:
        print(i, " ", end="")
        print()

#***python program to print a mltiplication table*****
num=8
for i in range(1,11):
    print(i, "*",num, "=", i*num)

#*****apply loop on list*********
l1=[2,4,6,8,0,11,33]
for val in l1:
    print(val, val**2)
    print()

#****** program to print * in inverted pyramid form****
for a in range(1,6,1):
    print(a*"*")
for a in range(4,0,-1):
    print(a*"*")
    print()

#****** program to print * in pyramid form****

print("*"*15,"Print * in a pyramid shape", "*"*15)
n = int(input("number of lines for pyramid: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*",end="")
    print()


#****** Program to find even and odd numbers form a given series****
print("*"*15,"Program to find even and odd numbers form a given series", "*"*15)
bucket = (1,3,2,4,6,7,8,9,12,54,31)
eve = 0
odd= 0

for i in bucket:
    if i%2==0:
        eve=eve+1
    else:
        odd=odd+1
print("No. of even:",eve)
print("No. of odd:", odd)
print()

#*****program to print a string 5 times*****
print("*"*15,"print a string five times", "*"*15)
a = str(input("String to print: "))
t=1
while t < 6:
    print(a)
    t=t+1
print()