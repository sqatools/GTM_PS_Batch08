import keyword
# print(keyword.kwlist)
# print(dir(keyword.kwlist))

from colorama import *

print("Find the Differences Between Two Lists Using Sets")
# Input:
List1 = [10, 45, 34, 20, 11]
List2 = [11, 25, 45, 20]

setA = set(List1)
setB = set(List2)

setC = setA.difference(setB),setB.difference(setA)
print(f"The difference from List1 to List2 and List2 to List1 is {list(setC)}")

print("_"*40)
setD = setA.symmetric_difference(setB)
print(f"The difference from List1 to List2 and List2 to List1 is {list(setD)}")

print("_" * 40)
print("Find Maximum and Minimum Values of a Set")
set1 = {15, 25, 2, 10, 11, 55}

min_val = max_val = next(iter(set1))
print(max_val)

for val in set1:
    if max_val < val:
        max_val = val
    elif min_val > val:
        min_val = val


print(f"The maximum value from the set is {Fore.BLUE}{max_val}{Style.RESET_ALL} and the minimum value is {Fore.BLUE}{min_val}{Style.RESET_ALL}")


print("_" * 40)
print("Get All the Subsets of a Given Size in a Set")
set1 = {15, 25, 2, 10, 11, 55}
set2 = {2,10,11}

set3 = set1.issuperset(set2)
print("Set1 is superset of Set2: ",set3)

print("_" * 40)
print("Determine if Two Sets Are Disjoint or Not Without In-built Methods")
set1 = {15, 25, 2, 10, 11, 55}
set2 = {12,19,31,45}
set3 = set1.isdisjoint(set2)  #Return True if two sets have a null intersection.

print("Set1 and Set2 are disjoints: ", set3)

print("_" * 40)
print("Remove the Given Items of a Set at Once")
set1 = {15, 25, 2, 10, 11, 55}
set3 = set1.clear()  #clear method remove all the data from set and remain empty set
print(set3)

print("_" * 40)
print("Count Number of Vowels in a Given String Using Sets")
StringA = "I am Learning Python"
String_Vol = set("aeiouAEIOU")

count = 0
# for string in range(0,len(StringA)):
#     if StringA[string] in String_Vol:
#         count +=1

for string in StringA:
    if string in String_Vol and string.isalpha():
        count +=1
print(f"The count of vowels in StringA is {count}")


print("_" * 40)
print("Convert a Set to String")
setA = {"WelCome to this World"}
stringA = "".join(setA)

print(stringA)


print("_" * 40)
print("Find Common Elements of Three Given Lists Using Sets")


list1 = [2,5,7,8,78,4]
list2 = [4,7,9,23,45,8,78]
list3 = [8,4,6,78,9]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

setA_result = set1.intersection(set2)
setB_result = set2.intersection(set3)
setFinal_result = setA_result.intersection(setB_result)
print(setFinal_result)

print("_" * 40)
print("Perform Intersection of Two Lists Using Set Methods")
list1 = [2,5,7,8,78,4]
list2 = [4,7,9,23,45,8,78]

set1 = set(list1)
set2 = set(list2)

setB_result = set2.intersection(set1)
print(setB_result)

print("_"*40)
print("Square the Elements of Set Using for Loop")


print("_" * 40)
print("Check if a Set Is Superset Itself or Another Given Set")
set_17 = {1,4,7,8,'b','P','Q','R'}
set_18 = {'P','Q','R'}

print("Is set_17 Superset of set_18", set_17.issuperset(set_18))


print("_" * 40)
print("Check if a Given Value Is Present in the Set or Not")
set_17 = {1,4,7,8,'b','P','Q','R'}
set_18 = {'P','Q','R'}

print(f"The values of set_18 : {set_18} is present in set_17",set_17.intersection(set_18))

print("_"*40)
print("WAPP to find out the diff, common value between lists")
#
l1 = [4, 76, 9, 22, 55, 77, 8]
l2 = [4, 22, 5, 66, 7, 22, 76, 8]


set1 = set(l1)
set2 = set(l2)

set3 = set2.difference(set1)
set5 = set1.difference(set2)


print(f"Values in l2 but not in l1 {list(set3)}")
print(f"Values in l2 but not in l1 {list(set5)}")

set4 = set1.intersection(set2)

print("The common values between two list {list(set4)}")

print(f"Unique values in either list {set1.symmetric_difference(set2)}")

print("_" * 40)
print("WAPP to remove all duplicate vowels from given string")
str1 = "Hello We Are Learning Python"
vowels = "aeiouAEIOU"
output =("")

for char in str1:
    if char in vowels and char not in output:
        output +=char
    elif char not in vowels:
        output +=char
    else:
        continue
print(f"The final removed duplicate vowels from string is {output}")


print("_"*40)
print("WAPP to remove all vowels from given string")
str1 = "Hello We Are Learning Python"
vowels = "aeiouAEIOU"
output =("")

for char in str1:
    if char in vowels and char in output:
        output = output
    elif char not in vowels and char not in output:
        output +=char
    elif char not in vowels and char in output:
        output += char
    else:
        continue
print(f"The final removed vowels from string is {output}")



print("_" * 40)
print("WAPP to remove all the duplicate value from given dictionary values")

dict1 = {'a' : [3, 5, 7, 3, 7, 8],
         'b' : 'Programming',
         'c' : (4, 7, 9, 11, 5, 7, 11, 77, 88, 11),
         'd' : [True, False, True, False]}

print(f"The original dictionary is \n {dict1}")
for key,val in dict1.items():
    if type(val) is list:
        dict1[key] = list(set(val))
    elif type(val) is str:
        dict1[key] = "".join(set(val))
    elif type(val) is tuple:
        dict1[key] = tuple(set(val))
    else:
        dict1[key] = set(val)
print(f"After removing the duplicates the dictionary value is \n {dict1}")

print("_"*40)

import shlex
print("Check if a Given String Is Heterogram or Not")

actual_string = "Python Programming 'The quick brown fox' hello"

string1 = shlex.split(actual_string)
for word in string1:
    processed_word = "".join(char.lower() for char in word if char.isalpha())
    char_set = set(processed_word)

    if len(char_set) == len(processed_word):
        result = "Heterogram"
    else:
        result = "Not a Heterogram"
    print(f"The word {word} is: ",result)

# split() → Breaks everything at spaces, including inside quotes.
# shlex.split() → Preserves quoted phrases as single elements.
