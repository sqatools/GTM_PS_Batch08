"""
# mode to access the file
# read mode(r) : we can open file in read mode to read its content .

# write mode(r) : -> we can open file in write mode if we want  to update the content in file
                  -> when we file in write mode and add some content to the file, then previous file
                   will overwrite in the new content.

# append mode(a) : -> we can open file in append mode to update the content of the file, and append
                      mode add new content to the file at end of the file
                   -> append mode keep the original data as well as update content.

# Note: Function to open file:
file = open(filepath, mode)
"""

# read content from file

def read_file_Content(filepath):
    file = open(filepath, "r")
    data = file.read()


    print(data)


read_file_Content("read_data.txt")

# write content to the file with write mode

def write_content_to_file(file_path, new_content):
    file_obj = open(file_path, "w")
    file_obj.write(new_content)
    file_obj.close()

# 1. write content to existing file
# write_content_to_file("new_file.txt", "Good morning team")

# 2. write content to non existing file : If file is not available then it will create file
#    and add content to the file
# write_content_to_file("new_File.txt", "very good morning")


# Append content to the file


def append_content_to_file(filepath, content):
    file = open(filepath, "a")
    file.write(content)
    file.close()

# 1) Add content to existing file: It will add content at end of existing file
# append_content_to_file("append_data.txt", "\n Adding new content")

# 2) Add content to non-existing file: It will create new file and add content to the file
#  append_content_to_file("append_data_new.txt", "writing first line\n")



#############################################
# context manager : Context manager has it own inbuilt enter  and exist method , when ever we open
#                   any file with context manager then no need to close it explicitly.

def read_file_content_with_context(filepath):
    with open(filepath, "r")as file_obj:
        data = file_obj.read()
        print(data)
        print("is file closed in context manager :", file_obj.closed)

        print("is file closed outside of context manager :", file_obj.closed)

    read_file_content_with_context("read_data.txt")

print("_"*50)
##########################################
# file read option
# 1. read specific number of bytes
# 2. read number of lines
# 3. read list of lines

# 1. read specific number of bytes/chars
def read_number_of_bytes(filepath, num_of_bytes):
    with open(filepath, "r") as file_obj:
         data = file_obj.read()
         print(data)

read_number_of_bytes("read_data.txt", 50)
"""
1. Good morning team
2. lets start a session
3. any doubts
"""

print("_"*50)
###################################
# 2. read number of lines
def read_number_lines(filepath, num_lines):
    with open(filepath, "r") as file_obj:
        for i in range(num_lines):
            print(file_obj.readline())

read_number_of_bytes("read_data.txt", 4)

"""
1. Good morning team
2. lets start a session
3. any doubts
4. Good morning team
5. lets start a session
6. any doubts
7. Good morning team
8. lets start a session
9. any doubts
10. Good morning team
11. lets start a session
12. any doubts
"""

print("_"*50)
########################################################

# 3. read list of lines with readlines() method : readlines method return list of lines given file

def read_list_of_lines(filepath):
    with open(filepath, "r")as file:
        list_lines = file.readlines()
        print(list_lines)

#read_list_of_lines("read_data.txt")


def read_specific_number_lines(filepath, start, stop):
    lines_list = read_list_of_lines(filepath)
    for i in range(start-1, stop):
        print(lines_list[i])


read_specific_number_lines("read_data.txt", 2, 7)