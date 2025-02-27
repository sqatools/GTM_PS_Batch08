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