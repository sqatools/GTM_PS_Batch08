"""
for cond1:
    for cond2:
       code
"""
# outer loop
for i in range(1, 5):  # i = 1,2
    # inner loop
    print("address ,i:", i)
    for j in range(1, 4):  # j = 1,2,3
        print("package ,j :", j)

    print("_"*50)
"""
"""

# multiple level inner loop
# outer loop -> inner loop -> inner loop

for a in range(1, 5):  # a = 1,2, 3, 4
    # inner loop 1
    print("address ,a:", a)
    for b in range(1, 4):  # b = 1,2,3
        print("package ,b :", b)
        
        #  inner loop 2
        for c in ['hello', 'good', 'morning']: # b ='hello','good','morning'
            print("greeting , c:", c)

    print("_"*50)


##### Execute inner loop with condition ########
for a in range(1, 5):  # a = 1,2, 3, 4
    # inner loop 1
    print("address ,a:", a)
    for b in range(1, 4):  # b = 1,2,3
        print("package ,b :", b)

        #  inner loop 2
        if a ==1 or a ==4 :
            for c in ['hello', 'good', 'morning']:  # b ='hello','good','morning'
                print("greeting , c:", c)

    print("_" * 50)

print()
print("_"*50)
# write a python program to print below pattern
"""
*
* *
* * *
* * * * 
* * * * *
"""

for i in range(1, 6):
    for j in range(0, i, 1):
        print(j, end=" ")

    print()

"""
* * * * *
* * * *
* * *
* * 
*
"""
print("_"*50)
for i in range(6, 1, -1):
    for j in range(0, i-1, 1):
        print(j, end=" ")

    print()
