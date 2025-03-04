print("Python program to create a set with some elements.")
set1 = {23,45,67,33,23,45}

print(f"The set values are {set1}")

print("_"*40)
print("Python program to add an element to a set.")
set1 = {23,45,67,33,23,45}
set1.add(7)
print(f"The final set values are {set1}")

print("_"*40)
print("Python program to remove an element from a set.")
set1.remove(23)

print(f"After remove teh set value for set3 is {set1}")

print("_"*40)
print("Python program to find the length of a set.")

set1 = {23,45,67,33,23,45}
set2 = {3,4,6,46}
print(f"The length of set2 is", len(set2), "and set1 is ", len(set1))

print("_"*40)
print("Python program to check if an element is present in a set.")

set4 = {23,33}
if set4.issubset(set1):
    print(f"The value of set4: {set4} is present in set1: {set1} ")
else:
    print(f"The value of set4: {set4} is not present in set1: {set1} ")

print("_"*40)
print("Python program to find the union of two sets.")
set1 = {23,45,67,33,23,45}

set2 = {25,46,68,31,20,45}
set5 = set1.union(set2)

print(f"The union of set1 and set2 is {set5}")

print("_"*40)
print("Python program to convert a set to a list.")
set2 = {25,46,68,31,20,45}
set6 = list(set2)

print(f"The new list is {set6}")

print("_"*40)
print("Python program to find the maximum element in a set.")
set2 = {25,46,68,31,20,45}
maximum = 0
for val in set2:
    if val > maximum:
        maximum = val
    else:
        maximum=maximum
print(f"The maximum value from the set {set2} is {maximum}")

print("_"*40)
print("Python program to find the longest word in a set.")
set8 = {'Hello', 'Python', 'is', 'the', 'best', 'language.'}
long_word = 'Hello'

for val in set8:
    if len(val) > len(long_word):
        long_word = val
    else:
        long_word = long_word
print(f"The maximum value from the set {set8} is {long_word}")


print("_"*40)
print("Python program to create two sets of books and find the intersection of sets.")
set10 = {'Hindi','Maths','English'}
set11 = {'Hindi1','Maths1','English'}

set12 = set10.intersection(set11)

print(f"The intersection of two sets are: {set12}")

print("_"*40)
print("Python program to create a set of odd numbers from 1 to 20.")
set9 = set()

for val in range(0,21):
    if val%2 ==0:
        continue
    else:
        set9.add(val)
print(f"The updated set with all odd numbers are {set9} ")

print("_"*40)
print("Python program to convert a set to a dictionary with each element as key and value to an empty set.")

set13 = {'Hello', 'Python', 'is', 'the', 'best', 'language.'}
dict1 = {}
for val in set13:
    dict1[val] = set()

print(f"The final dictionary using set is {dict1}")

print("_"*40)
print("Python program to find the intersection between multiple sets.")
set1 = {23,45,67,33,23,45}
set2 = {67,34,23,45}
set1.intersection(set2)

print(f"The intersection between the sets are: {set1}")

print("_"*40)
print("Python program to check if two sets are equal.")
set1 = {23,45,67,33,23,45}
set2 = {23,45,67,33,23,45}

if set1 == set2:
    print("Both the sets are equal")
else:
    print("Sets are unequal")

print("_"*40)
print("Python program to remove multiple elements from a set.")
set1 = {23,45,67,33,23,45}

set1.difference_update({23,45})

print(f"The remove 23,45 from set1 : {set1}")

print("_"*40)
print("Python program to find the union of multiple sets using the | operator.")
set1 = {23,45,67,33,23,45}

set2 = {25,46,68,31,20,45}
set5 = set1|(set2)

print(f"The union of set1 and set2 is {set5}")
