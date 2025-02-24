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