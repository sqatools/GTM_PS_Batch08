"""
# Mode to access the file
# read mode (r) : we can open file in read mode to read its content.

# write mode (w) : -> we can open file in write mode if we want to update the content of the file.
                   -> When we file in write mode and add some content to the file, then previous content
                      will overwrite in new content.

# append mode (a) : -> We can open file in append mode to update the content of the file, and
                       append mode add new content to the file at end of the file.
                    ->  Append mode keep the original data as well as updated content.

# Note :  function to open file:
file = open(filepath, mode)
"""

# seek(no_byte, offset) method : seek method help us to set the cursor position in the file.
# there are three offset value
# 0 : Default reference from beginning of the file
# 1 : reference position will be current position of the cursor
# 2 : reference position will be the end of the file

# tell() method : tell method return the current position of the cursor.

# 0 : Default reference from beginning of the file
def read_file_with_seek(filepath):
    with open(filepath, "r") as file:
        print("Default cursor position is: ", file.tell())
        file.seek(20, 0)   # setting file cursor at 20th position
        print("Updated cursor position is: ",file.tell())
        data_char_10 = file.read(10)
        print(data_char_10)
        print("New cursor position is: ",file.tell())

#read_file_with_seek("read_data1.txt")

def read_file_with_offset_1(filepath):
    with open(filepath, "r") as file:
        print("default cursor position :", file.tell())
        # set cursor position to 20 char
        file.seek(20, 0)
        print("updated cursor position :", file.tell())
        data_char_10 = file.read(10)
        print(data_char_10)
        print("new cursor position :", file.tell())
        file.seek(10, 1)
        print("new cursor position :", file.tell())

read_file_with_offset_1("read_data1.txt")


def read_file_with_seek_offset_2(filepath):
    with open(filepath, "rb") as file:
        file.seek(-50, 2)
        data = file.read()
        print(data)
        print(file.tell())

#read_file_with_seek_offset_2("read_data1.txt")

