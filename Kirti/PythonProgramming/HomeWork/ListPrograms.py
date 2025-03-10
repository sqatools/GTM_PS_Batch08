"""
1). Python program to calculate the square of each number from the given list.
"""
list1 = (6, 8, 4, 12, 6)
list2 = []
for i in list1:
    list2.append(i**2)

print("Program 1 : ", list2)

"""
2). Python program to combine two lists.
"""
list1 = [6, 8, 4, 12, 6]
list2 = [46, 62, 24, 2, 36]
list1.extend(list2)

print("Program 2 : ", list1)

"""
3). Python program to calculate the sum of all elements from a list.
"""
list3 = [46, 62, 24, 2, 36]

print("Program 3 :", sum(list3))


"""
4). Python program to find a product of all elements from a given list.
"""
list4 = [6, 8, 4, 12, 6]
product=1
for i in list4:
    product  = product * i

print("Program 4 : ",product)


"""
5). Python program to find the minimum and maximum elements from the list.
"""
list4 = [6, 8, 4, 12, 6]
min = min(list4)
max = max(list4)

print("Program 5 : ")
print("Min value is : ",min)
print("Max value is : ", max)


"""
6). Python program to differentiate even and odd elements from the given list.
"""
list6 = [6,9,23,2,7,45, 8,3, 4,1, 12, 6]
even =[]
odd = []
for ele in list6:
    if ele%2 == 0:
        even.append(ele)
    else:
        odd.append(ele)

print("Program 6 : ")
print(f"Even elements : {even} and Odd elements : {odd}")

"""
7). Python program to remove all duplicate elements from the list.
"""
list7 = [6,9,23,2,7,45,8,3,2,4,1,8,12, 6]
list_out =[]
for ele in list7:
    if ele not in list_out:
        list_out.append(ele)
    else:
        continue

print("Program 7 : Distinct element list  ", list_out)


"""
8). Python program to print a combination of 2 elements from the list whose sum is 10.
"""
list8 = [6, 9, 23, 2, 7, 45, 8, 3, 4, 1, -13]
list_out = []
for i in range(len(list8)):
    temp = list8[i]
    in_list=[]
    for j in range(i+1, len(list8)):
        if (temp + list8[j]) == 10:
            in_list.append(temp)
            in_list.append(list8[j])
            list_out.append(tuple(in_list))

print("Program 8 : ",list_out)


"""
9). Python program to print squares of all even numbers in a list.
"""
list9 = [6,9,23,2,7,45, 8,3, 4,1, 12, 6]
even =[]
for ele in list9:
    if ele%2 == 0:
        print(f"{i} : {ele**2}")

"""
10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
"""
list10 = [6,9,23,2,7,45, 8,3, 4,1, 12, 6]
even =[]
odd = []
for ele in list6:
    if ele%2 == 0:
        even.append(ele)
    else:
        odd.append(ele)

print("Program 10 : ", odd + even)


"""
Q 11 . Python program to get common elements from two lists.
Input =
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
Output : [4, 5, 7, 2]
"""
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
list3 = []
for element in list1:
    if element in list2:
        list3.append(element)

print("Program 11 : ", list3)

"""
12). Python program to reverse a list with for loop.
"""
list12 = [4, 5, 7, 9, 2, 1]
list_out =[]
for i in range(-1, -len(list12)-1, -1):
    list_out.append(list12[i])

print("Program 12 : ", list_out)


"""
13). Python program to reverse a list with a while loop.
"""
list13 = [4, 5, 7, 9, 2, 1]
list_out =[]
i=-1
while(i>= -len(list13)):
    list_out.append(list13[i])
    i-=1

print("Program 13 : ", list_out)


"""
14). Python program to reverse a list using index slicing.
"""
list14 = [4, 5, 7, 9, 2, 1]
print("Program 14 : ", list14[::-1])
print("Program 14 : ", list14[-1:-len(list14)-1:-1])


"""
15). Python program to reverse a list with reversed and reverse methods.
"""
list15 = [4, 5, 7, 9, 2, 1]
list15.reverse()
print("Program 15 list.reverse() : ", list15)

list15 = [4, 5, 7, 9, 2, 1]
print("Program 15 reversed(list) :  " )
for i in reversed(list15):
    print( i, end=' ')

"""
16). Python program to copy or clone one list to another list.
"""
list16 = [4, 5, 7, 9, 2, 1]
list17 = list16.copy()
print("Program 16 : ",list17)


"""
17). Python program to return True if two lists have any common member.
"""
list17 = [4, 5, 7, 9, 2, 1]
list18 = [11,21,3,40,5,6]
comm = False

for i in list17:
    if i in list18:
        comm = True
        break
    else:
        continue

print("Program 17 : ", comm)



"""
18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
"""
list18 = [4, 5, 7, 9, 2, 1,8, 4, 0,3]
list_out = []
for i in range(len(list18)):
    if i in [0,2,5]:
        continue
    else:
        list_out.append(list18[i])

print("Program 18 : ", list_out)


"""
19). Python program to remove negative values from the list.
"""
list19 = [4, 5, -7, 9, -2, 1,8, -4, 0,3]
list_out = []
for i in list19:
    if i < 0:
        continue
    else:
        list_out.append(i)

print("Program 19 : ", list_out)


"""
20). Python program to get a list of all elements which are divided by 3 and 7.
"""
list20 = [4, 5, 7, 9, 21, 1,8, 42, 0,3]
list_out = []
for i in list20:
    if i%3 == 0 and i%7 == 0 and i!=0:
        list_out.append(i)
    else:
        continue

print("Program 20 : ", list_out)