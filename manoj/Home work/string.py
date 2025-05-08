#  Longest and smallest word in the input string

string = "Iam learning python"
list1 = string.split(" ")


print("Longest word: ", max(list1, key = len))
print("Smallest word: ", min(list1, key = len))

# Longest word:  learning
# Smallest word:  Iam

# write a program Longest and smallest word in the input string

string = "we are learning python"
list1 = string.split(" ")
print("Longest word: ", max(list1, key = len)) # learning
print("Smallest word: ", min(list1, key = len)) # we


# write a program Get the first 4 characters of a string

string = "Sqatools"
print(string[:4]) # sqat


# write a program Get the first 7 characters of a string

string = "manojkumar"
print(string[:7]) #manojku

# write a program Print the mirror image of string.

string = "jaini manoj kumar"
print(string[::-1]) # ramuk jonam iniaj

# write a program Find duplicate characters in a string

string = "manojkumar"
list1 = []
for char in string:
  if string.count(char)>1:
    list1.append(char)

print(set(list1))
# {'a', 'm' }

# write a program Split a string on last occurrence of delimiter.

str1 = "m,a,n,o,j,k,u,m,a,r"
print(str1.rsplit(',',1))
# ['m,a,n,o,j,k,u,m,a', 'r']

# write a program Add two strings as they are numbers

n1 = 8
n2 = 1
result = int(n1)+int(n2)
print(result) # 9

# write a program subtract two strings as they are numbers

n1 = 8
n2 = 1
result = int(n1)-int(n2)
print(result) # 7


# write a program multiply two strings as they are numbers

n1 = 8
n2 = 1
result = int(n1)*int(n2)
print(result) # 8


# write a program division of two strings as they are numbers

n1 = 8
n2 = 2
result = int(n1)//int(n2)
print(result) # 4


# write a program to Print characters at even places in a string.
string = "abcd"
for i in range(len(string)):
  if i%2 == 0:
    print(string[i], end= "")
# ac

# write a program Combine two strings into one.
string1 = "manoj"
string2 = "jaini"
print(string1 + string2)
# manojjaini

# # write a program Calculate the length of string
string = "empowering over 300 million lives"
print(len(string))
# 33

# write a program Re-arrange the string

string = "India plays against Pakistan"
List2 = string.split(" ")
List2.reverse()
print(" ".join(List2))
# pakistan against plays India
print("_"*50)









str1 = " hello we are learning python"
print(set(str1)) # {'a', 'h', 'n', 'p', 'o', 't', 'l', 'g', 'r', 'e', ' ', 'w', 'i', 'y'}
vowels = 'aeiou'
# {'t', ' ', 'i', 'e', 'r', 'p', 'l', 'n', 'h', 'w', 'a', 'o', 'y', 'g'}