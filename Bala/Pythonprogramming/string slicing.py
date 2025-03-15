# ######### Practice program 1 ##########
# str1="slicing technique in python"
# print(str1[0:])
#
#
# ######### Practice program 2 ##########
# str1="slicing technique in python"
# print(str1[0:7:2])
#
# ######### Practice program 3 ##########
# b = "Hello, World!"
# print(b[:5])
#
# ######### Practice program 4 ##########
#
# b = "Hello, World!"
# print(b[2:])
#
# ######### Practice program 5 ########## Negative indexing
# x = "Hello, World!"
# print(x[-5:-2])
#
# ######## find longest string in the list######
# #input string
string = ["i", "am", "learning", "python"]
temp = 0

for word in string:
    y = len(word)
    if y > temp:
        temp = y

#Printing output
print(temp)




#Input string
string1 = "Sqatools"

#printing output
print(string1 [-2:]*4)


Reverse a string if its length is multiple of 4
string = "sqatools"

if len(string) % 4 == 0:
    print(string[::-1])

##########Count occurrences of a substring in a string.
string = "sqatoolspythonspy"
sub = "spy"

#Printng output
string.count("spy")

######The passed letter is a vowel or consonant
a="shjsiuekeslou"
vowels= 'a','i','e','o',u'
for vowels in a
    print(vowels)

####Longest and smallest word in the input string

string = "we are learning python"
list1 = string.split(" ")

#printing output
print("Longest word: ", max(list1, key = len))
print("Smallest word: ", min(list1, key = len))





