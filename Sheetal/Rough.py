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
#
# print("Q5: write a python to calculate total bill and update the inventory from given")
# # {'FruitName': [price, inventory]}
#
# fruits_details = {'Banana': [10, 100], 'watermelon': [60, 500], 'mango': [70, 250],
#                   'Apple': [50, 100], 'lichi': [20, 300]}
#
# fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 75, 'mango': 25}
# total_bill = 0
#
# for fruit,quant in fruit_purchase.items():
#     price_per_unit = fruits_details[fruit][0]
#     total_bill = total_bill + price_per_unit * quant
#     fruits_details[fruit][1] = fruits_details[fruit][1] - quant
# for fruit, details in fruits_details.items():
#     print({f"{fruit} : {details[1]}"})
#
#
# print(dir(set))
# print("WAP to remove all duplicate vowels from the string")
# srt11 = "Hello we are Learning Python"
# set_vol = "aeiouAEIOU"
# set3 = ""
# set4 = ""
#
# for vowel in srt11:
#     if vowel in set_vol and vowel not in set3:
#         set3 = set3 + vowel
#     elif vowel not in set_vol:
#         set4 = set4 + vowel
#     else:
#         continue
#
# print(set4)
# output = ''
# for char in str1:
#     if (char in vowels ) and (char not in output):
#         output += char
#     elif char not in vowels:
#         output += char
#     else:
#         continue
#
# print("output :", output)
# # Hello w ar lrning Pythn
#
# print("WAPP to find the difference and common values between the list")
# l1 = [1,2,3]
# l2 = [4,2,5]
#
# set1 = set(l1)
# set2 = set(l2)
#
# set3 = set2.difference(set1)
# set5 = set1.difference(set2)
#
#
# print(list(set3),"The difference")
# print(list(set5),"The difference")
#
# set4 = set1.intersection(set2)
#
# print(list(set4), " The common values")
#
# lib_b = [4,-6,8,-22,77,-99,22,-13,56]
#
# l1=[]
# l2=[]
#
# for val in range(len(lib_b)):
#     if lib_b[val] > 0:
#         l1.append(lib_b[val])
#     else:
#         l2.append(lib_b[val])
# print(f"The final list is {l1 +l2}")
#
# list1 = [2,4,3,8,6,1,1,4,3,3,7,5,1]
# k=6
#
# for i in range(len(list1)-1):
#     count = list1[i]
#     for j in range(i+1,len(list1)):
#         count+=list1[j]
#         if count == k:
#             print(f"Sum = {count}",(list1[i:j+1]))
#             break
#         elif count > k:
#             break
# #
# l1 =[]
# l2 = []
#
# for val in lib_b:
#     print(val)
#     if val > 0:
#         l1.append(val)
#     else:
#         l2.append(val)
# print(f"The final list is {l1 +l2}")
#
# def factorial(num):
#     fact = 1
#     while num > 0:
#         fact = fact * num
#         num -=1
#     return fact
#
# print(factorial(10))

# str1 = """print('hello world'*5)"""
# print(str1)
# exec(str1)
import os
import shutil
import json
#
# print(os.getpid())
# print(os.path)
# print(os.listdir())
# print(os.getcwd())
# # D:\PythonAutomation\GTM_PS_Batch08\Sheetal
# os.chdir("D:\PythonAutomation\GTM_PS_Batch08\Sheetal")
# os.mkdir("GT5")
# os.chdir("D:\Python_Selenium_Course")
# print(os.getcwd())
# os.mkdir("GT5")
# # os.makedirs(r"D:\Python_Selenium_Course\GT2\GT3")
# print(os.getcwd())
# dta_list =os.listdir(os.getcwd())
# print(dta_list,len(dta_list))
#
#
# # os.makedirs(r"D\")/
# # def read_json_data(filepath):
# #     with open(filepath,"r") as file:
# #         data = file.read()
# #         print(type(data))
# #         json_data = json.loads(data)
# #         print(json_data)
# #         return json_data
#
# # data =
#
#
# from datetime import datetime, timedelta
#
# # Get current time
# current_time = datetime.now()
#
# # Subtract 5 hours from current time
# time_minus_5_hours = datetime.now() - timedelta(hours=24)
# # (cls, days=0, seconds=0, microseconds=0,
# #                 milliseconds=0, minutes=0, hours=0, weeks=0)
#
# print(datetime.now() - timedelta(2,4,3,6,20,15))
#
# # Print the result
# print("Current time:", current_time)
# print("Time minus 5 hours:", time_minus_5_hours)
#
#
# import random
# answer1,rightanswer,score=0,0,0
# def main():
#     level1=get_level()
#     generate_integer(level1)
#
#
# def get_level():
#     while True:
#         try:
#             l1=int(input("Level: "))
#             if 1<=l1<=3:
#                 break
#             else:
#                 continue
#
#         except ValueError:
#             continue
#     return l1
#
# def generate_integer(level):
#     global answer1,score
#     for x in range(10):
#         if level==1:
#             num1=random.randint(0,9)
#             num2=random.randint(0,9)
#             print(num1, "+", num2, "=", end="")
#             try:
#                 answer1 = int(input())
#                 rightanswer = num1 + num2
#             except ValueError:
#                 print("EEE")
#                 print(num1, "+", num2, "=", end="")
#                 answer1 = int(input())
#                 for y in range(2):
#                     try:
#                         rightanswer = num1 + num2
#                         if answer1 != rightanswer and y == 1:
#                             print("EEE")
#                             print(num1, "+", num2, "=", num1 + num2)
#                         if answer1 == rightanswer:
#                             print(score)
#                             break
#                         if answer1 != rightanswer and y != 1:
#                             print("EEE")
#                             print(num1, "+", num2, "=", end="")
#                             answer1 = int(input())
#                     except ValueError:
#                         continue
#
#             else:
#                 for y in range(3):
#                     try:
#                         if answer1 != rightanswer and y == 2:
#                             print("EEE")
#                             print(num1, "+", num2, "=", num1 + num2)
#                         if answer1 == rightanswer:
#                             print(score)
#                             break
#                         if answer1 != rightanswer and y != 2:
#                             print("EEE")
#                             print(num1, "+", num2, "=", end="")
#                             answer1 = int(input())
#                     except ValueError:
#                         continue
#
#
#
#
# if __name__=="__main__":
#     main()
#

