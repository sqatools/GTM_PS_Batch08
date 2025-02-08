#

print("#"*50)

ch = int(input("Enter number from 1 to 20 to check string program: "))

if ch == 1:
    '''
    Program 1:
#1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string
    '''
    str_1 = "Hello world"

    len_str_1 = len(str_1)
    if len_str_1 < 2:
        print("True")
    else:
        print(str_1[0:2]+str_1[-2:])

elif ch == 2:
    '''
    Program 2:
    2). Python string program that takes a list of strings and returns the length of the longest string.
    '''
    list_str = ['Welcome', 'to', 'the', 'Python', 'Programming']
    temp = 0
    for i in list_str:
        #print(i, end='\t')
        len_list_str = len(i)
        if len_list_str > temp:
            temp = len_list_str
    print(temp)

elif ch == 3:
    '''
    3). Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
    '''
    str_2 = "sqatools"
    #if len(str_2) > 2:
    print(str_2[-2:]*4)

elif ch == 4:
    '''
    4). Python string program to reverse a string if it’s length is a multiple of 4.
    '''
    #str_3 = "welcome"
    str_3 = "multiple"
    print("The string is: ",str_3,"and the length of the string is: ",len(str_3))
    if len(str_3)%4 == 0:
        print("The length of the string is multiple by 4, \n hence reveresed the string: ", str_3[::-1])
    else:
        print("string is not multiple of 4: ", str_3)

elif ch == 5:
    '''
    5). Python string program to count occurrences of a substring in a string.
    '''
    str_4 = "hello to welcome to the python programming world"
    sub_str_4 = 'to'
    print(str_4.count(sub_str_4))
