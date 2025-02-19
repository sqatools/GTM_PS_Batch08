#write a python program to remove duplicate values from list without using method
list1=[4,7,9,2,4,7,8]
#output=[4,7,9,2,8]
list1_1=[]
for x in list1:
    if x not in list1_1:
        list1_1.append(x)
    else:
        continue
print(list1_1)


#the above program using list comprehension
list1=[4,7,9,2,4,7,8]
list2=[]
result= [list2.append(x) for x in list1 if x not in list2]
print("remove duplicate values using list comprehension",list2)
print("_"*100)
#################################

#write a python program to move all positive value in left side of the list and negative values to the right side of list
list2=[4,-6,8,-22,77,-99,22,-12,56]
#output=[4,8,77,22,56,-6,-22,-99,-12]
list_positive=[]
list_negative=[]
for x in list2:
    if x>=0:
        list_positive.append(x)
    else:
        list_negative.append(x)
list_positive.extend(list_negative)
print("using Extend",list_positive)

#the above program using list concatenation

list2=[4,-6,8,-22,77,-99,22,-12,56]
#output=[4,8,77,22,56,-6,-22,-99,-12]
list_positive1=[]
list_negative1=[]
for x in list2:
    if x>=0:
        list_positive1.append(x)
    else:
        list_negative1.append(x)
print("using list concatenation",list_positive1+list_negative1)

#using list comprehension
list2=[4,-6,8,-22,77,-99,22,-12,56]
#output=[4,8,77,22,56,-6,-22,-99,-12]
l1=[]
l2=[]
result=[l1.append(x) if x>=0 else l2.append(x) for x in list2]
print("Using list comprehension",l1+l2)
print("_"*100)
print(result)

######################################
#Write a python program to get average of all list value without using any function or method.
list_c=[55,66,33,22,12]
sum=0
for x in list_c:
    sum=sum+x
Average=sum/len(list_c)
print(Average)





