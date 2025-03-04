print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

######
# lower() and upper() method :
#      -> Lower method convert character in small case.
#      ->  Upper method convert characters in capital case.

str1 = "HELLO we are LEARNING PytHon"
print(str1.lower()) # hello we are learning python
print(str1.upper()) # HELLO WE ARE LEARNING PYTHON
output = str1.casefold()
print(output)

print("_"*50)
###################
# islower() and isupper():
# is_lower() : This method return True if all the character in string are in small case else return False
# is_upper() :  This method return True if all the character in string are in capital case

str_a = "HelLo"
str_b = "PYTHON"
str_c = "program"

print("str_a is lower :", str_a.islower()) # False
print("str_a is upper :", str_a.isupper()) # False

print("str_b is upper :", str_b.isupper()) # True
print("str_c is lower :", str_c.islower()) # True


print("_"*50)
###################
# capitalize Method: This method convert only first character of string in capital case and convert remaining into
#                     small case.
str_d = "india won Today's Match"
print(str_d.capitalize())  # India won today's match


print("_"*50)
###################
# title method :  This method convert first character each word into capital case.\
str_e = "pytHoN ,is  verY, To; leArn"
print(str_e.title())  # Python Is Very To Learn

str_f = "i,invited,reeta,sita,geeta"
print(str_f.title())  # I,Invited,Reeta,Sita,Geeta

# istitle() method :  This method check the given string in following the rule of
#                     title string or not, e.g. first character of each word in string
#                     should be capital case.

str_g = "Hello Python"
str_h = "python Programming"
print("str_g is title case :", str_g.istitle()) # True
print("str_h is title case :", str_h.istitle()) # False



print("_"*50)
###################
# swapcase() method : This method convert upper case to lower and lower case to upper in one single string.

str_j = "Hello GOOD Morning"
print(str_j.swapcase())  # hELLO good mORNING

output1 = ""
for char in str_j:
    print(char)
    if char.isupper():
        output1 = output1 + char.lower()
    elif char.islower():
        output1 = output1 + char.upper()
    else:
        output1 = output1 + char

print("output :", output1) # hELLO good mORNING


print("_"*50)
######################
#strip method : This method remove trailing spaces from given string. all the spaces in the begining and
#                end of string

str_l = "  Python Programing  "
print(str_l)
print(str_l.strip())

# lstrip method : This method only remove start spaces from given string.
print(str_l.lstrip())

# rstrip method : This method only remove end of string spaces from given string.
print(str_l.rstrip())

str_m = " Hello GoodMorning  "
var1 = str_m.lstrip()
var2 = var1.rstrip()
print(var2) # Hello GoodMorning

print("_"*50)
######################
# count() method :  This method return number of occurrences of any character/substring/special character

str_n = "Hello Good Morning, We are Learning Python"

print("count of e:", str_n.count('e')) # count of e: 4
print("count of ing:", str_n.count('ing')) # count of ing: 2
print("count of spaces:", str_n.count(' ')) # count of spaces: 6


print("_"*50)
######################
# index() method : Index method return index position of any substring or character
str_q = "India is Best Country"
# get index position of character which is available
print(str_q.index("B")) # 9
# If character is repeated, then it will return first occurrence of the character


# get index position of character which is not available
# print(str_q.index("T")) # 9
# ValueError: substring not found
# ->  if character or substring is not available then it will return error.


print("_"*50)
######################
# find() method :  This method return index position of character/substring/number/special character
#                   if it is available in the target string
#                   ->  if the given substring/character is not available, then it will return -1

str_w = "Learning if Fun"
print("find ing :", str_w.find("ing")) # 5 index of first character of substring
print("find TO :", str_w.find("TO")) # -1 return -1 value if string/char is not available


print("_"*50)
#####################
# split method :  This method split string from any char/substring/delimiter and return list of words.

str_A = "Hello Good Morning, How Are You?"
result1 = str_A.split(" ")
print(result1) # ['Hello', 'Good', 'Morning,', 'How', 'Are', 'You?']


str_B = "Python%Programming%is%Very%Easy%to%Learn"
result2 = str_B.split("%")
print(result2)  # ['Python', 'Programming', 'is', 'Very', 'Easy', 'to', 'Learn']


str_C = "Python Programing ios Fun"
print(str_C.split("o")) # ['Pyth', 'n Pr', 'graming i', 's Fun']

str_D = "HelloGoodMorning"
print(str_D.split()) # default value for split is space
# ['HelloGoodMorning']

print("_"*50)
#####################
# replace method :replace method help to replace any word/character/substring from target value

str_E = "Virat is Best Indian Player, Virat is good human"
result = str_E.replace("Virat", "Sachine")
print(result)
# Sachine is Best Indian Player, Sachine is good human

result2 = str_E.replace("Virat", "Dhoni").replace("Player", "Captain")
print("Result2 :", result2)
# Dhoni is Best Indian Captain, Dhoni is good human


print("_"*50)
############################################
# isdigit(): This method check given string only contains number
s1 = "Helo234"
print("s1 is contains only digit :", s1.isdigit()) #  False

s2 = "5453443453453"
print("s2 is contains only digit :", s2.isdigit()) # True

s3 = "545344 3453453"
print("s3 is contains only digit :", s3.isdigit()) # False

print("_"*50)
############################################
# isalpha() :  This method check if string only contains alphabates

p1 = "Hello"
print("p1 is contains only alphabates :", p1.isalpha()) # True
p2 = "Hello Good"
print("p2 is contains only alphabates :", p2.isalpha()) # False

print("_"*50)
############################################
# isalnum() :  This method check if given string contains only character and numbers

q1 = "Hello123"
print("q1 is contains only characters and numbers :", q1.isalnum()) # True
q2 = "Hello 123"
print("q2 is contains only characters and numbers :", q2.isalnum()) # False
q3 = "HelloPython"
print("q3 is contains only characters and numbers :", q3.isalnum()) # True
q4 = "34567"
print("q4 is contains only characters and numbers :", q4.isalnum()) # True


print("_"*50)
############################################
# isspace() : This method return True of given string contains only spaces.
r1 = " "
print("r1 contains only space :", r1.isspace()) #  True

# count the spaces without using count method.
str11 = "Hello good morning, how are you"
space_count = 0

for char in str11:
    if char.isspace():
        space_count += 1
    else:
        continue

print("total spaces :", space_count)
# total spaces : 5

print("_"*50)
########################################
# write a python program to replace the word Today with Tomorrow without using replace method

str_t = "Lets Learn Today Something New Today"
result = "" # Lets Learn Something New Tomorrow
word1 = 'Today'
word2 = 'Monday'

word_list = str_t.split() # ['Lets', 'Learn', 'Something', 'New', 'Today']
print(word_list)
for word in word_list:
    print(word)
    if word == word1:
        result = result + word2 + " "
    else:
        result = result + word + " "

print(result)

print("_"*40)
#################################
word_list = ['Lets', 'Learn', 'Something', 'New', 'Today']
word_list.insert(2, '2025')
print(word_list)


# Join method :  This method help to join string or list of string with specific char/substring/delimiter
result = " ".join(word_list)
print(result)  # Lets Learn 2025 Something New Today\

str_y = "Hello"
print("-".join(str_y)) # H-e-l-l-o

str1 = "Python Programming"
result2 = "*".join(str1)
print("Result :", result2)


###########################################
str2 = "Pyth2on 356 Programing 2"
result = str2 == ""
print(result)

password = "Admin@123"
updated_Value = "*&%^&%&^%^".join(password)
print(updated_Value)

org_password = updated_Value.replace("*&%^&%&^%^", "")
print(org_password)

print("_"*50)
########### use of is operator ##########
list1 = [True, False, None, 'Hello', 'Python']

# for val in list1:
#     if val is None:
#         continue
#     else:
#         print(val)


for val in list1:
    if val is not None:
        print(val)
    else:
        continue

str1 = "Python"


print(str1, type(str1))

# read string with positive and negative  indexing

"""
 0 1 2 3 4 5
 P y t h o n
-6-5-4-3-2-1

"""
print(str1[3]) # h

print(str1[-4]) # t

##### String Formatting  #####

name = "Mohit"
age = 25
city = "Mumbai"
# Hello My name is Mohit and age is 25 and I am living in Mumbai

# 1) String Concatenation
result1 = "Hello My name is "+name+" and age is "+str(age)+" and I am living in "+city
print("result1 :", result1)

# 2) String Format Method:

result2 = "Hello My name is {} and age is {} and I am living in {}".format(name, age, city)
print("result2 :", result2)

# 3) f-string Formatting:
result3 = f"Hello My name is {name} and age is {age} and I am living in {city}"
print("result3 :", result3)


print("_"*50)
####### Raw string conversion #############
# When we add r before the double quotes then entire string will convert into raw string.
# all special character property won't work e.g. \n or \t
# \t : for adding tab space in string
# \n : Adding next line output
str2 = r"Hello good \t morning, {name} we are learning \n \n Python Programming, its \t very  \n easy to \t learn"
print(str2)

print("_"*50)
############################ Slicing in the string #######################

# Rule1 :  str[start index : end index]
# In this rule sub string will include start index value and exclude end index value
# Output will always consider the string value from left to right
# It can contain both positive and negative index values

str_a = "Programming"
# [+ve:+ve]
print(str_a[2:7]) # ogram
print(str_a[0:9]) # Programmi

# If we try to get value from right to left then it will return blank output
print(str_a[7:2])  # blank

# [+ve, -ve]
print(str_a[2: -2])  # ogrammi
print(str_a[1:-1])  # rogrammin

# [-ve : +ve]
str3 = "Good Morning"
print(str3[-7:11])  # Mornin

# [-ve:-ve]
print(str3[-9:-2]) # d Morni


# Home work for string slicing
str4 = "Learning Python"
"""
1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
"""

print("_"*50)
##################
# Rule2 :  str[ : end index]
# Default initial index will be zero

str_b = "Programming"
print(str_b[:6]) # Progra

print(str_b[:-3]) # Programm
print(str_b[:-1]) # Programmin
print(str_b[:]) # Programming
print(str_b[:0]) # blank

print("_"*50)
##################
# Rule3 :  str[ start index: ]
# Default end index would be end of the string.

str_c = "Good Evening"
print(str_c[5:]) # Evening

print(str_c[-9:]) # d Evening


print("_"*50)
##################
# Rule4 :  str[ start index: end index : step]
# ->  substring output will contain start index value and exclude end index
# ->  substring output will depend on step value defined.
# ->  start index, end index and step value could be +ve and -ve.
# ->  substring output could be reverse as well


str_x = "IndiaIsBestCountry"

# [+ve:+ve:+ve]
print(str_x[2:10:1]) #

print(str_x[2:13:3]) # diaIsBes

print(str_x[0:17:2]) # Idasetonr

# [+ve:-ve:+ve]
print(str_x[1:-1:1]) # ndiaIsBestCountr
str_len  = len(str_x)
print(str_len)
print(str_x[1:len(str_x):1]) # ndiaIsBestCountry

# If we dont defined the end index, default end index would be end of string
print(str_x[1::1]) # ndiaIsBestCountry


# [-ve:-ve:+ve]
str_y = "PythonIsGreat"
print(str_y[-8:-1:1]) # nIsGrea

# [-ve:-ve:-ve]
print(str_y[-10:-1:-1]) # blank
print(str_y[-1:-10:-1]) # taerGsIno
print(str_y[-1:-len(str_y):-1]) # taerGsInohty
print(str_y[-1:-len(str_y)-1:-1]) # taerGsInohtyP

#str_y[-1:-13:-1]

# Notes: when we try to find the substring with the help slicing rule
# Then we have to look to next value of start index, if next index value is in between the range
# of start index and end index, then it will return output, otherwise it will return blank.

# Notes : Negative index movement consider as reverse substring
#       : Positive index movement consider as positive substring

##################################
# Rule 5:   str[:: step]
# -> IF step is positive:
#     -> In this rule if we don't define the start index, then default start index will 0
#     -> In this rule if we don't define the end index, then default end index will end of string.
#     -> It will read the sub-string from left to right

# -> IF step is Negative:
#    -> In this rule if we don't define the start index, then default initial index will -1
#    -> In this rule if we don't define the end index, then default end index will, start of string.
#    -> It will read the sub-string from right to left

print("_"*50)
# with +ve step
str_z = "WeAreLearningPython"
print(str_z[::1])  # WeAreLearningPython
print(str_z[::2])  # WAeerigyhn
print(str_z[:8:2]) # WAee
print(str_z[2::2]) # Aeerigyhn

print("_"*50)
# with -ve step
str_p = "LearningSlicing"
print(str_p[::-1]) # gnicilSgninraeL
#-1:-len(str)-1:-1]


print(str_p[::]) # LearningSlicing
print(str_p[:-1:]) # LearningSlicin
print(str_p[-1:len(str_p):1]) # g
print(str_p[-1::]) # g



# write a python program to get the longest word from given string
str1 = "lick Open Zoom Workplace app on the dialog shown by your browser"
long_word = ''
long_len = 0

# get word list with split method
word_list = str1.split()
# get each word using loop
for word in word_list:
    word_len = len(word)  # get length of each word
    print(word, word_len)
    # compare word_len with long_len:
    if word_len > long_len:  # |  4 > 4 | 9 > 4 | 3 > 9
        long_len = word_len  # 4 ,9
        long_word = word  # lick, Workplace
    else:
        continue

print("longest word :", long_word, long_len)

# Home Work
# write a python program to get smallest word from given string.


print("_" * 50)
######################################################
# write a python program to find out all the mobile numbers and email id from given string.
"""
We are working on python programs
"""

str2 = """
There are 9987878754 several user1@gmail.com types of automation 7787878754 frameworks, 
including 45 linear 8787878754 scripting, modular user2@facebook.com testing, 2344 data-driven, 
keyword-driven, user3@yahoo.com and hybrid 5587878754 testing. Each user4@hotmail.com type 53 has its 
own use case and advantages
"""
# get word list using split method
word_list = str2.split()
emails = ''
mobile = ''
for word in word_list:
    # check @ in given word, to consider as email
    if "@" in word:
        print(word)
        emails = emails + word + " "
    # check word length should be 10 and only contains digits, then consider as mobile number.
    elif len(word) == 10 and word.isdigit():
        print(word)
        mobile = mobile + word + " "
    else:
        continue

print("All emails :", emails)
# user1@gmail.com user2@facebook.com user3@yahoo.com user4@hotmail.com
print("All Mobile Numbers :", mobile)
# 9987878754 7787878754 8787878754 5587878754


print("_" * 50)
#################################################
# Q : write a python program to remove all duplicate words from given string
str3 = "Pramod Hema Kartik Bala Pramod Manoj Hema Kartik"
# output = "Pramod Hema Kartik Bala Manoj"

result = ""
word_list = str3.split()

for word in word_list:
    if word not in result:
        result = result + word + " "
    else:
        continue

print("Result :", result)
# Pramod Hema Kartik Bala Manoj


print("_" * 50)
# write a program to get words who len is 4

for w1 in word_list:
    # if len(w1) is 4:
    #     print(w1)
    # else:
    #     continue

    if len(w1) is not 4:
        print(w1)
    else:
        continue

######################## Home Work ################
# Q1 : Write a python program to find smallest word from given string

# Q2 :  write a python program to get count all vowels from given string
str_a = "Hello GoOd MOrnIong"
# output = 7

# Q3 :  Write a python program to Convert all Vowels from upper to lower and lower to upper.
str_b = "We Are LEarnIng Python PrOgrammIng"
# output = "WE arE LeArning PythOn ProgrAmming"

str6 = 'WqRtoolsta'
temp = ''
# for i in range(len(str6)):
#     for char in str6:
#         if char == str6[i] and char not in temp:
#             print((char, i))
#             temp += char
#     break


# Programs : 100
# flag = 0
# for i in range(len(str6)):
#     for j in range(i+1, len(str6)):
#         if str6[i] == str6[j]:
#             print((i, str6[i]))
#             flag += 1
#             break
#     if flag != 0:
#         break



# #Input string
# str1 = "Wqatools"
#
# for i in range(len(str1)):
#     for j in range(i+1,len(str1)):
#         if str1[i] == str1[j]:
#             print(f"({str1[i]},{str1.index(str1[i])})")
#     break
#


# 102). Write a program to remove repeated characters in a string and replace it with a single letter using python.
# Input = ‘aabbccdd’
# Output = ‘cabd’

str5 = 'aabbccdddddddaaaaaafgffffff'
# strB = set(str5)
# print("String after removing repeated characters in string is: ", str(strB))
# print("_"*70)
"""
output = ""
for char in str5:
    if char not in output:
        output += char
    else:
        continue

print("Output :", output)
"""


# 8). Print most simultaneously repeated characters in the input string.
str1="Hello how arrrrrrre youuuu"
max_count=0
max_char=""
for i in range(0, len(str1)-1):
    # if i==len(str1)-1:
    #     break
    # else:
    if str1[i] != str1[i+1]:
        temp=1
        continue
    else:
        temp=temp+1
        if temp>max_count:
            max_count=temp
            max_char=str1[i]

print("The most simultaneously repeated character is:",max_char)
print("The count of most simultaneously repeated character is:",max_count)
# str1 = "Good Morning"
# str_len = len(str1)
#
# for i in range(str_len):
#     print(i,":", str1[i])
#
#
# str1= "  Hello Good Morning  "
# print(str1.lstrip().rstrip().lower().upper().replace(" ", "_").split("_"))
# # ['HELLO', 'GOOD', 'MORNING']
#

# file = open("read_data.txt", "r")
# data = file.read()
# print(data)
# word_list = data.split(" ")
# for word in word_list:
#     if word.isdigit():
#         print(word)


dict1 = {'Name': 'Virat', 'Age': 35}
for val in dict1.items():
    print(val[0], val[1])
