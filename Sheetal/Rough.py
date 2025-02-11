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



