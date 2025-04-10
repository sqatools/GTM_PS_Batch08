#11th March'25
import random

ch = int(input('Enter any number (1 to 20) to check program: '))

if ch==1:
    '''
    1). Python Program How to read a file in reading mode.
    '''
    def read_file(filepath):

        with open(filepath, "r") as file:
            data = file.read()
            print(data)
    read_file("read_file.txt")


    #option 2

    print("*"*50)
    file = open("read_file.txt", "r")
    data = file.read()
    print(data)
    file.close()

elif ch == 2:
    '''
    2). Python file program to overwrite the existing file content.
    '''
    content = 'Document update 13_March_2025'
    file = open('read1_file.txt', 'w')
    data_overwrite = file.write(content)
    file.close()

elif ch == 3:
    '''
    3). Python file program to append data to an existing file.
    '''
    content = '\n Append text document on 13_March_2025'
    file_1 = open('read1_file.txt', 'a')
    data_append = file_1.write(content)
    file_1.close()

elif ch == 4:
    '''    
    4). Python file program to get the file’s first three and last three lines.
    
    '''
    file4_read = open('read_content.txt', 'r')
    data4_read = file4_read.readlines()
    for i in data4_read[:3]:
        print("First three lines: ", i)

    print("*"*50)

    for j in data4_read[-3:]:
        print("Last three lines: ", j)
    file4_read.close()

elif ch == 5:
    '''
    5). Python file program to get all the email ids from a text file.
    '''
    file5_read = open('read_email_file.txt', 'r')
    data5_read = file5_read.read()
    email_id = []
    data5_read_list = data5_read.split()
    for email in data5_read_list:
        if '@' in email:
            email_id.append(email)
        else:
            continue
    file5_read.close()
    print(email_id)

elif ch == 6:
    '''
6). Python file program to get a specific line from the file.
    '''
    file6_read = open('read_content.txt')
    data6_read = file6_read.readlines()
    print(data6_read[2])
    file6_read.close()

    #option 2:
    file6_1_read = open('read_content.txt')
    data6_1_read = file6_1_read.readlines()
    n = 2
    for i in range(0, len(data6_1_read)):
        if i == n:
            print(data6_1_read[i])
        else:
            continue
    file6_1_read.close()
elif ch == 7:
    '''
7). Python file program to get odd lines from files and append them to separate files.

    '''
    with open('read_7_content.txt', 'r') as file:
        data_7_read = file.readlines()

    data_7_write = open('write_content.txt', 'w')

    #content = '\n Line7 : This is sample_1'
    for i in range(0, len(data_7_read)):
        if i%2 != 0:
            '''When opening the file inside the loop only last item is updated, hence its commented'''
            #with open('write_content.txt', 'w') as file2:
                #data_7_write = file2.write(content)
                #data_7_write = file2.write(data_7_read[i])
            '''If we open write_content.txt file out of the for loop all odd number lines is updated'''
            print(i)
            write_7_content = data_7_write.write(data_7_read[i])
        else:
            continue

    file.close()
    data_7_write.close()

    #option 2:
    # f1 = open('read_7_content.txt', 'r')
    # # Open 2nd file in write mode
    # f2 = open('write_content.txt', 'w')
    # # Read lines of the file
    # lines_list = f1.readlines()
    # # Iterate over lines
    # for i in range(0, len(lines_list)):
    #     # Check for odd line
    #     if (i % 2 != 0):
    #         # Write lines to 2nd file
    #         print(i)
    #         print(lines_list[i])
    #         f2.write(lines_list[i])
    #     else:
    #         pass
    # # Close the file
    # f1.close()
    # f2.close()
elif ch ==8:
    '''
8). Python file program to read a file line by line and store it in a list.

    '''
    list8_var_read =[]
    with open('read_7_content.txt', 'r') as file:
        data = file.readlines()

    for i in range(len(data)):
        list8_var_read.append(data[i])

    print(list8_var_read)

elif ch == 9:
    '''
9). Python file program to find the longest word in a file.
    '''
    with open('read_7_content.txt', 'r') as file9:
        #data_9 = file9.readline()
        data_9 = file9.read()

        list_data_9 = data_9.split()
        max_len_word = 0
        max_word = ''

        for i in list_data_9:
            #print(i)
            #print(len(i))
            if len(i) > max_len_word:
                max_len_word = len(i)
                max_word = i
            else:
                continue

    print("max_length", max_len_word)
    print("max _word", max_word)

    #Not works:

    # for i in range(len(list_data_9)):
    #     print(i)
    #     print("*" * 20)
    #     print(len(list_data_9[i]))
    #     print("*" * 20)
    #     print(list_data_9[i])
    #     if len(list_data_9[i]) > max_len_word:
    #         max_len_word = len(list_data_9[i])
    #         max_word = list_data_9[i]
    #     else:
    #         continue

elif ch==10:
    '''

10). Python file program to get the count of a specific word in a file.
    '''
    with open('read_7_content.txt', 'r') as file_10:
        data_10 = file_10.read()

        list_data_10 = data_10.split()
        count = 0
        text_word = 'This'
        for word in list_data_10:
            print(list_data_10.count(word))
            if text_word in word:
                count = count + word.count(text_word)
            else:
                continue
        print(f"Count of {text_word} word is: ", count)

elif ch==11:
    '''
11). Python file program to read a random line from a file.
    '''
    import random
    with open("read_7_content.txt", 'r') as file11:
        data_11_read = file11.read()

    data_11_list = data_11_read.splitlines()
    data = random.choice(data_11_list)
    print(data)

elif ch == 12:
    '''
12). Python file program to copy the file’s contents to another file after converting it to lowercase.
    '''
    with open('read_upper.txt', 'r') as file_12:
        #data_12_read = file_12.read()

        #list_data_12_read = data_12_read.split()

        with open('copied_content.txt', 'w') as file_12_write:
            #data_12_write = file_12_write.read()

    #list_data_12_write = data_12_write.split()
    #     for i in list_data_12_read:
    #         #if i not in list_data_12_write:
    #             #list_data_12_write.append(i.lower())
    #         if i not in data_12_write:
    #             file_12_write.write(data_12_read.lower())
    #         else:
    #             continue
    # #output_str = str(list_data_12_write)
    #     output_str = file_12_write
    #     print(output_str)
            for readfile in file_12:
                data_output = file_12_write.write(readfile.lower())

            print(data_output)
elif ch == 13:
    '''
    13). Python file program to copy the file’s contents to another file after converting it to uppercase.
    '''
    def file_lower_upper_copied(filepath1, filepath2):
        with open(filepath1, 'r') as file13:
            with open(filepath2, 'a') as file_13_1:
                for i in file13:
                    data_output_1 = file_13_1.write(i.upper())
                #print(data_output_1)
        return data_output_1

    #print(file_lower_upper_copied(filepath1='read_lower.txt', filepath2='copied_upper_lower.txt'))
    output_13 = file_lower_upper_copied('read_lower.txt','copied_upper_lower.txt')
    print(output_13)

elif ch == 14:
    '''    
Solution
14). Python file program to count all the words from a file.
'''
    def count_all_words(filepath):
        with open(filepath, 'r') as file_14:
            data_14 = file_14.read()
        list_data_14 = data_14.split()
        len_list_data_14 = len(list_data_14)
        print(list_data_14)
        print(len_list_data_14)
        count_words = 0
        for word in list_data_14:
            #print(word)
            count_words = count_words + 1
        return count_words
    count_word = count_all_words('read_7_content.txt')
    print(count_word)

elif ch == 15:
    '''
    Solution
    15). Python file program to sort all the lines File as per line length size.
    
    Solution
    '''
    def sort_line_file(filepath_15, filepath_15_1):
        with open(filepath_15, 'r') as file:
            filelines_read = file.readlines()

        for i in range(len(filelines_read)):
            for j in range(i+1,len(filelines_read)):
                if len(filelines_read[i]) > len(filelines_read[j]):
                    temp = filelines_read[i]
                    filelines_read[i] = filelines_read[j]
                    filelines_read[j] = temp
                else:
                    continue
        with open(filepath_15_1, 'w') as file_15:
            data_15 = ''.join(filelines_read)
            sort_data_15 = file_15.write(data_15)

        return sort_data_15

    sort_file_len = sort_line_file('read_7_content.txt','sort_text.txt')
    print(sort_file_len)


elif ch==16:
    '''
16). Python file program to consider a text file as a DB file and store all the student information in a text file.
    '''

    def add_student_info(filepath, stud_id, stud_name, stud_section, stud_grade):
        with open(filepath, 'a') as file:
            data = file.write(f'{stud_id}, {stud_name}, {stud_section}, {stud_grade}\n')
            print(data)

    def get_student_info(filepath):
        with open(filepath, 'r') as file:
            print("stdent records")
            for i in file:
                data_1 = i.strip()
                stud_id, stud_name, stud_section, stud_grade = data_1.split(',')
                print(f'ID: {stud_id}, NAME: {stud_name}, SECTION: {stud_section}, GRADE: {stud_grade}')

    filepath = f'stud_info.txt'
    add_student_info(filepath, 1, 'Ram', 'A', 'C')
    add_student_info(filepath, 2, 'Mohan', 'C', 'B')

    get_student_info(filepath)

elif ch==17:
    '''
17). Python file program to create n number of text files with given strings.
    '''
    num_of_files_to_create = 5
    for num in range(1, (num_of_files_to_create+1)):
        with open(f'File_{num}.txt', 'w') as f:
            data = f.write('This is sample file')
    print(data)

elif ch==18:
    '''
18). Python file program to generate text files with all alphabets.  e.g. A.txt , B.txt, C.txt….. Z.txt
    '''
    import string

    for letter in string.ascii_uppercase:
        with open(f'{letter}.txt', 'w') as f:
            data = f.write(letter)
    print(data)

elif ch==19:
    '''
19). Python file program to get all odd and even length words in two lists.
    '''
    def get_all_odd_even_words(filepath):
        with open(filepath, 'r') as file:
            data = file.read()
            list_data_19 = data.split()

        odd_list_word = []
        even_list_word = []

        for word in list_data_19:
            if len(word)%2 == 0:
                even_list_word.append(word)
            elif len(word)%2 !=0:
                odd_list_word.append(word)
            else:
                continue
        print("even word list: ", even_list_word)
        print('odd list word: ', odd_list_word)

    #get_words = get_all_odd_even_words('read_len_words.txt')
    #print(get_words)

    get_all_odd_even_words('read_len_words.txt')

elif ch==20:
    '''
20). Python file program to get all mobile numbers from a file. e.g each mobile number size should be 10.
'''
    def get_all_mobile_num(filepath):
        with open(filepath, 'r') as file:
            data = file.read()
            data_list = data.split()

        num_list = []

        for num in data_list:
            if num.isnumeric():
                if num not in num_list and len(num) == 10:
                    num_list.append(num)

        print(num_list)

    mobile_num = get_all_mobile_num('mobile_num_read.txt')

'''
21). Python file program to get a list of all domains from a file. e.g. .com, .au, .in

22). Python file program to compare two files.

Solution
23). Python file program to count the number of lines in a file.

Solution
24). Python file program to get the file size of a file.

Solution
25). Python file program to write a tuple to a file.

Solution
26). Python file program to check whether a file is closed or not.

Solution
27). Python file program to extract characters from a text file into a list.

Solution
28). Python file program to read the data of two of the files created and add it to a new file.

Solution
29). Python file program to count the total number of characters in a file.

Solution
30). Python file program to count the total number of Uppercase characters in a file.

Solution
31). Python file program to count the total number of Lowercase characters in a file.

Solution
32). Python file program to count the total number of digits in a file.

Solution
33). Python file program to count the total number of special characters in a file.

Solution
34). Python file program to find the cursor position in a file.

Solution
35). Python file program to move the cursor to a specific position in a file.

Solution

36). Python file program to read the content of the file in reverse order.

Solution
37). Python file program to read a file and display each word separated by @.

38). Python file program to count the total number of vowels in a file.

Solution
39). Python file program to count the total number of consonants in a file.

Solution
40). Python file program to remove all the lines that contain the character ‘t’ in a file and write it to another file.

Solution
41). Python file program to display words from a file that has less than 5 characters.

Solution
42). Python file program to replace space by an underscore in a file.

    '''



# class Animal:
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"
#
# def animal_sounds(animal):
#     print(animal.make_sound())
#
# dog = Dog()
# cat = Cat()
#
# animal_sounds(dog)  # Output: "Woof!"
# animal_sounds(cat)  # Output: "Meow!"


# class Animal:
#     def make_sound(self):
#         print("making sound")
#
#
# class Dog(Animal):
#     def make_sound(self):
#         return 'woof!!!!'
#
# class Cat(Animal):
#     def make_sound(self):
#         return 'meooow!!!!!!'
#
# def animal_sounds(animal):
#     print(animal.make_sound())
#
# dog = Dog()
# cat = Cat()
#
# dog_sound = animal_sounds(dog)
# cat_sound = animal_sounds(cat)