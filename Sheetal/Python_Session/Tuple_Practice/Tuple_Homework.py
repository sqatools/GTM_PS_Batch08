from colorama import *

tup6 = (4,6,8,12,13,15,16,11,22,66)


print(tup6[1:len(tup6):2])

#Print between values and skip first and last
print(tup6[1:len(tup6)-1:1])

#Print First and Last value of Tuple
print(tup6[1::-1])
print(tup6[1:-1])

num = 8
print("_"*40)

print(Fore.GREEN+"Write a program to get max from tuple without using max function."+ Style.RESET_ALL)
t1 = (55,77,203,5,1,7)
max_val=t1[0]
for val in t1:
    if val >max_val:
        max_val = val

print("The max number from the tuple is: ", max_val)

print("_"*40)
print(Fore.GREEN+"Write a program to get list of combination of two values whose sum is 20"+ Style.RESET_ALL)
t2 = (3, 6, 9, 10, 11, 12, 8, 14, 6)
result = set()  # Use a list instead of a set to maintain duplicates

for val1 in range(len(t2)):
    for val2 in range(val1 + 1, len(t2)):
        if t2[val1] + t2[val2] == 20:
            result.add(tuple(sorted((t2[val1], t2[val2]))))
print("The combinations of two values whose sum is 20 from the tuple are:")
print("\n".join(f"20 = {pair[0]} + {pair[1]}" for pair in result))


print("_"*40)
print(Fore.GREEN+"Write a program to remove the values which is repeated more than two times & store that in list"+ Style.RESET_ALL)
t3 = (1,3,1,4,1,5,6,3,6,3,7,3,4,4)
count1 = 0
result_list = {}
final_list = []
for val4 in t3:
    if val4 in result_list:
        result_list[val4] +=1
    else:
        result_list[val4] = 1

for val5,count1 in result_list.items():
    if count1 >2:
        final_list.append(val5)

print(f"The actual count of each number from the list is {result_list}")
print("The repeated values more than 2 are: ",final_list)

print("_"*40)
t3 = (1, 3, 1, 4, 1, 5, 6, 3, 6, 3, 7, 3, 4, 4)
final_list = []

for val4 in t3:
    if t3.count(val4) > 2 and val4 not in final_list:
        final_list.append(val4)

print("The repeated values more than 2 times are:", final_list)


print("_"*40)
print("Python tuple program to create a tuple with 2 lists of data.")
# Input lists:
list1 = [4, 6, 8]
list2 = [7, 1, 4]

tup7 =tuple(zip(list1,list2))

print(tup7)
print("_"*40)



