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
# Homework
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
