#Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50
"""
for n in range (1,50,2):
    if n%5 == 0 and n%7 == 0:
        print("the n value is 5 and which is divisible by 5 and 7 from 1 to 50 is =", n)
   # else:
       #print ("the both values are not divisible by 5 and 7 from 1 to 50 , invalid output")
#Output: the n value is 5 and which is divisible by 5 and 7 from 1 to 50 is = 35

print('_'*100)

#Q2 write a python print square of even number and cube of odd from 1 to 20

for p in range (1,20,1):
   if p%2==0 and p%2!=0:
        print("print square of even number and cube of odd from 1 to 20", p**2, p**3)
for p in range (1,20,1):
    if p%2==0:
        print("the even nulmbers = ", p**2)
    else:
        print("the odd numbers=",p**3)

print(50*"$")

#3)Inner loops:
for q in range (1,5,1):
    print("address,q :" ,q)
    for s in range (1,5,1):
        print("rent homes:",s)
    print("*"*50)

#4)Multiple inner loops:
for a in range (1,5,1):
    print("this is execute first:",a)
    for b in range (5,8,1):
        print("this will be execute second:", b)
        for c in range (10,15,1):
            print("this will be execute third:", c)
        print("*"*50)

#5)
# multi level inner loop
# outer loop -> inner loop ->  inner loop
for a in range (1,5,1):
    print("this is execute first:",a)
    for b in range (5,8,1):
        print("this will be execute second:", b)
        for c in["Good Morning", "Evening", "Night"]:
            print("this will be execute third:", c)
        print("*"*50)
"""

# write a python program to print below pattern
"""
*
* *
* * *
* * * *
* * * * *



for i in range(1, 6):  # i = 1,  2, 3, 4, 5
    for j in range(0, i, 1):  # j = 1 | 1, 2 | 1, 2, 3 |1, 2, 3, 4 | 1, 2, 3, 4, 5
        print(j, end=" ")

    print()
"""

for c in range(1,6,): #c=1,2,3,4,5
    for d in range(1,c): #d=1
        print(d, end="")

    print()