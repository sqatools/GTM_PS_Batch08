# # start_pt = ord('a')
# #
# # for i in range(1, 8):
# #     print(" " * (7 - i), end="")  # Print leading spaces
# #
# #     temp = start_pt + (i - 1)  # Start from the correct letter
# #
# #     # Print first half (descending order)
# #     for j in range(i):
# #         print(chr(temp), end="")
# #         temp -= 1
# #
# #     # Print middle character again for mirroring effect
# #     temp += 1
# #     print(chr(temp), end="")  # Middle character repeated
# #
# #     # Print second half (ascending order)
# #     for j in range(i - 1):
# #         temp += 1
# #         print(chr(temp), end="")
# #
# #     print()  # Move to the next line
# #     start_pt += 2  # Move starting letter forward
# # # str1 = "Good Morning"
# # # str_len = len(str1)
# # #
# # # for i in range(str_len):
# # #     print(i,":", str1[i])
# # #
# # #
# # # str1= "  Hello Good Morning  "
# # # print(str1.lstrip().rstrip().lower().upper().replace(" ", "_").split("_"))
# # # # ['HELLO', 'GOOD', 'MORNING']
# # #
# #
# # file = open("read_data.txt", "r")
# # data = file.read()
# # print(data)
# # word_list = data.split(" ")
# # for word in word_list:
# #     if word.isdigit():
# #         print(word)
# #
# #
# # dict1 = {'Name': 'Virat', 'Age': 35}
# # for val in dict1.items():
# #     print(val[0], val[1])
# #
# # str6 = 'sqatools'
# # temp = ''
# # for i in range (len(str6)):
# #     for char in str6:
# #         if char == str6[i]:
# #             # if char == str6[i] and char not in temp:
# #             print((char, i))
# #             # temp +=char
# #
#
# str1 = "sqltools"
# temp = 0
# for char in range(len(str1)):
#     for comp in range(char+1,len(str1)):
#         if str1[comp] == str1[char]:
#             temp =1
#             print(str1[char],char, comp)
#             break
#     if temp != 0:
#         break
# # str1 = "sqatools"
# # # 100).Write a program to find the first repeated character in a string and its index.
# # Input = "sqatools"
# # # Output = (s, 0)
# # for i in range(len(str1)):
# #     for j in range(i + 1, len(str1)):
# #         if str1[i] == str1[j]:
# #             print(f"({str1[i]},{str1.index(str1[i])})")
# #     break
from Uttara.Homework.SQA_Strngprogrm import str11

print("Q5: write a python to calculate total bill and update the inventory from given")
# {'FruitName': [price, inventory]}

fruits_details = {'Banana': [10, 100], 'watermelon': [60, 500], 'mango': [70, 250],
                  'Apple': [50, 100], 'lichi': [20, 300]}

fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 75, 'mango': 25}
total_bill = 0

for fruit,quant in fruit_purchase.items():
    price_per_unit = fruits_details[fruit][0]
    total_bill = total_bill + price_per_unit * quant
    fruits_details[fruit][1] = fruits_details[fruit][1] - quant
for fruit, details in fruits_details.items():
    print({f"{fruit} : {details[1]}"})


print(dir(set))
print("WAP to remove all duplicate vowels from the string")
srt11 = "Hello we are Learning Python"
set_vol = "aeiouAEIOU"
set3 = ""
set4 = ""

for vowel in srt11:
    if vowel in set_vol and vowel not in set3:
        set3 = set3 + vowel
    elif vowel not in set_vol:
        set4 = set4 + vowel
    else:
        continue

print(set4)
output = ''
for char in str1:
    if (char in vowels ) and (char not in output):
        output += char
    elif char not in vowels:
        output += char
    else:
        continue

print("output :", output)
# Hello w ar lrning Pythn

print("WAPP to find the difference and common values between the list")
l1 = [1,2,3]
l2 = [4,2,5]

set1 = set(l1)
set2 = set(l2)

set3 = set2.difference(set1)
set5 = set1.difference(set2)


print(list(set3),"The difference")
print(list(set5),"The difference")

set4 = set1.intersection(set2)

print(list(set4), " The common values")