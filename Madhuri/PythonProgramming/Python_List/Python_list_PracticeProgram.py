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



#11). Write a python program to get to swap the last character of a given string.
#Input = “SqaTool”
#Output = “IqaTooS”

str9 = "SqaTool"
print(str9[-1]+str9[1:-1]+str9[0])

print("-"*50)
#12). Write a python program to exchange the first and last character of each word from the given string.
#Input = “Its Online Learning”
#Output = “stI enlino gearninL”

str10 = "Its Online Learning"
list=str10.split(" ")

for word in list:
    print(word)
    new_word=  word[-1]+word[1:-1]+word[0]
    index = list.index(word)
    list[index] = new_word
print(list) #['stI', 'enlinO', 'gearninL']


#13). Write a python to count vowels from each word in the given string show as dictionary output.
#Input = “We are Learning Python Codding”
#output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}

str11 = "We are Learning Python Codding"

list1 = str11.split(" ")

vowels = "aeiou"
dictionary = dict()

for word in list1:
    count=0
    print(word)
    for char in word:
        if char in vowels:
            count= count+1

    dictionary[word] = count
print(dictionary)


print("-"*50)
#15). Write a python program to re-arrange the string.
#Input = “Cricket Plays Virat”
#Output = “Virat Plays Cricket”

str12 = "Cricket Plays Virat"
list2 = str12.split(" ")
list2.reverse()
print(list2)
" ".join(list2)

"""

16). Write a python program to get all the digits from the given string.
Input = “””
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
“””
Output = [1112, 5324, 1773, 5324, 555]
"""

string = """Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial"""

list3=string.split(" ")
list4 = []

for val in list3:
    if val.isdigit():
        list4.append(val)

print(list4) #['1112', '1773', '444', '5324', '555']

print("-"*50)


#17). Write a python program to replace the words “Java” with “Python” in the given string.
#Input = “JAVA is the Best Programming Language in the Market”
#Output = “Python is the Best Programming Language in the Market”

string2 = "JAVA is the Best Programming Language in the Market"
list5 = string2.split(" ")

print(string2.replace("JAVA","Python"))


#18). Write a Python program to get all the palindrome words from the string.
#Input = “Python efe language aakaa hellolleh”
#output = [“efe”, “aakaa”, “hellolleh”]

string4 = "Python efe language aakaa hellolleh"
List4 = string4.split(" ")
new_list1 = []

for val in List4:
    if val == val[::-1]:
        new_list1.append(val)
print(new_list1) #['efe', 'aakaa', 'hellolleh']

print("-"*50)
#19). Write a Python program to create a string with a given list of words.
#Input = [“There”, “are”, “Many”, “Programming”, “Language”]
#Output = There are many programming languages.

list6 = ["There","are", "Many", "Programming", "Language"]
" ".join(list6)


#20. Write a Python program to get common words from strings.
#Input String1 = “Very Good Morning, How are You”
#Input String1 = “You are a Good student, keep it up”
#Output = “You Good are”

#Input strings
string1 = "Very Good Morning, How are You"
string2 = "You are a Good student, keep it up"
List = []

for word in string1.split(" "):
    if word in string2.split(" "):
        List.append(word)

" ".join(List)