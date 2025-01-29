#Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50

for n in range (1,50,2):
    if n%5 == 0 and n%7 == 0:
        print("the n value is 5 and which is divisible by 5 and 7 from 1 to 50 is =", n)
   # else:
       #print ("the both values are not divisible by 5 and 7 from 1 to 50 , invalid output")
#Output: the n value is 5 and which is divisible by 5 and 7 from 1 to 50 is = 35

print('_'*100)

#Q2 write a python print square of even number and cube of odd from 1 to 20
"""
for p in range (1,20,1):
   if p%2==0 and p%2!=0:
        print("print square of even number and cube of odd from 1 to 20", p**2, p**3)
"""
for p in range (1,20,1):
    if p%2==0:
        print("the even nulmbers = ", p**2)
    else:
        print("the odd numbers =",p**3)

