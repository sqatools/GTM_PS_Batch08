""""" 
1). Write a Python program to get a string made of the first and the last 2 chars from a given string. If the 
string length is less than 2, return instead of the empty string """""

str1 = input( "Enter the string1:" )
if len( str1 ) < 2:
    print( "string length is less than of two" )
else:
    print( str1[:2] + str1[-2:] )
# 2). Python string program that takes a list of strings and returns the length of the longest string.
str2 = "we are learning python for sure"
temp_length = 0
word_list = str2.split()
for word in word_list:
    word_length = len( word )
    if word_length > temp_length:
        temp_length = word_length
print( f"length of longest string is: {temp_length}" )

# 3). Python string program to get a string made of 4 copies of the last two characters of a specified string (length
# must be at least 2).
str3 = input( "Enter the string3:" )
print( str3[-2:] * 4 )

# 4). Python string program to reverse a string if it’s length is a multiple of 4.
str4 = input( "Enter the string4:" )
if len( str4 ) > 4:
    print( str4[::-1] )
else:
    print( "string length should be least of 4" )

# 5). Python string program to count occurrences of a substring in a string.
str5 = input( "Enter the string5:" )
print( str5.count( "I" ) )

# 6). Find the longest and smallest word in the input string.
str7 = "we are learnings python"
long_word = 0
largest_word = " "
smallest_word = 99999
small_word = " "
word_list = str7.split()
for word in word_list:
    word_length = len( word )

    if word_length > long_word:  # print(largest_word)
        long_word = word_length
        largest_word = word
        # print(smallest_word)
    if word_length < smallest_word:
        smallest_word = word_length
        small_word = word
print( small_word )
print( largest_word )

# 7 Python string program to test whether a passed letter is a vowel or consonant.
letter = "india got latent"
for char in letter:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print( f"{char} is vowel" )
    else:
        print( f"{char} is consonant" )

# 8. Print most simultaneously repeated characters in the input string.
str8 = "chronology"
max_count = 0
max_word = ""
for s in str8:
    word_count = str8.count( s )
    if word_count > max_count:
        max_count = word_count
        max_word = s
print( max_word )

# 9)  Write a Python program to calculate the length of a string with loop logic.
str9 = "we are learning python"
count = 0
for char in str9:
    count += 1
print( f"length of string using loop logic is: {count}" )

# 10). Write a Python program to replace the second occurrence of any char with the special character $.
str10 = "Programming"
result = " "
for char in str10:
    if char in result:
        result += "$"

    else:
        result += char

print( result )

# 11 Write a python program to get to swap the last character of a given string.
str11 = "Sidhant"
print(str11[-1]+str11[1:-1]+str11[:1])

# 12). Write a python program to exchange the first and last character of each word from the given string.
str12 = "student are learning python"
result = " "
word_list = str12.split()
for word in word_list:
    new_word = word[-1] + word[1:-1] + word[:1]  # exchange of first and last char
    result += new_word + " "  # store in result
print( result )

# 13). Write a python to count vowels from each word in the given string show as dictionary output.
str13 = "we are learning python"
vowels = "aeiou"
dictionary = dict()  # it will store key and value
split_list = str13.split()
for word in split_list:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    dictionary[word] = count
print( dictionary )

# 14 Write a python to repeat vowels 3 times and consonants 2 times.
str14 = "we are learning python"
vowels = "aeiou"
result = ""
split_list = str14.split()
for word in split_list:
    for char in word:
        if char in vowels:
            result += char * 3
        else:
            result += char * 2
print( result )

# 15 Write a python program to re-arrange the string.
str15 = "Cricket Plays Rishab"
List = str15.split( " " )
List.reverse()
print( " ".join( List ) )  # convert list into string

# 16). Write a python program to get all the digits from the given string.
str16 = """Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen"""
digit_list =str16.split()
list16 =[]
for digit in digit_list:
    if digit.isdigit():
        list16.append(digit)
print(list16)

# 17). Write a python program to replace the words “Java” with “Python” in the given string.
str17 = "JAVA is the Best Programming Language in the Market"
new_string = ""
list_str17 = str17.split()
for word in list_str17:
    if word == "JAVA":
        index = list_str17.index( word )
        list_str17[index] = "PYTHON"

print( " ".join( list_str17 ) )
# 18). Write a Python program to get all the palindrome words from the string.
str18 = "Python efe language aakaa hellolleh"
List = str18.split()
new_list = []
for word in List:
    if word == word[::-1]:
        new_list.append( word )
print( new_list )

# 19). Write a Python program to create a string with a given list of words.
str19 = ["There", "are", "Many", "Programming", "Language"]
print(" ".join(str19))

# 20). Write a Python program to remove duplicate words from the string.
str20 = "John jany sabi row john sabi"
List = str20.split()
List2 = []
for word in List:
    if word not in List2:
        List2.append( word )
print( " ".join( List2 ) )


