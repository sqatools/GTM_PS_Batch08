"""
install faker with below command
-> pip install faker
"""
from faker import Faker

fk = Faker()
print(dir(fk))
with open("user_data.txt", "a") as file:
    for _ in range(50):
        userinfo = f"{fk.first_name()}, {fk.last_name()}, {fk.email()}, {fk.phone_number()}\n"
        file.write(userinfo)
        # print("first name :", fk.first_name())
        # print("last name :", fk.last_name())
        # print("email :", fk.email())
        # print("phone :", fk.phone_number())
        # print("_"*50)
from datetime import datetime, timedelta
import time

print("current datetime :", datetime.now()) # 2025-03-10 21:25:50.372012

print("current year :", datetime.now().year) # 2025
print("current date :", datetime.now().date()) # 2025-03-10
print("current month :", datetime.now().month) # 3
print("current day :", datetime.now().day) # 10
print("current time :", datetime.now().time()) # 21:27:35.021952

var = datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%h_%D")
"""
%m : month
%M : minutes
%Y : Year :" 2025
%y : Year : 25
%H : Hour
%S : Seconds
%h : month name : Mar
%D : date : 03/10/2025

"""
print(var)

def write_file(filename):
    with open(filename, "w") as file:
        file.write("Goog Morning")


# for i in range(5):
#     var = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
#     filename = f"{var}.txt"
#     write_file(filename)
#     time.sleep(2)


"""
# get time difference between two activity
t1 = time.time()
time.sleep(5)
t2 = time.time()
print("time difference :", t2-t1)
"""

# time shows in epoc time format
print(time.time()) # 1741623558.8485603

# get yesterday date
yesterday = datetime.now() - timedelta(2)
print(yesterday)

print(datetime.strftime(yesterday, "%y-%m-%d")) # 25-03-08

# two house ago time.
two_hours_ago = datetime.now() - timedelta(hours=2)
print(two_hours_ago)
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
# check current path exists or not

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
import random

# get any random number from 1 to 10
print(random.randint(1, 10))

# get random value
print(random.random()) # 0.5844685452998718

# randrange return the random value from given range.
print("random range value:", random.randrange(1, 20, 2))


# random shuffle the list values
list1 = [4, 6, 8, 7, 1, 9]
random.shuffle(list1)
print(list1) # [6, 9, 7, 8, 1, 4]


# get random choice from list values
list2 = [5, 7, 9, 23, 55, 77, 8]
print(random.choice(list2)) # # 8
import sys

file_param = sys.argv

print(file_param)

# get platform information using sys
print(sys.platform) # win32

print(sys.version_info)
# sys.version_info(major=3, minor=12, micro=2, releaselevel='final', serial=0)

print(sys.version) # 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
