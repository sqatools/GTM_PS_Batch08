#Python dictionary 20 program

ch = int(input("Enter 1 to 20 to check programs: "))

if ch==1:
    '''
    1). Python Dictionary program to add elements to the dictionary.
    '''
    dic_var_1 = {}
    dic_var_1['id']=1
    dic_var_1['name']='Tom'
    print("After adding elements in dictionmary: ", dic_var_1)

elif ch ==2:
    '''
    2). Python Dictionary program to print the square of all values in a dictionary.
Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
Output :
a : 25
b : 9
c : 36
d : 64
    '''
    dict_var_2 ={'a': 5, 'b':3, 'c': 6, 'd' : 8}
    for k,v in dict_var_2.items():
        print(k, ":", v**2)

elif ch ==3:
    '''
    3). Python Dictionary program to move items from dict1 to dict2.
Input :
dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
dict2 = {}
Output :
dict1 = {}
dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
    '''
    dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
    dict2 = {}
    print("Dict1 before deleting: ", dict1)
    print("Dict2 before updating: ", dict2)
    for k,v in dict1.items():
        dict2[k]=v

    dict1.clear()
    print("dict1 after deleting: ", dict1)
    print("dict2 after updating: ", dict2)
elif ch==4:
    '''
    4). Python Dictionary program to concatenate two dictionaries.
Input :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’}
dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
Output :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}
    '''
    dict1_var_4 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
    dict2_var_4 = {'Age': 25, 'salary': '$25k'}
    print("Before concatenate dict1 value is: ", dict1_var_4)
    print("Before concatenate dict2 value is: ", dict2_var_4)
    for k,v in dict2_var_4.items():
        if dict2_var_4[k] not in dict1_var_4:
            dict1_var_4[k]=v
    print("After concarenating two dictionaries: ", dict1_var_4)
elif ch==5:
    '''
    5). Python Dictionary program to get a list of odd and even keys from the dictionary.
Input :
{1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’}
Output :
Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
    '''
    inp_var_5 = {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
    even_var_list=[]
    odd_var_list=[]

    for k,v in inp_var_5.items():
        #print(k, type(k))
        if k%2==0:
            #print(k)
            even_var_list.append([k,v])
        else:
            #print(k)
            odd_var_list.append([k,v])
    print("Even key: ",even_var_list)
    print("Odd key: ",odd_var_list)

elif ch==6:
    '''
    6). Python Dictionary Program to create a dictionary from two lists.
Input :
list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
list2 = [12, 23, 24, 25, 15, 16]
Output :
{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}
    '''
    list1 = ['a', 'b', 'c', 'd', 'e']
    list2 = [12, 23, 24, 25, 15, 16]
    dict_var_6 = {}

    for i in range(len(list1)):
        if i < len(list2):
            dict_var_6[list1[i]] = list2[i]
        else:
            dict_var_6[list1[i]] = None

    print(dict_var_6)

elif ch == 7:
    '''
    7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
Input :
[4, 5, 6, 2, 1, 7, 11]
Output :
{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
    '''
    inp_dict_7 = [4, 5, 6, 2, 1, 7, 11]
    out_dict_7 = {}

    for i in range(len(inp_dict_7)):
        if inp_dict_7[i]%2 ==0:
            out_dict_7[inp_dict_7[i]] = inp_dict_7[i]**2
        else:
            out_dict_7[inp_dict_7[i]] = inp_dict_7[i]**3
    print(out_dict_7)

    '''
    str1 = 'Hello we are learning python'
    vowels='aeiou'
    out_str1 =''
    for ch in str1:
        if ch in vowels and ch not in out_str1:
            out_str1 = out_str1 + ch
        elif ch not in vowels:
            out_str1 = out_str1 + ch
        else:
            continue

    print(out_str1)


    l1 = [4,76,9,22,55,77,8]
    l2 = [4,22,5,66,7,22,67,8]
    set_l1 =set(l1)
    set_l2 =set(l2)

    diff_out = set_l1.difference(set_l2)
    common_val = set_l1.intersection(set_l2)

    print(diff_out)
    print(common_val)

    print("list diff_out: ",list(diff_out))
    print("common: ", list(common_val))
    '''

elif ch==8:
    '''
    8). Python Dictionary program to clear all items from the dictionary.
    '''
    var_dict_8= {1:'a', 2:'b', 3:'c'}
    print("Before clearing values: ", var_dict_8)
    var_dict_8.clear()
    print("After clearing values: ",var_dict_8)

elif ch==9:
    '''
    9). Python Dictionary program to remove duplicate values from Dictionary.
Input :
{‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
Output :
{‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
    '''
    inp_var_9={'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
    output={}

    for k,v in inp_var_9.items():
        if v not in output.values():
            output[k]=v
        else:
            continue
    print(output)

elif ch==10:
    '''
    10). Python Dictionary program to create a dictionary from the string.
Input  = ‘SQATools’
Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
    '''
    inp_var_10 = 'SQATools'
    output_var_10={}

    for i in inp_var_10:
        if i not in output_var_10:
            output_var_10[i]=inp_var_10.count(i)
        else:
            continue
    print(output_var_10)

elif ch==11:
    '''
    11). Python Dictionary program to sort a dictionary using keys.
Input = {‘d’ : 21, ‘b’ : 53,  ‘a’: 13, ‘c’: 41}
Output =
(‘a’, 13)
(‘b’, 53)
(‘c’, 41)
(‘d’, 21)
    '''
    inp_var_11 = {'d': 21, 'b': 53, 'a': 13, 'c': 41}

    # for k,v in inp_var_11.items():
    #     print((k,v))

    for i in sorted(inp_var_11):
        print((i,inp_var_11[i]))

elif ch==12:
    '''
    12). Python Dictionary program to sort a dictionary in python using values.
Input = {‘d’ : 14, ‘b’ : 52,  ‘a’: 13, ‘c’: 1 }
Output= (c, 1) (a,13) (d, 14) (b, 52)
    '''
    #Doubt
    inp_var_12 = {'d': 14, 'b': 52,  'a': 13, 'c': 1}


elif ch==13:
    '''
    13). Python Dictionary program to add a key in a dictionary.
Input= {1:’a’, 2:’b’}
Output= (1:’a’, 2:’b’, 3:’c’}
    '''
    inp_var_13={1:'a', 2:'b'}
    inp_var_13[3] = 'c'
    print(inp_var_13)

elif ch==14:
    '''
    14). Python Dictionary program to concatenate two dictionaries.
Input:
D1 = {‘name’ : ’yash’, ‘city’ :  ‘pune’}
D1 = {‘course’ : ’python’, ‘institute’ : ’sqatools’}
Output :
{ ‘name’ : ’yash’, city: ‘pune’, ‘course’ : ’python’, ‘institute’ : ’sqatools’ }
    '''
    D1 = {'name': 'yash', 'city':  'pune'}
    D2 = {'course': 'python', 'institute': 'sqatools'}
    D1.update(D2)
    print(D1)

elif ch==15:
    '''
    15). Python Dictionary program to swap the values of the keys in the dictionary.
Input = {name:’yash’, city: ‘pune’}
Output = {name:’pune’, city: ‘yash’}
    '''
    #doubt:
    inp_var_15 = {'name':'yash', 'city': 'pune'}

elif ch ==16:
    '''
    16). Python Dictionary program to get the sum of all the items in a dictionary.
Input = {‘x’ : 23, ‘y’ : 10 , ‘z’ : 7}
Output = 40
    '''
    inp_var_16 = {'x': 23, 'y': 10, 'z': 7}
    out_var_16=0
    for i in inp_var_16.values():
        out_var_16 = out_var_16 + i
    print("the sum of dictionary items: ",out_var_16)

elif ch == 17:
    '''
    17). Python program to get the size of a dictionary in python.
Hint : use sys.getsizeof(var) method.
Input = {‘name’ : ’virat’, ‘sport’ : ’cricket’}
Output = 232bytes
    '''

elif ch==18:
    '''
    18). Python Dictionary program to check whether a key exists in the dictionary or not.
Input:
Dict1 = {city:’pune’, state=’maharashtra’}
Dict1[country]
Output= ‘key does not exist in dictionary
    '''
    #doubt
    Dict1 = {'city':'pune','state':'maharashtra'}
    #print(Dict1['country'])
    count = 0
    for k in Dict1.keys():
        #print(k)
        if k == 'country':
            count = count+1

    if count >0:
        print("Key exists")
    else:
        print("Key not exists")

elif ch==19:
    '''
    19). Python program to iterate over a dictionary.
Input :
Dict1 = {food:’burger’, type:’fast food’}
Output :
food : burger
type : fast food
    '''
    Dict1_var19 = {'food':'burger', 'type':'fast food'}
    for k,v in Dict1_var19.items():
        print(k, ":", v)

elif ch==20:
    '''
    20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
Input: n=4
Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}
    '''
    n = 4
    output_dict_20 = {}
    for i in range(n+1):
        if i > 0:
            output_dict_20[i] = i **3
        else:
            continue
    print(output_dict_20)

elif ch==21:
    '''
    21). Python Dictionary program to insert a key at the beginning of the dictionary.
Input = { ‘course’ : ’python’,  ‘institute’ : ’sqatools’ }
Insert : ( ‘name’ : ’omkar’ )
Output= { ‘name’ : ’omkar’, ‘course’ : ’python’, ‘institute’ : ’sqatools’}
    '''
    inp_var_21 = { 'course': 'python', 'institute': 'sqatools'}
    inp_var_21_2 = {'name': 'omkar'}
    inp_var_21_2.update(inp_var_21)
    print(inp_var_21_2)

elif ch==22:
    '''
    22). Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.
Output ={1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}
    '''

    output_var_22 = {}
    for i in range(1,6):
        output_var_22[i] = i**2
    print(output_var_22)

elif ch==23:
    '''
    23). Python Dictionary program to find the product of all items in the dictionary.
Input = { ‘a’ : 2, ‘b’ : 4, ‘c’ : 5}
Output = 40
    '''
    inp_var_23 = { 'a': 2, 'b': 4, 'c': 5}
    output_val_23 = 1
    for v in inp_var_23.values():
        output_val_23 = output_val_23 * v

    print(output_val_23)