print("_" * 40)
print("Python tuple program to create a tuple with 2 lists of data.")
# Input lists
list1 = [4, 6, 8]
list2 = [7, 1, 4]
# Output= ((4, 7), (6, 1), (8, 4))
tup7 = tuple(zip(list1,list2))

print(tup7)

print("_"*40)
print("Python tuple program to find the maximum value from a tuple.")
Input = (41, 15, 69, 55)
# Output = 69
maximum = 1
for maxim in Input:
    if maxim > maximum:
        maximum = maxim

print(f"The maximum number from Tuple is {maximum}")

print("_" * 40)
print("Python tuple program to find the minimum value from a tuple.")
Input1 = (36,5,79,25)
# Output = 5

max_val = Input1[0]

for val in Input1:
    if val > max_val:
        max_val = val

print(f"The maximum value from the Tuple is {max_val}")


print("_" * 40)
print("Python tuple program to create a list of tuples from a list having a number and its square in each tuple.")
Input2 = [4,6,3,8]
# Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]
output1 =[]
for num in Input2:
    num_sqr = num**2
    output = (num,num_sqr)
    output1.append(output)
print(output1)

print("_"*40)
print("Python tuple program to create a tuple with different datatypes.")
# Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})


print("_" * 40)
print("Python tuple program to create a tuple and find an element from it by its index no.")
Input3 = (4, 8, 9, 1)
Index = 2
# Output = 9

print("_"*40)
print("Python tuple program to assign values of tuples to several variables and print them.")
Input4 = (6,7,3)
# Variables = a,b,c
# Output:
# a, 6
# b, 7
# c, 3


print("_" * 40)
print("Python tuple program to add an item to a tuple.")
Input5= ( 18, 65, 3, 45)
# Output=(18, 65, 3, 45, 15)


print("_" * 40)
print("Python tuple program to convert a tuple into a string.")
Input = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
# Output = Sqatools


print("_" * 40)
print("Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.")
Input = ('s', 'q', 'a', 't', 'o', 'o' ,'l', 's')
# Output=
# q
# o


print("_" * 40)
print("Python tuple program to check whether an element exists in a tuple or not.")
Input = ( 'p' ,'y', 't', 'h', 'o', 'n')
# P in A
# Output=
# True


print("_" * 40)
print("Python tuple program to add a list in the tuple.")
# Input:
L=[12,67]
A=(6,8,4)
# Output:
# A=(6,8,4,12,67)


print("_"*40)
print("Python tuple program to find sum of elements in a tuple.")
# Input:
A=(4,6,2)
# Output:
# 12


print("_" * 40)
print("Python tuple program to add row-wise elements in Tuple Matrix")
# Input:
A = [[('sqa', 4)], [('tools', 8)]]
B = (3,6)
# Output:
# [[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]


print("_" * 40)
print("Python tuple program to create a tuple having squares of the elements from the list.")
Input6 = [(1,5,7), (3,6)]
# Output = (1, 81, 25, 49, 36)


print("_" * 40)
print("Python tuple program to multiply adjacent elements of a tuple.")
Input7 = (1,2,3,4)
# Output =  (2,6,12)


print("_" * 40)
print("Python tuple program to join tuples if the initial elements of the sub-tuple are the same.")
Input8 = [(3,6,7),(7,8,4),(7,3),(3,0,5)]
# Output:
# [(3,6,7,0,5),(7,8,4,3)]


print("_" * 40)
print("Python tuple program to convert a list into a tuple and multiply each element by 2.")
Input9 = [12,65,34,77]
# Output = (24, 130, 68, 154)


print("_" * 40)
print("Python tuple program to remove an item from a tuple.")
# Input:
A1=('p','y','t','h','o','n')
# Output: (p,y,t,o,n)


print("_" * 40)
print("Python tuple program to slice a tuple.")
# Input:
A2=(5,7,3,4,9,0,2)
# Output:
# (5,7,3)
# (3,4,9)


print("_" * 40)
print("Python tuple program to find an index of an element in a tuple.")
# Input:
A3=('s','q','a','t','o','o','l','s')
# Index of a?
# Output = 2


print("_" * 40)
print("Python tuple program to swap tuples.")
# Input=
A4=(7,4,9)
B2=(3,)
# Output=
# A=(3,)
# B=(7,4,9)


print("_" * 40)
print("Python tuple program to count the total number of unique tuples.")
Input10= [ (8, 9), (4, 7), (3, 6), (8, 9) ]
# Output= 3


print("_"*40)
print("Python tuple program to find common elements between two lists of tuples.")
# Input=
A6=[(1,5),(4,8),(3,9)]
B3=[(9,3),(5,6),(5,1),(0,4)]
# Output= {(3,9),(1,5)}


print("_"*40)
print("Python tuple program to order tuples by external list.")
# Input=
a=[('very',8),('i',6),('am',5),('happy',0)]
List=['i','am','very','happy']
# Output=
# [(‘i’,6),(‘am’,5),(‘very’,8),(‘happy’,0)]


print("_" * 40)
print("Python tuple program to sort a list of tuples by the minimum value of a tuple.")
Input11 = [(1,5,7),(3,4,2),(4,9,0)]
# Output= [(4,9,0),(1,5,7),(3,4,2)]