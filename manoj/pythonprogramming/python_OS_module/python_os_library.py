import os

###
# get current working directory path
print(os.getcwd())
# C:\manojautomation\GTM_PS_Batch08\manoj\pythonprogramming\python_OS_module


####
# change working directory path
os.chdir("C:\\C:\manojautomation\manoj_automationCode")
print(os.getcwd())  #C:\manojautomation\manoj_automationCode

with open("test_data123.txt", "w") as file:
    file.write("heyyy")

###############
# create new folder
"""
os.mkdir("C:\manojautomation\manoj_automationCode")
os.chdir(r"C:C:\manojautomation\manoj_automationCode")
os.mkdir("C:\manojautomation\manoj_automationCode")
"""
####################
# remove directory
os.rmdir("GTM_PS_Batch08")


#####################
# create multiple folder structure with child folders
os.makedirs(r"C:\manojautomation\batch\fold1\f2\f3\f4\f5")

# create multiple folders on same location
"""
for i in range(7, 12):
    os.makedirs(r"C:\manojautomation\batch08\fold{i}"

"""

print("_*50")
##################
# get list of files and folder from target location
src_path = r"C:\manojautomation"
data_list = os.listdir(src_path)
print(data_list)
print("total items :", len(data_list))

for data in data_list:
    print(data)
    print(os.path.join(src_path, data))
    print("+++++"*20)

# join the two path
filename = "count_name.txt"
filepath = os.path.join(src_path, filename)
print(filepath)

##########################
# check given path file or folder
path1 = r"C:\manojautomation\manoj_automationCode\userinput.txt"
path2 = r"C:\manojautomation\manoj_automationCode\batch04"

print("check for file :",, os.path.isfile(path1))
print("check for folder1 :", os.path.isdir(path1))
print("check for folder2 :", os.path.isdir(path2))


############
# write a python prograam to separate and file and folders in a list
src_path = r"C:\manojautomation\manoj_automationCode"
data_list = os.listdir(src_path)
files_list = []
dir_list = []

for data in data_list:
    data_path = os.path.join(src_path, data)
    if os.path.isfile(data_path)
        files_list.append(data)
    else:
        dir_list.append(data)


############################
# check current path is exist or not