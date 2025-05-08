# 1) write a python program Program to create a tuple with 2 lists of data

list1 = [3, 4, 5]
list2 = [4, 6, 7]
tup = tuple(zip(list1,list2))
print(tup) # ((3, 4), (4, 6), (5, 7))

# 2) write a program Find the maximum value from a tuple
tup = (12, 3, 55, 67)
print("maximum value :", max(tup)) # 67

# 3) write a program find the minumum value from a tuple
tup = (12, 3, 55, 67)
print("minimum value :", min(tup)) # 3

# 4) write a program Create a list of tuples from a list having a number and its square in each tuple
list3 = [2, 4, 6, 7]
tup =[(val, pow(val,2)) for val in list3]
print(tup)
# [(2, 4), (4, 16), (6, 36), (7, 49)]

# 5) write a python program Create a tuple and find an element from the tuple by its index number
tup = (2, 4, 9 ,3)
print("number in the tuple with index 2: ", tup[2]) # 9

# 6) Python tuple program to convert a tuple into a string
tup = ('s', 'a', 'p', 't')
string1 = ''
for char in tup:
  string1 += char
print("string: ", string1) # sapt

#7) Python tuple program to get elements from the tuple using indexing
tup = ('s', 'a', 'p', 't', 'e', 'r', 't')
print(" 2nd element from the front in the string:", tup[1]) # a
print(" 3rd element from the last in the string:", tup[-3]) # e

#8) Python tuple program to add a list in the tuple
list5 = [123,45]
tup = (6, 8, 5)
result = tuple(list(tup) + list5)
print(result) # (6, 8, 5, 123, 45)

#9) Python tuple program to find the sum of elements in a tuple

tup = (4, 6, 8)
print("sum :", sum(tup)) # 18



# 10) Python tuple program to slice a tuple
tup = (4, 7, 8, 9, 6, 3, 2)
print("original tuple:", tup)
print(tup[:3])
print(tup[2:5])
# (4, 7, 8)
# (8, 9, 6)

# 11_ write a python program Find an index of an element in a tuple
tup = ( 'm', 'a', 'n','o', 'j', 'k', 'u', 'm', 'a', 'r')
print("Index of a:", tup.index('a'))
# Index of a: 1


# 12) write a program Python tuple program to find the length of a tuple

tup =( 'm', 'a', 'n','o', 'j', 'k', 'u', 'm', 'a', 'r')
print("original tuple:", tup)
print("length of the the tuple:", len(tup))
# length of the the tuple: 10



# 13) write a program Python tuple program to reverse a tuple

tup = (3, 5, 7, 9, 1, 2)
print("original tuple:", tup)
tup1 = tuple(reversed(tup))
print("reversed tuple:", tup1)
# reversed tuple: (2, 1, 9, 7, 5, 3)





# 14) write a python program Python tuple program to convert a tuple to string datatype

tup = (3, 5, 7, 9, 1, 2)
print("original tuple:", tup) # (3, 5, 7, 9, 1, 2)
tup2 = str(tup)
print("after converting to a string: ", tup2) # (3, 5, 7, 9, 1, 2)
print("type of new tuple:", type(tup2)) # <class 'str'>


# 15) Python tuple program to convert a string into a tuple

str2 = "manojjaini"
print("string:", str2)
tup = tuple(str2)
print("after converting to a string to a tuple: ", tup)
# ('m', 'a', 'n', 'o', 'j', 'j', 'a', 'i', 'n', 'i')





























































































