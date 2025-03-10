"""
Modes to access a file:

1. Read mode (r) : We can open a file in read mode to read its content

2. Write mode (w) : --> We can open a file in write mode if we want to update the contents of the file
                    --> When we open a file in write mode and add some content to it then, previous
                        data will be overwritten

3. Append mode (a) : --> We can open file in append mode to update the contents of the file, and
                       append mode adds new content to the file at end of the file.
                     --> Append mode keeps the original data as well as updated content

# Function to open a file:
file = open(filepath, mode)

"""

# Read contents from a file :
def read_file_contents(file_path):
    file_obj = open(file_path, "r")
    data = file_obj.read()
    print(data)
    print("Is file readable: ", file_obj.readable())
    print("File name is: ",file_obj.name)
    print("Is file closed: ",file_obj.closed)
    file_obj.close()
    print("is file closed: ",file_obj.closed)
#    print(file_obj.read())

read_file_contents("read_data.txt")


# Write contents to the file :
def write_content_to_file(file_path, new_content):
    file_obj = open(file_path, "w")
    file_obj.write(new_content)
    file_obj.close()

write_content_to_file("new_data.txt", "Hello Good Morning")







