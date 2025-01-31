"""
for cond1:
    code
   for cond2:
       code
"""
# outer loop
for i in range(1, 5):
    print("Address :", i)
    # inner loop
    for j in range(1, 4):
        print("Package:", j)
    print("_"*50)

# Multiple inner loop
for a in range(1, 5):
    print("Address :", a)
    # inner loop 1
    for b in range(1, 4):
        print("Package:", b)
    # inner loop 2
    for c in ['Hello', 'Good', 'Morning']:
        print("Address :", c)

print("_"*50)
# nested three loop
for e in range(1, 5):
    print("Address :", e)
    # inner loop 1
    for f in range(1, 4):
        print("Package:", f)
        # inner loop 2
        for c in ['Hello', 'Good', 'Morning']:
            print("Address :", c)

    print("_" * 50)

# Execute inner loop with condition
for e in range(1, 5):
    print("Address :", e)
    # inner loop 1
    for f in range(1, 4):
        print("Package:", f)
        # inner loop 2
        if a == 1 or a == 4 :
            for c in ['Hello', 'Good', 'Morning']:
                print("Address :", c)

    print("_" * 50)

# Print star pattern
"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""

# 1st way
for q in range(6):
    print(q*"* ")

# 2nd way
print("_" * 50)
for z in range(1, 6):
    for y in range(z):
        print("*", end=" ")

    print("\n")


print("_"*50)
# Print above pattern in reverse order
# 1st way
for w in range(4, -1, -1):
    print(w*"* ")

# 2nd way
print("_" * 50, "ppppp")
for z in range(6, 0, -1):
    for y in range(z):
        print("*", end=" ")

    print()

# 30/01/2025
print("_" * 50)
#####################################################
# Note* : Prime numbers are only divisible by 1 and by itself.
# 1 we can ignore
num = 10
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
if prime:
    print("This is prime number:", num)
else:
    print("This is not prime number: ", num)

# print("Same above program with division by 2: ")
# taking half of number and checking for prime
num = 10
prime = True
for i in range(2, num // 2 + 1):
    #print(i)
    if num % i == 0:
        prime = False
if prime:
    print("This is prime number:", num)
else:
    print("This is not prime number: ", num)

print("_"*60)


# prime all prime number from 1 to 100
for num in range(2, 101): #2, 3, 4, 5, 6
    prime = True
    for i in range(2, num//2+1): # no |2|2,3|,2,3,4|2,3,4,5
        if num % i == 0:
            prime = False

    if prime:
        print(num, end=" ")
print()
print("_"*70)
# print below pattern with only @
"""
# # @ # #
# @ # @ #
@ # # # @
# @ # @ #
# # @ # #

"""

for i in range(6):
    for j in range(6):
        print("*")
