"""
# Mode to access the file:-

# read mode(r): we can open file in read mode to read its content.
# write mode(w): -> we can open file in write mode, if we want to update the content of the file.
                 -> when we update the content in write mode, old content will be removed.
# append mode(a): -> we can open file in append mode to update the content of the file.
                  -> append mode will add new content to file at the end of file.
                  -> append mode keep the original content and add updated content as well.

# Note : function to open file
file = open(filepath, mode)
"""

# import os
# print("Current working directory:", os.getcwd())

import os

print("Full path to the file:", os.path.abspath("sample.txt"))


# red content from file
def read_file_content(filepath):
    file_obj = open(filepath, "r")
    data = file_obj.read()
    print("Is file readable: ", file_obj.readable())  # Is file readable:  True
    print("File Name: ", file_obj.name)  # File Name:  sample.txt
    print("is file closed : ", file_obj.closed)
    print(data)
    print("for closing file  : ", file_obj.close())
    print("is file closed : ", file_obj.closed)


read_file_content("sample.txt")


# read_file_content("D:\\Python_Automation\\GTM_PS_Batch08\\Pankaj\\File_Handeling\\sample.txt")


########## write content ###############
def write_content_file(filepath, new_content):
    file = open(filepath, "w")
    file.write(new_content)
    file.close()


write_content_file("sample.txt", "Adding new line to file")
