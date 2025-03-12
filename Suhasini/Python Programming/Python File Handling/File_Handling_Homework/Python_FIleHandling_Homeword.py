# 1. Python Program How to read a file in reading mode.
import random

print("1. Python Program How to read a file in reading mode")

def read_file(filepath):
    with open(filepath, "r") as file:
        fileContent = file.read()

    print("Contents of the file is: ")
    print(fileContent)

# read_file("homework_data_file.txt")
print("_"*50)


# 2. Python file program to overwrite the existing file content
print("2. Python file program to overwrite the existing file content")

newContent = "Overwriting new content to the file. Now previous data will be lost and new text will be overwritten"
def overwite_file_content(filepath):
    with open(filepath, "w") as file:
        file.write(newContent)
    print(file)

# overwite_file_content("homework_data_file.txt")
print("_"*50)


# 3. Python file program to append data to an existing file
print("3. Python file program to append data to an existing file")

def append_new_content(filepath):
    with open (filepath, "a") as file:
        newContent = "\nAppending Contents to existing file"
        file.write(newContent)

    print(file)

# append_new_content("homework_data_file.txt")
print("_"*50)

#################### Doubt
# 4. Python file program to get the file’s first three and last three lines
print("4. Python file program to get the file’s first three and last three lines")

def read_specific_number_lines(filepath,):
    with open(filepath, "r") as file:
        lines_list = file.readlines()

        for i in lines_list[:3]:
            print(i, end="")
        print("")

        for i in lines_list[-3:]:
            print(i, end="")

# read_specific_number_lines("homework_data_file.txt")
print("_"*50)


# 5. Python file program to get all the email ids from a text file.
print("5. Python file program to get all the email ids from a text file.")

def get_emails(filepath):
    with open (filepath, "r") as file:
        list_lines = file.readlines()
        emails = []

        for lines in list_lines:
            if "@" in lines:
                emails.append(lines)

    print("The Emails in the file are: ",emails)

# get_emails("homework_data_file.txt")
print("_"*50)


# 6. Python file program to get a specific line from the file
print("6. Python file program to get a specific line from the file")

def get_specific_line(filepath, lineNum):
    with open(filepath, "r") as file:
        line = file.readlines()

    print("Specific line read is: ")
    print(line[lineNum])

get_specific_line("homework_data_file.txt", 5)
print("_"*50)


############## Doubt : How to move to next line after appending
# 7. Python file program to get odd lines from files and append them to separate files
print("7. Python file program to get odd lines from files and append them to separate files")

def get_odd_lines(filepath1, filepath2):
    with open(filepath1, "r") as file:
        line_list = file.readlines()
        file2 = open(filepath2, "w")

        for i in range(len(line_list)):
            if i % 2 != 0:
                file2.write(line_list[i])
        print(line_list)

    file2.close()

get_odd_lines("homework_data_file.txt", "NewFileOddLines.txt")
print("_"*50)


# 8. Python file program to read a file line by line and store it in a list.
print("8. Python file program to read a file line by line and store it in a list")

result_list = []
def file_lines_in_list(filepath):
    with open(filepath, "r") as file:
        while True:
            line = file.readline()

            if not line:
                break
            else:
                result_list.append(line)

    print("List of lines is: ", result_list)

# file_lines_in_list("homework_data_file.txt")
print("_"*50)


# 9. Python file program to find the longest word in a file.
print("9. Python file program to find the longest word in a file")

def find_longest_word(filepath):
    with open(filepath, "r") as file:
        file_data = file.read()
        word_list = file_data.split()

        longest_word = ''
        longest_len = 0

        for word in word_list:
            if len(word) > longest_len:
                longest_len = len(word)
                longest_word = word
            else:
                continue

    print("Longest word is: ",longest_word, " and its length is: ",longest_len)

# find_longest_word("homework_data_file.txt")
print("_"*50)


# 10. Python file program to get the count of a specific word in a file
print("10. Python file program to get the count of a specific word in a file.")

def get_count(filepath, spword):
    with open(filepath, "r") as file:
        file_data = file.read()
        data_list = file_data.split()

        count = 0
        for word in data_list:
            if word == spword:
                count += 1
            else:
                continue
    if count == 0:
        print("Word is not present in the file")
    else:
        print("The word ",word," is repeated ",count," no of times")

# get_count("Read_content.txt", "Programming")
print("_"*50)


# 11. Python file program to read a random line from a file
print("11. Python file program to read a random line from a file")

def read_line_from_file(filepath):
    with open(filepath, "r") as file:
        read_lines = file.read().splitlines()
        line = random.choice(read_lines)         # Explanation
        print(line)

# read_line_from_file("Read_content.txt")
print("_"*50)


# 12. Python file program to copy the file’s contents to another file after converting it to lowercase
print("12. Program to copy the file’s contents to another file after converting it to lowercase")

def convert_lowercase(filepath1, filepath2):
    with open(filepath1, "r") as file1:
        with open (filepath2, "a") as file2:

            for line in file1:
                file2.write(line.lower())

# convert_lowercase("Read_Content.txt", "Convert_to_lower.txt")
print("_"*50)


# 13. Python file program to copy the file’s contents to another file after converting it to uppercase.
print("13. Program to copy the file’s contents to another file after converting it to uppercase.")

def convert_to_uppercase(filepath1, filepath2):
    with open(filepath1, "r") as file1:
        with open(filepath2, "a") as file2:

            for line in file1:
                file2.write(line.upper())

# convert_to_uppercase("Convert_to_lower.txt", "Convert_to_upper.txt")
print("_"*50)


# 14. Python file program to count all the words from a file.
print("Python file program to count all the words from a file")

def count_words_in_file(filepath):
    with open(filepath,"r") as file:
        count = 0
        file_data = file.read().split()
        for word in file_data:
            count += 1

        print("Number of words in the file are: ",count)

# count_words_in_file("Convert_to_lower.txt")
print("_"*50)


# #################### Doubt
# 15. Python file program to sort all the lines File as per line length size
print("15. Python file program to sort all the lines File as per line length size")

def sort_lines_in_file(filepath):
    with open(filepath, "r") as file:
        fileLines = file.readlines()

        for i in range(len(fileLines)):
            for j in range(i+1, len(fileLines)):
                if len(fileLines[i]) > len(fileLines[j]):
                    temp = fileLines[i]
                    fileLines[i] = fileLines[j]
                    fileLines[j] = temp
                else:
                    continue

    with open(filepath, "w") as file:
        allLines = ''.join(fileLines)
        file.write(allLines)

# sort_lines_in_file("Read_content.txt")
print("_"*50)


############################ Formatting doubt
# 16. Python file program to consider a text file as a DB file and store all the student information in a text file
print("16. Program to consider a text file as a DB file and store all the student information in a text file")

def store_stud_info(filepath, name, age, phone, course):
    with open(filepath, "a") as file:

        file.write(name)
        file.write(str(age))
        file.write(str(phone))
        file.write(course)


# store_stud_info("Convert_to_lower.txt","Suhasini",33, 23542637678, "MCA")
# store_stud_info("Convert_to_lower.txt","Mrinalini",35, 23542637678, "MCA")
# store_stud_info("Convert_to_lower.txt","Preeti",32, 23542637678, "MCA")
# store_stud_info("Convert_to_lower.txt","Raju",25, 23542637678, "BCom")
# store_stud_info("Convert_to_lower.txt","Ramesh",27, 23542637678, "BE")
print("_"*50)


# 17. Python file program to get all odd and even length words in two lists.
print("17. Python file program to get all odd and even length words in two lists")

def find_odd_even_words(filepath):
    with open(filepath, "r") as file:
        fileLines = file.read()
        file_data = fileLines.split()
        evenList = []
        oddList = []

        for word in file_data:
            if len(word) % 2 == 0:
                evenList.append(word)
            else:
                oddList.append(word)
    print("List with words of even length : ", evenList)
    print("List with words of odd length : ",oddList)

find_odd_even_words("homework_data_file.txt")
print("_"*50)


# 18. Python file program to get all mobile numbers from a file. e.g each mobile number size should be 10
print("18. Program to get all mobile numbers from a file. e.g each mobile number size should be 10")

def find_mob_num(filepath):
    with open(filepath, "r") as file:
        fileLines = file.read()
        file_data = fileLines.split()
        mobNum = []

        for word in file_data:
            if word.isdigit() and len(word) == 10:
                mobNum.append(word)

        print("The Mobile Numbers in file are: ",mobNum)

# find_mob_num("Read_content.txt")
print("_"*50)


# 19. Python file program to count the number of lines in a file
print("19. Python file program to count the number of lines in a file")

def find_lines_in_file(filepath):
    with open (filepath, "r") as file:
        fileLines = file.readlines()
        noOfLines = len(fileLines)

        print("Number of lines in the file are: ",noOfLines)

# find_lines_in_file("Read_content.txt")
print("_"*50)


################## Explanation
# 20. Python file program to get the file size of a file
print("20. Python file program to get the file size of a file")
import os
# Read file
info = os.stat('Read_content.txt')
# Print size of the file
print("Size of the file: ",info.st_size)




####################### Doubt
# 17, 22














