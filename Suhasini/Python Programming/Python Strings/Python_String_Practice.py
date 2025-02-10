str1 = "Python"
print(str1, type(str1))

# String indexing:
"""
 0 1 2 3 4 5
 P y t h o n
-6-5-4-3-2-1

"""

print(str1[2])      # t
print(str1[-4])     # t

##### String Formatting  #####

name = "Suhasini"
age = 33
city = "Bellary"
# Expected output: Hello My name is Suhasini and age is 33 and I am living in Bellary

# 1) String Concatenation
print("String concatenation:")
result1 = "Hello My name is "+name+" and age is "+str(age)+" and I am living in "+city
print(result1)
print("_"*50)

# 2) String Format Method:
print("Using format():")
result2 = "Hello My name is {} and age is {} and I am living in {}".format(name,age,city)
print(result2)
print("_"*50)

#  3) f-string Formatting:
print("Using f-string Formatting:")
result3 = f"Hello My name is {name} and age is {age} and I am living in {city}"
print(result3)
print("_"*50)


####### Raw string conversion #############
# When we add r before the double quotes then entire string will convert into raw string.
# all special character property won't work e.g. \n or \t
# \t : for adding tab space in string
# \n : Adding next line output

print("############# Raw string conversion ###############")

str2 = "Hello good \t morning, {name} we are learning \n \n Python Programming, its \t very  \n easy to \t learn"
print("Initial string is: \n",str2)
result4 = r"Hello good \t morning, {name} we are learning \n \n Python Programming, its \t very  \n easy to \t learn"
print("Result is: \n",result4)
print("_"*50)


############################ Slicing in the string #######################

# Rule1 :  str[start index : end index]
# In this rule sub string will include start index value and exclude end index value
# Output will always consider the string value from left to right
# It can contain both positive and negative index values

print("######### String Slicing ###########")
str3 = "Programming"
# [+ve:+ve]
print("When : # [+ve:+ve] indexing")
print(str3[2:7])    # ogram
print(str3[0:5])    # Progr

# If we try to get value from right to left then it will return blank output
print(str3[7:3])    # Blank output

# [+ve, -ve]
print("When : # [+ve:-ve] indexing")
print(str3[1:-2])   # rogrammi
print(str3[1:-1])   # rogrammin
print()

# [-ve : +ve]
print("When : # [-ve:+ve] indexing")
str4 = "Good Morning"
print(str4[-11:8])      # ood Mor
print()

# [-ve:-ve]
print("When : # [-ve:-ve] indexing")
print(str4[-9:-2]) # d Morni
print("_"*50)


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
# Rule 2: str[ : end index]
# Default initial index will be zero

str5 = "Programming"

print(str5[:6]) # Progra
print(str5[:-3]) # Programm
print(str5[:-1]) # Programmin
print(str5[:]) # Programming
print(str5[:0]) # blank

print("_"*50)

#######################
# Rule 3 : str [start index :]
# Default end index would be end of the string

str6 = "Good Evening"




