"""
# 1). Python Program How to read a file in reading mode.

file = open('textfile1.txt','r')   # open file in read mode
data = file.read()                 # read content of the file
print(data)                        # print file data
file.close()                       # close the opened file


Output:
Line1 : This is India.
Line2 : This is America.
Line3 : This is Canada.
Line4 : This is Australia


#2). Python file program to overwrite the existing file content.

# Solution 1:
content = "New Line : This is China"
file = open("writecontent.txt","w")   # open file and provide filename and write mode as (w)
file.write(content)                   # write content to file using write method
file.close                            # close the file

# Solution 2:  write content into file using function.
content = "New Line : This is China11111"

def write_content(filepath,content):
    file = open(filepath,"w")
    file.write(content)
    file.close()

write_content("textfile1.txt",content)


#3). Python file program to append data to an existing file.

f = open("appendcontend.txt","a")   # Open file with append mode
f.write("New Line : This is china11111") # write new line to the file
f.close()                           # Close the file



#4). Python file program to get the file’s first three and last three lines.

file = open("readcontent.txt","r")  # Open file with read mode
linelist = file.readlines()        ## Read file lines in the list


# Print first three lines
for i in (linelist[:3]):
    print(i)

# Print last three lines
for i in (linelist[-3:]):
    print(i)

Output:
Line1 : This is India.
Line2 : This is America.
Line3 : This is Canada.

Line3 : This is Canada.
Line4 : This is Australia.
Line5 : This is China.



#5). Python file program to get all the email ids from a text file.


email_list = []                         # Create an empty list
file = open("ReadContentEmail.txt","r") ## Open the file in reading mods
data = file.read()                      # Read the data in the file
word_list = data.split(" ")             # Convert the data into words

# Iterate over the words
for word in word_list:
    if '@' in word:                 # Check for @ in the word
        email_list.append(word)     # Add word to the empty list
    else:
        continue
print(email_list)                   # Print output
file.close()                       # Close the file


Output: ['test1@gmail.com', 'test2@gmail.com', 'test3@gmail.com']




#6). Python file program to get a specific line from the file.

file = open("readcontent.txt","r")
data = file.readlines()
print("1st Line")
print(data[0])
file.close()

Output:
1st Line
Line1 : This is India.


#7). Python file program to get odd lines from files and append them to separate files.

f1 = open('readcontent.txt','r')  # Open 1st file in read mode
f2 = open('writecontent3.txt','w') # Open 2nd file in write mode

line_list = f1.readline()          ## Read lines of the file

for i in range(0, len(line_list)): # Iterate over lines
    if (i % 2!= 0):               # Check for odd line
        f2.write(line_list[i])        # Write lines to 2nd file
    else:
        pass

f1.close()                        # Close the file
f2.close()                        # Close the file


#8). Python file program to read a file line by line and store it in a list.
result_list = []
with open("ReadContent.txt", "r") as file: # Read file with context manager
    while True:
        line = file.readline()
        if not line:
            break
        result_list.append(line)

print(result_list)
#['Line1 : This is India.\n', 'Line2 : This is America.\n', 'Line3 : This is Canada.\n', 'Line4 : This is Australia.\n', 'Line5 : This is China.']



#9). Python file program to find the longest word in a file.

max_word = ''
max_len = 0

with open("ReadContent3.txt","r") as file:
    data = file.read()
    word_list = data.split()

    for word in word_list:
        if len(word) > max_len:
            max_len = len(word)
            max_word = word
        else:
            continue

print("Max word from the file is:",max_word )

#Max word from the file is: Programming


#10). Python file program to get the count of a specific word in a file.
file = open("ReadContent3.txt","r") # Open file with read mode
words = file.read().split()         # Read the data in the file and convert it into words
count = 0                           # Create count variable

for word in words:
    if word == 'Python':
        count = count+1
print("Count of python in the file", count)




#11). Python file program to read a random line from a file.

import random
lines = open("ReadContent3.txt").read().splitlines()
data = random.choice(lines)
print(data)

#Its very easy to learn to and


#12). Python file program to copy the file’s contents to another file after converting it to lowercase.

with open('ReadContent3.txt','r') as datafile: ## Open file in read mode
    with open('Writecontent3.txt','a') as outputfile:         # Open another file in append mode
        for line in datafile:
            outputfile.write(line.lower())                 # Convert characters in the line to lowercases and Write it to 2nd file


#13). Python file program to copy the file’s contents to another file after converting it to uppercase.

with open('file name', 'r') as data_file: ## Open file in read mode
    with open('file.txt', 'a') as output_fil:    # Open another file in write mode
        for line in data_file:                   # Iterate over lines of the file
            output_file.write(line.upper())      # Convert characters in the line to uppercases and # Write it to 2nd file


#14). Python file program to count all the words from a file.

file = open("readcontent.txt") # Open the file
words = file.read().split() # Convert data to words
count = 0                   # Create a count variable
for word in words:
    count = count + 1       # Add 1 to the count variable for each word
print ("Count of word in the file", count)

#Count of word in the file 25



#15). Python file program to sort all the lines File as per line length size.

with open("sortcontent.txt", "r") as file:  ## Open file in read mode with context manager
    FileLines = file.readlines() ## Read list of lines.
    for i in range(len(FileLines)):     # Initial for loop to start picking each line one by one
        for j in range(i+1, len(FileLines)):         # Initial for loop to compare all remaining line with previous one.
            if len(FileLines[i]) > len(FileLines[j]):             # compare each line length, swap small len line with long len line.
                temp = FileLines[i]
                FileLines[i] = FileLines[j]
                FileLines[j] = temp
            else:
                continue

# re-write all the line one by one to the file
with open('ReadContent.txt', "w") as file:
    # Combine all the sequentially arrange lines with join method.
    all_lines = ''.join(FileLines)
    # overwrite all the existing lines with new one
    file.write(all_lines)

Output:

This is Java
This is Python
Python is good language
Hello Good Morning How Are You.



#16). Python file program to write a tuple to a file.

tup = ('1','2','3') # Create a tuple
f = open('readcontent.txt','w') # Open file in write mode
f.write(" ".join(tup)) # Write tuple to file
f.close() # Close the file

Output:
Output : Open the readcontent.txt file to see the tuple.
1 2 3


#17). Python file program to check whether a file is closed or not.

f = open('readcontent.txt','r') # Open file in read mode
print(f.closed) # Check whether the file is closed or not
f.close() # Close the file
print(f.closed) # Check whether the file is closed or not


Output:
False
True

"""

#18). Python file program to read the data of two of the files created and add it to a new file.

str1 = str2 = ""  # Create two empty strings
with open("readcontent1.txt") as f:  # Open first file
    str1 = f.read() # Read the data
with open("readcontent2.txt") as f: # Open second file
    str2 = f.read() # Read the data

str1 = str1 + "\n" # Add a new line
str1 = str1 + str2 # Combine data
with open("writecontent5.txt",'w') as f: # Open third file in write mode and write the new data to it
    f.write(str1)

"""
Output:
Output : Open the writecontent4.txt file to see the result

Line1 : This is India.
Line2 : This is America.
Line3 : This is Canada.
Line4 : This is Australia.

Line5 : This is Africa.
Line6 : This is Korea.
Line7 : This is Germany.
Line8 : This is China.



#19). Python file program to count the total number of characters in a file.

file = open('readcontent.txt') # Open the file
words = file.read().split() # Read the file and converting data into words
count = 0 # Create a count variable

for word in words: # Iterate over words

    for char in word: # Iterate over characters in the word
        if char.isalpha():     # Check for alphabet
            count += 1     # Add 1 to the count varibale for each alphabet

# Print output
print("Total number of characters in the file: ",count)

#Total number of characters in the file: 67
"""

#20). Python file program to count the total number of Uppercase characters in a file.
file = open('readcontent1.txt')
words = file.read().split()
count = 0
for word in words:
    for char in word:
        if char.isupper():
            count = count+1
print("Total number of upper case characters in the file: ",count)
#Total number of upper case characters in the file:  12


#31). Python file program to count the total number of Lowercase characters in a file
file = open('readcontent1.txt')
words = file.read().split()
count = 0
for word in words:
    for char in word:
        if char.islower():
            count = count+1
print("Total number of lower case characters in the file: ",count)
Total number of lower case characters in the file:  55
