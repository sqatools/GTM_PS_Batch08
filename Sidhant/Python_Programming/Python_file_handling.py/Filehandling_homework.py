""""
# 1). Python Program How to read a file in reading mode.
def read_file(filepath):
    file = open( filepath, "r" )
    file.read()
    file.close()
read_file( "Pfile.txt" )
"""
import random

'''
# 2). Python file program to overwrite the existing file content.
def write_file(filepath, data):
    file = open( filepath, "w" )
    file.write( data )
    file.close()


write_file( "Pfile.txt", 'This is India.' )
'''

'''
# 3). Python file program to append data to an existing file.
def append_data(filepath, data):
    file = open( filepath, "a" )
    file.write( data )
    file.close()

append_data( "Pfile.txt", "\nThis is China." )
'''
'''
# 4). Python file program to get the file’s first three and last three lines.
def customised_func(filepath):
    data = open( filepath, "r" )
    lines = data.readlines()

    first_three = lines[:3]
    last_three = lines[-3:]

    for line in first_three:
        print(line.strip())
    for line in last_three:
        print( line.strip() )
        
customised_func( "Pfile.txt" )
'''

'''
# 5). Python file program to get all the email ids from a text file.
def customised_func(filepath):
    email_id =[]
    file = open( filepath, "r" )
    file_data = file.read()
    word_list = file_data.split()
    for word in word_list:
        if '@' in word:
            email_id.append(word)
        else:
            continue
    print(email_id)
    file.close()







customised_func( "Pfile.txt" )
'''
'''
# 6). Python file program to get a specific line from the file.
def customised_func(filepath):
    file = open( filepath, "r" )
    file_data = file.readlines()
    print(file_data[5])
    file.close()


customised_func( "Pfile.txt" )
'''

'''
# 7). Python file program to get odd lines from files and append them to separate files.
def odd_file_func(filepath, output_filepath):
    data1 = open( filepath, "r" )
    read_data = data1.readlines()
    data1.close()
    data2 = open( output_filepath, "w" )
    for i in range( len( read_data ) ):
        if i % 2 ==0:
            data2.write( read_data[i] )
            print(read_data[i].strip())
    data2.close()


odd_file_func( "Pfile.txt", "oddfile.txt" )

'''

"""
# 8). Python file program to read a file line by line and store it in a list.
def Linebyline_func(filepath):
    file = open( filepath, "r" )
    list1 = []
    while (1):
        data_file = file.readlines()
        list1.append( data_file )
        if not data_file:
            break
    print(list1)
    file.close()


Linebyline_func( "Pfile.txt", )
"""

""""
#  9). Python file program to find the longest word in a file.
def max_word_func(filepath):
    file = open( filepath, 'r' )
    file_data = file.read()
    word_list = file_data.split()
    word_len = 0
    longest_word = ""
    for word in word_list:
        if len( word ) > word_len:
            word_len = len( word )
            longest_word = word
    print( "longest word is:", longest_word )
    print( "max_length is :", word_len )
    file.close()


max_word_func( "oddfile.txt" )
"""

"""
# 10). Python file program to get the count of a specific word in a file.
def specific_word_func(filepath):
    file = open( filepath, 'r' )
    file_data = file.read().split()
    count = 0
    for word in file_data:
        if "are" in word:
            count += 1
    print( count )
    file.close()


specific_word_func( "oddfile.txt" )
"""

"""
# 11). Python file program to read a random line from a file.
def randomm_word_func(filepath):
    file = open( filepath, 'r' )
    file_data = file.read().split()
    res1 = random.choice(file_data)
    print(res1)
    file.close()

    
randomm_word_func( "oddfile.txt" )
"""

"""
# 12). Python file program to copy the file’s contents to another file after converting it to lowercase.
def copy_content_func(readfile, appfile):
    read_file = open( readfile, 'r' )
    data_file = read_file.readlines()
    read_file.close()
    file2 = open( appfile, 'a' )
    for word in data_file:
        file2.write( word.lower() )
    file2.close()


copy_content_func( "oddfile.txt", "Pfile.txt" )

"""

"""
# 13). Python file program to copy the file’s contents to another file after converting it to uppercase.
def copy_upper_content_func(readfile, appfile):
    read_file = open( readfile, 'r' )
    data_file = read_file.readlines()
    read_file.close()
    file2 = open( appfile, 'a' )
    for word in data_file:
        file2.write( word.upper() )
    file2.close()


copy_upper_content_func( "oddfile.txt", "Pfile.txt" )

"""

'''
# 14). Python file program to count all the words from a file.
def count_all_word_func(filepath):
    file = open( filepath, 'r' )
    total_word = file.read().split()
    count = 0
    for word in total_word:
        count += 1
    print( count )
    file.close()


count_all_word_func( "oddfile.txt" )
'''