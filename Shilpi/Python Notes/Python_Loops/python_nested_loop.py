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

print("_" * 50)
##### Execute inner loop with condition ###############

for a in range(1, 5):  # a = 1, 2, 3, 4
    # inner loop1
    print("address , a:", a)
    for b in range(1, 4):  # b= 1, 2, 3
        print("package , b:", b)

        # inner loop2
        if a == 1 or a == 4:
            for c in ['Hello', 'Good', 'Morning']:  # c = 'Hello', Good', 'Morning'
                print("greeting , c:", c)

    print("_" * 50)

print()
print("_" * 50)
# write a python program to print below pattern
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6):  # i = 1,  2, 3, 4, 5
    for j in range(0, i, 1):  # j = 1 | 1, 2 | 1, 2, 3 |1, 2, 3, 4 | 1, 2, 3, 4, 5
        print(j, end=" ")

    print()

"""
* * * * *
* * * *
* * *
* *
*
"""
print("_" * 50)

for i in range(5, 0, -1):  # i = 5
    for j in range(0, i):  #
        print(j, end=" ")

    print()

print("_" * 50)
#####################################################
# write a program to check given number is prime or not

num = 10
prime = True

for i in range(2, num // 2 + 1):
    print(i)
    if num % i == 0:
        # print(i)
        prime = False

# print("count value :", count)
if prime is True:
    print("This is prime number:", num)
else:
    print("This is not a prime number :", num)

print("_" * 50)
#####################################################
# write a program to get list of prime numbers from 1 to 100
prime_list = []
for num in range(2, 101): # 2, 3, 4, 5, 6
    prime = True
    for i in range(2, num): # no | 2 |2, 3 | 2, 3, 4 | 2, 3, 4, 5
        if num % i == 0:
            prime = False

    if prime:
        print(num, end=" ")
        prime_list.append(num)

print()
print(prime_list)


print("_"*50)
"""
# # @ # #
# @ # @ #
@ # # # @
# @ # @ #
# # @ # #
"""

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 and j == 3:
            print("@", end=" ")
        elif ( i == 2 and j == 2) or ( i == 2 and j == 4):
            print("@", end=" ")
        elif ( i == 3 and j == 1) or ( i == 3 and j == 5):
            print("@", end=" ")
        elif ( i == 4 and j == 2) or ( i == 4 and j == 4):
            print("@", end=" ")
        elif i == 5 and j == 3:
            print("@", end=" ")
        else:
            print(" ", end=" ")

    print()



"""
# # @ # #
# @ @ @ # 
@ @ @ @ @
# @ @ @ #
# # @ # #
"""
print("_"*50)
num_star = 5
num_rows = 5
a = 2 # 1
b = 4 # 5

for i in range(1, num_rows+1):
    if i >= 4:
        a = a + 2
        b = b - 2

    for j in range(1, num_star+1):
        if j > a and j < b:
            print("@", end=" ")
        else:
            print("#", end=" ")

    if i <= 4:
        a = a - 1
        b = b + 1


    print()




