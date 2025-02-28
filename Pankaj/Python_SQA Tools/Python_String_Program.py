print("_" * 70)
# 1). Python string program to get a string made of 4 copies of the last two characters of a specified string
# (length must be at least 2).
str1 = "Pankaj"
print(str1[-2] * 4)

print("_" * 70)
# 2). Python string program that takes a list of strings and returns the length of the longest string.
str1 = ("Hello", "i", "am", "learning", "python")
longest_str = 0
for word in str1:
    x = len(word)
    if x > longest_str:
        longest_str = x
print(longest_str)

print("_" * 70)
# 3). Python string program to reverse a string if it’s length is a multiple of 4.
str2 = "Pankaj"
if len(str2) % 2 == 0:
    print(str2[::-1])

print("_" * 70)
#4). Python string program to count occurrences of a substring in a string.
str3 = "dalda"
occ = "da"
print(str3.count(occ))

print("_" * 70)
#5. Python string program to test whether a passed letter is a vowel or consonant.
str4 = "pankaj"
for char in str4:
    if char == "a" or char == "e" or char == "i" or char == "u" or char == "o" or char == "u":
        print(f"{char} is vowels")
    else:
        print(f"{char} is consonant")

print("_" * 70)
#6). Find the longest and smallest word in the input string.
str5 = "hello everyone we are learning python"
word1 = str5.split(" ")
print("Longest Word: ", max(word1, key=len))
print("Smallest Word: ", min(word1, key=len))

print("_" * 70)
#7). Write a Python program to replace the second occurrence of any char with the special character $.
#Input = “Programming”
#Output = “Prog$am$in$”
str6 = "Programming"
str6_0 = ""
for char in str6:
    if char in str6_0:
        str6_0 = str6_0 + "$"
    else:
        str6_0 = str6_0 + char
print(str6_0)

print("_" * 70)
#8).Write a python program to get to swap the last character of a given string.
#Input = “SqaTool”
#Output = “IqaTooS”
str7 = "sqatools"
print(str7[-1]+str7[1:-1]+str7[0])

print("_" * 70)
#9). Write a python program to exchange the first and last character of each word from the given string.
#Input = “Its Online Learning”
#Output = “stI enlino gearninL”

str8 = "Its Online Learning"
list1 = str8.split(" ")
for word in list1:
    new_word = word[-1]+word[1:-1]+word[0]
    index = list1.index(word)
    list1[index] = new_word
" ".join(list1)
print(list1)

print("_" * 70)
#10.  Write a python to repeat vowels 3 times and consonants 2 times.
#Input = “Sqa Tools Learning”
#Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”
str9 = "Sqa Tools Learning"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for char in str9:
    if char in vowels:
        result += char*3
    else:
        result += char*2
print(result)

print("_" * 70)
#11. Write a python program to re-arrange the string.
#Input = “Cricket Plays Virat”
#Output = “Virat Plays Cricket”
str10 = "Cricket Plays Virat"
word = str10.split(" ")
word.reverse()
" ".join(word)
print(word)


print("_" * 70)
#12. Write a python program to get all the digits from the given string.
"""
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
"""
# Output = [1112, 5324, 1773, 5324, 555]
str11 = """
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
"""
word = str11.split(" ")
list1 = []
for value in word:
    if value.isdigit():
        list1.append(value)

print(list1)


print("_" * 70)
#13.) Write a python program to replace the words “Java” with “Python” in the given string.
# Input = “JAVA is the Best Programming Language in the Market”
# Output = “Python is the Best Programming Language in the Market”

str13 = "JAVA is the Best Programming Language in the Market"
list1 = str13.split(" ")
for word in list1:
    if word == "JAVA":
        index = list1.index(word)
        list1[index] = "Pyhton"

print(" ".join(list1))

print("_" * 70)
#14.


print("_" * 70)
#8).Write a python program to get to swap the last character of a given string.
#Input = “SqaTool”
#Output = “IqaTooS”
str7 = "sqatools"
print(str7[-1]+str7[1:-1]+str7[0])

print("_" * 70)
#9). Write a python program to exchange the first and last character of each word from the given string.
#Input = “Its Online Learning”
#Output = “stI enlino gearninL”

str8 = "Its Online Learning"
list1 = str8.split(" ")
for word in list1:
    new_word = word[-1]+word[1:-1]+word[0]
    index = list1.index(word)
    list1[index] = new_word
" ".join(list1)
print(list1)

print("_" * 70)
#10.  Write a python to repeat vowels 3 times and consonants 2 times.
#Input = “Sqa Tools Learning”
#Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”
str9 = "Sqa Tools Learning"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for char in str9:
    if char in vowels:
        result += char*3
    else:
        result += char*2
print(result)

print("_" * 70)
#11. Write a python program to re-arrange the string.
#Input = “Cricket Plays Virat”
#Output = “Virat Plays Cricket”
str10 = "Cricket Plays Virat"
word = str10.split(" ")
word.reverse()
" ".join(word)
print(word)


print("_" * 70)
#12. Write a python program to get all the digits from the given string.
"""
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
"""
# Output = [1112, 5324, 1773, 5324, 555]
str11 = """
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
"""
word = str11.split(" ")
list1 = []
for value in word:
    if value.isdigit():
        list1.append(value)

print(list1)


print("_" * 70)
#13.) Write a python program to replace the words “Java” with “Python” in the given string.
# Input = “JAVA is the Best Programming Language in the Market”
# Output = “Python is the Best Programming Language in the Market”

str13 = "JAVA is the Best Programming Language in the Market"
list1 = str13.split(" ")
for word in list1:
    if word == "JAVA":
        index = list1.index(word)
        list1[index] = "Pyhton"

print(" ".join(list1))

print("_" * 70)
#14.
