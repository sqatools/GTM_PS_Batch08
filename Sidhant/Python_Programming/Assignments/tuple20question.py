# 1). Python tuple program to create a tuple with 2 lists of data.
list1 = [4, 6, 8]
list2 = [7, 1, 4]
list3 = zip( list1, list2 )
print( tuple( list3 ) )

# 2). Python tuple program to find the maximum value from a tuple.
Input = (41, 15, 69, 55)
print( "maximum value:", max( Input ) )

# 3). Python tuple program to find the minimum value from a tuple.
Input = (41, 15, 69, 55)
print( "minimum value:", min( Input ) )

# 4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
Input = [4, 6, 3, 8]
tup = [(val, pow( val, 2 )) for val in Input]
print( tup )

# 5). Python tuple program to create a tuple with different datatypes.
tup = (2.6, 1, 'Python', True, [5, 6, 7], (5, 1, 4), {'a': 123, 'b': 456})
print( tup )

# 6). Python tuple program to create a tuple and find an element from it by its index no.
Input = (4, 8, 9, 1)
print( Input[2] )
# 7). Python tuple program to assign values of tuples to several variables and print them.
Input = (6, 7, 3)
(a, b, c) = Input
print( a, b, c )

# 8). Python tuple program to add an item to a tuple.
tup = (6, 24, 4, 77, 88, 2)
tup1 = list( tup )
tup1.append( 66 )
tup = tuple( tup1 )
print( tup )

# 9). Python tuple program to convert a tuple into a string.
tup = (6, 24, 4, 77, 88, 2)
tup1 = str( tup )
print( tup1, type( tup1 ) )

# 10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
tup = ('a', 'c', 'v', 'd', 'r', 'k')
print( tup[1] + ' ' + tup[3] )

# 11). Python tuple program to check whether an element exists in a tuple or not.
tup =('a','b','c','d','e')
if 'd' in tup:
    print(True)
else:
    print(False)

# 12). Python tuple program to add a list in the tuple.
tup =(4,87,6,7,8)
list1 =['s','b','g']
tup1 =list(tup)
tup3 =tup1 + list1
tup =tuple(tup3)
print(tup)

# 13). Python tuple program to find sum of elements in a tuple.
tup =(4,6,2)
print("sum is: ",sum(tup))

# 14). Python tuple program to create a tuple having squares of the elements from the list.
tup =(8,4,3,2,6,9)
tup=[(pow(i,2)) for i in tup]
print(tup)

# 15). Python tuple program to multiply adjacent elements of a tuple.
tup =(4,6,2,5)
list1 =[]
for (a,b) in zip(tup,tup[1:]):
    c=a*b
    list1.append(c)
    tup = tuple(list1)
print(tup)

# 16). Python tuple program to convert a list into a tuple and multiply each element by 2.
list1 = [4,3,7,9,33]
list2 =[]
tup =tuple(list1)
for i in tup:
   j = i*2
   list2.append(j)
   tup =tuple(list2)
print(tup)

# 17). Python tuple program to remove an item from a tuple.
tup =('a','b','c','d','e')
list1 = list(tup)
list1.remove('c')
tup =tuple(list1)
print(tup)

# 18 Python tuple program to slice a tuple.
tup = (4,9,8,7,5,1)
print(tup[0:3])
print(tup[3:])

# 19). Python tuple program to find an index of an element in a tuple.
tup = (9,6,3,2,5)
print(tup.index(3))

#20). Python tuple program to find the length of a tuple.
tup =(3,5,6,7,8,9,1,2,3,45,6,7)
print("length of tuple is:", len(tup))

