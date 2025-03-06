"""
# while loop:
while condition:
    code
"""
num1 = 1
while num1 <= 10:
    print(num1)
    num1 += 1

print("_"*50)
num1 = 10
while 10 <= num1 <= 15:
    print(num1)
    num1 += 1

print("_"*50)

# continue and break statement
# continue: continue statement, help to move on next interation without executing
# the remaining after continue
for i in range(1, 11):
    if i > 3 and i < 6:
        continue
    print(i)

print("_"*50)
print()
for j in range(1, 10):
    if j == 6:
        break
    print(j)

print("_"*50)
for i in range(1, 11):
    if i > 3 and i < 6:
        break
    print(i)

print("_"*50)
# infinite loop
num1 = 1
while True:
    print(num1)
    num1 += 1
    if num1 == 10000:
        break