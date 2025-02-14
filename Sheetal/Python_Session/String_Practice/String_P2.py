from colorama import *

#Program 1
print(Fore.MAGENTA+ "Write a Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string:"+Style.RESET_ALL)
Input1 = input("Enter a String: ")
str1=""
print(Input1[0]+Input1[-1:-4:-1])

if len(Input1) <=2:
    print("The actual String is : ",Input1)
else:
    str1 = Input1[0]+Input1[-1:-(len(Input1)+1):-1]
    print(str1)

print("_"*40)
#Program 2
print(Fore.GREEN+"Write a program to add elements from one list to another list and print It in descending order using Python Loops."+Style.RESET_ALL)
# Input :
A = [2 ,5 ,8 , 0 , 1, 4]
B=[]
# Output = [8,5,4,2,1,0]
for i in A:
    B.append(i)
    B.sort()
print(B)

print("_"*40)
print(Fore.GREEN+"Write a program to find the total number of special characters in a file using Python Loops."+Style.RESET_ALL)
"""Input :
(file.txt – file name
Content-
student@gmail.com
##comment)
Output = 3
"""
file1=open("C:/Users/Admin/Downloads/Python_Program.txt","r")
data = file1.read()
file1.close()  # Always close the file after reading

special_char = 0  # Initialize as integer

for j in data:
    if not j.isalnum() and not j.isspace():  # Count non-alphanumeric and non-space characters
        special_char += 1

print("Number of special characters:", special_char)

print("_"*40)
print(Fore.GREEN+"Write a program to find the total number of digits in a file using Python Loops."+Style.RESET_ALL)
"""Input :
(file.txt – file name
Content-
Virat Kohli scored 100 in the last match)
Output = 3"""

file2 = open("C:/Users/Admin/Downloads/Python_Program.txt","r")
data = file2.read()
file2.close()

num_digit = 0
num_string = 0

for i in data:
    if i.isdigit():
        num_digit +=1
    elif i.isalpha():
        num_string +=1

print("Total Number of digits in a file are: ",num_digit)
print("Total Number of string in a file are: ",num_string)

print("_"*40)



