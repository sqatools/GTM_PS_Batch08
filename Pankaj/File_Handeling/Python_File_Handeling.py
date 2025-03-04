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


# red content from file
def read_file_content(filepath):
    file_obj = open(filepath, "r")
    data = file_obj.read()
    print(data)


def write_content_file(filepath, new_content):
    file_obj = open(filepath, "w")
    file_obj.write(new_content)
    file_obj.close()


write_content_file("Hello its done")
