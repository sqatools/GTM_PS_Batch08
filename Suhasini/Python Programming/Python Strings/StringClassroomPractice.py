# 1. Program to find longest word from a statement

str1 = ("Click open Zoom workspace app on the dialog shown by your browser")
long_word = ""
long_len = 0

word_list = str1.split()
for word in word_list:
    word_len = len(word)
    print(word, word_len)

    if word_len > long_len:
        long_len = word_len
        long_word = word

print("Longest word is: ",long_word, "and it's length is: ",long_len)
print("_"*50)


# 2. write a python program to find out all the mobile numbers and email id from given string.
str2 = """
There are 9987878754 several user1@gmail.com types of automation 7787878754 frameworks, 
including 45 linear 8787878754 scripting, modular user2@facebook.com testing, 2344 data-driven, 
keyword-driven, user3@yahoo.com and hybrid 5587878754 testing. Each user4@hotmail.com type 53 has its 
own use case and advantages
"""

num = ""
email = ""
str3 = str2.split()
for word in str3:
  if word.isdigit() and len(word)==10:
      num = num + word + " "
  elif '@' in word:
      email = email + word + " "
  else:
      continue

print("The contact numbers are: ")
print(num, end=" ")
print("\nThe email ids are :")
print(email, end=" ")
print()
print("_"*80)


# write a python program to remove all duplicate words from given string
str3 = "Pramod Hema Kartik Bala Pramod Manoj Hema Kartik"
# output = "Pramod Hema Kartik Bala Manoj"

result = ''
word_list = str3.split()

for word in word_list:
    if word not in result:
        result = result + word + " "
    else:
        continue

print("Actual string: Pramod Hema Kartik Bala Pramod Manoj Hema Kartik")
print("String after removing duplicates: ",result)
print("_"*80)

# 4. write a program to get words who len is 4
str4 = "Pramod Hema Kartik Bala Pramod Manoj Hema Kartik Sita Gita Mita Rita Suvi"
res = str4.split()

print("Names with 4 letters are: ")
for word in res:
    if len(word) == 4:
        print(word)
    else:
        continue
print("_"*80)


################################# Homework questions #####################################

#Q1 : Write a python program to find smallest word from given string
"Click open Zoom workspace app on the dialog shown by your browser"

str1 = "Click open Zoom workspace app on the dialog shown by your browser"
res = str1.split()
shortWord = res[0]
shortLen = ''

for word in res:
    if len(word) < len(shortWord):
        shortWord = word
        shortLen = len(word)
    else:
        continue
print("Shortest word is: ",shortWord, "and its length is ",shortLen)
print("_"*80)


# Q2 :  write a python program to get count all vowels from given string
str_a = "Hello GoOd MOrnIong"

count = 0
for char in str_a:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A'
            or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        count += 1
    else:
        continue

print("Number of Vowels in string are: ",count)
print("_"*80)


# Q3 :  Write a python program to Convert all Vowels from upper to lower and lower to upper.
str_b = "We Are LEarnIng Python PrOgrammIng"

print("Actual string is: ",str_b)
print("String after converting lower case vowels to upper case and vice versa is:")
count = 0
for char in str_b:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A'
            or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        count += 1
        if char.isupper():
            char = char.lower()
            print(char, end="")
        elif char.islower():
            char = char.upper()
            print(char, end="")
        else:
            print(char, end="")
    else:
        print(char, end="")

print("\nNumber of vowels is: ",count)
print("_"*50)
