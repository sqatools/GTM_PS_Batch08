print(dir(tuple))
# 'count', 'index'
print("#"*50)

"""
1). Python tuple program to create a tuple with 2 lists of data.
Input lists:
list1 = [4, 6, 8]
list2 = [7, 1, 4]
"""
list1 = [4, 6, 8]
list2 = [7, 1, 4]
tup1 =tuple(zip(list1,list2))
print(tup1) # ((4, 7), (6, 1), (8, 4))

print("#"*50)


"""
2). Python tuple program to find the maximum value from a tuple.
Input = (41, 15, 69, 55)
Output = 69
"""
tup2 = (41, 15, 69, 55)
print("Maximum Values: ", max(tup2)) #69

print("#"*50)

"""
3). Python tuple program to find the minimum value from a tuple.
Input = (36,5,79,25)
Output = 5
"""
tup2 = (41, 15, 69, 55)
print("Minimum Values: ", min(tup2)) #15


"""
4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
Input = [4,6,3,8]
Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]

tup4 = [4,6,3,8]
output = ()

for val in tup4:
    if val not in output:
        output [val] = val ** 2
    else:
        continue

print(output)
"""

print("#"*50)

"""

5). Python tuple program to create a tuple with different datatypes.
Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})
"""
tup5 = (1.1, 'Hello', 23, True, [1,2,3], (4,5,6), {'a': 11, 'b' : 22})
print(tup5, type(tup5)) #tup5 = (1.1, 'Hello', 23, True, [1,2,3], (4,5,6), {'a': 11, 'b' : 22})


"""
6). Python tuple program to create a tuple and find an element from it by its index no.
Input = (4, 8, 9, 1)
Index = 2
Output = 9
"""

tup6 = (4, 8, 9, 1)
print(tup6[2]) #9


print("#"*50)
"""
7). Python tuple program to assign values of tuples to several variables and print them.
Input = (6,7,3)
Variables = a,b,c
Output:
a, 6
b, 7
c, 3
"""

tup7 = (6,7,3)
a,b,c = tup7
print("a ", a)
print("b ", b)
print("c ", c)


print("#"*50)


"""
8). Python tuple program to add an item to a tuple.
Input= ( 18, 65, 3, 45)
Output=(18, 65, 3, 45, 15)
"""
tup8 = ( 18, 65, 3, 45)
#tup8.append(15)
# print(tup8) AttributeError: 'tuple' object has no attribute 'append',  we cannot use append direct in tuple.
#first we convert tuple into the list

tup8 = list(tup8)
print(tup8) #[18, 65, 3, 45]
tup8.append(15)
print(tup8) #[18, 65, 3, 45, 15]


"""
9). Python tuple program to convert a tuple into a string.
Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’, ‘l’, ‘s’)
Output = Sqatools
"""
tup9 = ('s','q', 'a' , 't' , 'o' , 'o', 'l', 's')
str9 = ''

for char in tup9:
    str9 = str9+char

print(str9) #sqatools

"""
10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’ ,’l’, ‘s’)
Output=
q
o
"""
tup10 = ('s','q', 'a' , 't' , 'o' , 'o', 'l', 's')
print(tup10[1],tup10[5]) # q o
print(tup10[1],tup10[-3]) # q o


