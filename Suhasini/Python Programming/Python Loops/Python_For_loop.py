"""
for conditn:
    code

"""

for i in range(1,10,1):
    print(i, end=",")
# range (start, stop, difference)
# when we run loop with range, then it include the start value and exclude stop value
print()
print("_"*50)

# range with 2 parameter range(start, stop), default difference value will be 1
for i in range(1,10):
    print(i, end=(","))

print()
print("_"*50)

# print negative values in reverse order
for i in range (-1, -10, -1):
    print(i, end=",")
print()
print("_"*50)

# range with one parameter, range(stop_value), default initial value will 0 and difference value 1
for i in range (10):
    print(i, end=",")
print()
print("_"*50)

"""
Range Class Rules:
1. range accepts 3 parameters: range(start_value, stop_value, difference)
2. range output include start value and exclude stop value
3. if we don't define the initial value and step value then, 
    default initial value will be zero (0)
    default step value will be 1
    range(30) -> range(0, 30, 1) 
4. Range parameter only accept int value, float values are not allowed.
5. If we define two parameter in the range, then it will consider start value, stop value
    default step value will be 1
    range(2, 10) -> start=2, stop=10, step=1
    
"""

print()
print("_"*50)
####################
# apply if condition in the loop
# write a program to get all the numbers which are divisible by 7 from 1 to 50
print("Numbers from 1-50 that are divisible by 7 are:")
for i in range(1, 50, 1):
    if i%7 ==0:
        print(i, end=",")
print()

# OR

for i in range (7, 50, 7):
    print(i, end=",")
print()
print("_"*50)


# write a python program to print table of any given number
num = 9

for i in range (1, 11, 1):
    print(i,"*", num, "=",i*9)
print("_"*50)

###############Apply Loop on list ############
list1 = [3, 5, 1, 6, 8, 3]
list2 = []

for val in list1:
    list2.append(val*2)
print(list2)     # [6, 10, 2, 12, 16, 6]
print("_"*50)

list_len = len(list2)
for i in range (-list_len, 0, 1):     #negative indexing
    print(i, list2[i])


# Homework :
#Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50
#Q2 write a python print square of even number and cube of odd from 1 to 20