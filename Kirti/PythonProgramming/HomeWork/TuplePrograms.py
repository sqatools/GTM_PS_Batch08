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