"""
for cond1:
    for cond2:
       code
"""
"""
# outer loop
for i in range(1, 5): # i = 1, 2, 3, 4
    # inner loop
    print("address , i:", i)
    for j in range(1, 4): # j= 1, 2, 3
        print("package , j:", j)

    print("_"*50)
"""

# multiple inner loops
"""
for a in range(1, 5): # i = 1, 2, 3, 4
    # inner loop1
    print("address , a:", a)
    for b in range(1, 4): # j= 1, 2, 3
        print("package , b:", b)

     # inner loop2
    for c in ['Hello', 'Good', 'Morning']: # j= 1, 2, 3
        print("greeting , c:", c)

    print("_"*50)
"""

# multi level inner loop
# outer loop -> inner loop ->  inner loop
"""
for a in range(1, 5): # a = 1, 2, 3, 4
    # inner loop1
    print("address , a:", a)
    for b in range(1, 4): # b= 1, 2, 3
        print("package , b:", b)

        # inner loop2
        for c in ['Hello', 'Good', 'Morning']: # c = 'Hello', Good', 'Morning'
            print("greeting , c:", c)

    print("_"*50)
"""

##### Execute inner loop with condition ###############

for a in range(1, 5): # a = 1, 2, 3, 4
    # inner loop1
    print("address , a:", a)
    for b in range(1, 4): # b= 1, 2, 3
        print("package , b:", b)

        # inner loop2
        if a == 1 or a == 4:
            for c in ['Hello', 'Good', 'Morning']: # c = 'Hello', Good', 'Morning'
                print("greeting , c:", c)

    print("_"*50)

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
"""
for i in range (1, 6):
    print(i*"* ")
print()
"""

# Program to print below pattern
"""
* * * * *
* * * *
* * *
* *
*
"""

for i in range (5, -1, -1):
    print(i*"* ")
print()
print("_"*80)

