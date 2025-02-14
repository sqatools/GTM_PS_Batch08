#13thFeb2025

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

elif ch ==101:
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

elif ch ==111:
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
    list_str_b = str_b.split()
    #print(list_str_b)
    out_put = ''
    count = 0
    for i in str_b:
        #print(i)
        if i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i =='O' or i == 'U' or i== 'I' or i.isupper() or i.islower():
            up_str_b = str_b + i.upper()+ i.lower()
        if i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i =='O' or i == 'U' or i== 'I' and i.islower():
            up_str_b = str_b + i.upper()
            #up_str_b = up_str_b + i.upper()
        else:
            continue
    print(up_str_b)
    print(out_put)

elif ch==10:
    '''
    105). Write a program to get all the email id’s from given string using python.
Input str = “”” We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string.”””
Output = [‘john@gmail.com’, ‘ jay@lic.com’, ‘hari@facebook.com’, ‘mery@hotmail.com’ ]

    '''

    str_r = 'We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string'
    mailid_str = ''
    str_r_list = str_r.split()

    for i in str_r_list:
        if '@' in i:
            mailid_str = mailid_str + i + ","

    #print(mailid_str)
    mailid_str_list = mailid_str
    print("Email id from the given string: ",mailid_str)

elif ch == 11:
    '''
    106). Write a program to get a list of all the mobile numbers from the given string using python.
Input str = “”” We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string.”””
Output = [‘8988858683’, ‘2312245566’, ‘4532892234’, ‘9999234355’]
    '''
    inp_str = 'We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string'
    inp_str_list = inp_str.split()
    mobile_str = ''
    for i in inp_str_list:
        if i.isdigit() and len(i) >=10:
            mobile_str = mobile_str + i + ","

    print("The mobile number from the string is: ", mobile_str)

elif ch == 12:
    '''
    104). Write a program to print each character on a new line using python.
Input = ‘python’
Output:
p
y
t
h
o
n

    '''
    str_line = 'python'
    print("To print each character on a new line: ")
    for ch in str_line:
        print(ch)


elif ch == 13:
    '''
    103). Write a program to print a string 3 times using python.
Input = ‘sqatools’
Output = ‘sqatoolssqatoolssqatools’
    '''
    str_ch = 'sqatools'
    str_ch_op = 3 * str_ch
    print("To print a string 3 times: ", str_ch_op)

elif ch == 14:
    '''
    102). Write a program to remove repeated characters in a string and replace it with a single letter using python.
Input = ‘aabbccdd’
Output = ‘cabd’

    '''
    ch_str = 'aabbccdd'
    mult_ch_str = ''
    #count = 0
    #ch_str_list = ch_str.split()

    # for i in ch_str_list:
    #     print(i)

    for j in ch_str:
        if j not in mult_ch_str:
            mult_ch_str = mult_ch_str + j
            # if j in mult_ch_str:
            #     continue
        else:
            continue
        #break
    print(mult_ch_str)

elif ch == 15:
    '''
    101). Write a program to swap cases of a given string using python.
Input = ‘Learning Python’
Output = ‘lEARNING pYTHON’
    '''
    str_101 = 'Learning Python'
    print("The swap case of the given string: " + str_101.swapcase())

    #solution2;
    swap_str = ''

    for i in range(len(str_101)):
        if str_101[i].islower():
            swap_str = swap_str + str_101[i].upper()
        if str_101[i].isupper():
            swap_str = swap_str + str_101[i].lower()
        else:
            continue
    print("swap string: ", swap_str)

elif ch == 123:
    '''
    100). Write a program to find the first repeated character in a string and its index.
Input = ‘sqatools’
Output = (s,0)
    '''
    inp_str = 'sqatools'
    repeat_str = ''
    index_str = 0
    count = 0
    for i in inp_str:
        if i not in repeat_str:
            repeat_str = repeat_str + i
            count = count + 0
            if i in repeat_str:
                repeat_str = i
                index_str = 0 + inp_str.index(i)
        else:
            continue
    print(repeat_str, ",", index_str)

elif ch == 16:
    '''
    99). Write a program to print the index of each character in a string.
Input =  ‘sqatools’
Output :
Index of s is 0
Index of q is 1
Index of a is 2
Index of t is 3
Index of o is 4
Index of o is 5
Index of l is 6
Index of s is 7

    '''
    print("#"*50)
    inp_str_16 = 'sqatools'

    for i in inp_str_16:
        print(f"Index of {i} is {inp_str_16.index(i)}")

elif ch == 17:
    '''
    98). Write a program to reverse words in a string using python.
Input = ‘string problems’
Output = ‘problems string’
    '''
    inp_str_17 = 'string problems'
    inp_str_17_list = inp_str_17.split()
    print(inp_str_17_list)
    output = ''
    # for i in range(len(inp_str_17)):
    #     #output = inp_str_17[i]
    #     output = inp_str_17_list[]
    # print(output)
    print("The reverse words are: ", inp_str_17_list[::-1])
    opt_1 =inp_str_17_list[::-1]

    # str1 = "sqatools"
    #
    # for i in range(len(str1)):
    #     for j in range(i + 1, len(str1)):
    #         if str1[i] == str1[j]:
    #             print(f"({str1[i]},{str1.index(str1[i])})")
elif ch == 18:
    '''
    97). Write a program to add ly at the end of the string if the given string ends with ing.
Input = ‘winning’
Output = ‘winningly’
    '''
    str_ip_18 = 'winning'
    output_str_s8 = ''
    if str_ip_18.endswith('ing'):
        output_str_s8 = output_str_s8 + str_ip_18.replace('ing','ingly')
    print(output_str_s8)

    #solution 2:

    if str_ip_18[4:]=='ing':
        str_ip_18 = str_ip_18 + 'ly'
    print(str_ip_18)

elif ch == 19:
    '''
    96). Write a program to add ‘ing’ at the end of the string using python.
Input = ‘xyz’
Output = ‘xyzing’
    '''

    str_inp_19 = 'xyz'
    if len(str_inp_19) == 3:
        str_inp_19 = str_inp_19 + 'ing'
    print(str_inp_19)

elif ch == 20:
    '''
    94). Write a program to remove the kth element from the string
K=2
Input = ‘sqatools’
Output = ‘sqtools’
    '''
    str_inp_20 = 'sqatools'
    k = 2
    output_str_20= ''
    for i in range(len(str_inp_20)):
       if i != k:
           output_str_20 = output_str_20 + str_inp_20[i]
       else:
           continue
    print(output_str_20)



elif ch == 21:
    '''
    95). Write a program to check if a given string is binary or not.
Hint: Binary numbers only contain 0 or 1.

Input = ‘01011100’
Output = yes

Input = ‘sqatools 100’
Output = ‘No’

    '''

    str_ip_21 = '01011100'
    count = 0
    for i in range(len(str_ip_21)):
        if str_ip_21[i] == "0" or str_ip_21[i] == "1":
            count = count + 1
        else:
            continue
    print("length: ", len(str_ip_21))
    print("count: ", count)
    if len(str_ip_21) == count:
        print("yes, its binary number and value is: ", str_ip_21)
    else:
        print("no, its not a binary number and value is: ", str_ip_21)

    str_ip_21_2 = 'sqatools 100'
    count_2 = 0

    for j in range(len(str_ip_21_2)):
        if str_ip_21_2[j] == '0' or str_ip_21_2[j] == '1':
            count_2 = count_2 + 1
        else:
            continue

    print("digit: ", str_ip_21_2.isdigit())
    print("length: ", len(str_ip_21_2))
    print("count: ", count_2)

    if count_2 == len(str_ip_21_2):
        print("yes, binary and value: ",str_ip_21_2)
    else:
        print("no, its not binary and value: ",str_ip_21_2)