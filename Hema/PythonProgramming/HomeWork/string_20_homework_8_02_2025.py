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

elif ch == 6:
    '''
    6). Python string program to test whether a passed letter is a vowel or consonant.
    '''
    str_5 = 'welcome'
    for ch in str_5:
       if ch == 'a' or ch == 'e' or ch == 'i' or ch =='o' or ch == 'u':
           print("The vowel letter in the string is: ", ch, end= "\n")
       else:
           print("Consonant letter is: ", ch, end= "\n")

elif ch == 7:
    '''
    9). Write a Python program to calculate the length of a string with loop logic.
    '''
    str6 = 'Hello welcome to the python programming'
    print("The length of string is: ", len(str6))
    count = 0
    for i in str6:
        count = count+1

    print("The count of the string is: ", count)
    if count == len(str6):
        print("the length is same")
    else:
        print("Not same")

elif ch == 8:
    '''
    10). Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”
    '''
    str_7 = "Programming"
    occurance_result= ''
    for i in str_7:
        #print(i)
        if i in occurance_result:
            occurance_result = occurance_result + '$'
        else:
            occurance_result = occurance_result + i
    print(occurance_result)

elif ch == 9:
    '''
    11). Write a python program to get to swap the last character of a given string.
Input = “SqaTool”
Output = “lqaTooS”
    '''
    str_8 = 'SqaTool'
    temp = ''
    for i in str_8:
        if i == str_8[0]:
            temp = i
            temp+ i.replace(str_8[0],str_8[-1])
    print(temp)

elif ch ==10:
    '''
    practice session1
    '''
    str3 = "Pramod Hema Karthik Bala Pramod Manoj Hema Kathik"
    list_str3 = str3.split()
    str4_1 = ''
    for i in list_str3:
        print(i)
        if i not in  str4_1:
            str4_1 = str4_1 + i
        else:
            continue
    print(str4_1)

elif ch ==11:
    '''
    ######################## Home Work ################
# Q1 : Write a python program to find smallest word from given string

# Q2 :  write a python program to get count all vowels from given string
str_a = "Hello GoOd MOrnIong"
# output = 7

# Q3 :  Write a python program to Convert all Vowels from upper to lower and lower to upper.
str_b = "We Are LEarnIng Python PrOgrammIng"
# output = "WE arE LeArning PythOn ProgrAmming"
    '''
    print("program to find smallest word")
    str11 = "click Open Zoom Workplace app on the dialog shown by your browser"

    small_word = ''
    small_len= 0

    long_word = ''
    long_len = 0

    list_str11 = str11.split()

    for word in list_str11:
        len_word = len(word)
        print(word, " " , len_word)
        if len_word > long_len:
            long_word = word
            long_len = len_word
        else:
            continue
    #print(small_word)
    #print(small_len)

    # Q2 :  write a python program to get count all vowels from given string
    str_a = "Hello GoOd MOrnIong"
    # output = 7
    output = ''
    for i in str_a:
        if i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i =='O' or i == 'U' or i== 'I':
            output = output + i
        else:
            continue
    print(output)
    print(len(output))

    # Q3 :  Write a python program to Convert all Vowels from upper to lower and lower to upper.
    str_b = "We Are LEarnIng Python PrOgrammIng"
    # output = "WE arE LeArning PythOn ProgrAmming"
    up_str_b = ''
    for i in str_b:
        if i.islower():
            up_str_b = up_str_b + i.upper()
        elif i.isupper():
            up_str_b = up_str_b + i.lower()
        else:
            continue
    print(up_str_b)