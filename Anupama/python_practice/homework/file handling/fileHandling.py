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


# read content from file
def read_file_content(file_path):
    file_obj = open(file_path, "r")
    data = file_obj.read()
    print("is file readable :", file_obj.readable())
    print("file name :", file_obj.name)
    print("is file closed :", file_obj.closed)
    print(data)
    file_obj.close()
    print("is file closed :", file_obj.closed)
    # print(file_obj.read())


# read file from current location
# read_file_content("read_data.txt")

# read file from different location
# read_file_content("E:\\Filesdata\\count_name.txt")


# write content to the file with write mode.

def write_content_to_file(file_path, new_content):
    file_obj = open(file_path, "w")
    file_obj.write(new_content)
    file_obj.close()


write_content_to_file("new_file.txt", "Hello Good Morning")