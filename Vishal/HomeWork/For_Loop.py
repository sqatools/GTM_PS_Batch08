#Program1
"""
x = 123

for x in range(1500, 2701):
    if x%7 == 0 and x%5 == 0:
        print(x, end=' ')
"""
#Program2
"""
even = 0
odd = 0
for x in range(1, 100):
    if x%2 == 0:
        even = even+1
    else:
        odd = odd+1
print("even :", even)
print("odd :", odd)
"""

#Program3
"""
for x in range(0, 7):
    if x == 3 or x == 6:
        continue
    print(x,end=' ')
"""

#Program4

"""
for x in range(1, 30):
    if x%3==0 and x%5==0:
        print("FixxBuzz")
    elif x%5==0:
        print("buzz")
    elif x%3==0:
        print('Fizz')
"""
#Program5
"""
for i in range(1, 6):
    for j in range(i):
        print("*", end=' ')
    print()
"""

#Program6
"""
for i in range(6,-1, -1):
    for j in range(i):
        print("*", end=' ')
    print()
"""

#Program7
"""
for i in range(1, 6):
    for j in range(i):
        print("*", end=' ')
    print()
for i in range(6,-1, -1):
    for j in range(i):
        print("*", end=' ')
    print()
"""

#Program8
"""
count = 0
for x in range(0,101):
    if x%2==0:
        count+= 1
print("total numbers of even numbers between 0 to 100 is :", count)
"""

#Program9
"""
sum = 0
count = 0
for x in range(0,101):
    if x%2!=0:
        count+= 1
        sum = sum+x
print("total numbers of odd numbers between 0 to 100 is :", count)
print("Sum of all odd numbers between 0 to 100 is :", sum)
"""

#Program10
"""
for i in range(1,3):
    for j in range(1,7):
        print("*", end=' ')
    print()
for i in range(1,5):
    for j in range(1,6):
        if 2 < j < 5:
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()
"""

