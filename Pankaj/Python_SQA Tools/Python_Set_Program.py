print("_" * 70)
# 1). Python program to create a set with some elements.
set1 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), True, False}
print(set1, type(set1))

print("_" * 70)
# 2). Python program to add an element to a set.
set2 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), True, False}
set2.add(300)
set2.add(99.9)
print(set2)

print("_" * 70)
# 3). Python program to remove an element from a set.
set3 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), True, False}
set3.remove(2.2)
print(set3)

print("_" * 70)
# 4). Python program to find the length of a set.
set4 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), True, False}
print(len(set4))

print("_" * 70)
# 5). Python program to check if an element is present in a set.
set5 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), True, False}
if "Pankaj" in set5:
    print("Is present")
else:
    print("Not Present")

print("_" * 70)
# 6). Python program to find the union of two sets.
set6 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), False}
set6_1 = {"Prasad", "Pankaj", 2, 4, 5, True}
value = set6_1.union(set6)
print(value)

print("_" * 70)
# 7). Python program to find the intersection of two sets.
set7 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), False}
set7_1 = {"Prasad", "Pankaj", 2, 4, 5, True}
value2 = set7_1.intersection(set7)
print(value2)

print("_" * 70)
# 8). Python program to find the difference of two sets.
set8 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), False}
set8_1 = {"Prasad", "Pankaj", 2, 4, 5, True}
value3 = set8.difference(set8_1)
print(value3)
value4 = set8 - set8_1  # another way
print(value4)

print("_" * 70)
# 9). Python program to find the symmetric difference of two sets.

set9 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), False}
set9_1 = {"Prasad", "Pankaj", 2, 4, 5, True}
value5 = set9.symmetric_difference(set9_1)
print(value5)

print("_" * 70)
# 10). Python program to show if one set is a subset of another set.
set10 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), True}
set10_1 = {"Pankaj", 2, 2.2, True}
value6 = set10_1.issubset(set10)
print(value6)

print("_" * 70)
# 11). Python program to check if two sets are disjoint.
set11 = {2, 2.2, 'P', "Pankaj", (2, 3, 4), True}
set11_1 = {"Pankaj", 2, 2.2, True}
set11_1_1 = {100, 200, 400}
print(set11_1.isdisjoint(set11))
print(set11_1_1.isdisjoint(set11))

print("_" * 70)
# 12). Python program to convert a list to a set.
list1 = [2, 3, 4, 5.5, "Pankaj"]
set12 = set(list1)
print(set12)

print("_" * 70)
# 13). Python program to convert a set to a list.
set13 = {2, 3, 55, "Pankaj", True}
list2 = list(set13)
print(list2)

print("_" * 70)
# 14). Python program to find the maximum element in a set.
set14 = {2, 3, 55, 111, 1000}
value6 = max(set14)
print(value6)
# or
max_value = 0
for value in set14:
    if value > max_value:
        max_value = value
    print(max_value)

print("_" * 70)
# 15). Python program to find the minimum element in a set.
set13 = {2, 3, 55, 111, 1000}
value7 = min(set13)
print(value7)

print("_" * 70)
# 16). Python program to find the sum of elements in a set.
set16 = {2, 3, 55, 111, 1000}
sum1 = 0
for element in set16:
    sum1 += element
print(sum1)

print("_" * 70)
# 17). Python program to find the average of elements in a set.

set17 = {2, 3, 55, 111, 1000}
sum1 = 0
for element in set16:
    sum1 += element
avg_value = sum1 / len(set17)
print(avg_value)

print("_" * 70)
# 18). Python program to check if all elements in a set are even.

set18 = {2, 3, 55, 111, 1000}
count = 0
for value in set18:
    if value % 2 == 0:
        count += 1
if count == len(set17):
    print("All are even")
else:
    print("All are not even")

print("_" * 70)
#19). Python program to check if all elements in a set are odd.
set19 = {2, 3, 55, 111, 1000}
count = 0
for value in set18:
    if value % 2 == 0:
        count += 1
if count == len(set17):
    print("All are odd")
else:
    print("All are not odd")


print("_" * 70)
#20). Python program to remove all elements from a set.
set19 = {2, 3, 55, 111, 1000}
final_value = set19.clear()
print(final_value)