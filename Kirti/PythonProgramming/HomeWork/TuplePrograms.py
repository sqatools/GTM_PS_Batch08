"""
# Q1 : write tuple program to get max from tuple without using max function.
t1 = (55, 77, 203, 5, 1, 7)
output = 203
"""
t1 = (55, 77, 203, 5, 1, 7)
temp=0
for i in t1:
    if i>temp:
        temp=i
    else:
        continue
print("Max value = ",temp)


#==============================================================


"""
# Q2 : write a python program to get list of combination of two values whose sum is 20
t2 = (3, 6, 9, 10, 11, 12, 8, 14, 6)
(9, 11)
(12, 8)
(14, 6)
"""
t2 = (3, 6, 9, 10, 11, 12, 8, 14, 6)
list1=[]

for i in range(len(t2)):
    for j in range (i+1,len(t2)):
        if t2[i]+t2[j] == 20:
           list1.append((t2[i],t2[j]))
        else:
            continue
print(list1)


#===============================================================================

"""
#Q3 : write a python remove value which is repeated more two times and store in list.
t3 = (1, 3, 1, 4, 1, 5, 3, 6, 3, 7, 3, 4, 6 ,4)
output = [5, 6, 7]
"""
t3 = (1, 3, 1, 4, 1, 5, 3, 6, 3, 7, 3, 4, 6 ,4)
count=0
list2=[]
for val in t3:
    if t3.count(val)>2:
        continue
    elif val in list2:
        continue
    else:
        list2.append(val)
print(list2)

"""
Q-4 Python tuple program to create a tuple with 2 lists of data.
Input lists:
list1 = [4, 6, 8]
list2 = [7, 1, 4]
Output= ((4, 7), (6, 1), (8, 4))
"""
list1 = [4, 6, 8]
list2 = [7, 1, 4]
tup4=tuple(zip(list1, list2))
print("Program 4 : ",tup4)


"""
Q-5 Python tuple program to find the maximum value from a tuple.
Input = (41, 15, 69, 55)
Output = 69
"""
Input = (41, 15, 69, 55)
result= max(Input)
print("Program 5 result = ", result)

"""
Q 6. Python tuple program to find the minimum value from a tuple.
Input = (36,5,79,25)
Output = 5
"""
Input = (36,5,79,25)
result= min(Input)
print("Program 6 result = ", result)

"""
Q. 7: Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
Input = [4,6,3,8]
Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]
"""
list7 = [4,6,3,8]
list1=[]
for i in list7:
    temp = []
    temp.append(i)
    temp.append(i**2)
    list1.append(tuple(temp))

print("Program 7 result : ", list1)


"""
Q.8 : Python tuple program to create a tuple with different datatypes.
Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})
"""
tup = (2.6,1,'Python',True,[5, 6, 7],(5, 1, 4),{'a':123,'b':456})
print("Program 8 : Tuple: ",tup)



"""
Q.9 : Python tuple program to create a tuple and find an element from it by its index no.
Input = (4, 8, 9, 1)
Index = 2
Output = 9
"""
tup9 = (4, 8, 9, 1)
Index = 2
print("Program 9 = ", tup9[2])


"""
Q. 10 : Python tuple program to assign values of tuples to several variables and print them.
Input = (6,7,3)
Variables = a,b,c
Output:
a, 6
b, 7
c, 3
"""
tup10 = (6,7,3)
(a,b,c) = (6,7,3)

print("Program 10 : ")
print("a = ",a)
print("b = ",b)
print("c = ",c)


"""
Q. 11 Python tuple program to add an item to a tuple.
Input= ( 18, 65, 3, 45)
Output=(18, 65, 3, 45, 15)
"""
tup11 = ( 18, 65, 3, 45)
list11= list(tup11)
list11.append(15)

print("Program 11 = ", tuple(list11))


"""
Q. 12 : Python tuple program to convert a tuple into a string.
Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’, ‘l’, ‘s’)
Output = Sqatools
"""

tup12 = ("s", "q", "a", "t", "o", "o", "l", "s")
str12 =''
for i in tup12:
    str12+= i

print("Program 12 : ", str12)


"""
Q. 13  : Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’ ,’l’, ‘s’)
Output=
q
o
"""
tup13 = ("s", "q", "a", "t", "o", "o", "l", "s")
print("program 13 : ")
print("2nd element from the front :",tup13[1])
print("3rd element from the back : ",tup13[-3])


"""
Q. 14 .Python tuple program to check whether an element exists in a tuple or not.
Input = ( ‘p’ ,’y’, ‘t’, ‘h’, ‘o’, ‘n’)
P in A
Output=
True
"""
tup14 = ("p","y","t","h","o","n")
char_to_check = "P"
if char_to_check.lower() in tup14:
    print("True")
else:
    print("False")



"""
Q. 15 : Python tuple program to add a list in the tuple.
Input:
L=[12,67]
A=(6,8,4)
Output:
A=(6,8,4,12,67)
"""
L=[12,67]
A=(6,8,4)

A_list=list(A)
A_list= A_list + L
print("Program 15 : ", tuple(A_list))


"""
Q. 16 13). Python tuple program to find sum of elements in a tuple.
Input:
A=(4,6,2)
Output:
12
"""
tup16=(4,6,2)
print("Program 16 : ", sum(tup16))



"""
Q.17 : Python tuple program to create a tuple having squares of the elements from the list.
Input = [1, 9, 5,  7, 6]
Output = (1, 81, 25, 49, 36)
"""

list17 = [1, 9, 5,  7, 6]
list18 = []
for ele in list17:
    list18.append(ele**2)

tup17 = tuple(list18)
print("Program 17 : ", tup17)


"""
Q. 18 : Python tuple program to multiply adjacent elements of a tuple.
Input = (1,2,3,4)
Output =  (2,6,12)
"""
tup18 = (1,2,3,4)
list18 = list(tup18)
list19 = []
for i in range(len(list18)):
    if i+1 < len(list18):
        list19.append(list18[i]*list18[i+1])

tup19 = tuple(list19)
print("Program 18 : ", tup19)


"""
Q. 19 Python tuple program to convert a list into a tuple and multiply each element by 2.
Input = [12,65,34,77]
Output = (24, 130, 68, 154)
"""
list19 = [12,65,34,77]
list20 = []
for ele in list19:
    list20.append(ele * 2)

tup20 = tuple(list20)
print("Program 19 : ", tup20)


"""
Q. 20 : Python tuple program to remove an item from a tuple.
Input:
A=(p,y,t,h,o,n)
Output: (p,y,t,o,n)
"""
tup20 = ("p","y","t","h","o","n")
list20 = list(tup20)
list20.remove("h")
tup21 = tuple(list20)
print("Program 20: ", tup21)