#############
'''
Python tuple is a data structure that can hold any number of objects. A tuple is an immutable sequence of values
'''
##############
ch = int(input("Enter any number from 1 to 100 to check the program: "))

if ch == 1:
        '''
        1). Python tuple program to create a tuple with 2 lists of data.
Input lists:
list1 = [4, 6, 8]
list2 = [7, 1, 4]
Output= ((4, 7), (6, 1), (8, 4))

        '''

        ch = 'y'
        while ch == 'y':
            list1 = [4,6,8]
            list2 = [7,1,4]
            out_1 = ()
            # out_1_var = ((list1),(list2),)
            # print(out_1_var)
            #Not work:
            # for i in range(len(list1)):
            #     for j in range(len(list2)):
            #         out_1=out_1+((list1[i],list2[j]),)

            #### works
            len_of_list1 = len(list1)
            len_of_list2 = len(list2)
            if len_of_list1 == len_of_list2:
                for i in range(3):
                    out_1 = out_1 + ((list1[i],list2[i]),)
            else:
                print("length of the two list id different")
            print(out_1)
            ch = input("Do you still want to continue, type (n or y): ")
        print("thank you")

elif ch == 2:
    '''
    2). Python tuple program to find the maximum value from a tuple.
Input = (41, 15, 69, 55)
Output = 69
    '''
    var_2 = (41, 99, 15, 69, 55, 78)
    max_var_2 = var_2[0]

    for i in var_2:
        if max_var_2 < i:
            max_var_2 = i
        else:
            continue

    print("Output, the maximum value is: ", max_var_2)

elif ch == 3:
    '''
    3). Python tuple program to find the minimum value from a tuple.
Input = (36,5,79,25)
Output = 5
    '''
    var_3 = (36,5,79,25)
    min_var_3 = var_3[0]

    for i in var_3:
        if min_var_3 > i:
            min_var_3 = i
    print("The minimum value from a tuple is: ",min_var_3)

elif ch == 4:
    '''
    4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
Input = [4,6,3,8]
Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]
    '''
    var_4 = [4,6,3,8]
    result = [(x,x**2) for x in var_4]
    print(result)

elif ch == 5:
    '''
    5). Python tuple program to create a tuple with different datatypes.
Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})
    '''
    var_5 = ( 2.6, 1, 'Python', True, [5, 6, 7], (5, 1, 4), {'a': 123, 'b': 456})
    print("Tuple with different datatypes: ", var_5)

elif ch == 6:
    '''
    6). Python tuple program to create a tuple and find an element from it by its index no.
Input = (4, 8, 9, 1)
Index = 2
Output = 9
    '''
    var_6 = (4, 8, 9, 1)
    index_var = var_6.index(9)
    out_var = 0
    for i in range(len(var_6)):
        if var_6.index(var_6[i]) == index_var:
            out_var = out_var + var_6[i]

    print("The element value by its index no: ", out_var)

elif ch == 7:
    '''
    7). Python tuple program to assign values of tuples to several variables and print them.
Input = (6,7,3)
Variables = a,b,c
Output:
a, 6
b, 7
c, 3
    '''
    # var_7 = (6,7,3)
    # var_7_1 = 'a','b','c'
    #
    # len_var_7 = len(var_7)
    # len_var_7_1 = len(var_7_1)
    # print("Length of var: ", len_var_7)
    # out_7 = ()
    #
    # if len_var_7 == len_var_7_1:
    #     #print((var_7_1,var_7))
    #     for i in range(3):
    #         var_7_1 = var_7
    #     print()
    # print(var_7_1)

elif ch == 8:
    '''
    8). Python tuple program to add an item to a tuple.
Input= ( 18, 65, 3, 45)
Output=(18, 65, 3, 45, 15)
    '''
    inp_var_8 = (18,65,3,45)
    list_inp_var_8 = list(inp_var_8)

    list_inp_var_8.append(15)

    #print(list_inp_var_8)
    out_list_var8 = tuple(list_inp_var_8)
    print("Item updated: ", out_list_var8)

elif ch == 9:
    '''
    9). Python tuple program to convert a tuple into a string.
Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’, ‘l’, ‘s’)
Output = Sqatools

    '''

    inp_var_9 = ('s','q','a','t','o','o','l','s')

    #solution 1:

    for i in inp_var_9:
        print(i, end="")

    #solution 2:
    print()
    print("#"*50)
    str_9 = ''
    for j in inp_var_9:
        str_9 = str_9 + j
    print(str_9)
elif ch == 10:
    '''
    10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’ ,’l’, ‘s’)
Output=
q
o
    '''
    inp_var_9=('s','q','a','t','o','o','l','s')
    output_var_9 = inp_var_9[1: : 4]
    print(output_var_9)
    print("to get the 2nd element from the front : ", inp_var_9[1])
    print("To get the 3rd element from the back of the tuple: ", inp_var_9[-3])

elif ch == 11:
    '''

        11). Python tuple program to check whether an element exists in a tuple or not.
    Input = ( ‘p’ ,’y’, ‘t’, ‘h’, ‘o’, ‘n’)
    P in A
    Output=
    True
        '''
    inp_var_10 = ('p', 'y', 't', 'h', 'o', 'n')
    element = 'p'

    if element in inp_var_10:
        print('True')
    else:
        print('False')

elif ch == 12:
    '''
    12). Python tuple program to add a list in the tuple.
Input:
L=[12,67]
A=(6,8,4)
Output:
A=(6,8,4,12,67)
    '''
    L = [12,67]
    A = (6,8,4)

    var_L = tuple(L)
    output_var_12 = A + var_L

    print(output_var_12)

elif ch == 13:
    '''
    13). Python tuple program to find sum of elements in a tuple.
Input:
A=(4,6,2)
Output:
12
    '''
    inp_A_13 = (4,6,2)
    output_var_13 = 0
    for i in range(len(inp_A_13)):
        output_var_13 = output_var_13 + inp_A_13[i]

    print(output_var_13)

elif ch == 14:
    '''
    14). Python tuple program to add row-wise elements in Tuple Matrix
Input:
A = [[(‘sqa’, 4)], [(‘tools’, 8)]]
B = (3,6)
Output:
[[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]
    '''
    ##############  WORKING ###################
    A_var_14 = [[('sqa', 4)], [('tools', 8)]]
    B = (3,6)

    out_var_14 = []
    if len(A_var_14) == len(B):
        for i in range(len(A_var_14)):
            out_var_14 = out_var_14+[(A_var_14[i][0]+(B[i],))]
    print(out_var_14)

    # out_var_14_1 = A_var_14.extend(B)
    # print(out_var_14_1)

elif ch == 15:
    '''
    15). Python tuple program to create a tuple having squares of the elements from the list.
Input = [(1,5,7), (3,6)]
    Origianl tuple:  (1, 3, 5, 7, 6)
After sqauring elements:  (1, 9, 25, 49, 36)
    '''
    inp_var_15 = (1, 3, 5, 7, 6)
    out_var_15 = []
    list_inp_var_15 = list(inp_var_15)
    for i in list_inp_var_15:
        out_var_1_15 = i**2
        out_var_15.append(out_var_1_15)

    print("Tuple having squares: ", tuple(out_var_15))

elif ch == 16:
    '''
    16). Python tuple program to multiply adjacent elements of a tuple.
Input = (1,2,3,4)
Output =  (2,6,12)

    '''
    inp_var_16 = (1,2,3,4)
    out_var_16 =()
    for i in range(len(inp_var_16)-1):
        row = [(inp_var_16[i]*inp_var_16[i+1])]
        out_var_16 = out_var_16 + tuple(row)
    print(out_var_16)

elif ch == 17:
    '''
    17). Python tuple program to join tuples if the initial elements of the sub-tuple are the same.
Input:
[(3,6,7),(7,8,4),(7,3),(3,0,5)]
Output:
[(3,6,7,0,5),(7,8,4,3)]
    '''
    inp_var_17 = [(3,6,7),(7,8,4),(7,3),(3,0,5)]
    output_var_17 = []

    for i in range(len(inp_var_17)):
        #print(inp_var_17[i])
        #print(inp_var_17[i][0])
        for j in range(i+1, len(inp_var_17)):
            if inp_var_17[i][0] == inp_var_17[j][0]:
                output_var_17.append(inp_var_17[i]+inp_var_17[j],)
    print(output_var_17)

elif ch == 18:
    '''    
18). Python tuple program to convert a list into a tuple and multiply each element by 2.
Input = [12,65,34,77]
Output = (24, 130, 68, 154)
    '''
    inp_var_18 = [12,65,34,77]
    output_var_18 = []
    print("The input value is: ", inp_var_18)
    for i in inp_var_18:
        output_var_18.append(i*2)
        tup_output_var_18 = tuple(output_var_18)
    print("List output: ",output_var_18)
    print("convert list into a tuple and multiply each element by 2", tup_output_var_18)
elif ch == 19:
    '''
19). Python tuple program to remove an item from a tuple.
Input:
A=(p,y,t,h,o,n)
Output: (p,y,t,o,n)
    '''
    A = ('p','y','t','h','o','n')
    print("Original value: ",A)
    output_A = []
    for i in A:
        if i == 'h':
            continue
        else:
            output_A.append(i)
            tup_var_A = tuple(output_A)
    print("After remove an item in tuple: ", tup_var_A)

elif ch ==20:
    '''
    20). Python tuple program to slice a tuple.
Input:
A=(5,7,3,4,9,0,2)
Output:
(5,7,3)
(3,4,9)
    '''
    A_var_20 = (5, 7, 3, 4, 9, 0, 2)
    print(A_var_20[0:3])
    print(A_var_20[2:5])