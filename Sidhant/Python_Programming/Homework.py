# 1. write a python program to get The Smallest word from given string.

str1 = "GOAL WITHOUT PLAN IS JUST A WISH "
small_len = 999999
small_word = " "
word_list = str1.split()
for word in word_list:
    exact_len = len( word )
    if exact_len < small_len:
        small_len = exact_len
        small_word = word
print( f"The smallest word is{small_word}of length:", small_len )

# Q2 :  write a python program to get count all vowels from given string
str_a = "Hello GoOd MOrnIong"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in str_a:
    if char in vowels:
        vowel_count += 1
print( vowel_count )

# Q3 :  Write a python program to Convert all Vowels from upper to lower and lower to upper.
str_a = "We Are LEarnIng Python PrOgrammIng"
vowels = "aeiouAEIOU"
Final_string = ""
for char in str_a:
    if char in vowels:
        if char.islower():
            Final_string += char.upper()
        elif char.isupper():
            Final_string += char.lower()
    else:
        Final_string += char
print(Final_string)