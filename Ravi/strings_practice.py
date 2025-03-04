# """
# 1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string
# """
#
# string_1 = input("Enter the string:")
#
# if len(string_1) < 2:
#     print("You have entered a sting which is less than 2 characters")
# else:
#     print(string_1[0:2]+string_1[-2:])
#
# print("-"*50)
#
# """
# 2). Python string program that takes a list of strings and returns the length of the longest string.
# """
# string_list = ["Hello", "my", "name", "is", "Ravi", "Dontaraju"]
# len_list = []
#
# for i in string_list:
#     len_list.append(len(i))
#
# print("The length of the longest string in the given list is:", max(len_list))
#
# print("-"*50)
#
# """
# 3). Python string program to reverse a string if it’s length is a multiple of 4.
# """
# str_3 = input("Enter the string:")
#
# if len(str_3) % 4 == 0:
#     print(str_3[::-1])
# else:
#     print("The provided string length is not divisible by 4")
#
# print("-"*50)
#
# """
# 4). Python string program to count occurrences of a substring in a string.
# Enter the string:bababababbababababababababababab
# Enter the sub string:bab
# 15
# """
# str_4 = input("Enter the string:")
# str_4_sub = input("Enter the sub string:")
# i = 0
# j = len(str_4_sub)
# count = 0
#
# while i <= (len(str_4)-len(str_4_sub)):
#     if str_4[i:j] == str_4_sub:
#         count += 1
#     i += 1
#     j += 1
#
# print(count)
# print("-"*50)
#
# """
# 5). Print most simultaneously repeated characters in the input string.
# """
# string_5 = input("Enter the string:")
# string_5_dict ={}
#
# for i in string_5:
#     if i in string_5_dict:
#         string_5_dict[i] += 1
#     else:
#         string_5_dict[i] = 1
#
# print(max(string_5_dict.values()))
#
# print("-"*50)
#
# '''
# 6). Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$”
# '''
#
# str_6 = input("Enter the string:")
# out_str = ''
#
# for i in str_6:
#    if i not in out_str:
#        out_str += i
#    else:
#        out_str += "$"
#
# print(out_str)
#
# print("-"*50)
#
# '''
# 7). Write a python program to exchange the first and last character of each word from the given string.
# Input = “Its Online Learning”
# Output = “stI enlino gearninL”
# '''
#
# str_7 =  'Its Online Learning'
# list_7 = str_7.split()
#
# for i in list_7:
#     i.replace(i[0],i[-1])
#     i.replace(i[-1],i[0])
#
# print(list_7)
#
# print("-"*50)
#
# """
# 8). Write a python to count vowels from each word in the given string show as dictionary output.
# Input = “We are Learning Python Codding”
# output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}
# """
# string= "We are Learning Python Codding"
# list1 = string.split(" ")
# vowels = "aeiou"
#
# dictionary = dict()
#
# for word in list1:
#     count = 0
#     for char in word:
#         if char in vowels:
#             count +=1
#     dictionary[word] = count
#
# print(dictionary)
#
# print("-"*50)
#
# """
# 9). Write a python to repeat vowels 3 times and consonants 2 times.
# Input = “Sqa Tools Learning”
# Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”
# """
# str9 = "Sqa Tools Learning"
# result = ""
# vowels = ["a","e","i","o","u",
#           "A","E","I","O","U"]
#
# for char in str9:
#     if char in vowels:
#         result = result + char*3
#     else:
#         result = result + char*2
#
# print(result)
# print("-"*50)
#
# """
# 10). Write a python program to get all the digits from the given string.
# Input = “””
# Sinak’s 1112 aim is to 1773 create a new generation of people who
# understand 444 that an organization’s 5324 success or failure is
# based on 555 leadership excellence and not managerial
# acumen
# “””
# Output = [1112, 5324, 1773, 5324, 555]
# """
# string10 = """"Sinak’s 1112 aim is to 1773 create a new generation of people who understand 444 that an organization’s
#         5324 success or failure is based on 555 leadership excellence and not managerial acumen"""
#
# List1 = string10.split(" ")
# List2 = []
#
# for val in List1:
#     if val.isdigit():
#         List2.append(val)
#
# print(List2)
# print("-"*50)
#
# """
# 11). Write a Python program to get all the palindrome words from the string.
# Input = “Python efe language aakaa hellolleh”
# output = [“efe”, “aakaa”, “hellolleh”]
# """
# string = "Python efe language aakaa hellolleh"
# List = string.split(" ")
# new_list = []
#
# for val in List:
#     if val == val[::-1]:
#         new_list.append(val)
#
# print(new_list)
# print("-"*50)
#
# """
# 12). Write a Python program to remove duplicate words from the string.
# Input = “John jany sabi row john sabi”
# output = “John jany sabi row”
# """
# string12 = "John jany sabi row John sabi"
# list1 = string12.split(" ")
# list2 = []
#
# for val in list1:
#     if val not in list2:
#         list2.append(val)
#
# " ".join(list2)
#
# print("-"*50)
#
# """
# 13). Write a Python program to find the smallest and largest word in a given string.
# Input = “Learning is a part of life and we strive”
# Output = “a”, “Learning”
# """
# string13 = "Learning is a part of life and we strive"
#
# print("Longest words: ",max(string13.split(" "),key=len))
# print("Smallest word: ",min(string13.split(" "),key=len))
#
# print("-"*50)
#
# """
# 14). Write a program to calculate the frequency of each character in a string.
# Input = “sqatools”
# Output = {‘s’:2, ‘q’:1, ‘a’: 1, ‘t’:1,‘o’:2, ‘l’:1, ‘s’:1}
# """
# string = "sqatools"
# dictionary = dict()
#
# for char in string:
#     dictionary[char] = string.count(char)
#
# print(dictionary)
#
# print("-"*50)
#
# """
# 15). Write a program to print characters at even places in a string.
# Input = ‘sqatools’
# Output = saol
# """
# string15 ="sqatools"
#
# for i in range(len(string15)):
#     if i%2 == 0:
#         print(string15[i], end = "")
#
# print(string15[::2])
#
# print("-"*50)
#
# """
# 16). Write a program to remove all duplicate characters from a given string in python.
# Input = ‘sqatools’
# Output = ‘sqatol’
# """
# string = "sqatools"
#
# from collections import OrderedDict
#
# "".join(OrderedDict.fromkeys(string))
#
# print("-"*50)
#
# """
# 17). Write a program to convert numeric words to numbers.
# Input = ‘five four three two one’
# Output = 54321
# """
#
# string17 = "five four three two one"
# new_str = ""
#
# for val in string17.split():
#     if val == "one":
#         new_str += "1"
#     elif val == "two":
#         new_str += "2"
#     elif val == "three":
#         new_str += "3"
#     elif val == "four":
#         new_str += "4"
#     elif val == "five":
#         new_str += "5"
#     elif val == "six":
#         new_str += "6"
#     elif val == "seven":
#         new_str += "7"
#     elif val == "eight":
#         new_str += "8"
#     elif val == "nine":
#         new_str += "9"
#     elif val == "ten":
#         new_str += "10"
#
# print(new_str)
#
# print("-"*50)
#
# """
# 19). Write a python program to sort a string
# Input = ‘xyabkmp’
# Output = ‘abkmpxy’
# """
# string19="xyabkmp"
#
# print("".join(sorted(string19)))
#
# print("-"*50)
#
# """
# 20). Write a python program to convert a string into a list of words.
# Input = ‘learning python is fun’
# Output = [learning, python, is, fun]
# """
# string = "learning python is fun"
# list1 = string.split(" ")
#
# print(list1)
#
# print("-"*50)
