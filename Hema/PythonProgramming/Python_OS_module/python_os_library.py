import os
import shutil

####
# get current working directory path
print(os.getcwd())
# E:\Trainings\GTM_PS_Batch08_6Jan25\GTM_PS_Batch08\Deepesh\PythonProgramming\Python_OS_module


########
# change working directory path
"""
os.chdir("E:\\Filesdata")
print(os.getcwd()) # E:\Filesdata

# It will create new file in new path we have set.
with open("test_data.txt", "w") as file:
    file.write("Good Morning")
"""
##############
# create new folder
"""
os.mkdir("GTM_Batch08")
os.chdir(r"E:\Trainings\GTM_PS_Batch08_6Jan25\GTM_PS_Batch08\Deepesh\PythonProgramming\Python_OS_module")
os.mkdir("GTM_Batch08")
"""

################
# remove directory
#os.rmdir("GTM_Batch08")


################
# create multiple folder structure with child folders
#os.makedirs(r"E:\Filesdata\batch08\fold1\f2\f3\f4\f5")


# create multiple folders on same location.
"""
for i in range(7, 12):
    os.mkdir(fr"E:\Filesdata\batch08\fold{i}")

"""

print("_"*50)
###############
# get list of files and folder from target location
src_path = r"E:\Filesdata"
data_list = os.listdir(src_path)
print(data_list)
print("total items :", len(data_list))

for data in data_list:
    print(data)
    print(os.path.join(src_path, data))
    print("++++"*20)


print("_"*50)
# join the two path
filename = "count_name.txt"
filepath = os.path.join(src_path, filename)
print(filepath)

print("_"*50)
#####################
# check given path file or folder
path1 = r"E:\Filesdata\userinput.txt"
path2 = r"E:\Filesdata\batch04"

print("check for file :", os.path.isfile(path1)) # True
print("check for folder1 :", os.path.isdir(path1)) # False
print("check for folder2 :", os.path.isdir(path2)) # True


print("_"*50)
##############
# write a python program to separate and files and folders in two lists
src_path = r"E:\Filesdata"
data_list = os.listdir(src_path)  # it will return list of all files and folders.
files_list = []
dir_list = []

for data in data_list:
    data_path = os.path.join(src_path, data)
    if os.path.isfile(data_path):
        files_list.append(data)
    else:
        dir_list.append(data)

print("All files :", files_list)
print("files count :", len(files_list))

print("All folders :", dir_list)
print("Count of folders :", len(dir_list))


print("_"*50)
#################################
# check current path is exists or not

path3 = r"E:\Filesdata\userinput.txt"
path4 = r"E:\Filesdata\userinput_new.txt"

print(os.path.exists(path3)) # True
print(os.path.exists(path4)) # False


print("_"*50)
#################################
# copy file from one location to another
path6 = r"E:\Filesdata\userinput.txt"
path7 = r"E:\Filesdata\batch08\userinput.txt"
path8 = r"E:\Filesdata\batch08\userinput_updated.txt"

# copy file with same on target location
shutil.copy(path6, path7)
# copy file with different name on target location
shutil.copy(path6, path8)

print("_"*50)
#################################
# get size of the file
path9 = r"E:\Filesdata\userinput.txt"
print("size of file in byte:", os.path.getsize(path9)) # 135
print("creation time :", os.path.getctime(path9)) # 1615561501.6832726
print("modification time :", os.path.getmtime(path9)) # 1615561501.6832726

##################################
# run windows command
os.system("control")
os.system("dir E:\\Filesdata")
os.system("notepad.exe")

##################################
# get CPU count on the system
print("CPU count:", os.cpu_count()) # CPU count: 8
