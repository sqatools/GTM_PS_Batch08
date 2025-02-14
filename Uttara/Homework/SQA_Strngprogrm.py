#SQA Practice string Program

#1..Python string program to reverse a string if it’s length is a multiple of 4.
string2 = "Pythonprogra"
if len(string2) % 4 == 0:
    print(string2[::-1])
#argorpnohtyP

#3. Python string program to count occurrences of a substring in a string.

string3 = "Pythonprogram"
substrng = "program"
string3.count(substrng)  #"program"
print("substring:",substrng)

#4.Python string program to test whether a passed letter is a vowel or consonant.

letter = "aerv"
for char in letter:
    if char == "a" or char =="e" or char =="i" or char =="o" or char =="u":
        print(" Letter is vowel",char)
    else:
        print(" Letter is consonant",char)

"""Letter is vowel a
        Letter is vowel e
    Letter is consonant r
    Letter is consonant v"""
########################################################################################################
#5.Print most simultaneously repeated characters in the input string.

str11 = "Helllllo Worllld off progrrram"
max_repeat_count = 0
max_repeat_char = ''

temp = 1
for i in range(len(str11)-1):
    if str11[i] == str11[i+1]:
        temp = temp + 1
        if temp > max_repeat_count:
            max_repeat_count = temp
            max_repeat_char = str11[i]
    else:
        temp = 1

print("Max repeated char :", max_repeat_char,
      "\nMax repeated count :", max_repeat_count)

"""Max repeated char : l 
Max repeated count : 5"""
#########################################################################################################
#6.Write a Python program to calculate the length of a string with loop logic.

string5 = "im am learing python"
count = 0

for char in string5:
    count +=1

print("Length of the string using loop logic: ", count)
print("Length of the string using len(): ", len(string5))

"""Length of the string using loop logic:  20
Length of the string using len():  20"""
###############################################################################################################
#7.Write a python program to get to swap the last character of a given string.
"""Input = “Python”
Output = “nythoP”
code:"""
string6 = "Python"
print(string6[-1]+string6[1:-1]+string6[0])
#nythoP

"""8.Write a python program to replace the words “Java” with “Python” in the given string.
Input = “JAVA is the Best Programming Lanuage in the Market”
Output = “Python is the Best Programming Language in the Market”
code:"""

string7 = "JAVA is the Best Programming Language in the Market"
List1 = string7.split(" ")

for word in List1:
    if word == "JAVA":
        index = List1.index(word)
        List1[index] = "PYTHON"

print(" ".join(List1))
#PYTHON is the Best Programming Language in the Market

#############################################################################################################
"""9.Write a Python program to create a string with a given list of words.
Input = [“There”, “are”, “Many”, “Programming”, “Language”]
Output = There are many programming languages.
code:"""
ls1 = ["There", "are", "Many", "Programming", "Language"]

print(" ".join(ls1))
#There are Many Programming Language

"""10.Write a Python program take a string as input and count all the Uppercase, Lowercase, 
special character and numeric values in a given string.
code:"""
str8 = "@PythonPrograms1"
upper = 0
lower = 0
digit = 0
symbol = 0

for val in str8:
    if val.isupper():
        upper += 1
    elif val.islower():
        lower += 1
    elif val.isdigit():
        digit += 1
    else:
        symbol += 1

print("Uppercase: ", upper)
print("Lowercase: ", lower)
print("Digits: ", digit)
print("Special characters: ", symbol)
"""output:Uppercase:  2
Lowercase:  12
Digits:  1
Special characters:  1"""

###############################################################################################################

"""11.Check whether the given string is a palindrome (similar) or not.
Input= sqatoolssqatools
Output= Given string is not a palindrome"""

string9 ="sqatoolssqatools"
string10 = string9[::-1]

if string9 == string10:
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")

##############################################################################################################

"""12.Write a program to calculate the length of a string.
Input= “python”
Output = 6
code:"""
string12="python"
print("Lenght of String:",len(string12))

"""13.Write a program to combine two strings into one.
Input: 
A = ’abc’
B = ’def’
Output = abcdef
code:"""
str111 = "abc"
str222 = "def"
#combine=str111 + str222

print("combine two strings into one:",str111 + str222)
###############################################################################################################

"""14.write a program to check if a string has a number or not.
Input = ‘python1’
Output = ‘Given string have a number’"""

string13 = "python1"
checknum = 0
for char in string13:
    if char.isnumeric():
        checknum += 1

#Checking for numbers
if checknum > 0:
    print("Given string have a number")
else:
    print("Given string does not have a number")
#############################################################################################################
"""15.Write a python program to count the number of consonants in a string.
Input= ‘PythonProgram’
"""
string14 = "PythonProgramming"
vowel = ["a","e","i","o","u","A","E","I","O","U"]
count = 0

for char in string14:
    if char not in vowel:
        count += 1

print("Number of consonants: ",count)
#Number of consonants:  13
############################################################################################################
"""16.Write a program to exchange the first and last letters of the string
Input = We are learning python
Output = ne are learning pythoW
code:"""

string15= "We are learning python"
print(string15[-1]+string15[1:-1]+string15[0])

"""17.Write a program to convert all the characters in a string to Upper Case.
Input = ‘I live in pune’
Output = ‘I LIVE IN PUNE’
code:"""""
string17= "I live in pune"
print(string17.upper())
print("_" * 100)

###############################################################################################################
#18.Write a program to remove a new line from a string using python.
"""Input = ‘objectorientedprogramming\ns’
Output = ‘objectorientedprogramming’
code:"""
string18= "objectorientedprogramming\ns"
print(string18.rstrip())
print("_" * 100)

################################################################################################################
#19.Write a program to print floating numbers up to 3 decimal places and convert it to string.

num = 5.56789
result = ""
result += str(round(num, 3))

print(result)
print("_" * 100)
#5.568
#20.Print the mirror image of string.

string19 = "Python"
print(string19[::-1])
print("_" * 100)
#nohtyp
###################################################################################################################
#21.Take a string as input and get all the email id’s from the given string.
"""Input str = “” We have some employee whos
john@gmail.com email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com all
the email mery@hotmail.com id’s from this given string."""

str0 = """"We have some employee whos john@gmail.com 
           email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com
            all the email mery@hotmail.com id’s from this given string"""
List_a = str0.split(" ")
List_b = []

for char in List_a:
    for val in char:
        if val == "@":
            List_b.append(char)


print(List_b)
#['john@gmail.com', 'jay@lic.com', 'hari@facebook.com\n', 'mery@hotmail.com']