# 1. Write Python Program to het max number from the tuple without using inbuilt function.
tup1 = (55, 77, 203, 5, 1, 7)
#Output = 203
result1 = tuple(sorted(tup1))
print("Sorted Tuple is: ",result1)
print("Max of the Tuple is: ",result1[-1])
print("Minimum of the Tuple is: ",result1[0])
print("_"*70)


#################  Doubt : is (10, 10) combination ok to have ?
# 2. Write Python Program to get list of combination of 2 values whose sum is 20
tup2 = (3, 6, 9, 10, 11, 12, 8, 14, 6)
tupA = tup2
listA = []
# print(tupA)
for i in range (len(tup2)):
    for j in range (i, len(tupA)):
        if tup2[i] + tupA[j] == 20:
            tup = (tup2[i], tupA[j])
            listA.append(tup)
print("Combination of elements whose sum is 20 are:")
print(listA)
print("_"*70)


# 3. Write a Python Program to remove value which is not repeated more than 2 times and store in list.
tup3 = (1, 3, 1, 4, 1, 5, 3, 6, 3, 7, 3, 4, 6, 4)
listA = []
for val in tup3:
    if tup3.count(val) <= 2:
        if val not in listA:
            listA.append(val)
print(listA)
print("_"*70)


# Doubt
# 4. Python tuple program to create a tuple with 2 lists of data.
# Input lists:
list1 = [4, 6, 8]
list2 = [7, 1, 4]
# Output= ((4, 7), (6, 1), (8, 4))

tup2 = ()
for i in range (len(list1)):
    for j in range (i, len(list2)):
        if i == j:
            tup1 = list1[i], list2[j]
            #tup2 = tup2 + tup1
            print(tup1)

print("_"*70)


# 5. Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
# Input = [4,6,3,8]
# Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]

list1 = [4, 6, 3, 8]
for val in list1:
    tup1 = val, val**2
    # tup1 += tup1
    print(tup1)

print("_"*70)


################### Doubt : website 7th question
# 6. Python tuple program to assign values of tuples to several variables and print them.
# Input = (6,7,3)
# Variables = a,b,c

tup6 = (6, 7, 3)
(a, b, c) = tup6

print("a: ",a)
print("b: ",b)
print("c: ",c)
print("_"*50)


# 7. Python tuple program to add an item to a tuple.
# Input= ( 18, 65, 3, 45)
# Output=(18, 65, 3, 45, 15)
print("7. Tuple program to add an item to a tuple")
tup7 = (18, 65, 3, 45)
list7 = list(tup7)
list7.append(15)
print("List after appending a value: ",list7)
tup7 = tuple(list7)
print("List after converting to Tuple: ",tup7)
print("_"*50)


# 8. Python tuple program to convert a tuple into a string.
# Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’, ‘l’, ‘s’)
# Output = Sqatools

print("8. Python tuple program to convert a tuple into a string")
tup8 = ('S', 'q', 'a', 't', 'o', 'o', 'l', 's')
str1 = ""

for char in tup8:
    str1 = str1 + char
print("String after converting from tuple: ",str1)
print("_"*50)


# 9. Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
# Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’ ,’l’, ‘s’)
# Output=
# q
# o

print("9. program to get the 2nd element from the front and the 3rd element from the back of the tuple")
tup9 = ('S', 'q', 'a', 't', 'o', 'o', 'l', 's')

print("Second element from the front is: ", tup9[1])
print("Third element from the back is: ", tup9[-3])
print("_"*50)


# 10. Python tuple program to check whether an element exists in a tuple or not.
# Input = ( ‘p’ ,’y’, ‘t’, ‘h’, ‘o’, ‘n’)
# P in A
# Output= True
print("10. Program to check whether an element exists in a tuple or not")
tup10 = ('p', 'y', 't', 'h', 'o', 'n')
count = 0
for char in tup10:
    if char == 'p':
        print(True)
        count += 1
if count ==0:
    print("Element does not exist in given tuple")
print("_"*50)


# 11. Python tuple program to add a list in the tuple.
# Input:
# L=[12,67]
# A=(6,8,4)
# Output:
# A=(6,8,4,12,67)
print("11. Python tuple program to add a list in the tuple")
list11 = [12,67]
tup11 = (6,8,4)

listA = list(tup11)
listA = listA + list11
print("Tuple after adding list to tuple: ", tuple(listA))
print("_"*50)


# 12. Python tuple program to find sum of elements in a tuple.
# Input:
# A=(4,6,2)
# Output:
# 12
print("12. Python tuple program to find sum of elements in a tuple")
tup12 = (4, 6, 2)
sum = 0
for val in tup12:
    sum = sum + val
print("sum of the elements in tuple is: ",sum)
print("_"*50)


# 13. Python tuple program to add row-wise elements in Tuple Matrix
# Input:
# A = [[(‘sqa’, 4)], [(‘tools’, 8)]]
# B = (3,6)
# Output:
# [[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]

print("13. Python tuple program to add row-wise elements in Tuple Matrix")
listA = [[('sqa', 4)], [('tools', 8)]]
tupB = (3, 6)

for x in range(len(listA)):
    C = list(listA[x][0])
    C.append(tupB[x])
    listA[x][0] = tuple(C)

print(listA)

"""
A = [[('sqa', 4)], [('tools', 8)],[('shilpi', 3)]]
B = (3,6,12)
Output3=[]
l1=[]
for x in range(len(A)):
    C=list(A[x][0])
    C.append(B[x])
    A[x][0]=tuple(C)

print(A)
"""
print("_"*50)


# 14. Python tuple program to create a tuple having squares of the elements from the list.
Input = [(1,5,7), (3,6)]
Output = (1, 9, 25, 49, 36)
out1 = []
for x in range (0, len(Input)):
    for y in (Input[x]):
        out1.append(y**2)
print(tuple(out1))

# OR
Input2=(1,3,5,7,6)
out2 =[x**2 for x in Input2]
print(tuple(out2))
print("_"*50)


# 15. Python tuple program to multiply adjacent elements of a tuple.
Input = (1,2,3,4)
# Output =  (2,6,12)

listA = list(Input)
out = []
for x in range(0, len(listA)-1):
    out.append(listA[x] * listA[x+1])
print(tuple(out))
print("_"*50)


# 15. Python tuple program to join tuples if the initial elements of the sub-tuple are the same.
Input= [(3,6,7),(7,8,4),(7,3),(3,0,5)]
# Output: [(3,6,7,0,5),(7,8,4,3)]
out = []
for x in range(len(Input)):
    for y in range(x+1, len(Input)):
        if Input[x][0] == Input[y][0]:
            out.append(Input[x]+Input[y])
print("Output: ",out)
print("_"*50)


# 16. Python tuple program to convert a list into a tuple and multiply each element by 2.
Input = [12,65,34,77]
# Output = (24, 130, 68, 154)
print("16. Python tuple program to convert a list into a tuple and multiply each element by 2")
tup16 = tuple(Input)
print("After converting to tuple: ",tup16)
out = []

for val in Input:
    out.append(val*2)
print(tuple(out))
print("_"*50)


# 17. Python tuple program to remove an item from a tuple.
# Input:
print("17. Python tuple program to remove an item from a tuple")
A=('p', 'y', 't', 'h', 'o', 'n')
# Output: (p,y,t,o,n)
listA = list(A)

listA.remove('h')
print("Tuple after removing 'h' from the tuple is: ", tuple(listA))
print("_"*50)


# 18. Python tuple program to slice a tuple.
# Input:
# A=(5,7,3,4,9,0,2)
# Output:
# (5,7,3)
# (3,4,9)
print("18. Python tuple program to slice a tuple")
A=(5,7,3,4,9,0,2)
B = A[0:3]
C = A[2:5]
print("Tuples after slicing: ")
print(B, C)
print("_"*50)


# 19. Python tuple program to reverse a tuple.
Input = ( 4, 6, 8, 3, 1)
# Output= (1, 3, 8, 6, 4)

Input1 = tuple(reversed(Input))
print(Input1)
print("_"*50)


##################### Doubt #########################
# 19. Python tuple program to convert a list of tuples in a dictionary.
Input = [('s', 2), ('q', 1), ('a', 1), ('s', 3), ('q', 2), ('a', 4)]
# Output ={ s: [ 2, 3 ], q: [ 1, 2 ], a: [ 1 ,4 ] }

print("list of tuples is: ", Input)
D = {}

for k, v in Input:
    D.setdefault(k,[]).append(v)

print("Dictionary: ",D)
print("_"*50)


# 20. Python tuple program to pair all combinations of 2 tuples.
# Input :
# A=(2,6)
# B=(3,4)
# Output :
# [ (2, 3), (2, 4), (6, 3), (6, 4), (3, 2), (3, 6), (4, 2), (4, 6) ]
A=(2,6)
B=(3,4)

print("Pairs of all combinations of the 2 given tuples: ")
for x in range (len(A)):
    for y in range(len(B)):
        print((A[x],B[y]), end=",")
        # print(tup20)
        # tup20 = tup20 + (B[y],A[x])
        print((B[y],A[x]), end=",")

print()
print("_"*50)










