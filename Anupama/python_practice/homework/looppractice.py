"""for i in range(1,11,1):
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
    print()"""

#****** program to print * in inverted pyramid form****
for a in range(1,6,1):
    print(a*"*")
for a in range(4,0,-1):
    print(a*"*")