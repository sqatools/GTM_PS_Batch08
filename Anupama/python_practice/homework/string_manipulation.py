str1="India is my country"
print(str1)
print(str1[4:19:1])
print(str1[2:13:2])

#**string concatination**
str1="India"
str2="is best"
concat= str1+" "+str2
print(concat)
print("-"*50)

#**slicing**
str1="Hello Friends"
slice= str1[7:]
print(slice)
print("-"*50)

#***searching the string***
str1= "i like python."
w="python"
str_len= len(str1)
print(str_len)
if w in str1:
    print("Present")
else:
    print("Not present")
print("-"*50)

#**replace the string**
str1= "i like python."
replaced_string = str1.replace("like","love")
print(replaced_string)
print("-"*50)

#*** string reverse***
str1= "India is great"
print(len(str1))
print(str1[-1:-15:-1])

#****program to  make a string pyramid***



