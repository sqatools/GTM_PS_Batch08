#3,6
print("1). Python Dictionary program to add elements to the dictionary.")
dict1={}
dict1["FirstName"]="Shilpi"
dict1["LastName"]="Johri"
dict1["City"]="Allahabad"
dict1["Country"]="India"
dict1["Phone"]="9999999999"
print(dict1)
print("_"*100)

################################################################################################
print("2). Python Dictionary program to print the square of all values in a dictionary.")
# Input : {'a': 5, 'b':3, 'c': 6, 'd' : 8}
# Output :
# a : 25
# b : 9
# c : 36
# d : 64
dict2={'a':5,'b':3,'c':6,'d':8}
for x,num in dict2.items():
    print(x,":",num**2)
print("_"*100)
####################################QUESTION##########################################################
print("3). Python Dictionary program to move items from dict1 to dict2.")
#Please check my approach. Website approach I think will not leave dict1 {} empty.
# Input :
# dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
# dict2 = {}
# Output :
# dict1 = {}
# dict2 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
#
# Solution")
dict1={'name':'john','city':'London','country':'UK'}
dict2={}
# dict2.update(dict1)
# # for k,v in dict1.items():
# #     dict2[k]=v
# dict1.clear()
# print("dict1",dict1)
# print("dict2",dict2)

for k in dict1:
    dict2[k]=dict1[k]
dict1.clear()
print("dict1",dict1)
print("dict2",dict2)
print("_"*100)
###################################################################################################

print("4). Python Dictionary program to concatenate two dictionaries.")
# Input :
# dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
# dict2 = {'Age' : 25, 'salary': '$25k'}
# Output :
# dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan', 'Age' : 25, 'salary': '$25k'}
dict1={'Name':'Harry','Rollno':345,'Address':'Jordan'}
dict2={'Age':25,'salary':'$25k'}
dict1.update(dict2)
print("dict1 : ",dict1)
print("_"*100)
###################################################################################################
print("5). Python Dictionary program to get a list of odd and even keys from the dictionary.")
# Input :
# {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
# Output :
# Even Key = [[8, 'pqr'], [12, 'def'], [2, 'utv']]
# Odd Key = [[1, 25], [5, 'abc'], [21, 'xyz']]
dict5={1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}
print("Input : ",dict5)
Even_Key=[]
Odd_Key=[]
for k,v in dict5.items():
    if k%2==0:
        Even_Key.append([k,v])
    else:
        Odd_Key.append([k,v])
print("Even Keys =",Even_Key)
print("Odd Keys =",Odd_Key)
print("_"*100)

##################################QUESTION#################################################################
print("6). Python Dictionary Program to create a dictionary from two lists.")
#Please explain wesite solution and check my 2 approaches
# Input :
# list1 = ['a', 'b', 'c', 'd', 'e']|
# list2 = [12, 23, 24, 25, 15, 16]
# Output :
# {'a': 12, 'b': 23, 'c': 24, 'd': 25, 'e': 15}
#Using zip function
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
dict6=dict(zip(list1,list2))
print("Using zip function",dict6)

#Using for loop
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
dict3={}
for x in range(len(list1)):
    dict3[list1[x]]=list2[x]
print("Using for loop",dict3)
print("_"*100)

#############################QUESTION##################################################################
print("7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.")
#Please check my approach. The solution on the website is for loop and not list comprehension.
#Dictionary comprehension to be taught in class.
# Input :
# [4, 5, 6, 2, 1, 7, 11]
# Output :
# {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
#First approach when figuring out dict comprehension
list7=[4, 5, 6, 2, 1, 7, 11]
dict7={x:x**2 for x in list7 if x%2==0}
dict8={x:x**3 for x in list7 if x%2!=0}
dict7.update(dict8)
print(dict7)
#Better Solution using Dictionary comprehension
list7=[4, 5, 6, 2, 1, 7, 11]
dict9={x:x**2 if x%2==0 else x**3 for x in list7}
print(dict9)
# for loop solution
#Better Solution using Dictionary comprehension
list7=[4, 5, 6, 2, 1, 7, 11]
dict10={}
for x in list7:
    if x%2==0:
        dict10[x]=x**2
    else:
        dict10[x]=x**3
print(dict10)
print("_"*100)

###################################################################################################
print("8). Python Dictionary program to clear all items from the dictionary.")
dict8={2:4,3:9,4:16,5:25,6:36}
print("dict8: ",dict8)
dict8.clear()
print("dict8 after clearing:",dict8)
print("_"*100)

#####################################################################################################
print("9). Python Dictionary program to remove duplicate values from Dictionary.")
# Input :
# {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
# Output :
# {'a': 12, 'b': 2, 'd': 5, 'e': 35}
dict9={'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
print("Original list : ",dict9)
l1=[]
l2=[]
for k,v in dict9.items():
    l1.append(k)
    l2.append(v)
l2New=[]
for i in l2:
    if i not in l2New:
        l2New.append(i)
    else:
        l2New.append("None")
dict10=dict(zip(l1,l2New))
dict11={}
for k,v in dict10.items():
    if v!="None":
        dict11[k]=v
print("After removing duplicate keys: ",dict11)

#Better approach

dict9={'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
dict12={}
for k,v in dict9.items():
    if v not in dict12.values():
        dict12[k]=v
print(dict12)
print("_"*100)

###############################################################################################
print("10). Python Dictionary program to create a dictionary from the string.")
# Input  = 'SQATools'
# Output = {'S': 1, 'Q': 1, 'A': 1, 'T': 1, 'o': 2, 'l': 1, 's': 1}")
str1='SQATools'
dict10={}
for x in str1:
    dict10[x]=str1.count(x)
print(dict10)
print("_"*100)

####################################################################################################
print("11). Python Dictionary program to sort a dictionary using keys.")
# Input = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
# Output =
# ('a', 13)
# ('b', 53)
# ('c', 41)
# ('d', 21)")
dict11 = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
dict12=sorted(dict11)
dict14={}
for k in dict12:
    dict14[k]=dict11[k]
print(dict14)
print("_"*100)
##################################QUESTION#################################################################
print("12). Python Dictionary program to sort a dictionary in python using values.")
#Website solution not clear. Uses lambada. Please explain

# Input = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
# Output= (c, 1) (a,13) (d, 14) (b, 52)
dict12 = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
dict12_2={}
s2=sorted(dict12.values())
for y in range(len(s2)):
    for x in dict12:
        if dict12[x]==s2[y]:
            dict12_2[x]=dict12[x]

print(dict12_2)
print("_"*100)
#####################################################################################
print("13). Python Dictionary program to add a key in a dictionary.")
# Input= {1:’a’, 2:’b’}
# Output= (1:’a’, 2:’b’, 3:’c’}
dict2={1:'a',2:'b'}
dict2[3]='c'
print(dict2)

#Using update method
dict2_2={1:'a',2:'b'}
dict2_2.update({3:'c'})
print("Using update method: ",dict2_2)
print("_"*100)
############################################################################################
print("14). Python Dictionary program to concatenate two dictionaries.")
# Input:
# D1 = {'name’ : ’yash’, 'city’ :  'pune’}
# D1 = {'course’ : ’python’, 'institute’ : ’sqatools’}
# Output :
# { 'name’ : ’yash’, city: 'pune’, 'course’ : ’python’, 'institute’ : ’sqatools’ }

D1 = {'name' : 'yash', 'city' :  'pune'}
D2 = {'course' : 'python', 'institute' :'sqatools'}
D1.update(D2)
print(D1)
print("_"*100)
#################################QUESTION#############################################################
print("15). Python Dictionary program to swap the values of the keys in the dictionary.")
#The solution in website is to switch key and value not below. which is the correct question.
#website output {'yash': 'name', 'pune': 'city'}
# Input = {name:’yash’, city: "pune’}
# Output = {name:’pune’, city: "yash’}

dict15 = {'name':'yash', 'city': 'pune'}
l1=[]
l2=[]
l3=[]
for k,v in dict15.items():
    l1.append(k)
    l2.append(v)

for x in range(-1,-len(l2)-1,-1):
    l3.append(l2[x])
print(l1)
print(l3)
dict15_1=dict(zip(l1,l3))
print(dict15_1)

print("15). Python Dictionary program to swap the values with the keys in the dictionary.")
#Input = {name:’yash’, city: "pune’}
#Output={'yash': 'name', 'pune': 'city'}
dict15 = {'name':'yash', 'city': 'pune'}
dict15_2={}
for k,v in dict15.items():
    dict15_2[v]=k
print(dict15_2)
print("_"*100)

################################################################################################
print("16). Python Dictionary program to get the sum of all the items in a dictionary.")
# Input = {‘x’ : 23, ‘y’ : 10 , ‘z’ : 7}
# Output = 40
dict16={'x':23,'y':10,'z':7}
output=0
for k,v in dict16.items():
    output+=v
print(output)
print("_"*100)

##################################QUESTION#### PLEASE HELP ##################################################
print("17). Python program to get the size of a dictionary in python.")
# Hint : use sys.getsizeof(var) method.
# Input = {‘name’ : ’virat’, ‘sport’ : ’cricket’}
# Output = 232bytes")

print("_"*100)
##########################################QUESTION################################################################
print("18). Python Dictionary program to check whether a key exists in the dictionary or not.")
#different solution on website. Please check my approach and explain the website one
# Input:
# Dict1 = {city:’pune’, state=’maharashtra’}
# Dict1[country]
# Output= ‘key does not exist in dictionary
Dict1 = {'city':'pune', 'state':'maharashtra'}
keysearch='country'
if keysearch in Dict1:
    print(keysearch,"key is available in Dictionary")
else:
    print(keysearch, "key is not available in Dictionary")
print("_"*100)

############################################################################################################
print("19). Python program to iterate over a dictionary.")
# Input :
# Dict1 = {food:’burger’, type:’fast food’}
# Output :
# food : burger
# type : fast
Dict1 = {'food':'burger', 'type':'fast food'}
for k,v in Dict1.items():
    print(k,":",v)
print("_"*100)
###########################################################################################################
print("20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8")
# Input: n=4
# Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}
num=4
OutputDict={}
for x in range(1,num+1):
    OutputDict[x]=x**3
print(OutputDict)