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
print("_" * 50)
for z in range(6, 1):
    for y in range(z):
        print("*", end=" ")

    print("\n")
