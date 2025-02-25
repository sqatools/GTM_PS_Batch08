# 1). Python program to calculate the square of each number from the given list.
list1 = [1, 2, 3, 4, 5]
for i in list1:
    print( i ** 2, end=' ' )

# 2). Python program to combine two lists.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3, 4]
list3 = [list1 + list2]
print( list3 )

# 3). Python program to calculate the sum of all elements from a list.
list3 = [1, 2, 3, 4, 5, 6, 7]
count = 0
for i in list3:
    count += i
print( count )

# 4). Python program to calculate the product of all elements from a list.
list4 = [1, 2, 3, 4, 5, 6, 7]
count = 1
for i in list4:
    count *= i
print( count )

# 5). Python program to find the minimum and maximum elements from the list.
list5 = [67, 33, 5, 2, 3, 89]
min_val = list5[0]
max_val = list5[0]
for i in range( len( list5 ) ):
    if list5[i] < min_val:
        min_val = list5[i]
    elif list5[i] > max_val:
        max_val = list5[i]

print( min_val, max_val )

# 6). Python program to differentiate even and odd elements from the given list.
list6 = [2, 54, 6, 7, 9, 10]
even = []
odd = []
for i in list6:
    if i % 2 == 0:
        even.append( i )
    elif i % 2 != 0:
        odd.append( i )

print( even, odd )

# 7). Python program to remove all duplicate elements from the list.
list7 =[1,3,4,3,1,88,4,56,7,88,9]
final_list=[]
for i in list7:
    if i not in final_list:
        final_list.append(i)
print(final_list)

# 8). Python program to print a combination of 2 elements from the list whose sum is 10.
list8 = [2, 4, 6, 71, 8, 9, 1, 5, 5]
for i in range( len( list8 ) ):
    for j in range( i + 1, len( list8 ) ):
        if list8[i] + list8[j] == 10:
            print( list8[i], list8[j] )

# 9). Python program to print squares of all even numbers in a list.
list9 = [3, 5, 7, 3, 8, 34]
new_list = []
for i in list9:
    if i % 2 == 0:
        new_list.append( i ** 2 )
print( new_list )


# 10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
  Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
odd=[]
even=[]
for i in Input:
    if i % 2 ==0:
        even.append(i)
    else:
        odd.append(i)
odd.extend(even)
print(odd)

#11).  Python program to get common elements from two lists.

list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
common_list=[]
for i in list1:
    if i in list2:
        common_list.append(i)
print(common_list)

# 12). Python program to reverse a list with for loop.
list1 = [5,6,3,2,44,67,88,23]
for i in range(len(list1)-1,-1,-1):
    print(list1[i],end =' ')

# 13). Python program to reverse a list with a while loop.
list1 = [3,2,46,7,3,2]
count = len(list1)-1
while count>0:
      print(list1[count],end=" ")
      count -= 1

# 14). Python program to reverse a list using index slicing.
list1 =[6,3,6,10,1,5,8,9]
print(list1[::-1])

# 15). Python program to reverse a list with reversed and reverse methods.
list1 = [2,3,7,9,3,1]
list1.reverse()
print(list1)
list2 =[7,3,91,12,34,222,3,1]
print(list(reversed(list2)))

# 16). Python program to copy or clone one list to another list.
list = [8,3,99,12,44,22,11]
list1 = list.copy()
print(list1)

# 17). Python program to return True if two lists have any common member.
list1 =[2,3,4,6,10]
list2 =[1,3,6,10,7,98]
for i in list1:
    if i in list2:
     print(True)

# 18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
list1 = [3,5,3,2,6,8,887,55,42]
list1 = [element for (value,element) in enumerate(list1) if value not in (2 , 4 , 7)]
print(list1)

# 19). Python program to remove negative values from the list.
list =[4,5,3,9,6,-3,-8,-1,55,33]
for i in list:
    if i >=0:
        print(i ,end=" ")

# 20). Python program to get a list of all elements which are divided by 3 and 7.
list1 = [21,12,18,56,76,273,4,33,67,55,234]
list2=[]
for i in list1:
    if i % 3 ==0 or i % 7 == 0:
        list2.append(i)
print(list2)


