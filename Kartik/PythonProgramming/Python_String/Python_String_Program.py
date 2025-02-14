# write a python program to get the longest word from given string
str1 = "lick Open Zoom Workplace app on the dialog shown by your browser"
long_word = ''
long_len = 0

# get word list with split method
word_list = str1.split()
# get each word using loop
for word in word_list:
    word_len = len(word)  # get length of each word
    print(word, word_len)
    # compare word_len with long_len:
    if word_len > long_len:  # |  4 > 4 | 9 > 4 | 3 > 9
        long_len = word_len  # 4 ,9
        long_word = word  # lick, Workplace
    else:
        continue

print("longest word :", long_word, long_len)

# Home Work
# write a python program to get smallest word from given string.


print("_" * 50)
######################################################
# write a python program to find out all the mobile numbers and email id from given string.
"""
We are working on python programs
"""

str2 = """
There are 9987878754 several user1@gmail.com types of automation 7787878754 frameworks, 
including 45 linear 8787878754 scripting, modular user2@facebook.com testing, 2344 data-driven, 
keyword-driven, user3@yahoo.com and hybrid 5587878754 testing. Each user4@hotmail.com type 53 has its 
own use case and advantages
"""
# get word list using split method
word_list = str2.split()
emails = ''
mobile = ''
for word in word_list:
    # check @ in given word, to consider as email
    if "@" in word:
        print(word)
        emails = emails + word + " "
    # check word length should be 10 and only contains digits, then consider as mobile number.
    elif len(word) == 10 and word.isdigit():
        print(word)
        mobile = mobile + word + " "
    else:
        continue

print("All emails :", emails)
# user1@gmail.com user2@facebook.com user3@yahoo.com user4@hotmail.com
print("All Mobile Numbers :", mobile)
# 9987878754 7787878754 8787878754 5587878754


print("_" * 50)
#################################################
# Q : write a python program to remove all duplicate words from given string

str3 = "Promod hema kartik bala Promod manoj hema kartik"
final_str = ''
word_list = str3.split()
for word in word_list:
        if word not in final_str:
           final_str = final_str + word + " "
        else:
            continue

print("Result :", final_str)

print("_" * 50)
# write a program to get words who len is 4

for w1 in word_list:
    # if len(w1) is 4:
    #     print(w1)
    # else:
    #     continue

    if len(w1) is not 4:
        print(w1)
    else:
        continue

######################## Home Work ################
# Q1 : Write a python program to find smallest word from given string

# Q2 :  write a python program to get count all vowels from given string
str_a = "Hello GoOd MOrnIong"
# output = 7

# Q3 :  Write a python program to Convert all Vowels from upper to lower and lower to upper.
str_b = "We Are LEarnIng Python PrOgrammIng"
# output = "WE arE LeArning PythOn ProgrAmming"



