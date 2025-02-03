"""
for cond:
   code
"""
# range(start, stop, difference)
# when we run loop with range, then it include the start value and exclude stop value

for i in range(1, 10, 1):
    print(i)

print("_"*50)
# range with 2 parameter range(start, stop), default difference value will be 1
for j in range(2, 8):
    print(j)


print("_"*50)
# print negative values in reverse order
for j in range(-10, -20, -1):
    print(j, end="")

# -10 -11 -12 -13 -14 -15 -16 -17 -18 -19


# class
# pass
# continue

print()
print("_"*50)
# range with one parameter, range(stop_value), default initial value will 0 and difference value 1
for k in range(15):
    print(k, end=" ")


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
print()
print("_"*50)
####################
# apply if condition in the loop
# write a program to get all the numbers which are divisible by 7 from 1 to 50
for i in range(1, 51, 1):
    if i%7 == 0:
        print(i, end=" ")

print()
for i in range(7, 51, 7):
    print(i, end=" ")


print()
print("_"*50)
# write a python program to print table of any given number
num= 9
for i in range(1, 11):
    print(i, "*", num, "=", i*num)

"""
1 * 9 = 9
2 * 9 = 18
3 * 9 = 27
4 * 9 = 36
5 * 9 = 45
6 * 9 = 54
7 * 9 = 63
8 * 9 = 72
9 * 9 = 81
10 * 9 = 90
"""

print("_"*50)
###############Apply Loop on list ############
list1 = [5, 7, 8, 2, 88]
list2 = []
for val in list1:
    #print(val, val**2)
    list2.append(val+2)
    #print(list2)
print(list2)

print("_"*40)
list_len = len(list1)
for i in range(-list_len, 0, 1):
    print(i, list1[i])


#Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50
#Q2 write a python print square of even number and cube of odd from 1 to 20
