"""#1). Python program to create a set with some elements.

list1 = {1,4,5,7}
print("set:", list1) #set: {1, 4, 5, 7}

str = {"Hello","Hi","Morning"}
print("set:", str) #set: {'Hello', 'Hi', 'Morning'}
"""

print("#"*50)
"""
#2). Python program to add an element to a set.

list1 = {1,4,5,7}
list1.add(50)
print(list1) #{1, 4, 5, 7, 50}

"""
"""
#3). Python program to remove an element from a set.
list1 = {1,4,5,7}
print("Orginal Set is:", list1)  #Orginal Set is: {1, 4, 5, 7}
list1.remove(4)
print(list1) #{1, 5, 7}
"""
"""
#4). Python program to find the length of a set.
list1 = {1, 4, 5, 7, 50}
Length = len(list1)
print(Length) #5
"""
"""
#5). Python program to check if an element is present in a set.
list1 = {1, 4, 5, 7, 50}
if 2 in list1:
    print("True") # if 7 true
else:
    print("False") #if 2 false



# 6). Python program to find the union of two sets.

set1 = {1,2,4,5}
set2 = {7,8,9,1}
print(set1.union(set2)) #{1, 2, 4, 5, 7, 8, 9}



print("#"*50)

#7). Python program to find the intersection of two sets.

set1 = {1,2,4,5}
set2 = {7,8,9,1}
print(set1.intersection(set2)) # {1}



#8). Python program to find the difference of two sets.

set1 = {1,2,4,5}
set2 = {7,8,9,1}
print(set1.difference(set2)) #{2, 4, 5}
print(set2.difference(set1)) #{8, 9, 7}



#9). Python program to find the symmetric difference of two sets.

set1 = {1,2,4,5}
set2 = {7,8,9,1}
print(set1.symmetric_difference(set2)) #{2, 4, 5, 7, 8, 9}



#10). Python program to show if one set is a subset of another set.


set1 = {1,2,4,5}
set2 = {2,4}
print("Set2 is Subset of set2 :", set2.issubset(set1))  #T
print("Set2 is Supper of set1 :", set2.issuperset(set1)) #F
print("Set1 is Subset of set2 :", set1.issubset(set2)) #F
print("Set2 is supper of set1:", set1.issuperset(set2)) #T





#11). Python program to check if two sets are disjoint.

set1 = {1,2,4,5}
set2 = {7,8,9}
print(set1.isdisjoint(set2)) #true
print(set2.isdisjoint(set1)) #true


#12). Python program to convert a list to a set.
List = [1,2,3,4,5]
list_set = set(List)
print(list_set) #{1, 2, 3, 4, 5}



#13). Python program to convert a set to a list.

Set = {1,2,3,4,5}
set_list = list(Set)
print(set_list) #[1, 2, 3, 4, 5]



#14). Python program to find the maximum element in a set.
Set = {1,2,3,4,5}
print(max(Set)) # 5

max = 0
for ele in Set:
    if ele > max:
        max = ele
print(max)   #5



#5). Python program to find the minimum element in a set.

Set = {1,2,3,4,5}
print(min(Set)) # 1

min = 1
for ele in Set:
    if ele < min:
        min = ele
print(min)   #1


#16). Python program to find the sum of elements in a set.
Set = {1,2,3,4,5}
print(sum(Set)) # 15

total = 0
for ele in Set:
    total = total + ele
print(total) ## 15



#17). Python program to find the average of elements in a set.
Set = {1,2,3,4,5}

total = 0
for ele in Set:
    total = total + ele
print(total/len(Set)) ## 3.0



#18). Python program to check if all elements in a set are even.
Set = {2,4,8}
count = 0
for ele in Set:
    if ele%2==0:
        count=count +1
if count == len(Set):
    print("All ele are even") #All ele are even

else:
    print("Ele are not even ")



#19). Python program to check if all elements in a set are odd.
Set = {1,3,5}
count = 0
for ele in Set:
    if ele%2 !=0:
        count=count +1
if count == len(Set):
    print("All ele are Odd")
else:
    print("Ele are not Odd ") #All ele are even

"""

#20). Python program to remove all elements from a set.


set4 = {1,2,4,5}
set4.clear()
print(set4) #set()