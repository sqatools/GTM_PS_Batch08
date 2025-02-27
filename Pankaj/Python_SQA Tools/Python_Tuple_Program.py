# 1). Python tuple program to create a tuple with 2 lists of data.
# Input lists:
# list1 = [4, 6, 8]
# list2 = [7, 1, 4]
# Output= ((4, 7), (6, 1), (8, 4))
list1 = [4, 6, 8]
list2 = [7, 1, 4]
value = tuple(zip(list1, list2))
print(value)

# 2). Python tuple program to find the maximum value from a tuple.
# Input = (41, 15, 69, 55)
# Output = 69
Input = (41, 15, 69, 55)
print(max(Input))

# 3). Python tuple program to find the minimum value from a tuple.
# Input = (36,5,79,25)
# Output = 5
Input1 = (36, 5, 79, 25)
print(min(Input1))

# 4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
# Input = [4,6,3,8]
# Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]
Input2 = [4, 6, 3, 8]
tuple1 = [(value, value**2) for value in Input2]
print(tuple1)

# 5). Python tuple program to create a tuple with different datatypes.
# Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})

tup1 = ( 2.6, 1, 'Python', True, [5, 6, 7], (5, 1, 4), {'a': 123, 'b': 456})
print(tup1)

# 6). Python tuple program to create a tuple and find an element from it by its index no.
# Input = (4, 8, 9, 1)
# Index = 2
# Output = 9

tup2 = (4, 8, 9, 1)
print(tup2[2])

# 7). Python tuple program to assign values of tuples to several variables and print them.
# Input = (6,7,3)
# Variables = a,b,c
# Output:
# a, 6
# b, 7
# c, 3

tup3 = (6, 7, 3)
a, b, c = tup3
print('a,', a)
print('b,', b)
print('c,', c)

# 8). Python tuple program to add an item to a tuple.
# Input= ( 18, 65, 3, 45)
# Output=(18, 65, 3, 45, 15)
tup4 = (18, 65, 3, 45)
list1 = list(tup4)
list1.append(15)
tup5 = tuple(list1)
print(tup5)

# 9). Python tuple program to convert a tuple into a string.
# Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’, ‘l’, ‘s’)
# Output = sqatools
tup6 = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
str1 = ""
for char in tup6:
    str1 += char
print(str1)

#10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
# Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’ ,’l’, ‘s’)
#Output=
#q
#o
tup7 = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
print(tup7[1])
print(tup7[4])

# 11). Python tuple program to check whether an element exists in a tuple or not.
# Input = ( ‘p’ ,’y’, ‘t’, ‘h’, ‘o’, ‘n’)
# P in Input
# Output=
# True

tup7 = ('p', 'y', 't', 'h', 'o', 'n')
if 'p' in tup7:
    print(True)
else:
    print(False)

# 12). Python tuple program to add a list in the tuple.
# Input:
# L=[12,67]
# A=(6,8,4)
# Output:
# A=(6,8,4,12,67)

list1 = [12, 67]
tup8 = (6, 8, 4)
list2 = list(tup8)
value = list2+list1
final_value = tuple(value)
print(final_value)

# 13). Python tuple program to find sum of elements in a tuple.
# Input:
# A=(4,6,2)
# Output:
# 12

tup9 = (4, 6, 2)
empty = 0
for value in tup9:
    empty += value
print(empty)

print("_"*78)
# 14). Python tuple program to create a tuple having squares of the elements from the list.
#Input = [1, 9, 5,  7, 6]
#Output = (1, 81, 25, 49, 36)

list4 = [1, 9, 5,  7, 6]
emp1 = list()
for value in list4:
    b = value**2
    emp1.append(b)
tup10 = tuple(emp1)
print(tup10)

# 15). Python tuple program to convert a list into a tuple and multiply each element by 2.
# Input = [12,65,34,77]
# Output = (24, 130, 68, 154)
list5 = [12, 65, 34, 77]
emp22 = []
for i in list5:
    b = i * 2
    emp22.append(b)
tup13 = tuple(emp22)
print(tup13)

# 16). Python tuple program to remove an item from a tuple.
# Input:
# A=(p,y,t,h,o,n)
# Output: (p,y,t,o,n)
tup14 = ('p', 'y', 't', 'h', 'o', 'n')
list_14 = list(tup14)
list_14.remove('h')
print(tuple(list_14))


# 17). Python tuple program to slice a tuple.
# Input:
# A=(5,7,3,4,9,0,2)
# Output:
# (5,7,3)
# (3,4,9)

A = (5, 7, 3, 4, 9, 0, 2)
print(A[0:3])
print(A[2:5])

# 18). Python tuple program to find an index of an element in a tuple.
# Input:
# A=(s,q,a,t,o,o,l,s)
# Index of a?
# Output = 2

tup15 = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
print(tup15.index('a'))

# 19). Python tuple program to find the length of a tuple.
# Input:
# A=(v,i,r,a,t)
# Output=
# 5
A = ('v', 'i', 'r', 'a', 't')
print(len(A))

# 20). Python tuple program to convert a tuple into a dictionary.
# Input:
# A=((5,s),(6,l))
# Output = { s: 5, l: 6 }

A = ((5, 's'), (6, 'l'))
print(dict(A))


