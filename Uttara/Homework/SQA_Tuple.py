#1.Python tuple program to find the maximum value from a tuple.
#Input = (41, 15, 69, 55)
#Output = 69

tup = (41, 15, 69, 55)
print("Maximum value: ",max(tup))

"""2.Python tuple program to find the minimum value from a tuple.
Input = (36,15,79,25)
Output = 5"""

tup = (36,15,79,25)
print("Minimum value: ",min(tup))

"""3.Python tuple program to create a tuple with different datatypes.
Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})"""

tup = (2.6,1,'Python',True,[5, 6, 7],(5, 1, 4),{'a':123,'b':456})
print("Tuple: ",tup)

"""4. Python tuple program to create a tuple and find an element from it by its index no.
Input = (4, 8, 9, 1)
Index = 2
Output = 9"""

tup = (4,8,9,1)
print("Number in the tuple with index 2: ",tup[2])
#op: Number in the tuple with index 2:  9

"""5. Python tuple program to add an item to a tuple.
Input= ( 18, 65, 3, 45)
Output=(18, 65, 3, 45, 15)"""

tup = (18,65,3,45)
print("Old tuple: ",tup)
tup = list(tup)
tup.append(15)
tup = tuple(tup)
print("New tuple: ",tup)

"""6.Python tuple program to convert a tuple into a string.
Input = (‘a’, ‘p’, ‘p’, ‘l’, ‘e’)
Output = apple"""

tup = ('a','p','p','l','e')
str1 = ''
for char in tup:
    str1 += char

print("String: ",str1)


