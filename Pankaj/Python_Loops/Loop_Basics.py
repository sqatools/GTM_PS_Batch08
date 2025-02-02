"""
for cond:
    code

"""

# range (start,stop,difference)
# when we run loop with range, then it include the start value and exclude stop value
print("_*60")
for i in range(1, 10, 2):  # range is class
    print(i)
print("_*60")
# range with two parameter (start,stop), default value will be 1 if not defined
for j in range(2, 7):
    print(j)

print("_*60")
# Reverse order
for x in range(-20, -10):
    print(x, end=" ")  # for printing in horizontal line

print("_*60")
# range with single value (by default it will start from 0 till range with difference 1)

for y in range(10):
    print(y, end=" ")

for q in (1, 20, 2):
    print(q, q * q * q)
# Note: range (start, stop, step)
# Note: range() can not generate sequence of float

"""
Range class rules
->  range accepts three parameters range(start, stop, step)
->  range output include start value and exclude stop value
->  if we don't define the initial value and step value then, 
    default initial value will be zero (0)
    default step value will be 1
    range(30) -> range(0, 30, 1) 
->  Range parameter only accept int value, float values are not allowed.
->  If we define two parameter in the range, then it will consider start value, stop value
    default step value will be 1
    range(2, 10) -> start=2, stop=10, step=1
"""

# apply if condition in the loop
# write a program to get all the numbers which are divisible by 7 from 1 to 50
for i in range(1, 51):
    if i % 7 == 0:
        print(i, end=" ")
print()
for i in range(1, 51, 7):
    print(i, end=" ")
print()
print("_" * 50)

# write a python program to print table of any given number
num = 9
for i in range(1, 11, 1):
    print(f"{num} * {i} = ", num * i)

print("_" * 50)
###############Apply Loop on list ############

list1 = [5, 7, 8, 2, 88]
list2 = []
for var in list1:
    list2.append(var+2)
print(list2)

print("_"*70)

# for printing index in negative
length = len(list1)
for i in range(-length, 0, 1):
    print(i, list1[i])

# for printing in +ve index
for i in range(length):
    print(i, list1[i])

#Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50
#Q2 write a python print square of even number and cube of odd from 1 to 20