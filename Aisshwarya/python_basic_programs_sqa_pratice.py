#Python program to get the median of given numbers.
#all the numbers should be arranged in ascending order

'''
list= [10,40,20,80,70]
list.sort()
print(list)
l= len(list)
print(l)

#Python program to interchange values between variables.
a= 10
b=20

c=a
a=b
b=c
print(a,b)

import datetime
date= datetime.datetime.now()
print(date.strftime("%d,%b,%Y"))

from datetime import date
a= date(2023, 1, 5)
b= date (2023, 1, 22)
print(a-b)

number = 5
fact = 1
for i in range (1, 6) :
    print (i * fact)
    fact = fact * i

    print(fact)



# reverse number

number1= int(input("enter any number "))
revernum = str(number1)
print(revernum[::-1])

string = 'i am learning python'

list1 = string.split('2')

print(list1)
'''

'''
num1= 0
num2=1
count = 0

while count< 50:
    Num1 = 0
    num2 = 1
    n2 = num1 + num2
    num1 = num2
    num2 = n2
    count = count +1
'''
'''
fact = 1
num = int(input("enter number"))
while num >0:
    fact = fact *num
    num = num-1
print (fact)

'''

'''
a = int(input("enter any number "))
b = str(a)
print("reverese", b[::-1])
'''
'''

a= input('enter string')
b = a[::-1]
print( "reverse = " , b)
'''
A= int(input("enter marks"))

if 90 < A< 100:
    print("A grade")
elif 60 < A <= 89 :
    print( " b grade")
else :
    print( "no garde")
