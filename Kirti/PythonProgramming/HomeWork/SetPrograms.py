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


# Write a python program to find out difference & common values between two lists
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


#Q.3 Write a python program to remove all the duplicate value from given dictionary values


dict1 = {'a' : [3, 5, 7, 3, 7, 8],
         'b' : 'Programming',
         'c' : (4, 7, 9, 11, 5, 7, 11, 77, 88, 11),
         'd' : [True, False, True, False]}