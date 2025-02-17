str6 = 'WqRtoolsta'
temp = ''
# for i in range(len(str6)):
#     for char in str6:
#         if char == str6[i] and char not in temp:
#             print((char, i))
#             temp += char
#     break


# Programs : 100
# flag = 0
# for i in range(len(str6)):
#     for j in range(i+1, len(str6)):
#         if str6[i] == str6[j]:
#             print((i, str6[i]))
#             flag += 1
#             break
#     if flag != 0:
#         break



# #Input string
# str1 = "Wqatools"
#
# for i in range(len(str1)):
#     for j in range(i+1,len(str1)):
#         if str1[i] == str1[j]:
#             print(f"({str1[i]},{str1.index(str1[i])})")
#     break
#


# 102). Write a program to remove repeated characters in a string and replace it with a single letter using python.
# Input = ‘aabbccdd’
# Output = ‘cabd’

str5 = 'aabbccdddddddaaaaaafgffffff'
# strB = set(str5)
# print("String after removing repeated characters in string is: ", str(strB))
# print("_"*70)
"""
output = ""
for char in str5:
    if char not in output:
        output += char
    else:
        continue

print("Output :", output)
"""


# 8). Print most simultaneously repeated characters in the input string.
str1="Hello how arrrrrrre youuuu"
max_count=0
max_char=""
for i in range(0, len(str1)-1):
    # if i==len(str1)-1:
    #     break
    # else:
    if str1[i] != str1[i+1]:
        temp=1
        continue
    else:
        temp=temp+1
        if temp>max_count:
            max_count=temp
            max_char=str1[i]

print("The most simultaneously repeated character is:",max_char)
print("The count of most simultaneously repeated character is:",max_count)
