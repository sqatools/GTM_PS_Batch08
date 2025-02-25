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

print("#"*50)
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

print("#"*50)

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

print("#"*50)
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


print("#"*50)
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


print("#"*50)
"""
11). Python tuple program to check whether an element exists in a tuple or not.
Input = ( ‘p’ ,’y’, ‘t’, ‘h’, ‘o’, ‘n’)
P in A
Output=
True

"""

tuple11 = ('p','y','t','h','o','n')
if 'p' in tuple11:
    print("True")
else:
    print("False")

print("#" * 50)

"""
12). Python tuple program to add a list in the tuple.
Input:
L=[12,67]
A=(6,8,4)
Output:
A=(6,8,4,12,67)
"""

L = [12,47]
A = (6,8,4)
result = list(A)
tupleList = result + L
print(tupleList) #[6, 8, 4, 12, 47]

print("#"*50)
"""

13). Python tuple program to find sum of elements in a tuple.
Input:
A=(4,6,2)
Output:
12
"""

Tuple13 = (4,6,2)
result2 = list(Tuple13)
print("Sum is: ", sum(result2)) #12

print("#"*50)
"""
14). Python tuple program to add row-wise elements in Tuple Matrix
Input:
A = [[(‘sqa’, 4)], [(‘tools’, 8)]]
B = (3,6)
Output:
[[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]
"""


print("#"*50)
"""
15). Python tuple program to create a tuple having squares of the elements from the list.
Input = [1, 9, 5,  7, 6]
Output = (1, 81, 25, 49, 36)


List15 = [1,9,5,7,6]
Tuple15 = list(List15)
print(List15)
list()
output = {}

for i in Tuple15:
    output = i**2
    list.append(output)
List15 = tuple(list())
print(List15)
"""


print("#"*50)

"""
18). Python tuple program to convert a list into a tuple and multiply each element by 2.
Input = [12,65,34,77]
Output = (24, 130, 68, 154)
"""
emptyList = []
list18 = [12,65,34,77]
for i in list18:
    result = 2*i
    emptyList.append(result)

tup = tuple(emptyList)
print("Original List:", list18)
print("Updated List:", tup)


"""
19). Python tuple program to remove an item from a tuple.
Input:
A=(p,y,t,h,o,n)
Output: (p,y,t,o,n)
"""

tuple19 = ('p','y','t','h','o','n')
result19 = list(tuple19)
result19.remove('o')
tup = tuple(result19)
print(tup) #('p', 'y', 't', 'h', 'n')

"""
20). Python tuple program to slice a tuple.
Input:
A=(5,7,3,4,9,0,2)
Output:
(5,7,3)
(3,4,9)
"""

tuple20 = ('5','7','3','4','9','0','2')
print(tuple20[:6]) # ('5', '7', '3', '4', '9', '0')
print(tuple20[:]) # ('5', '7', '3', '4', '9', '0', '2')
print(tuple20[2:]) #('3', '4', '9', '0', '2')


"""
21). Python tuple program to find an index of an element in a tuple.
Input:
A=(s,q,a,t,o,o,l,s)
Index of a?
Output = 2
"""

tuple21 = ('s','q','a','t','o','o','l','s')
print(tuple21.index('a')) #2

"""
22). Python tuple program to find the length of a tuple.
Input:
A=(v,i,r,a,t)
Output=
5
"""

tuple22 = ('v','i','r','a','t')
print(len(tuple22)) #5

"""
23). Python tuple program to convert a tuple into a dictionary.
Input:
A=((5,s),(6,l))
Output = { s: 5, l: 6 }
"""

tuple23 = ((5,'s'),(6,'l'))
dict23 = dict(tuple23)
print(dict23) #{5: 's', 6: 'l'}


"""
25). Python tuple program to convert a list of tuples in a dictionary.
Input = [ (s, 2), (q, 1), (a, 1), (s, 3), (q, 2), (a, 4) ]
Output ={ s: [ 2, 3 ], q: [ 1, 2 ], a: [ 1 ,4 ] }


tuple25 = [ ('s', 2), ('q', 1), ('a', 1), ('s', 3), ('q', 2), ('a', 4) ]
dict25 = dict(tuple25)
print(dict25)

"""