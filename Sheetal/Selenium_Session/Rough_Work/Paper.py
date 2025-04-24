# names = "Rahul Mohit John Rahul Vaibhav John"
#
# name_counts = {}
# #
# # # Step 3: Iterate through the list of names and count their occurrences
# # for name in names:
# #     if name in name_counts:
# #         name_counts[name] += 1
# #     else:
# #         name_counts[name] = 1
# #
# # # Step 4: Find the names that appear more than once
# # duplicates = [name for name, count in name_counts.items() if count > 1]
# #
# # # Step 5: Print the result
# # print(" ".join(duplicates))
# #
# #
# #
# # # Output = “Rahul John”
#
# def print_t_word_pattern():
#     for i in range(6):
#         if i < 2:
#             print('   ****')
#         else:
#             print('      **')
#
# print_t_word_pattern()
#
# def read_largest_word(filepath):
#
#     with open(filepath, 'r') as file:
#         content = file.read()
#
#     words = content.split()
#
#     longest_word = max(words, key=len)
#
#     print("The longest word in the file is:", longest_word)
#
# read_largest_word("help.txt")


# print("18. What is the output of the following code?")
#
# def reverse():
#     num = n = 123
#     rev = 0
#     while n > 0:
#         r = n % 10
#         rev = (rev * 10) + r
#         n = n // 10
#     print("Reverse number: ", rev)
#
# reverse()
#
# 17. What is the output of the following code?

# text = "Hello World"
# # tet = text.join("-")
# # # print(text.join("-"))
# # print(tet)
# #
# #
# #
# # # 16.  What is the output of the following code?
# #
# # i = 10
# #
# # while True:
# #
# #     print(i)
# #
# #     i - = 3
# #
# #     if i == 1:
# #
# #         break

# list1 = [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]
#
# index_list = [0, 3, 5, 6]
#
# new_list = []
#
# for value in index_list:
#     new_list.append(list1[value])
#
# print(new_list)

# my_dict = {'grapes': 2, 'banana': 3, 'blueberry': 4}
#
# for key in my_dict:
#
#     print(key)

# for i in range(1, 6):
#
#        if i == 3:
#
#            continue
#
#        print(i)



# x = 5
#
# if x > 3:
#
#     if x < 7:
#
#         print("A")
#
#     elif x < 10:
#
#         print("B")
#
# elif x < 7:
#
#     print("C")
#
# else:
#
#     print("D")

#
# x = 10
#
# if x > 5:
#     print("A")
#
# if x > 7:
#     print("B")
#
# if x > 15:
#
#     print("C")

# else:
#
#     print("D")
#
# class MyClass:
#     def __init__(self):
#         self.__private_var = 25
#
#
#     def __private_method(self):
#         print("Private method")
#
#
#     def public_method(self):
#         print("Public method")
#
#         self.__private_method()
#
#
#     # Create an object of the class
#
# obj = MyClass()
#
# # Access public method and variable
#
# obj.public_method()
#
# print(obj._MyClass__private_var)


# dict1 = { 'x': 10, 'y': 20, 'c': 50, 'f': 44 }
# dict2 = { 'x': 60, 'c': 25, 'y': 56 }
#
# # Create a dictionary with only common keys, summing their values
# result = { key: dict1[key] + dict2[key] for key in dict1 if key in dict2 }
#
# print("Output:", result)




# Dict1 = {'x': 10, 'y': 20, 'c': 50, 'f': 44}
# Dict2 = {'x': 60, 'c': 25, 'y': 56}
#
# result_dict = {}
#
# for key in Dict1:
#     if key in Dict2:
#         result_dict[key] = Dict1[key] + Dict2[key]
#     else:
#         result_dict[key] = Dict1[key]
# for key in Dict2:
#     if key not in Dict1:
#         result_dict[key] = Dict2[key]
#
# print("Resulting Dictionary:", result_dict)


# def find_duplicates(input_str):
#     words = input_str.split()
#     duplicates = []
#     seen = set()
#
#     for word in words:
#         if word in seen and word not in duplicates:
#             duplicates.append(word)
#         else:
#             seen.add(word)
#
#     return ' '.join(duplicates)
#
# # Input string
# str1 = "Rahul Mohit John Rahul Vaibhav John"
#
# # Result
# Output1 = find_duplicates(str1)
# print("Output:", output)


# rows = 5
#
# for i in range(rows):
#     if i == 0:
#         print("*" * rows)
#     else:
#         print(" " * (rows // 2) + "*")

# def rearrange_list(nums):
#     positives = [x for x in nums if x >= 0]
#     negatives = [x for x in nums if x < 0]
#     return positives + negatives
#
# # Input list
# input_list = [2, -16, 6, 44, -71, 18, -11, -1]
#
# # Rearranged output
# output_list = rearrange_list(input_list)
# print("Output:", output_list)
# Output: [2, 6, 44, 18, -16, -71, -11, -1]


# def list_arrange(nums):
#     positive = []
#     negative = []
#
#     for x in nums:
#         if x >= 0:
#             positive.append(x)
#         else:
#             negative.append(x)
#
#     return positive + negative
#
# # Input list
# input_list = [2, -16, 6, 44, -71, 18, -11, -1]
#
# output_list = list_arrange(input_list)
# print("Output:", output_list)

#
# rows = 5
#
# for i in range(rows):
#     if i == 0:
#         print("*" * rows)
#     else:
#         print(" " * (rows // 2) + "**")

print("1. Write a python program to find the duplicate names from given string.")

str1 = "Rahul Mohit John Rahul Vaibhav John"

Output = "Rahul John"

def find_duplicates(input_str):
    words = input_str.split()
    duplicates = []
    seen = set()

    for word in words:
        if word in seen and word not in duplicates:
            duplicates.append(word)
        else:
            seen.add(word)

    return ' '.join(duplicates)


# Input string
str1 = "Rahul Mohit John Rahul Vaibhav John"

# Output
output = find_duplicates(str1)
print("Output:", output)

print("2.Python file program to find the longest word in a file.")

# "Note: Create a file and add some content and read the file content and find out The longest word from content."
def read_largest_word(filepath):
    with open(filepath, 'r') as file:
        content = file.read()

    words = content.split()

    longest_word = max(words, key=len)

    print("The longest word in the file is:", longest_word)


read_largest_word("help.txt")

print(" 3.Write a python Program to print the T word pattern with stars." )

    # ** ** ** **
    # ** ** ** **
    #     **
    #     **
    #     **
    #     **

rows = 5

for i in range(rows):
    if i == 0:
        print("*" * rows)
    else:
        print(" " * (rows // 2) + "**")
print("4.  Write Python Program to move all positive number on left side and negative values on right side.")

Input: [2, -16, 6, 44, -71, 18, -11, -1]

# Output: [2, 6, 44, 18, -16, -71, -11, -1]

def list_arrange(nums):
    positive = []
    negative = []

    for x in nums:
        if x >= 0:
            positive.append(x)
        else:
            negative.append(x)

    return positive + negative


    # Input list
    input_list = [2, -16, 6, 44, -71, 18, -11, -1]

    output_list = list_arrange(input_list)
    print("Output:", output_list)
print("5.Python Dictionary program to add two dictionaries if the keys are the same then add their value.")
Dict1 = { 'x':10, 'y':20, 'c':50, 'f':44}

Dict2 = {'x':60,'c':25,'y':56}

Output = {'x': 70, 'c': 75, 'y': 76}


print("6. What is the output of the following code?")
x = 10

if x > 5:
    print("A")

if x > 7:
    print("B")

if x > 15:

    print("C")

else:

    print("D")

# a) A B C D
# b) A
# B
# D
# c) A
# D
# d) B
# D
print("7. What is the output of the following code?")

x = 5

if x > 3:
    if x < 7:

        print("A")

    elif x < 10:

        print("B")

elif x < 7:

    print("C")

# else:
#
#     print("D")
#
# # a) A
# # b) B
# # c) C
# # d) D
# print("8.What is the output of the following code?")
#
#
# for i in range(1, 6):
#     if i == 3:
#
#         continue
#
#     print(i)
#
#
# # a) 1
# # 2
# # 4
# # 5
# # b 1
# # 2
# # 3
# # 4
# # 5
# # c 1
# # 2
# # 3
# # d) 1
# # 2
# # 4
# # 9.
# print("What is the
# output
# of
# the
# following
# code?
#
# my_dict = {'grapes': 2, 'banana': 3, 'blueberry': 4}
#
# for key in my_dict:
#     print(key)
#
#     *
#     a) 0
# 1
# 2
# 3
# b) 1
# 2
# 3
# c) grapes
# banana
# blueberry
# d) TypeError: ‘int’ object is not iterable
# 10.
# Which
# method is used
# to
# convert
# an
# integer
# to
# a
# string in Python?
#
# *
# a) int_to_string()
# b) convert_to_string()
# c) str()
# d) to_string()
# 11.
# Which
# method is used
# to
# check if a
# string
# contains
# only
# lowercase
# characters?
#
# *
# """a) islower()
# b) islowercase()
# c) islowerchar()
# d) islc()"""
# 12.
# What is the
# output
# of
# the
# following
# code?
#
#
#
# text = “Hello
# World”
#
# print(text.join(“-“))
#
# *
# a) Hello
# World!
# b) Hello - World!
# c) H - e - l - l - o - -W - o - r - l - d"
#  Error
# 13.
# What is the
# output
# of
# the
# following
# code?
#
#
#
# string = “i # am # learning # python”
#
# list1 = string.split(” “)
#
# print(list1)
#
# *
# a) [“i”, “am”, “learning”, “python”]
# b) [“i # am # learning # python”]
# c) [“i”, “am”, “learning”, “p”, “y”, “t”, “h”, “o”, “n”]
# d) [“i”, “, ”, “am”, “, ”, “learning”, “, ”, “python”]
# Option
# 5
# 14.
# What is the
# output
# of
# the
# following
# code?
#
#
#
# list1 = [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]
#
# index_list = [0, 3, 5, 6]
#
# new_list = []
#
# for value in index_list:
#     new_list.append(list1[value])
#
# print(new_list)
#
# *
# a) [2, 7, 1, 5]
# b) [3, 4, 1, 6]
# c) [2, 4, 1, 5]
# d) [7, 3, 1, 6]
# 15.
# What is the
# output
# of
# the
# following
# code?
#
#
#
# list1 = [(“mike”, 1), (“sarah”, 20), (“jim”, 16)]
#
# dict1 = {}
#
# for val in list1:
#     dict1[val[0]] = val[1]
#
# print(dict1)
#
# *
# a) {‘mike’: 1, ‘sarah’: 20, ‘jim’: 16}
# b) {‘mike’: 1, ‘sarah’: 20, ‘jim’: 16, ‘val’: 1, ‘val’: 20, ‘val’: 16}
# c) {‘mike’: 1, ‘sarah’: 20, ‘jim’: 16, 0: ‘mike’, 1: ‘sarah’, 2: ‘jim’}
# d) Error
# 16.
# What is the
# output
# of
# the
# following
# code?
#
# i = 0
#
# while i < 15:
#     print(i)
#
#     i += 3
#
# *
# a) 0
# 1
# 2
# 3
# 4
# b) 1
# 2
# 3
# 4
# 5
# c) 0
# 3
# 6
# 9
# 12
# d) 3
# 6
# 9
# 12
# 15
# Option
# 5
# 16.
# What is the
# output
# of
# the
# following
# code?
#
# i = 10
#
# while True:
#
#     print(i)
#
#     i - = 3
#
#     if i == 1:
#         break
#
# *
# a) 5
# 4
# 3
# 2
# 1
# b) 1
# 2
# 3
# 4
# 5
# c) 10, 7, 4, 1
# d) 10, 7, 4
# 17.
# What is the
# output
# of
# the
# following
# code?
#
# text = “Hello
# World”
# print(text.join(“-“))
#
# *
# a) Hello
# World!
# b) Hello - World!
# c) H - e - l - l - o - -W - o - r - l - d!
# d) Error
# Option
# 5
# 18.
# What is the
# output
# of
# the
# following
# code?
#
# def reverse():
#     num = n = 123
#     rev = 0
#     while n > 0:
#         r = n % 10
#         rev = (rev * 10) + r
#         n = n // 10
#     print(“Reverse
#     number: “, rev)
#
#     reverse()
#
#     *
#     a) Reverse
#     number: 123
#     b) Reverse
#     number: 321
#     c) Reverse
#     number: 312
#     d) Reverse
#     number: 132
#     19.
#     What is the
#     output
#     of
#     the
#     following
#     code?
#
#     def __init__(self):
#         self.__private_var = 25
#
#     def __private_method(self):
#         print("Private method")
#
#     def public_method(self):
#         print("Public method")
#
#         self.__private_method()
#
#     # Create an object of the class
#
#     obj = MyClass()
#
#     # Access public method and variable
#
#     obj.public_method()
#
#     print(obj._MyClass__private_var)
#
#     *
#     a) “Public
#     method” followed
#     by
#     an
#     error
#     b) “Public
#     method” followed
#     by “Private
#     method” and then
#     25
#     c) “Private
#     method” followed
#     by
#     an
#     error
#     d) “Private
#     method” followed
#     by “Public
#     method” and then
#     25
#
# dict1 = { 'x': 10, 'y': 20, 'c': 50, 'f': 44 }
# dict2 = { 'x': 60, 'c': 25, 'y': 56 }
#
# # Create a dictionary with only common keys, summing their values
# result = { key: dict1[key] + dict2[key] for key in dict1 if key in dict2 }
#
# print("Output:", result)