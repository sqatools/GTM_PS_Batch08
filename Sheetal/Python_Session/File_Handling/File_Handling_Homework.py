def file_open(file_path):
    file_read = open(file_path,"r")
    data = file_read.read()
    file_read.close()
    return data

print("The content of the file is: \n",file_open("read_data.txt"))

#  1. Hello this is a new Python File
# 2. This contains the notes related to Python
#
print("WAP to Append the text in the new file")
def file_open(file_path,file_append):
    file_write = open(file_path,"w")
    data = file_write.write("3. This is new content in the file\n")
    file_write.close()

    file_read = open(file_append, "r")
    data1 = file_read.read()
    file_read.close()

    file_write = open(file_path, "a")
    file_write.write(data1 + "\n")
    file_write.close()

    file_read = open(file_path, "r")
    data2 = file_read.read()
    file_read.close()

    return data2

print("The new file with the new content is:\n",file_open("write_data.txt","read_data.txt"))

print("Read content from file1 and file2 and add content to the file3.")

def file_open(file_path1,file_path2,file_append):
    file_write = open(file_append,"w")
    print("Direct text update")
    file_write.write("1. This is a new content in the file\n")
    file_write.close()

    with open(file_path1, "r") as file_read:
        data1 = file_read.read()

    with open(file_append, "a") as file_write:
        file_write.write("This is the Data of File1\n")
        file_write.write(data1)

    with open(file_path2, "r") as file_read:
        data2 = file_read.read()

    with open(file_append, "a") as file_write:
        file_write.write("This is the Data of File2\n")
        file_write.write(data2)

    with open(file_append, "r") as file:
        lines = file.readlines()

    non_blank_lines = [content_line for content_line in lines if content_line.strip() != ""]

    with open(file_append, "w") as file:
        file.writelines(non_blank_lines)

    with open(file_append, "r") as file_read:
        data3 = file_read.read()

    return data3

print(file_open("write_data.txt","read_data.txt"," append_data.txt"))
