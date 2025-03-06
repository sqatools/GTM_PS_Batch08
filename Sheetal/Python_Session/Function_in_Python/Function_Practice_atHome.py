# from Sheetal.Python_Session.List_Practice.List_Classwork import in_list_1
#
#
# def add_word(w1, w2) -> str:
#     return ((w1) + (w2)), ((w2) * (w1)), ((w2) // (w1)), ((w2) - (w1))
#
#
# r1, r2, r3, r4 = add_word(20, 30)
#
# print("Result", r1)
# print("Result", r2)
# print("Result", r3)
# print("Result", r4)
#
#
# # Q2 : replace the specific word in file
# def replace_word_from_file(filepath, word1, word2):
#     # with open(filepath, "r") as file:
#     #     file_data = file.read()
#     #     # content = file.read()
#     #     print(file_data)
#     try:
#         with open(filepath, "r") as file:
#             file_data = file.read()
#             print(file_data)
#     except FileNotFoundError:
#         print("The file was not found.")
#
#     updated_content = file_data.replace(word1, word2)
#
#     with open(filepath, "w") as file:
#         file1 = file.write(updated_content)
#
#         return file1
#     print(file1)
#
#
# replace_word_from_file("D:/PythonAutomation/GTM_PS_Batch08/Sheetal/Python_Session/File_Handling/read_data.txt", "Python", "JAVA")

print("""Given a list of non-negative numbers and a target integer k,
,check if the array has a continuous subarray of size at least 2 that sums up to k
""")

in_list_1 = [23, 2,4, 6, 7]
k=6
count =0

for i in range(0, len(in_list_1)):
    if in_list_1[i] < k:
        count += in_list_1[i]
        j = i+1
        while count < k:
            count += in_list_1[j]
            j += 1
            if count == k:
                print("True")
                break
            else:
                count = 0
    else:
        continue


#Example 1:


#
# Output: True
#
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

