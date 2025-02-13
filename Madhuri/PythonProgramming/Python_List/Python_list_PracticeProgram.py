# 1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string

str1 = "Python"
if len(str1)<2:
    print(True)
else:
    print(str1[0:2]+str1[-2:])
#Pyon

print("-"*50)


#2). Python string program that takes a list of strings and returns the length of the longest string.

str2 = ['i','am','learning','python']
temp=0

for word in str2:
    Length = len(word)
    if Length > temp:
        temp = Length
    print(temp)
print("The longest strings is:", temp)

print("-"*50)

#3). Python string program to get a string made of 4 copies of the last two characters of a specified string
#(length must be at least 2).

str3= "Morning"

print(str3[-2:]*4)
#ngngngng

print("-"*50)
#4). Python string program to reverse a string if it’s length is a multiple of 4.

str4= "Hello"
if len(str4) % 4 == 0:
    print(str4[::-1])
else:
    print("Nothing") #Nothing

print("-"*50)

str5= "Kolhapur"
if len(str5) % 4 == 0:
    print(str5[::-1])
else:
    print("Nothing") #rupahloK

print("-"*50)

# 5). Python string program to count occurrences of a substring in a string.

str6 = "PandharpurPandharpur Pandharpur"
sub="dhar"
print(str6.count('dhar')) #3

print("-"*50)

""" 
#6). Python string program to test whether a passed letter is a vowel or consonant.

letter = "Pandharpur"

for char in letter:
    if char == 'a' or char == 'e' or char =='i' or char=='o' or char=='u':
        print("Char is vowel")
    else:
        print("Char is Consonant")

Output: 
Char is Consonant
Char is vowel
Char is Consonant
Char is Consonant
Char is Consonant
Char is vowel
Char is Consonant
Char is Consonant
Char is vowel
Char is Consonant
"""
"""
#7). Find the longest and smallest word in the input string.
str7 = "we are learning python"
list1 = str7.split(" ")
print(list1)

for i in str7 
print("Longest word: ", max(list1,))
print("Smallest word: ",min(list1,))

"""
print("-"*50)
#8). Print most simultaneously repeated characters in the input string.


#9). Write a Python program to calculate the length of a string with loop logic.
string = "im am learing python"
count = 0

for char in string:
    count = count + 1
print("Length of the string using len(): ", len(string))
#Length of the string using len():  20

#10). Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$

str8 = "Programming"
result = " "

for char in str8:
    if char in result:
        result = result + '%'
    else:
        result = result + char
print(result) # Prog%am%in%

print("-"*50)

