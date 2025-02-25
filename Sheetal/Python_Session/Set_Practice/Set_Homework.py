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
print("Check if a Given String Is Heterogram or Not")

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


print("_" * 40)
print("Determine if Two Sets Are Disjoint or Not Without In-built Methods")


print("_" * 40)
print("Remove the Given Items of a Set at Once")


print("_" * 40)
print("Count Number of Vowels in a Given String Using Sets")
StringA = "I am Learning Python"
String_Vol = set("aeiouAEIOU")

count = 0
# for string in range(0,len(StringA)):
#     if StringA[string] in String_Vol:
#         count +=1

for string in StringA:
    if string in String_Vol:
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
print(setB_result)

print("_"*40)
print("Square the Elements of Set Using for Loop")


print("_" * 40)
# print("Check if a Set Is Superset Itself or Another Given Set")



print("_" * 40)
print("Check if a Given Value Is Present in the Set or Not")