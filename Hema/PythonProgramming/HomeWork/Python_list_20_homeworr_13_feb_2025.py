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

elif ch == 200:
    list_c = [55, 66, 33, 22, 12]
    sum = 0

    for i in list_c:
        sum = sum + i

    avg = sum/len(list_c)

    print(avg)

    list_inp_14 = [9,42,33,21,28,25]
    final_out_14 = []

    for i in list_inp_14:
        if i % 3 == 0 and i % 7 == 0:
            final_out_14.append(i)
        else:
            continue

    print("List of elements which are divisible by 3 and 7: ", final_out_14)

elif ch == 22:
    '''
    45). Python program to create a sublist of numbers and their squares from 1 to 10.
Output : [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100]]

    '''
    result_22 = [[x, x**2] for x in range(1,11)]
    print(result_22)

elif ch == 23:
    '''
    95). Python program to remove the 2nd character of each word from a given list.
Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Python’, ‘Language’]
Output: [‘Hllo’, ‘sudent’, ‘ae’, ‘larning’, ‘Pthon’, ‘Is’, ‘Pthon’, ‘Lnguage’]
    '''
    inp_var_23 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
    output_23 = []
    for i in inp_var_23:
        #print(i, end=" ")
        output_23.append(i[:1]+i[2:])

    print(output_23)

elif ch == 24:
    '''
    94). Python program to convert the 3rd character of each word to a capital case from the given list.
Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Python’, ‘Language’]
Output: [‘HelLo’, ‘stuDent’, ‘are’, ‘leaRning’, ‘PytHon’, ‘Its’, ‘PytHon’, ‘LanGuage’]
    '''
    inp_var_24 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']
    output_24 = []

    for i in inp_var_24:
        if len(i) > 3:
            output_24.append(i[:3]+i[3].upper()+i[4:])
        else:
            output_24.append(i)

    print(output_24)

elif ch == 25:
    '''
    93). Python program to replace ‘Java’ with ‘Python’ from the given list.
Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Python’, ‘Language’]
Output: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Java’, ‘Its’, ‘Java’, ‘Language’]
    '''
    inp_var_25 = ['Hello', 'student', 'are', 'learning', 'Python', 'Its', 'Python', 'Language']

    output_25 = []

    for i in range(len(inp_var_25)):

        if inp_var_25[i] == 'Python':
            inp_var_25[i] = 'Java'

    print(inp_var_25)

elif ch == 26:
    '''
    92). Python program to create a dictionary from a sublist in a given list.
Input: [[‘a’, 5], [‘b’, 8], [‘c’, 11], [‘d’, 14], [‘e’, 23]]
Output: {‘a’: 5, ‘b’: 8, ‘c’: 11, ‘d’: 14, ‘e’: 23}
    '''
    inp_var_26 = [['a', 5], ['b', 8], ['c', 11], ['d', 14], ['e', 23]]
    #result =
    output_26 = dict()
    #var_26 = []
    # for i in inp_var_26:
    #     for j in i:
    #         #print(i," ", j)
    #         print({i[0]: i[1]})
    #         #var_26.append(output_26)
    #         #print()
    # print(var_26)
    # out_27 = tuple()
    # print(out_27, type(out_27))
    for i in inp_var_26:
        #result = {i[0]:i[1]}
        #var_26.append(result)
        output_26[i[0]] = i[1]
    #print(var_26)
    print(output_26) #{'a': 5, 'b': 8, 'c': 11, 'd': 14, 'e': 23}

elif ch == 27:
    '''
    8). Python program to print a combination of 2 elements from the list whose sum is 10.
    '''
    var_27 = [2,5,8,1,5,7,3,9]
    num_27 = 10
    sum1 = []
    out_27 = []
    for i in range(len(var_27)):
        for j in range(i+1, len(var_27)):
            #sum = var_27[i] + var_27[j]
            #if sum == num_27:
            if var_27[i]+var_27[j] == num_27:
                sum1.append((var_27[i], var_27[j]))
            else:
                continue
    print(sum1)
    # for k in range(len(sum1)):
    #     if sum1[k] == num_27:
    #         out_27.append(sum1)
    #         continue
    #     else:
    #         out_27.append(k)
    # print(out_27)

    #doubt in class

    #Given a list of non - negative numbers and a target integer k, , check if the array has a continuous subarray of
    #size at least 2 that sums up to k

    # Example 1:

    # Input: [23, 2,4, 6, 7], k=6
    #
    # Output: True
    #
    # Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6
    # in_list_1 = [23, 2, 4, 6, 7]
    # k = 6
    # count = 0
    #
    # for i in range(0, len(in_list_1)):
    #     if in_list_1[i] < k:
    #         count += in_list_1[i]
    #         j = i + 1
    #         while count < k:
    #             count += in_list_1[j]
    #             j += 1
    #             if count == k:
    #                 print("True")
    #                 break
    #             else:
    #                 count = 0
    #     else:
    #         continue

elif ch == 28:
    '''
    13). Python program to reverse a list with a while loop.
    '''
    list_28=[1,2,3,4,5,6,7]
    #solution 1:
    count = 0
    while count <= len(list_28):
        temp = list_28[len(list_28)-1::-1]
        count=count+1
    print(temp)

    #solution2:
    count1 = len(list_28)-1
    out_28=[]
    while count1 >=0:
        out_28.append(list_28[count1])
        count1=count1-1
    print(out_28)

elif ch==29:
    '''
    16). Python program to copy or clone one list to another list.
    '''
    list_var_29 = [1.2,3,9,8,7]
    cop_list_var_29 = list_var_29.copy()
    print("Deep copy value is: ", cop_list_var_29)

    print("updating values")
    list_var_29.append(20)
    print("original list value after updating new value: ", list_var_29)
    print("Deep copy list value is: ", cop_list_var_29)

elif ch==30:
    '''
    17). Python program to return True if two lists have any common member.
    '''
    list_30 =[1,2,3,4]
    list_30_1 = [1,2,3,4]
    list_30_2 = ['a', 'b','c','d']
    list_30_3 = [1,2,5,6]
    if list_30 == list_30_1:
        print(bool(list_30 == list_30_1))
    else:
        print("False")

    if list_30 == list_30_2:
        print('True')
    else:
        print(bool(list_30 == list_30_2))
    if list_30 == list_30_3:
        print("True")
    else:
        print("False")

elif ch==31:
    '''
    18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
    '''
    #solution 1:

    list_var_31 = [1,2,3,4,5,6,7]
    list_var_1_31 = [1,3,6]

    out_31=[]
    for i in range(len(list_var_31)):
        if list_var_31[i]== 1 or list_var_31[i] == 3 or list_var_31[i] == 6:
            continue
        else:
            out_31.append(list_var_31[i])
    print(out_31)

    #solution 2:

    out_31_1 = []
    for i in range(len(list_var_31)):
        if list_var_31[i] in list_var_1_31:
            continue
        else:
            out_31_1.append(list_var_31[i])
    print(out_31_1)

elif ch ==32:
    '''
    19). Python program to remove negative values from the list.
    '''
    list_var_32 = [1, -5, 3, 6, -8, 9, -10]
    out_32 = []
    for i in range(len(list_var_32)):
        if list_var_32[i] < 0:
            continue
        else:
            out_32.append(list_var_32[i])
    print(out_32)

elif ch == 33:
    '''
    21). Python program to check whether the given list is palindrome or not. (should be equal from both sides).
    '''
    list_var_33 =[2,4,6,6,4,2]
    list_2_var_33 = []
    count = len(list_var_33)-1
    while count >= 0:
        list_2_var_33.append(list_var_33[count])
        count = count -1
    print(list_2_var_33)
    print(list_var_33)
    if list_2_var_33 == list_var_33:
        print("Its palindrome")
    else:
        print("Its not a palindrome")

elif ch ==34:
    '''
    89). Python program to get the list of all palindrome strings from the given list.
Input: [‘data’, ‘python’, ‘oko’, ‘test’, ‘ete’]
Output: [‘oko’, ‘ete’]
    '''
    inp_var_89 = ['data', 'python', 'oko', 'test', 'ete']
    out_var_89 = []
    rev_var_28 = []
    # count = len(inp_var_89)-1
    # while count>=0:
    #     rev_var_28.append(inp_var_89[count])
    #     count = count -1
    rev_var_28 = inp_var_89[::-1]
    for i in range(len(inp_var_89)):
        for j in range(len(rev_var_28)):
            if inp_var_89[i] == rev_var_28[j]:
                out_var_89.append(inp_var_89[i])

    print(out_var_89)