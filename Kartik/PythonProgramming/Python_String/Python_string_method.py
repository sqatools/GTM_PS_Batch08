print(dir(str))
"""
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
'title', 'translate', 'upper', 'zfill']
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
