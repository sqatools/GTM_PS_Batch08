
# write a python program to remove all duplicate vowels from given string.
str1 = "Hello we are learning Python"
print(set(str1)) # {'g', ' ', 'o', 'n', 'P', 'H', 't', 'e', 'h', 'a', 'r', 'y', 'w', 'l', 'i'}
vowels = 'aeiou'


output = ''
for char in str1:
    if (char in vowels ) and (char not in output):
        output += char
    elif char not in vowels:
        output += char
    else:
        continue

print("output :", output)
# Hello w ar lrning Py
print("*"*50)

#python program to create a set from 2 lists
list1=[20,30,30,35,46,74,20,45,45,35]
list2=[10,15,60,25,10]
set1= set(list1+list2)
print(set1)
print("*"*50)

#program to check if the value exist in the set
book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
if 'Harry Potter' in book_set:
    print("Book exists in the book set")
else:
    print("Book doesn't exist in the book set")
# Output Book exists in the book set

# check another item which is not present inside a set
print("A Man called Ove" in book_set)
print("*"*50)

#program to get a new set from two sets with common values
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
print("*"*50)

#Get Only unique items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))
print("*"*50)

#Update the first set with items that don’t exist in the second set
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)
print("*"*50)

#Remove items from the set at once
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)
print("*"*50)

#Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.symmetric_difference(set2))
print("*"*50)

#display the common elements from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))
print("*"*50)

#Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)
print("*"*50)

#Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)
print("*"*50)

#print("*"*50)
sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.update(["Blue", "Green", "Red"])
print(sampleSet)

set1 = {10, 20, 30, 40}
set2 = {50, 20, "10", 60}

set3 = set1.union(set2)
print(set3)

sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.discard("Blue")
print(sampleSet)
print("*"*50)

################################################################
#Q2 write a python program to find out the diff, common value between lists
#
l1 = [4, 76, 9, 22, 55, 77, 8]
l2 = [4, 22, 5, 66, 7, 22, 76, 8]

#Q3 write a python program to remove all the duplicate value from given dictionary values

"""input_dict = {'a' : [3, 5, 7, 3, 7, 8],
         'b' : 'Programming',
         'c' : (4, 7, 9, 11, 5, 7, 11, 77, 88, 11),
         'd' : [True, False, True, False]}


def remove_duplicates(input_dict):
    # Create a new dictionary to store unique values
    unique_dict = {}

    # Create a set to track seen values
    seen_values = set()

    for key, value in input_dict.items():
        if value not in seen_values:
            unique_dict[key] = value
            seen_values.add(value)

    return unique_dict

input_dict = {'a' : 6,
         'b' : 6,
         'c' : 7,
         'd' : 4,
         'e' : (4,6,8,9),
         'f' : 9}

result = remove_duplicates(input_dict)
print("Dictionary after removing duplicates:", result)"""

test_dict = {'gfg': 10, 'is': 15, 'c':(2,4,6,8,2), 'for': 10, 'geeks': 20}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Remove duplicate values in dictionary
# Using loop
temp = []
res = dict()

for key, val in test_dict.items():

    if val not in temp:
        temp.append(val)
        res[key] = val

# printing result
print("The dictionary after values removal : " + str(res))