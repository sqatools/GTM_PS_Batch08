#Python program to get the median of given numbers.
#all the numbers should be arranged in ascending order

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
for i in number :
    print (i * fact)
