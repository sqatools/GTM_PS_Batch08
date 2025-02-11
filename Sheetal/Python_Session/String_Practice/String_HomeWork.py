from colorama import *

print(Fore.MAGENTA+"WAP to get smallest word from given string"+Style.RESET_ALL)
str11= "WAP to get smallest word from given string"

str11_list = str11.split()
small_len = 9
small_word =""

for char in str11_list:
    char_len = len(char)
    print(char, " : ", char_len)
    if char_len < small_len:
        small_len = char_len
        small_word = char

print("The smallest length word in string is of length : ","\033[4m" + Fore.BLUE+ str(small_len) +Style.RESET_ALL, "of string ","\033[4m" + Fore.BLUE+ small_word +Style.RESET_ALL)


print("_"*40)
print(Fore.GREEN+ "WAP to get count of all vowels from the given string"+Style.RESET_ALL)
str1 = "We are Learning Python Program"
str_vowel = "aeiouAEIOU"

Count1 = {v: 0 for v in str_vowel}
print(Count1)

for i in str1:
    if i in Count1:
        Count1[i] += 1

for vowel1, count in Count1.items():
    if count > 0:
        print(f"The count of '{vowel1}': {count} times")


print("_"*40)
print(Fore.BLUE+ "WAP to convert all vowels upper to lower and lower to upper"+Style.RESET_ALL)
str_b = "We Are LEarnIng Python ProgramIng"
str_vowel = "aeiouAEIOU"

Count1 = {v: 0 for v in str_vowel}
print(Count1)

for i in str_b:
    if i in Count1:
        Count1[i] += 1
print(Count1)

result=""
# result = "".join([char.lower() if char in "AEIOU" else char.upper() if char in "aeiou" else char for char in str_b])
for char in str_b:
    if char in "AEIOU":
        result += char.lower()
    elif char in "aeiou":
        result += char.upper()
    else:
        result += char

print("Original String  :", str_b)
print("Converted String :", result)
