#write tuple program to get max from tuple without using max function.

my_tup=(6,7,4,9,44,23,64,21,1)
my_lst=list(my_tup)
my_lst.sort()
print(my_lst)
print(my_lst[8::])
print("*"*50)


#write a python program to get list of combination of two values whose sum is 20
import itertools

list1 = (3, 6, 9, 10, 11, 12, 8, 14, 6)
var = 20

list3 = []

for i in range(len(list1)):
    for combi in itertools.combinations(list1,i):
        if sum(combi) == var:
            list3.append(combi)

print(list3)
print("*"*50)

#Program to create a tuple with 2 lists of data
list1 = [4, 6, 8]
list2 = [7, 1, 4]
tup =tuple(zip(list1,list2))
print(tup)
print("*"*50)

#Find the maximum value from a tuple
tup = (41, 15, 69, 55)
print("Maximum value: ",max(tup))
print("*"*50)

#another way for above
tup = (41, 15, 69, 101, 55)
max_val = 0
for val in tup:
    if val > max_val:
        max_val = val
    else:
        continue

print("maximum value :", max_val)
print("*"*50)

#Create a list of tuples from a list having a number and its square in each tuple
list1 = [4,6,3,8]

tup = [(val, pow(val, 2)) for val in list1]
print(tup)
print("*"*50)

#Program to create a tuple with different datatypes
tup = (2.6,1,'Python',True,[5, 6, 7],(5, 1, 4),{'a':123,'b':456})
print("Tuple: ",tup)
print("*"*50)

#Create a tuple and find an element from the tuple by its index number
tup = (4,8,9,1)
print("Number in the tuple with index 2: ",tup[2])
print("*"*50)

#Program to assign values of tuples to several variables
tup =  (6,7,3)
(a,b,c) = tup
print("a: ",a)
print("b: ",b)
print("c: ",c)
print("*"*50)

#Python tuple program to add an item to a tuple
tup = (18,65,3,45)
print("Old tuple: ",tup)
tup = list(tup)
tup.append(15)
tup = tuple(tup)
print("New tuple: ",tup)
print("*"*50)

#Python tuple program to convert a tuple into a string
tup = ('s','q','a','t','o','o','l','s')
str1 = ''
for char in tup:
    str1 += char

print("String: ",str1)
print("*"*50)

#Python tuple program to get elements from the tuple using indexing
tup = ('s','q','a','t','o','o','l','s')
print("2nd element from the front in the String: ",tup[1])
print("3rd element from the last in the String: ",tup[-3])
print("*"*50)

#Check whether an element exists in a tuple or not
tup = ('p','y','t','h','o','n')
if 'p' in tup:
    print("True")
else:
    print("False")
print("*"*50)

#Python tuple program to add a list in the tuple
list1 = [12,67]
tup = (6,8,4)
result = tuple(list(tup) + list1)
print(result)
