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


print()
print("_"*50)
# range with one parameter, range(stop_value), default initial value will 0 and difference value 1
for k in range(15):
    print(k, end=" ")


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