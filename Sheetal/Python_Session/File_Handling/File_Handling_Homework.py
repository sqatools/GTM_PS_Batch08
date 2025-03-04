def file_open(file_path):
    file_read = open(file_path,"r")
    data = file_read.read()
    file_read.close()
    return data

print("The content of the file is: \n",file_open("read_data.txt"))

#  1. Hello this is a new Python File
# 2. This contains the notes related to Python

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

