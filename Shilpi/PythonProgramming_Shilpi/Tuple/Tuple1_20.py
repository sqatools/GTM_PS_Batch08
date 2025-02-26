"""
print("1). Python tuple program to create a tuple with 2 lists of data.")
# Input lists:
# list1 = [4, 6, 8]
# list2 = [7, 1, 4]
# Output= ((4, 7), (6, 1), (8, 4))

list1 = [4, 6, 8]
list2 = [7, 1, 4]
output1=[]
for x in range(0,len(list1)):
    for y in range(x,x+1):
        output1.append((list1[x],list2[y]))
result1=tuple(output1)
print(result1)

#Using zip function
list1 = [4, 6, 8]
list2 = [7, 1, 4]
list3=tuple(zip(list1,list2))
print("Using zip function",list3)


#Method 3-One for loop
list1 = [4, 6, 8]
list2 = [7, 1, 4]
output20=[]
for x in range(len(list1)):
    output20.append((list1[x],list2[x]))
print(tuple(output20))
print("_"*100)
##################################################################################
print("2). Python tuple program to find the maximum value from a tuple.")
# Input = (41, 15, 69, 55)
# Output = 69
tup1=(41, 15, 69, 55)
maxnum=tup1[0]
for x in range(0,len(tup1)):
    for y in tup1[x+1:]:
        if y>maxnum:
            maxnum=y
print("The maximum number is :",maxnum)
print("_"*100)
##################################################################################

print("3). Python tuple program to find the minimum value from a tuple.")
# Input = (36,5,79,25)
# Output = 5
tup2=(36,5,79,25)
minnum=tup2[0]
for x in range(0,len(tup2)):
    for y in tup2[x+1:]:
        if y<minnum:
            minnum=y
print("The minimum number is : ",minnum)
print("_"*100)

#####################################################################################

print("4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.")
# Input = [4,6,3,8]
# Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]
tup3=[4,6,3,8]
output=[]
for x in tup3:
    output.append((x,x**2))
print(output)

#Using list comprehension
result2=[(x,x**2) for x in tup3]
print("Using list comprehension",result2)
print("_"*100)

########################################################################################
print("5). Python tuple program to create a tuple with different datatypes.")
# Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})
tup4=(2.6,1,'Python',True,[5,6,7],(5,1,4),{'a':123,'b':456})
print(tup4,type(tup4))
print("_"*100)

##########################################################################################
print("6). Python tuple program to create a tuple and find an element from it by its index no.")
# Input = (4, 8, 9, 1)
# Index = 2
# Output = 9
tup5=(4,8,9,1)
i=int(input("Enter the index number: "))
print("The element in the Tuple at index position",i,"is",tup5[i])

##############################################################################################
print("7). Python tuple program to assign values of tuples to several variables and print them.")
# Input = (6,7,3)
# Variables = a,b,c
# Output:
# a, 6
# b, 7
# c, 3

Input=(6,7,3)
a,b,c=Input
print("a,",a)
print("b,",b)
print("c,",c)
print("_"*100)
#################################################################
print("8). Python tuple program to add an item to a tuple.")
# Input= ( 18, 65, 3, 45)
# Output=(18, 65, 3, 45, 15)
tup6=(18,65,3,45)
print("Original tuple :",tup6)
l1=list(tup6)
l1.append(15)
tup6=tuple(l1)
print("Updated Tuple: ",tup6)
print("_"*100)

#####################################################################
print("9). Python tuple program to convert a tuple into a string.")
# Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’, ‘l’, ‘s’)
# Output = Sqatools
tup7=('s','h','i','l','p','i')
str1=""
for x in tup7:
    str1+=x
print(str1)

#using join method
tup8=('s','h','i','l','p','i')
print("Using join method: ",''.join(tup8))
print("_"*100)
#######################################################################
print("10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.")
# Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’ ,’l’, ‘s’)
# Output=
# q
# o

tup8=('s','q','a','t','o','o','l','s')
print("2nd element from the front of the tuple: ",tup8[1])
print("3rd element from the back of the tuple: ",tup8[-3])
print("_"*100)

#########################################################################
print("11). Python tuple program to check whether an element exists in a tuple or not.")
# Input = ( ‘p’ ,’y’, ‘t’, ‘h’, ‘o’, ‘n’)
# P in A
# Output=
# True
tup9=('p','y','t','h','o','n')
result=True if 'p' in tup9 else False
print(result)
print("_"*100)
############################################################################
print("12). Python tuple program to add a list in the tuple.")
# Input:
L=[12,67]
A=(6,8,4)
# Output:
# A=(6,8,4,12,67)
A=list(A)
B=tuple(A+L)
print("Using Concatenation",B,type(B))

#using extend
A.extend(L)
tup10=tuple(A)
print("Using extend",tup10)
print("_"*100)
"""
####################################################################################
print("13). Python tuple program to find sum of elements in a tuple.")
# Input:
# A=(4,6,2)
# Output:
# 12
tup11=(4,6,2)
sum1=0
for x in tup11:
    sum1+=x
print("The sum is :", sum1)

#Using sum function
tup11=(4,6,2)
s1=sum(tup11)
print("Using sum function",s1)
print("_"*100)

######################################QUESTION###############################
print("14). Python tuple program to add row-wise elements in Tuple Matrix")#Check approach
#No solution on website to check
# Input:
# A = [[(‘sqa’, 4)], [(‘tools’, 8)]]
# B = (3,6)
# Output:
# [[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]
# tupA=[[('sqa',4)],[('tools',8)]]
# tupB=(3,6)
# print("Input A : ",tupA)
# print("Input B : ",tupB)
# l1=list(tupA[0][0])
# l2=list(tupA[1][0])
# l1.append(tupB[0])
# l2.append(tupB[1])
# tup1=tuple(l1)
# tup2=tuple(l2)
# Output=[[tup1],[tup2]]
# print("Output : ",Output)

#Other approach which works for more than any number of elements(but equal) in both the input A and B
A = [[('sqa', 4)], [('tools', 8)],[('shilpi', 3)]]
B = (3,6,12)
Output3=[]
l1=[]
for x in range(len(A)):
    C=list(A[x][0])
    C.append(B[x])
    A[x][0]=tuple(C)

print(A)

#This approach deals with more items in A or B. Please check if the approach is correct. also please check if this
#is giving the output as desired. The stry items in B will not appear inside a tuple in a list as they are single
#items. is that acceptable?
A = [[('sqa', 4)], [('tools', 8)],[('shilpi', 3)]]
#[[('sqa', 4, 3)], [('tools', 8, 6)], [('shilpi', 3,4)],[(5)]]
B = (3,6,4,5)
#len(A)=len(B)
l1=[]

if len(A)==len(B):
    for x in range(len(A)):
        C=list(A[x][0])
        C.append(B[x])
        A[x][0]=tuple(C)
elif len(A)>len(B):
    for x in range(len(B)):
        C = list(A[x][0])
        C.append(B[x])
        A[x][0] = tuple(C)
elif len(A)<len(B):
    for x in range(len(B)):#b=4 a 3
        if x<len(A):
            C = list(A[x][0])
            C.append(B[x])
            A[x][0] = tuple(C)
        else:
            l1.append(B[x])
A.extend(l1)
print(A)
print("_"*100)

#############################QUESTION#####################################
print("15). Python tuple program to create a tuple having squares of the elements from the list.")
#Output not same as required by the program. The solution on website uses straight forward tuple (1,3,5,7,6)
#Please check my program
# Input = [(1,5,7), (3,6)]
# Output = (1, 81, 25, 49, 36)
Input1=[(1,5,7),(3,6)]
Output1=[]
for x in range(0,len(Input1)):
    for y in Input1[x]:
        Output1.append(y**2)
print(Output1)

#Input=(1,3,5,7,6)
#Output=(1, 9, 25, 49, 36)
Input2=(1,3,5,7,6)
print("Input",Input2)
Output2=[x**2 for x in Input2]
print("The Output is ",tuple(Output2))
print("_"*100)

###############################################################################################
print("16). Python tuple program to multiply adjacent elements of a tuple.")
# Input = (1,2,3,4)
# Output =  (2,6,12)
Input2=(1,2,3,4)
print("Input : ",Input2)
Output=[]
for x in range(0,len(Input2)-1):
    Output.append(Input2[x]*Input2[x+1])
Outputtup=tuple(Output)
print("Output :",Outputtup)
print("_"*100)

######################################QUESTION#############################################################
#Please check approack. Solution not on website
print("17). Python tuple program to join tuples if the initial elements of the sub-tuple are the same.")
# Input:
# [(3,6,7),(7,8,4),(7,3),(3,0,5)]
# Output:
# [(3,6,7,0,5),(7,8,4,3)]
# Input3=[(3,6,7),(7,8,4),(7,3),(3,0,5)]
# print("Input :",Input3)
# Output2=[]
# for x in range(0,len(Input3)):
#     for y in range(x+1,len(Input3)):
#         if Input3[x][0]==Input3[y][0]:
#             Output2.append(Input3[x]+Input3[y])# how are we able to concatenate tuple when we cannot change the value of tuple
# print(Output2)
# newlist1=[list(i) for i in Output2]
# print(newlist1)
# Output3=[]
# for a in range(0,len(newlist1)):
#     for b in newlist1[a]:
#         if b in newlist1[a]:
#             print(b)

#17). Python tuple program to join tuples if the initial elements of the sub-tuple are the same.
# Input:
# [(3,6,7),(7,8,4),(7,3),(3,0,5)]
# Output:
# [(3,6,7,0,5),(7,8,4,3)]
Input3=[(3,6,7),(7,8,4),(7,3),(3,0,5)]
New_Input=[list(i) for i in Input3]
print("Input: ",Input3)
print(New_Input)
Output2=[]
for x in range(0,len(New_Input)):
    for y in range(x+1,len(New_Input)):
        if New_Input[x][0]==New_Input[y][0]:
            Output2.append(New_Input[x]+New_Input[y][1:])
print(Output2)
Outputfinal=[tuple(c) for c in Output2]
print("Output : ",Outputfinal)
print("_"*100)

##################################################################################################
print("18). Python tuple program to convert a list into a tuple and multiply each element by 2.")
# Input = [12,65,34,77]
# Output = (24, 130, 68, 154)
Input4=[12,65,34,77]
print("Input : ",Input4)
Output4=tuple([x*2 for x in Input4])
print("Tuple Output after multiplying by 2 :",Output4)
print("_"*100)

##################################################################################################
print("19). Python tuple program to remove an item from a tuple.")
# Input:
# A=(p,y,t,h,o,n)
# Output: (p,y,t,o,n)
Input=('p','y','t','h','o','n')
A=list(Input)
A.remove('h')
B=tuple(A)
print("Output:",B)
print("_"*100)
######################################################################################################
print("20). Python tuple program to slice a tuple.")
# Input:
# A=(5,7,3,4,9,0,2)
# Output:
# (5,7,3)
# (3,4,9)
A=(5,7,3,4,9,0,2)
B=A[0:3]
print(B)
C=A[2:5]
print(C)
print("_"*100)
###############################################################################################################
print("21). Python tuple program to find an index of an element in a tuple.")
# Input:
# A=(s,q,a,t,o,o,l,s)
# Index of a?
# Output = 2
A=('s','q','a','t','o','o','l','s')
B=input("Enter the letter to find the index of : ")
I=A.index(B)
print("Index of",B,"is",I)
