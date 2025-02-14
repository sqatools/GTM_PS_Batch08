#13th Feb'2025

ch = int(input("Enter number 1 to 100 to check list practice program: "))

if ch == 1:
    '''
    1). Python program to calculate the square of each number from the given list.
    '''

    list_inp_1 = [1,2,3,4,5,6,7]
    sq_out_list = []
    for i in list_inp_1:
        sq_out = i ** 2
        sq_out_list.append(sq_out)
    print("Calculation of the square of each number: ",sq_out_list)

elif ch==2:
    '''
    2). Python program to combine two lists.
    '''
    list_in_2 = [1,2,3,4]
    list_in_2_1 = [5,6,7,8]

    list_in_2_2 = list_in_2 + list_in_2_1
    print("combination of two list: ",list_in_2_2)

elif ch==3:
    '''
    3). Python program to calculate the sum of all elements from a list.
    '''
    list_inp_3 = [1,2,3,4]
    temp = 0

    for i in range(len(list_inp_3)):
        temp = temp + list_inp_3[i]

    print("The sum of all elements in list: ",temp)

    #solution2: using while loop

    count_3 = 0
    sum_3 = 0

    while count_3 < len(list_inp_3):
        sum_3 = sum_3 + list_inp_3[count_3]
        count_3 = count_3 + 1

    print("sum: ", sum_3)

elif ch == 4:
    '''
    4). Python program to find a product of all elements from a given list.
    '''
    list_inp_4 = [1,2,3,4,5]
    mul_out_5 = 1

    for i in list_inp_4:
        mul_out_5 = mul_out_5 * i

    print("product: ", mul_out_5)

    mul_out_5_1 = 1
    for j in range(len(list_inp_4)):
        mul_out_5_1 = mul_out_5_1 * list_inp_4[j]

    print("The product of all elements from given list: ", mul_out_5_1)

    mul_out_5_2 = 1
    count_5 = 0
    while count_5 < len(list_inp_4):
        mul_out_5_2 = mul_out_5_2 * list_inp_4[count_5]
        count_5 = count_5 + 1

    print("product using while loop: ", mul_out_5_2)

elif ch == 5:
    '''
    5). Python program to find the minimum and maximum elements from the list.
    '''


    list_inp_5 = [1,2,3,4,6,1]
    min_5 = list_inp_5[0]
    max_5 = list_inp_5[0]

    #count_5 = 0
    for i in list_inp_5:
        #count_5 = count_5 + list_inp_5[count_5]
        if i > max_5:
            max_5 = i
        elif i < min_5:
            min_5 = i

    #print(count_5)
    print(max_5)
    print(min_5)

elif ch == 6:
    '''
    6). Python program to differentiate even and odd elements from the given list.
    '''
    list_inp_6 = [12, 11, 14, 16, 13, 9]
    odd = []
    even = []

    for i in list_inp_6:
        if i%2 == 0:
            #print(list_inp_6[i])
            even.append(i)
        else:
            #print(i)
            odd.append(i)
    print(even)
    print(odd)

elif ch == 7:
    '''
    7). Python program to remove all duplicate elements from the list.
    '''
    list_inp_7 = [2, 3, 4, 5, 2, 6, 3]
    rem_duplicate_list_7 = []

    for i in list_inp_7:
        if i not in rem_duplicate_list_7:
            rem_duplicate_list_7.append(i)
        else:
            continue

    print(rem_duplicate_list_7)

elif ch == 8:
    '''
    9). Python program to print squares of all even numbers in a list.
    '''
    list_inp_8 = [8,1,2,3,4,5,6]
    sq_list_inp_8 = []

    for i in list_inp_8:
        if i%2 == 0:
            sq_list_inp_8.append(i**2)
        else:
            continue
    print("To print squares of all even number: ", sq_list_inp_8)

elif ch == 9:
    '''
    10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
    '''
    inp_9 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
    odd_9 = []
    even_9 = []

    for i in inp_9:
        if i%2 == 0:
            even_9.append(i)
        else:
            odd_9.append(i)

    print("Even: ", even_9)
    print("odd: ", odd_9)
    odd_9.extend(even_9)

    print("To split the list into two part: ", odd_9)

elif ch == 10:
    '''
    11).  Python program to get common elements from two lists.
Input =
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
Outputt : [4, 5, 7, 2]

    '''
    list1 = [4, 5, 7, 9, 2, 1]
    list2 = [2, 5, 8, 3, 4, 7]
    common_out_10 = []
    for i in list1:
        if i in list2:
            common_out_10.append(i)

    print("list1: ", list1)
    print("list2: ", list2)
    print("Common elements of two list are: ", common_out_10)

elif ch == 11:
    '''
    12). Python program to reverse a list with for loop.
    '''
    list_11 = [2, 1, 3, 5, 6]
    rev_list = []
    for i in range(len(list_11)-1,-1,-1):
        rev_list.append(list_11[i])

    print("reverse list: ", rev_list)

elif ch == 12:
    '''
    14). Python program to reverse a list using index slicing.
    '''
    list_inp_12 = [2,1,3,6,4]
    print("Reverse value using slicing: ", list_inp_12[::-1])

elif ch == 13:
    '''
    15). Python program to reverse a list with reversed and reverse methods.
    '''

    list_inp_13 = [1, 2, 3, 4, 5, 6]
    list_inp_13.reverse()
    print("reverse: ", list_inp_13)
    list_inp_13_1 = [1, 2, 3, 4, 5, 6]
    rev_list = list(reversed(list_inp_13_1))
    print("reversed: ", rev_list)

elif ch == 14:
    '''
    20). Python program to get a list of all elements which are divided by 3 and 7.
    '''
    list_inp_14 = [3, 7 , 21, 8, 49, 16, 27, 14, 10, 30, 35]
    final_out_14 = []

    for i in list_inp_14:
        if i %3 == 0 and i%7 ==0:
            final_out_14.append(i)
        else:
            continue

    print("List of elements which are divisible by 3 and 7: ", final_out_14)

elif ch == 15:
    '''
    22). Python Program to get a list of words which has vowels in the given string.
Input: “www Student ppp are qqqq learning Python vvv”
Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]
    '''
    inp_15 = 'www Student ppp are qqqq learning Python vvv'
    out_15 = []
    inp_15_list = inp_15.split()
    #out_15_1 = ''
    #vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in inp_15_list:
        #print(i)
        for j in i:
            if j=='a' or j=='e' or j=='i' or j=='o' or j =='u' or j=='A' or j=='E' or j=='O' or j=='I' or j=='U':
                out_15.append(i)
                break
            else:
                continue
    print(" to get a list of words which has vowels in the given string: ", out_15)

elif ch==16:
    '''
    38). Python program to replace the last and the first number of the list with the word.
Input: [12, 32, 33, 5, 4, 7]
output : [‘SQA’, 32, 33, 5, 4, ‘Tools’]
    '''
    inp_16 = [12, 32, 33, 5, 4, 7]
    inp_16[0] = 'SQA'
    inp_16[-1] = 'Tools'
    print(inp_16)

elif ch == 17:
    '''
    39). Python program to check whether the given element is exist in the list or not.
    '''

    # Input list
    list1 = [22, 45, 67, 11, 90, 67]
    num = 45
    #for i in range(len(list1)):
    if num in list1:
        print("The element ", num, " is available in list1", list1)
    else:
        print("not in list")

elif ch == 18:
    '''
    43). Python program to convert words of a list into a single string.
Input: [‘Sqa’, ‘Tools’, ‘Best’, ‘Learning’, ‘Platform’]
Output: SqaToolsBestLearningPlatform
    '''
    inp_18 = ['Sqa', 'Tools', 'Best', 'Learning', 'Platform']
    out_18 = ''
    for i in inp_18:
        print(i, end = "")



elif ch ==19:
    '''
    49). Python program to move all positive numbers on the left side and negative numbers on the right side.
Input: [2, -4, 6, 44, -7, 8, -1, -10]
Output: [2, 6, 44, 8, -4, -7, -1, -10]
    '''
    inp_19 =  [2, -4, 6, 44, -7, 8, -1, -10]
    negative_op_19 = []
    positive_op_19 = []

    for i in inp_19:
        if i < 0:
            negative_op_19.append(i)
        else:
            positive_op_19.append(i)

    print("The negative values are: ", negative_op_19)
    print("The positive values are: ", positive_op_19)

    positive_op_19.extend(negative_op_19)

    print("To move all positive numbers on the left side and negative numbers on the right side: ", positive_op_19)

elif ch ==20:
    '''
    50). Python program to move all zero digits to the end of a given list of numbers.
Input: [3, 4, 0, 0, 0, 0, 6, 0, 4, 0, 22, 0, 0, 3, 21, 0]
Output: [3, 4, 6, 4, 22, 3, 21, 0, 0, 0, 0, 0, 0, 0, 0]
    '''
    inp_list_20 =  [3, 4, 0, 0, 0, 0, 6, 0, 4, 0, 22, 0, 0, 3, 21, 0]
    out_20 = []
    zero_list = []
    for i in inp_list_20:
        if i != 0:
            out_20.append(i)
        else:
            zero_list.append(i)

    out_20.extend(zero_list)

    print("to move all zero digits to the end of a given list of numbers: ", out_20)

elif ch ==21:
    '''
    54). Python program to remove consecutive duplicates of given lists.
Input: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 4]

    '''
    inp_21 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    dup_list_21 = []

    for i in inp_21:
        if i not in dup_list_21:
            dup_list_21.append(i)
        else:
            continue
    print("to remove consecutive duplicates of given lists: ", dup_list_21)
