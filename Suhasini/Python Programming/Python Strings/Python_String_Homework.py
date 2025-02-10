# Home work for string slicing
# 1. String Slicing Program
str4 = "Learning Python"
"""
1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
"""

print("1. read only Learning")
print(str4[0:8])        # Learning
print()
print("_"*50)

print("2. read only First and last character :  Ln")
slen = len(str4)
print(str4[0],str4[slen-1])
print("_"*50)

"""
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
"""
print("3. print the pattern 'earning Pythoearning Pytho'")
slen = len(str4)
str5 = str4[1:slen-1]
print(str5*2)
print("_"*50)

"""
4. get given output  : "LLLearning Pythonnn" 0,14
"""
print("4. get given output  : 'LLLearning Pythonnn'")
s1 = str4[0]*2
s2 = str4[14]*2
s3 = s1+str4+s2
print(s3)
print("_"*50)


# 2. Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string

str1 = "Hippopotamus"

if len(str1) < 2:
    print("True")
else:
    str2 = str1[:2] + str1[-2:]
    print("String made with first and last 2 characters of string: ",str2)
print("_"*70)

# 3. Python string program to get a string made of 4 copies of the
# last two characters of a specified string (length must be at least 2).

str3 = "Suhasini"
if len(str3) < 2:
    print("String length should be greater than 2")
else:
    strA = str3[-2:]
    print("String made of 4 copies of last 2 characters of string: ", strA*4)
print("_"*70)


#4. Write a program to print each character on a new line using python.

str4 = 'python'
for char in str4:
    print(char)
print("_"*70)

"     DOUBT.   "
#5. Write a program to remove repeated characters in a string and replace it with a single
# letter using python.
# Input = ‘aabbccdd’
# Output = ‘cabd’

str5 = 'aabbccdd'
strB = set(str5)
print("String after removing repeated characters in string is: ", str(strB))
print("_"*70)


# 6. Write a program to find the first repeated character in a string and its index.
# Input = ‘sqatools’

str6 = 'sqatools'
for i in range (len(str6)):
    for char in str6:
        if char == str6[i]:
            print(char, i)
    break


#Input string
str1 = "sqatools"

for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        if str1[i] == str1[j]:
            print(f"({str1[i]},{str1.index(str1[i])})")
    break

print("_"*70)


# 7. Write a program to print the index of each character in a string.
# Input =  ‘sqatools’

str7 = "sqatools"
for i in range (len(str7)):
    print("Index of ",str7[i]," is ",i)

print("_"*70)


# 8. Write a program to reverse words in a string using python.
# Input = ‘string problems’

str8 = "string problems"
length = len(str8)

print("String after reversing: ",str8[-1:-len(str8)-1:-1])
print("_"*70)


# 9. Write a program to add ly at the end of the string if the given string ends with ing.
# Input = ‘winning’

str9 = "Winning"
if str9.count("ing") != 0:
    strA = str9 + "ly"
    print("String after adding 'ly' to it: ", strA)
else:
    print("String does not contain 'ing' in it")
print("_"*70)


# 10. Write a program to add ‘ing’ at the end of the string using python.
# Input = ‘xyz’

str10 = "xyz"
print("String after adding 'ing' to it: ",str10+"ing")
print("_"*70)


# 11. Write a program to check if a given string is binary or not.

str11 = "001010101001"
count = 0
for char in str11:
    if char == '0' or char == '1':
        count += 1

if count == len(str11):
    print("Given string is Binary")
else:
    print("Given string is not Binary")
print("_"*70)


# 12. Write a program to remove the kth element from the string
# K=2

str12 = "sqatools"
strA = str12[0:2]+str12[3:len(str12)]
print("String after removing kth element: ",strA)
print("_"*70)


# 13. Write a program to accept a string that contains only vowels

str13 = "Python"
str13a = "aaieou"

count = 0
for char in str13a:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A'
            or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        count += 1

if count == len(str13a):
    print("String contains only Vowels")
else:
    print("String is not made of vowels only")
print("_"*70)


# 14.Write a program to avoid spaces in string and get the total length

str14 = "sqatools is best for learning python"

spaceno = str14.count(" ")
# print(spaceno)
print("Length of string after avoiding spaces is: ",len(str14)-spaceno)
print("_"*70)


# 15. Write a program to split and join a string using “-“.
# Input = ‘Sqatools is best’
# Output = ‘Sqatools-is-best’

str15 = "Sqatools is best"
strA = str15.replace(" ","-")
print("String after replacing space with - : ",strA)
print("_"*70)


# 16. Write a program to uppercase half string using python.

str16 = "banana"
#a = len(str16)//2
# print(a)
strA = str16[len(str16)//2:len(str16)]
print("String after changing 2nd half of the string to upper case: ",strA.upper())
print("_"*70)


# 17. Write a program to insert space before every capital letter appears in a given word using python.
# Input = ‘SqaTools pyThon’
# Output = ‘ Sqa Tools py Thon’

strA = ""
str17 = "SqaTools pyThon"
for char in str17:
    if char.isupper():
        #print("true")
        strA = strA + " " + char
    else:
        strA = strA + char

print("Output after adding space before all uppercase characters: ",strA)
print("_"*70)


# 18. Write a  program that counts the number of leap years within
# the range of years using python. The range of years should be accepted as a string.
#(“1981-2001")  =  Total leap year 5

str1 ="1981-2001"
l = str1.split("-")
total = 0

for i in range(int(l[0]),int(l[1])+1):
    if (i % 400 == 0 or i % 100 !=0) and i % 4 == 0:
        total += 1

print("Range of years:", str1)
print("Total leap year: ",total)
print("_"*70)


# 19. Write a program to extract name from a given email address using python.
# Input = ‘student1@gmail.com’
# Output = ‘student’

str19 = "student1@gmail.com"
ind = str19.index("@")
name = ""

for i in range (0, ind-1):
    if str19[i].isalpha():
        name = name + str19[i]

print("Name extracted from email id is: ",name)
print("_"*70)


# 20. Write a program to split a given multiline string into a list of lines using python.
# Input =”’This string Contains
# Multiple
# Lines”’
# Output = [‘This string Contains’, ‘Multiple’, ‘Lines’]

str20 = "This string Contains \n Multiple \n Lines"
strA = str20.split("\n")
print("Text after splitting multiple lines:\n",strA)
print("_"*70)






















