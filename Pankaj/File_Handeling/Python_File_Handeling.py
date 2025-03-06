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


# 1) way to call function if text file is inside same folder.
# read_file_content("sample.txt")

# ) way to call function if text file is outside the folder.
read_file_content("D:\\Python_Automation\\GTM_PS_Batch08\\Pankaj\\File_Handeling\\sample.txt")


# Write content to the file with write mode.
def write_content_file(filepath, new_content):
    file = open(filepath, "w")
    file.write(new_content)
    file.close()


# 1. way to write content in existing file
# write_content_file("sample.txt", "Hello writing new content from function: Test File")

# 2. if file is not present it will create new file and write the content.
# write_content_file("sample1.txt", "Hello Pankaj how are your ?")


################ Append content ################
def append_content(filename1, append_new_content):
    file = open(filename1, "a")
    file.write(append_new_content)
    file.close()


# without \n it will not add in new line
# append_content("sample1.txt", "Add new line in file via append method\n")

para = """
Selenium is an open-source, automated testing tool used to test web applications across various browsers. 
Selenium can only test web applications, unfortunately, so desktop and mobile apps can't be tested. 
However, other tools like Appium and HP's QTP can be used to test software and mobile applications.
"""
append_content("sample.txt", para)

print("_" * 70)


##################### Context Manager ######################
# --> when ever we open file with context manager no need to close file explicitly.
def read_file_context_manager(file_path):
    with open(file_path, "r") as file_a:
        data = file_a.read()
        print(data)
        print("is file is closed: ", file_a.closed)  # False
    print("is file is closed: ", file_a.closed)  # True


# Note outside it will give you true result.
read_file_context_manager("sample1.txt")

print("_" * 50)


#######################################################
# File read options.
# 1. read specific number of bytes
# 2. read number of lines
# 3. read list of lines

# read specific number of bytes/chars
def read_number_of_bytes(file_path, num_of_bytes):
    with open(file_path, "r") as file_object:
        data = file_object.read(num_of_bytes)
        print(data)


read_number_of_bytes("sample1.txt", 20)  # Hello Pankaj how are
print("_" * 50)
read_number_of_bytes("sample1.txt", 50)  # Hello Pankaj how are your ?Add new line in file vi

print("_" * 50)


#############################
# 2. read number of lines with readline() method.
def read_number_line(file_path, num_lines):
    with open(file_path, "r") as file_obj2:
        for _ in range(num_lines):
            print(file_obj2.readline(), end="")


read_number_line("sample1.txt", 50)

print("_" * 50)
print("...................3.............")


# 3. read list of lines with readlines() method: readlines method return list of lines from given file.
def read_list_of_lines(filepath):
    with open(filepath, "r") as file:
        lines_list = file.readlines()
        print(lines_list)
        return lines_list


read_list_of_lines("sample1.txt")

print("_" * 70)


def read_specific_number_line(filepath, start, stop):
    line_list = read_list_of_lines(filepath)
    for i in range(start - 1, stop):
        print(line_list[i], end="")


read_specific_number_line("sample1.txt", 5, 7)
