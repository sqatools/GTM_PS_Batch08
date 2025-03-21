""""
# 1). Python Program How to read a file in reading mode.
def read_file(filepath):
    file = open( filepath, "r" )
    file.read()
    file.close()
read_file( "Pfile.txt" )
"""

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

def read_file(filepath):
    file = open( filepath, "r" )
    file.read()
    file.close()