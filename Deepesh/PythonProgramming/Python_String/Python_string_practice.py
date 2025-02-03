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






