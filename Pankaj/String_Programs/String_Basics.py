########################## String ####################

str1 = "Pankaj"
print(str1, type(str1))
print(str1[0])
print(str1[2])
print(str1[-3])

# 0 1 2 3 4 5
# P y t h o n
#-6-5-4-3-2-1

##### String Formatting  #####

print("_"*50)
# 1. String concatenation
name = "pankaj"
age = 38
city = 'Bangalore'
# 1) String Concatenation
str2 = "Hello my name is " + name + ", my age is " + str(age) + " and i am currently residing in " + city
# if only int in between the --> TypeError: can only concatenate str (not "int") to str
print(str2)

print("_"*50)
# 2) String Format Method:
str3 = "Hello my name is {}, my age is {} and currently i am residing in {}".format(name, age, city)
print(str3)

print("_"*50)
# 3) f-string Formatting:
str4 = f"Hello my name is {name}, my age is {age} and currently i am residing in {city}"
print(str4)

print("_"*50)
############################ Slicing in the string #######################

# Rule1 :  str[start index : end index]
# In this rule sub string will include start index value and exclude end index value
# Output will always consider the string value from left to right
# It can contain both positive and negative index values

str4 = "Pankaj Prasad"
# with positive indexing
# [+ve:+ve]
print(str4[2:6])
print(str4[0:12])
print(str4[0:])

# with +ve and -ve indexing
print(str4[2:-3])

# with -ve and +ve indexing
print(str4[-7:10])

# with -ve and -ve indexing
print(str4[-10:-2])

# Home work for string slicing
str4 = "Learning Python"
"""
1. read only "Learning" 
2. read only First and last character :  Ln
3. read all characters except first and last and repeat 2 times the output.
"earning Pythoearning Pytho"
4. get given output  : "LLLearning Pythonnn"
"""
# 1. read only "Learning"
str5 = "Learning Python"
print(str5[0:8])

# 2. read only First and last character :  Ln
print(str5[0] + str5[-1])

# 3. read all characters except first and last and repeat 2 times the output.
ch1 = str5[1:-1]
print(ch1*2)

# 4. get given output  : "LLLearning Pythonnn"
ch2 = str5[0:]
print(str5[0]*2+ch2+str5[-1]*2)



# Date: 06/02/2024
print("_"*70)
# Rule 2 : str[ : end index]
# Default index value will be zero

str11 = "Python_String"
print(str11[:7])
print(str11[:-1])
print(str11[:]) # Default end index would be end of the string.
print(str11[:0]) # blank
print(str11[:-7])

print("_"*50)
##################
# Rule3 :  str[ start index: ]
# Default end index would be end of the string.
print(str11[1:])
print(str11[-4:])

print("_"*50)
#################################################################################################
# Rule4 :  str[ start index: end index : step]
# ->  substring output will contain start index value and exclude end index
# ->  substring output will depend on step value defined.
# ->  start index, end index and step value could be +ve and -ve.
# ->  substring output could be reverse as well

str_x = "Selenium"
# [+ve:+ve:+ve]
print(str_x[2:8:1])
print(str_x[0:8:2])

# [+ve:-ve:+ve]
print(str_x[1:-1:1])
str_len = len(str_x)
print(str_len)
print(str_x[1:len(str_x):1])

# If we don't define the end index, default end index would be end of string
print(str_x[1::1])

print("_"*50)
# [-ve:-ve:+ve]
str_y = "pankaj"
print(str_y[-5:-1:1])
print("_"*50)
# [-ve:-ve:-ve]
print(str_y[-5:-1:-1])# Blank
print(str_y[-1:-5:-1])
print(str_y[-1:-len(str_y):-1])
print(str_y[-1:-len(str_y)-1:-1])

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
str_z = "Selenide"
print(str_z[::1])
print(str_z[::2])
print(str_z[:5:2])
print(str_z[2::2])

print("_"*50)
# with -ve step
str_p = "LearningSlicing"
print(str_p[::-1])
#-1:-len(str)-1:-1]


print(str_p[::])
print(str_p[:-1:])
print(str_p[-1:len(str_p):1])
print(str_p[-1::])

###################################### String Reverse #################
# String Homework
str11 = "We are learning Python Programming"
w1 = str11[0:2]
w2 = str11[3:6]
w3 = str11[7:15]
w4 = str11[16:22]
w5 = str11[23:34]
print(w1, ":", w2, ":", w3, ":", w4, ":", w5)
W1 = f"{w1[-1]}{w1[0]}"
print(W1)
W2 = f"{w2[-1]}{w2[1]}{w2[0]}"
print(W2)
W3 = f"{w3[-1]}{w3[1:-1]}{w3[0]}"
W4 = f"{w4[-1]}{w4[1:-1]}{w4[0]}"
W5 = f"{w5[-1]}{w5[1:-1]}{w5[0]}"

result1 = f"{W1} {W2} {W3} {W4} {W5}"
print(result1)

# Reverse each word of the string.
M1 = w1[::-1]
M2 = w2[::-1]
M3 = w3[::-1]
M4 = w4[::-1]
M5 = w5[::-1]
result2 = f"{M1} {M2} {M3} {M4} {M5}"
print("Result2 :", result2)

print("_"*50)
########################## Python String Methods ##########################
print(dir(str))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
  'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

#########
# upper() and lower() method: These method convert upper case string to lower case
#         and lower case string to upper case
str_a = "Hello We Are Learning PYthon Programming language"
Str_A = str_a.upper()
print(Str_A)
print(Str_A.lower())
print(Str_A[34].lower())

print("_"*50)
######
# islower() and isupper() Method:
# These methods check the given string is in lower case or upper case
str_b = "HELLO GOOD MORNING"
str_c = "good evening"
print("for checking upper case : ", str_b.isupper())
print("for checking lower case : ", str_b.islower())
print("for checking upper case : ", str_b.islower())

print("_"*50)
###################
# capitalize Method: This method convert only first character of string in capital case and convert remaining into
#                     small case.
str_0 = "today i have To go Office"
print(str_0.capitalize())

print("_"*50)
################
# title() and istitle method:
# title method convert first letter of each word into camel case and istitle check the given string
# follows the rule of title sentence.
str_g = "HeY hope yoU Are DOing Good"
print("str_g : ", str_g.title())
output = str_g.title()

print("title check: ", str_g.istitle())
print("title check: ", output.istitle())

print("_"*50)
################
# Replace Method: Replace method helps to update any character or substring in the given string.

str_b = "Pankaj"
str_B = str_b.replace("P", "p")
print(str_B)
str_BB = str_b.replace("j", "J")
print(str_BB)

str_C = str_b.replace("Pankaj", "Prasad")
print(str_C)

################# Strip ##############################

print("_"*50)
#################################################################

#  count() Method: This method count the occurrences of any character or substring in the given string
str_d = "Hello i am from Varanasi and i am working in banagalore"
print("Count of char a : ", str_d.count('a'))
print("Count of am : ", str_d.count('am'))

# How to find total character
Total_Char = len(str_d)
print("Total number of char used in String is : ", Total_Char)

print("_"*50)
# ################
#  swapcase() Method: This method covert all the character from Upper to lower and lower to upper.

str_e = "Hello i am from Varanasi and i am working in banagalore"
print("Swapcase result : ", str_e.swapcase())

# same thing by using for loop
output_x = ""
for char in str_e:
    #print(char)
    if char.isupper():
        output_x = output_x + char.lower()
    elif char.islower():
        output_x = output_x + char.upper()
    else:
        output_x = output_x + char
print(output_x, end=" ")

# count of character using for loop
print("_"*50)
# Write a python program to get count of each character in the string.
str_l = "Lets HopE IndIa wiLL win the last Test India Match"
temp = "" # empty string
for char in str_l:
    if char not in temp:
        print(char, str_l.count(char))
        temp = temp+char
    else:
        continue

print("_"*50)
# ################
#  index() Method : This method return the index position of available sub-string or character.
str_f = "Good Morning"
print("Index of M: ", str_f.index("M"))
print("Index of ning: ", str_f.index("ning"))

# print("If char is not present in string P", str_f.index("P"))
# find the index of un-available string
# print("index of ing :", str_x.index("MM")) # 9
# It gives error and fail the program if the target sub-string in not available
# ValueError: substring not found

print("_"*50)
############
# find method : This method return the index position of character or sub-string if it is available or
#               method will return -1 if the sub-string/character is not available.

str_g = "Hello python is easier than java"
print(str_g.find("python"))
print(str_g.find("csharp")) # o/p -1: if this method is not able to find i will give you output as -1

print("_"*50)
############
# split method: This method split the string with given delimiters or substring and return the list of words.

str_p = "Python#Programming#Is#Easy#To#Learn"
# split the string with #
result = str_p.split("#")
print("Split result: ", result)
# split with space
str_q = "Hello i know java python and csharp"
result_1 = str_q.split(" ")
print(result_1)


print("_"*50)
############
# strip method : This method helps to remove trailing spaces from given string.
# Trailing space means, spaces that are available in the beginning and end of string.
str_w = "       Pankaj Prasad       "
result_3 = str_w.strip()
print(result_3)
# remove right space
print(str_w.lstrip())
#remove right space
print(str_w.rstrip())

print("_"*50)
###################################################
# join() method : This help to join string with any word/character/number/special character
str_r = "Pankaj"
result_4 = "_".join(str_r)
print(result_4)

print("_"*50)
##########################
# isnumeric method : This method check the given string only contains numbers
str_t = "1312312312"
str_y = "12312312 p"
str_u = "Darshika"
print(str_t.isnumeric())
print(str_y.isnumeric())

#isalpha : This method check the target string contains only alhabates.
print(str_t.isalpha())
print(str_u.isalpha())

# isalnum : This method check the given string contains alphanumeric value
str_p = "Python123"
str_q = "Hello 345"
str_q1 = ""
print(str_p.isalnum(), "ppppp") # this method is for alphanumeric
print(str_q.isalnum())

#isspace : This method return true if string only contains space.
str_x = "   "
str_y = "N E H A"
print(str_x.isspace())
print(str_y.isspace())

# Count space without using count method
str_11 = "Hello my name is pankaj"
space_count = 0
for char in str_11:
    if char.isspace():
        space_count += 1
    else:
        continue
print("No of space in string", space_count)


# isDigit Method: This method is used to check given string only contains digit or not
str_r = "Pankaj12345"
str_r1 = "12345"
str_r2 = "12345qwqwqw"
print(str_r.isdigit())
print(str_r1.isdigit())
print(str_r2.isdigit())

# Write a python program to replace the word today with tomorrow
str_t = "lets learn python Today"
result = ""
word1 = "Today"
word2 = "Tomorrow"
word_list = str_t.split()
print(word_list)
for word in word_list:
    print(word)
    if word == word1:
        result = result + word2 + " "
    else:
        result = result + word + " "
print(result)

print("_"*60)
word_list1 = ['lets', 'learn', 'python', 'Today']
word_list1.insert(2, '2025')
print(word_list1)

########################################################
str_22 = "Prasad"
result22 = "*".join(str_22)
print(result22)
########################################################
str_21 = "Python is fun to learn"
updated_value = "&^@*&$#^!@*&".join(str_21)
print(updated_value)

org_password = updated_value.replace("&^@*&$#^!@*&", "")
print(org_password)

########################################################
print("_"*70)












