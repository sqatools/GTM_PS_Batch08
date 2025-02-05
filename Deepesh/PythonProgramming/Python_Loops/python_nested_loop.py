"""
for cond1:
    for cond2:
        code

"""
for i in range(1, 5):  # outerloop
    print("address :", i)
    for j in range(1, 4):  # inner loop
        print("package :", j)

    print("_" * 30)


for a in range(1, 5):  # outerloop
    print("address :", a)
    for b in range(1, 4):  # inner loop
        print("package :", b)
    for c in ['HEllo','Goood','Morning']:
        print("Greeting :",c)

    print("_" * 30)

#Multi level loop
#Outerloop -->inner loops-->inner loop


for a in range(1, 5):  # outerloop
    print("address :", a)
    for b in range(1, 4):  # inner loop
        print("package :", b)
        for c in  ['HEllo','Goood','Morning']:
                print("Greeting :",c)

    print("_" * 30)

for a in range(1, 5):  # outerloop
    print("address :", a)
    for b in range(1, 4):  # inner loop
        print("package :", b)

        if a == 1 or a == 4:
         for c in  ['HEllo','Goood','Morning']:
                print("Greeting :",c)

    print("_" * 30)
print()
print("_"*50)
#write a python program to print below pattern
""" 
*
* *
* * * 
* * * * 
* * * * *
"""
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
