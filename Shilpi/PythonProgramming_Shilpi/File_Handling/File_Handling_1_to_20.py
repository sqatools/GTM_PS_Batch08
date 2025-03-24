"""
print("1). Python Program How to read a file in reading mode.")
def read_file(filepath):
    with open(filepath,"r") as file:
        data=file.read()
        print(data)
        return data

read_file("file3.txt")
print("_"*100)
###############################################################################################################

print("2). Python file program to overwrite the existing file content.")

def write_file(filepath):
    with open(filepath,"w") as file:
        data1=file.write("This is one of my favorite poems")
        return data1

read_file("file1.txt")
write_file("file1.txt")
read_file("file1.txt")

print("_"*100)

############################################################################################################

print("3). Python file program to append data to an existing file.")

def append_file(filepath,content):
    with open(filepath,"a") as file:
        data2=file.write(content)
        print(data2)
        return data2

read_file("file1.txt")
append_file("file1.txt","\nAnd miles to go before I sleep\nAnd miles to go before I sleep ")
read_file("file1.txt")
print("_"*100)
###############################################################################################
print("4). Python file program to get the file’s first three and last three lines.")
def read_specific_lines(filepath):
    with open(filepath,"r") as file:
        data4=file.readlines()
        length_data=len(data4)
        for x in range(3):
            print(data4[x],end="")
        print()
        for y in range(length_data-3,length_data):
            print(data4[y],end="")

print("Method 1")
read_specific_lines("file3.txt")
print()
print("_"*100)

def read_specific_line2(filepath):
    with open(filepath,"r") as file:
        data=file.readlines()
        for x in data[:3]:
            print(x,end="")
        print()
        for y in data[-3:]:
            print(y,end="")

print("Method 2")
read_specific_line2("file3.txt")
print()
print("_"*100)
#############################################################################################################
print("5). Python file program to get all the email ids from a text file.")

def get_email_ids(filepath):
    list_of_emails = []
    with open(filepath,"r") as file:
        data=file.read()
        words=data.split()
        for word in words:
            if "@" in word:
                list_of_emails.append(word)
    return list_of_emails

e_mails=get_email_ids("emails_phones.txt")
for x in e_mails:
    print(x)
print("_"*100)
################################################################################################
print("6). Python file program to get a specific line from the file.")
def get_specific_line(filepath):
    with open(filepath,"r") as file:
        data=file.readlines()
        while True:
            try:
                userinput = int(input(f"Enter line number 1 to {len(data)} : "))
                if 1 <= userinput <= len(data):
                    break
                else:
                    continue
            except ValueError:
                continue

        for x in range(len(data)):
            if userinput==x+1:
                return data[x]

linetoprint=get_specific_line("lines.txt")
print(linetoprint)
print("_"*100)
###################################QUESTION###############################################
print("7). Python file program to get odd lines from files and append them to separate files.")
# Please check my approach. The website solution will give even lines not odd.i+1 required
# Website solution not clear. when open in write mode why is it not overwriting the previous i.
def odd_lines(filepath,newfilepath):
    with open(filepath,"r") as file:
        data=file.readlines()
        for x in range(len(data)):
            if (x+1)%2!=0:
                if x+1==1:
                    with open(newfilepath,"w") as file1:
                        file1.write(data[x])
                else:
                    with open(newfilepath,"a") as file1:
                        file1.write(data[x])
            else:
                continue
    with open(newfilepath,"r") as file2:
        data1=file2.read()
        print(data1)

odd_lines("lines.txt","Oddlines.txt")
print("_"*100)
#######################################################################################################
print("8). Python file program to read a file line by line and store it in a list.")
def read_line_by_line(filepath):
    list1=[]
    with open(filepath,"r") as file:
        while True:
            line=file.readline()

            if not line:
                break
            else:
                list1.append(line)

    print(list1)

read_line_by_line("lines.txt")
print("_"*100)
##########################################################################################################
print("9). Python file program to find the longest word in a file.")
def longest_word(filepath):
    with open(filepath,"r") as file:
        data=file.read()
        words=data.split()
        c=0
        longest_word=""
        for word in words:
            if c<len(word):
                c=len(word)
                longest_word=word
            else:
                continue
        print(f"The longest word in the file is {longest_word} with {c} letters")

longest_word(("lines.txt"))
print("_"*100)
###########################################################################################################
print("10). Python file program to get the count of a specific word in a file.")
def count_word(filepath):
    with open(filepath,"r") as file:
        data=file.read()
        words=data.split()
        userinput=input("Enter the word you need to count : ")
        c=0
        for word in words:
            if word==userinput:
                c+=1
        return userinput,c

word,countofword=count_word("readcontent.txt")
print(f"The count of {word} is {countofword}")
print("_"*100)

#######################################################################################################
print("11). Python file program to read a random line from a file.")
import random


def read_random_line(filepath):
    with open(filepath, "r") as file:
        data3 = file.readlines()
        randomline = random.choice(data3)
        print("Random Line : ", randomline)
        return randomline


read_random_line("file3.txt")
print("_" * 100)
####################################QUESTION#######################################################################
print("12). Python file program to copy the file’s contents to another file after converting it to lowercase.")


# check my approach. in the program append mode used. will it not keep adding the content to the file if we
# run the program multiple times
def content_to_lowercase(filepath, lowercasefile):
    with open(filepath, "r") as file:
        data4 = file.read()
        lowerdata = data4.lower()

    with open(lowercasefile, "w") as file:
        file.write(lowerdata)

    with open(lowercasefile, "r") as file:
        data5 = file.read()
        print(data5)
        return data5


content_to_lowercase("readcontent.txt", "NewLowercaseFile.txt")
print("_" * 100)
#########################################QUESTION#############################################################
print("13). Python file program to copy the file’s contents to another file after converting it to uppercase.")


def content_to_uppercase(filepath, uppercasefile):
    with open(filepath, "r") as file:
        data6 = file.read()
        upperdata6 = data6.upper()

    with open(uppercasefile, "w") as file:
        data7 = file.write(upperdata6)

    with open(uppercasefile, "r") as file:
        data8 = file.read()
        print(data8)
        return data8


content_to_uppercase("file3.txt", "NewUppercaseFile.txt")
print("_" * 100)
###############################################################################################################
print("14). Python file program to count all the words from a file.")


def count_all_words(filepath):
    count = 0
    with open(filepath, "r") as file:
        data9 = file.read()
        words9 = data9.split()
        for word in words9:
            count += 1
        print("The number of words in the file are: ", count)
        return count


count_all_words("readcontent.txt")
print("_" * 100)
###############################################QUESTION##################################################
print("15). Python file program to sort all the lines File as per line length size.")
#Please check approach.explain website solution and the use of join. how to better tackle the problem of the
#last item in the list not having\n
def sort_per_line_length(filepath,newfilepath):
    with open(filepath, "r") as file:
        data10 = file.readlines()
        data10[len(data10)-1]=data10[len(data10)-1]+"\n"
        sortedlinelist =data10.copy()
        for x in range(len(sortedlinelist)):
            for y in range(x+1,len(sortedlinelist)):
                if len(sortedlinelist[y])<len(sortedlinelist[x]):
                    a=sortedlinelist[x]
                    sortedlinelist[x]=sortedlinelist[y]
                    sortedlinelist[y]=a
    with open(newfilepath,"w") as file:
        for i in sortedlinelist:
            file.write(i)
    with open(newfilepath,"r") as file:
        data12=file.read()
        print(data12)
        return data12

sort_per_line_length("sortcontent.txt","NewSortedContent.txt")
print("_"*100)
#########################################QUESTION############################################################
print("16). Python file program to consider a text file as a DB file and store all the student information in a text file.")
#What is a DB file? no solution in website. how to handle DB file. Does the extension of DB file need to be .DB

def Add_student(filepathDB):
    with open(filepathDB,"r") as file:
        data5=file.readlines()
        a=len(data5)
        for x in range(len(data5)):
            d1=data5[x].split("=")
            print(d1)
            if x==len(data5)-1:
                stu1=d1[0]
                studentnumber=int(stu1[-1])
        userinput=input("Do you want to add more student info to the file? y/n : ")
        if userinput=="y":
            print("Press ctrl+D when you are done adding the information")
            try:
                while True:
                    name1=input("Enter Student Name : ")
                    mobile1=input("Enter Mobile number : ")
                    mail1=input("Enter e-mail id : ")

                    with open(filepathDB, "a") as file:
                        if a==0:
                            studentnumber=1
                            str_stu_num=str(studentnumber)
                            dict1 = {'Name' : name1, 'mobile': mobile1, 'mail': mail1}
                            line  = f"STU_{str_stu_num}={dict1}\n"
                            file.write(line)
                            #file.write('\n' + 'STU_' + str_stu_num + '=' + '{' + '"Name"' + ':' + '"' + name1 + '"' + ',' + '"Mobile"' + '=' + mobile1 + ',' + '"E-mail"' + '=' + '"' + mail1 + '"' + '}')
                            a=a+1
                            a=a+1
                            continue
                        elif a>0:
                            studentnumber += 1
                            str_stu_num = str(studentnumber)
                            file.write('\n'+'STU_' + str_stu_num + '=' + '{' + '"Name"' + ':' + '"'+name1 + '"'+',' + '"Mobile"' + '=' + mobile1 + ',' + '"E-mail"' + '=' + '"'+mail1 + '"'+'}')
                            continue
            except EOFError:
                pass

Add_student("DB.txt")

print("_"*100)

#####################################################################################################################
print("17). Python file program to create n number of text files with given strings.")

def create_text_file():
    n1=int(input("Enter the value of n: "))
    for x in range(n1):
        filename1=input(f"Enter filename {x+1} : ")
        filenamefinal=filename1+".txt"
        with open(filenamefinal,"w") as file:
            file.write("")

create_text_file()
print("_"*100)
"""
##################################################################################################################
print("18). Python file program to generate text files with all alphabets.  e.g. A.txt , B.txt, C.txt….. Z.txt")
def create_text_files_alphabets():


create_text_files_alphabets()
