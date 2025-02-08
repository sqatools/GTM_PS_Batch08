# 3rd Feb'2025

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

#5th Feb'2025


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








