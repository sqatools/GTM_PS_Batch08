import os

# print("1. Program to change the directory and create new file")
# os.getcwd()
# print(os.getcwd())
# os.chdir("D:\\PythonAutomation\\GTM_PS_Batch08\\Sheetal\\Python_Session\\File_Handling\\File_Handling_Homework")
# # os.chdir("D:\\PythonAutomation\\GTM_PS_Batch08\\Sheetal\\Python_Session\\File_Handling")
# print(os.getcwd())
#
# # os.mkdir("File_Handling_Homework")
# print(os.getcwd())
# def create_file(filepath):
#     with open(filepath,"w") as file:
#         print(os.getcwd())
#         data = file.write("First Program")
#
# file_path = os.path.join(os.getcwd(), "File_Handlin_HomeWork.py")

# Call the function to create the file in the current directory
# create_file(file_path)

# print("*"*50)
#
# print("2. Program to remove the file from the specified location")

# def file_remove(filepath):
# #     os.remove(filepath)
# #
# # file_remove("File_Handling_HomeWork.py")
#
# print("3. Python Program How to read a file in reading mode.")
#
# def read_file(filepath):
#     with open(filepath,"r") as file:
#         data = file.readline()
#         print(data)
#
# file_path = os.path.join(os.getcwd(), "File_Handling_HomeWork.py")
# read_file(file_path)
#


# print("*"*50)
# print("4. Python file program to replace space by an underscore in a file.")
#
# file_path = os.path.join(os.getcwd(), "File_Handle.txt")
#
# print(file_path)
#
# def rep_space(filepath,val1,val2):
#     with open(filepath,"r") as file:
#         data = file.read()
#         final_content = data.replace(val1,val2)
#
#     with open(filepath, "w") as file:
#         file.write(final_content)
#
#
# rep_space(file_path,"_", " ")


# print("*"*50)
# print("5. Python file program to display words from a file that has less than 5 characters.")
#
# def word_find(filepath):
#     count =0
#     with open(filepath,"r") as file:
#         data = file.readlines()
#         for sentence in data:
#             words = sentence.split()
#             # print(words)
#             for word in words:
#                 if len(word) <5:
#                     data1 = "".join(word)
#                     count +=1
#                     print(data1, end = " ")
#         print("\nTotal word count = ",count)
#
#
# word_find("File_Handle.txt")

# print(" ")
# print("*" * 50)
# print("6. Python file program to remove all the lines that contain the character ‘t’ in a file and write it to another file.")
# def remove_t(filepath,filepath2):
#     data2 = ""
#     with open(filepath,"r") as file:
#         data = file.readlines()
#
#     with open(filepath2, "w") as file2, open(filepath,"w") as file3:
#         for sentences in data:
#             data1 = sentences.split()
#             for word in data1:
#                 if word.__contains__('t'):
#                     # data1.remove(word)
#                     file2.write(word + " ")
#
#                 else:
#                     file3.write("".join(word) + "\n")
#
#
# remove_t("File_Handle.txt","File_Handle2.txt")

# print("*"*50)
# print("7. Python file program to count the total number of consonants in a file.")
#
# def total_cons(filepath):
#     vowel = "aeiouAEIOU"
#     count = 0
#     with open(filepath, "r") as file:
#         data = file.readlines()
#         for sentences in data:
#             for words in sentences:
#                 if words not in vowel and words.isalpha():
#                     count +=1
#     print(f"The total number of consonants are: {count}")
#
# total_cons("File_Handle.txt")
#


# print("*"*50)
# print("8. Python file program to count the total number of vowels in a file.")
# def total_cons(filepath):
#     vowel = "aeiouAEIOU"
#     count = 0
#     with open(filepath, "r") as file:
#         data = file.readlines()
#         for sentences in data:
#             for words in sentences:
#                 if words in vowel and words.isalpha():
#                     count +=1
#     print(f"The total number of vowels are: {count}")
#
# total_cons("File_Handle.txt")



# print("*"*50)
# print("9. Python file program to read a file and display each word separated by @.")
# def total_cons(filepath):
#     data3 = ""
#     word_list = []
#     with open(filepath, "r") as file:
#         data = file.readlines()
#         for sentences in data:
#             data2 = sentences.split()
#             for word in data2:
#                 if "@" in word:
#                     word_list.append(word)
#             # words_with_at = [word for word in data2 if "@" in word]
#             # if words_with_at:
#     data3 = " ".join(word_list) + " "
#     print(f"The total number of words contain @ are: {data3}")
#
# total_cons("File_Handle.txt")
#
#
# print("*"*50)
# print("10. Python file program to read the content of the file in reverse order.")


# print("*"*50)
# print("11. Python file program to move the cursor to a specific position in a file.")
# def file_spe_pos(filepath1):
#     with open(filepath1,"r") as file1:
#         print("The default cursor position:",file1.tell())
#         file1.seek(20,0)
#         print("The updated cursor position: ",file1.tell())
#         file1.seek(20, 1)
#         print("The updated cursor position after 20 steps: ", file1.tell())
#         file1.seek(-50,2)
#         print("The updated cursor position from end of file ", file1.tell())
#
# file_spe_pos("File_Handle.txt")
#
# print("*"*50)
# print("12. Python file program to find the cursor position in a file.")
# def file_spe_pos(filepath1):
#     with open(filepath1,"r") as file1:
#         print("The default cursor position:",file1.tell())
#         file1.seek(20,0)
#         print("The updated cursor position: ",file1.tell())
#
# file_spe_pos("File_Handle.txt")
#
#
# print("*"*50)
# print("13. Python file program to count the total number of special characters in a file.")
# def file_spe_char(filepath1):
#     spe_char = ("@#$%^&*()!.")
#     count = 0
#     with open(filepath1,"r") as file1:
#         data1 = file1.readlines()
#         for num in data1:
#             for totnum in num:
#                 for t_num in totnum:
#                     if t_num in spe_char:
#                         count +=1
#     print(count)
#
# file_spe_char("File_Handle.txt")
#

# # print("*"*50)
# print("14. Python file program to count the total number of digits in a file.")
# def file_num_digit(filepath1):
#     count =0
#     with open(filepath1,"r") as file1:
#         data1 = file1.readlines()
#         for num in data1:
#             # num1 = num.split()
#             for totnum in num:
#                 for t_num in totnum:
#                     if t_num.isdigit():
#                         count +=1
#     print(count)
#
# file_num_digit("File_Handle.txt")
# #
# print("*"*50)
# print("15. Python file program to count the total number of Lowercase characters in a file.")
# def file_text_lower(filepath1):
#     count =0
#     with open(filepath1,"r") as file1:
#         data1 = file1.readlines()
#         for num in data1:
#             # num1 = num.split()
#             for totnum in num:
#                 for t_num in totnum:
#                     if t_num.islower() and t_num.isalpha():
#                         count +=1
#     print(count)
# file_text_lower("File_Handle.txt")
# #
# print("*"*50)
# print("16. Python file program to extract characters from a text file into a list.")
#
# def file_text_list(filepath1):
#     count =0
#     with open(filepath1,"r") as file1:
#         data1 = file1.readlines()
#         for num in data1:
#             num1 = num.split()
#             print(num1)
#
# file_text_list("File_Handle.txt")
#
# print("*"*50)
# print("17. Python file program to write a tuple to a file.")


# print("*"*50)
# print("18. Python file program to compare two files.")
#
# def file_compare(filepath1, filepath2):
#     with open(filepath1,"r") as file1, open(filepath2,"r") as file2:
#         data1 = file1.read()
#         data2 = file2.read()
#         if data1 == data2:
#             print("Both the files are equal")
#         else:
#             print("Files are different")
#
# file_compare("File_Handle.txt", "File_Handle2.txt")
#
# print("*"*50)
# import re
# print("19. Python file program to get a list of all domains from a file. e.g .com, .au, .in")
# def list_domain(filepath):
#     list1 = []
#     domain_pattern = r"\.[a-zA-Z]{2,6}"
#     with open(filepath,"r") as file:
#         data1 = file.readlines()
#         for data2 in data1:
#             data3 = data2.split()
#             for data4 in data3:
#                 # if data4.__contains__(".com") or data4.__contains__(".in") or data4.__contains__(".au"):
#                 # if domain_pattern in data4:
#                 domains = re.findall(domain_pattern, data4)
#                 list1.extend(domains)
#
#     print(list1)
#
# list_domain("File_Handle.txt")
#
# print("*"*50)
print("20. Python file program to get all odd and even length words in two lists.")


print("*"*50)
print("21. Python file program to generate text files with all alphabets.  e.g. A.txt , B.txt, C.txt….. Z.txt")


print("*"*50)
print("22. Python file program to consider a text file as a DB file and store all the student information in a text file.")


print("*"*50)
print("23. Python file program to copy the file’s contents to another file after converting it to uppercase.")


print("*"*50)
print("24. Python file program to get the count of a specific word in a file.")


print("*"*50)
print("25. Python file program to find the longest word in a file.")



print("*"*50)
print("26. Python file program to get the file’s first three and last three lines.")
