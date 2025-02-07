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


