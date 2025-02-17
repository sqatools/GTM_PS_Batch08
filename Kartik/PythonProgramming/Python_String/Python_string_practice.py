str1 = "PythonisEasy"


print(str1, type(str1))

# read string with positive and negative  indexing

"""
 0   1  2 3 4 5 6 7 8 9 10 11
 P   y  t h o n i s E a s   y
-12-11-10-9-8-7-6-5-4-3-2  -1

"""
print(str1[8]) # E

print(str1[-11]) # y


###### String Formatting ###############

name = 'Kartik'
age = 28
city = " Surat"

# Hello My name is kartik and age is 28, and I am living in surat


# 1) String Concatenation
"""
result1 = "My name is " + name + " and age is " + age  + " and i living in " +city 
# in age TypeError: can only concatenate str (not "int") to str
"""
result1 = "My name is " + name + " and age is " + str(age) + " and i living in " + city
print(result1)

# 2) String Formatting

result2 = "Hello my name is {} and age is {} and i living in {}".format(name, age, city)
print(result2)


# 3) F String Formatting
result3 = f"Hello my name is {name} and age is {age} and i living in {city}"
print(result3)

print('_' * 50)
# ---------------Raw String Conversion -----------------------


str2 = " Hello Good morning.\twe are learning Python  \n programming .\n \n it is very easy to learn"
str3 = r" Hello Good morning.\twe are learning Python  \n programming .\n \n it is very easy to learn"

print(str2)

print(str3)
"""
Note : \t = for adding tab spaces in string
       \n = adding next line output
Note : when we add r before the double quote (") then entire string will convert in to raw string.
       All Special character properties won't work e.g \t and \n
    
"""

print('_' * 50)
# -----------Slicing in the String -----------------------

"""

Rules 1 : str [start index : End index]
         - sub string will include start index value and exclude end index value.
        - output will always consider the string value from left to right ( Left --> Right)
        - It can contain both positive and negative index values.

"""

print('_' * 50)
str_a = 'Transaction'
"""
 (1) - [ +ve :+ve ] 
"""
print(str_a[2:7])

print('_' * 50)
"""
 print(str_a[7:2])      # as per rules right to left is not possible ,it gives blank output
 
                        if we try to get values from right to left then it will return blank output
 
 """
print(str_a[0:9])
print('_' * 50)
"""
 (2) - [ +ve :-ve ] 
"""
print(str_a[2:-2])
print('_' * 50)
print(str_a[1:-1])

print('_' * 50)
"""
 (3) - [ -ve :+ve ] 
"""
str_b = "Python programming"
print(str_b[-9:12])

print('_' * 50)
"""
 (4) - [ -ve :-ve ] 
"""
print(str_b[-13: -3])

# --- Home work --
str_c = "Learning Python"
str_d = 'India is best Country'

print('_' * 50)
"""
Q-1 Read only "Learning"
"""
print(str_c[0:8])  # Learning
print(str_d[0:8])
"""
Q-2 Read only First Character and last character "Ln"
"""
str_1 = (str_c[0])
# print(str_1)
str_2 = (str_c[-1])
# print(str_2)
output = "" + str_1 + "" + str_2
print(output)  # Ln
output1 = f"{str_1}{str_2}"
print(output1)  # Ln

# print(str_c[0],str_c[-1])

"""
Q-3 Read  All character except First character and last character and repeat 2 times "earning Pythoearning Pytho" 
"""
print((str_c[1:-1]) * 2)
"""
Q-4 Read  All character except First character and last character and repeat 2 times "earning Pythoearning Pytho" 
"""
str_cfc = str(str_c[0])
# print(str_cfc)
str_clc = str(str_c[-1])
# print(str_clc)

final_str1 = "" + str_cfc + "" + str_c + "" + str_clc

print(final_str1)

# print((str_c[1:-1])*2) # LLearning Pythonn

print("_"*50)
#######-------
"""
Rules 2 : str [ : End index]
        - Default initial index will be zero
"""

print("_"*50)

str_b = "Programming"
print(str_b[:6])
print(str_b[:6])
print(str_b[:6])

# ######---------------------
"""
Rules 3 : str [start index : ]
        - Default end index would be end of the string.
"""
str_3 = " Good Evening"

print(str_3[5 :])

print(str_3[-9 :])

# ######---------------------
"""
Rules 4 : str [start index : End index :Step ]
        - Default end index would be end of the string.
"""
str_x = "IndiaIsBestCountry"

# [+ve:+ve:+ve]
print(str_x[2:10:1])

print(str_x[2:13:3])

print(str_x[0:17:2])


# [+ve:-ve:+ve]

print(str_x[1:-1:1])
str_len= len(str_x)
print(str_len)
print(str_x[1:len(str_x):1])
# if we don't defined the end index,default end index would be end of string
print(str_x[1::1])

# [-ve:-ve:+ve]
str_y = "PythonIsGreat"
print(str_y[-8:-1:1])

# [-ve:-ve:-ve]
print(str_y[-10:-1:-1]) # blank

print(str_y[-1:-10:-1]) # taerGsIno

print(str_y[-1:-len(str_y):-1]) #taerGsInohty

print(str_y[-1:-len(str_y)-1:-1]) # taerGsInohtyP

# ######---------------------
"""
Rules 5 : str [:end index :step ]
        - .
"""

"""
Rules 6 : str [:end index :step ]
        - .
"""
print("_"*50)
#with +ve step
str_z="WeAreLearningPython"
print(str_z[::1])
print(str_z[::2]) # WAeerigyhn
print(str_z[:8:2])
print(str_z[2::2])

#with -ve step
print("_"*50)
str_p = "LearningSlicing"
print(str_p[::-1]) # gnicilSgninraeL

print(str_p[::]) # LearningSlicing

print(str_p[:-1:]) # LearningSlicin

print(str_p[-1:len(str_p):1]) # g

print(str_p[-1::]) # g






