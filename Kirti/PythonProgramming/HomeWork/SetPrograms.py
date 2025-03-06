# Q  .1 - Write a python program to remove all duplicate vowels from given string using set
str1 = "Hello we are learning python"
str1 = str1.lower()
list_vowels = []
list_consonants=[]
for i in range(len(str1)):
    if str1[i] in ['a','e','i','o','u']:
        list_vowels.append(str1[i])
    elif str1[i] == ' ':
        continue
    else:
        list_consonants.append(str1[i])

set1= set(list_vowels)
list_vowels=list(set1)

print("output = ", set(list_vowels + list_consonants))

#output =  ['a', 'o', 'e', 'i', 'h', 'l', 'l', 'w', 'r', 'l', 'r', 'n', 'n', 'g', 'p', 'y', 't', 'h', 'n']

str1 = "Hello we are learning python"
vowel = 'aeiou'


"""
#Q2 Write a python program to find out difference & common values between two lists
"""
list1 = [4,76,9,22,55,77,8]
list2 = [4,22,5,66,7,22,76,8]

set1=set(list1)
set2=set(list2)

set3 = set1.difference(set2)
print("set1.difference(set2) = ", list(set3))     #[9, 77, 55]

set4 = set2.difference(set1)
print("set2.difference(set1) = ", list(set4))     #[66, 5, 7]

comm_val = set1.intersection(set2)
print("comm values = ", list(comm_val))    #[8, 4, 22, 76]

"""
3). Python program to create a set with some elements.
"""
set1 = {11,2.3, 'e',False, None ,(1,2,3), True}
print("Program 3 : ", set1)

"""
4). Python program to add an element to a set.
"""
set2 = {11,2.3, 'e',False, None ,(1,2,3), True}
set2.add((9,2,4))
print("Program 4 : ", set2)


"""
5). Python program to remove an element from a set.
"""
set5 = {11,2.3, 'e',False, None ,(1,2,3), True}
set5.remove(None)
print("Program 5 : ", set5)


"""
6). Python program to find the length of a set.
"""
set6 = {11,2.3, 'e',False, None ,(1,2,3), True}
print("Program 6 : ", len(set6))


"""
7). Python program to check if an element is present in a set.
"""
set7 = {11,2.3, 'e',False, None ,(1,2,3), True,8,45,6,89,34}
ele_to_find  = 890
if ele_to_find in set7:
    print("Program 7 : Element Present in set")
else:
    print("Program 7 : Element not Present in set")


"""
8). Python program to find the union of two sets.
"""
set8 = {11,2.3, 'e',False, None ,(1,2,3), True,8,45,6,89,34}
set9 = {'a','g','e',8,(1,2,3,4,5),61,89.76,2.3}
set10 = set8.union(set9)
print("Program 8 : Union of sets : ", set10)


"""
9). Python program to find the intersection of two sets.
"""
set8 = {11,2.3, 'e',False, None ,(1,2,3), True,8,45,6,89,34}
set9 = {'a','g','e',8,(1,2,3),61,89,2.3}
set10 = set8.intersection(set9)
print("Program 9 : Intersection of sets :", set10)


"""
10). Python program to find the difference of two sets.
"""
set8 = {11,2.3, 'e',False, None ,(1,2,3), True,8,45,6,89,34}
set9 = {'a','g','e',8,(1,2,3),61,89,2.3}
set10 = set8.difference(set9)
print("Program 10 : Difference of sets :", set10)


"""
11). Python program to find the symmetric difference of two sets.
"""
set8 = {11,2.3, 'e',False, None ,(1,2,3), True,8,45,6,89,34}
set9 = {'a','g','e',8,(1,2,3),61,89,2.3}
set10 = set8.symmetric_difference(set9)
print("Program 11 : Symmetric Difference of sets :", set10)


"""
12). Python program to show if one set is a subset of another set.
"""
set8 = {11,2.3, 'e',False, None ,(1,2,3), True,8,45,6,89,34}
set9 = {'e',8,(1,2,3),89,2.3}
print("Program 12 : set8.issuperset(set9) : ", set8.issuperset(set9))
print("Program 12 : set9.issuperset(set8) : ", set9.issuperset(set8))
print("Program 12 : set8.issubset(set9) : ", set8.issubset(set9))
print("Program 12 : set9.issubset(set8) : ", set9.issubset(set8))


"""
13). Python program to check if two sets are disjoint.
"""
set8 = {11,2.3, 'e',False, None,8,45,89,34}
set9 = {'e',8,(1,2,3),89,2.3}
set10 = {1,3,4,5,6,7}
print("Program 13: set8.isdisjoint(set9) : ", set8.isdisjoint(set9))
print("Program 13: set8.isdisjoint(set10) : ", set8.isdisjoint(set10))

"""
14). Python program to convert a list to a set.
"""
list14 = ['e',8,(1,2,3),89,2.3]
set14=set(list14)
print("Program 14 : ",set14)


"""
15). Python program to convert a set to a list.
"""
set15 =  {2.3, 8, (1, 2, 3), 'e', 89}
list15 = list(set15)
print("Program 15 : ",list15)


"""
16). Python program to find the maximum element in a set.
"""
set16 =  {2.3, 8, 56, 6,34, 89}
print("Program 16 : max(set16) : ",max(set16))


"""
17). Python program to find the minimum element in a set.
"""
set16 =  {2.3, 8, 56, 6,34, 89}
print("Program 16 : min(set16) : ",min(set16))


"""
18). Python program to find the sum of elements in a set.
"""
set16 =  {2.3, 8, 56, 6,34, 89}
print("Program 16 : sum(set16) : ",sum(set16))


"""
19). Python program to find the average of elements in a set.
"""
set16 =  {2.3, 8, 56, 6,34, 89}
print("Program 16 : min(set16) : ",sum(set16)/len(set16))


"""
20). Python program to check if all elements in a set are even.
"""
set20 =  {2, 8, 56, 6,34, 88}
count=0
for ele in set20:
    if ele %2 == 0:
        count+=1
    else:
        continue
if count == len(set20):
    print("Program 20 : All elements of set are even ")
else:
    print("Program 20 : All elements of set are not even ")


"""
#Q.21 Write a python program to remove all the duplicate value from given dictionary values
"""
dict1 = {'a' : [3, 5, 7, 3, 7, 8],
         'b' : 'Programming',
         'c' : (4, 7, 9, 11, 5, 7, 11, 77, 88, 11),
         'd' : [True, False, True, False]}