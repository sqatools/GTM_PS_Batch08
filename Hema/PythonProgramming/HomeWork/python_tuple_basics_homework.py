#18 Feb'2025

'''
1. Write a program to get max from tuple without max function
ip: (55,77,203,5,1,7)
op:203
'''

ip_1 = (55,77,203,5,1,7)
op_1 = ()

max_val = ip_1[0]

for i in ip_1:
    if i > max_val:
        max_val=i
    else:
        continue
print("The maximum value is: ",max_val)

'''
2.write a python program to get list of combination of 2 values whose sum is 20
ip=(3,6,9,10,11,12,8,14,6)
op=(9,11)(12,8)(14,6)
'''
ip_var_2=(3,6,9,10,11,12,8,14,6)
sum=20
list_ip_var2=[]
for i in range(len(ip_var_2)):
    #print("i: ",ip_var_2[i], end=" ")
    for j in range(i+1, len(ip_var_2)):
        #print("j: ",ip_var_2[j], end=" ")
        if ip_var_2[i]+ip_var_2[j] == sum:
            list_ip_var2.append((ip_var_2[i],ip_var_2[j]))
        else:
            continue
print("The values are: ",list_ip_var2)
'''
3.write a python program to print removed values which is repeated more than two times and store it in list
ip=(1,3,1,4,1,5,3,6,3,7,3,4,6,4)
op=[5,6,7]

'''
#ip_3=(1,3,1,4,1,5,3,6,3,7,3,4,6,4)
#ip_3_1=(5,6,7)
#op_3=[]
#rem_val_3=[]
#op_3_1=[]
# count=0
# for i in range(len(ip_3)):
#     #print((ip_3.count(i)))
#     if ip_3.count(i) > 0:
#         count=count+1
#     #if i not in op_3:
#         op_3.append(ip_3[count])
#     else:
#         rem_val_3.append(ip_3[i])

#solution 1:

# for i in range(len(ip_3)):
#     #print(ip_3[i])
#     if ip_3.count(ip_3[i]) >2 :
#         print(ip_3[i])
#         #if ip_3[i] not in ip_3_1:
#         if ip_3[i] not in ip_3_1:
#             op_3_1.append(ip_3[i])
#         else:
#             continue
#     elif ip_3.count(ip_3[i]) <= 2:
#         print("----------",ip_3[i])
#         if ip_3[i] in ip_3_1:
#             rem_val_3.append(ip_3[i])

#print(rem_val_3)
#Not works
#solution 2:

# for i in ip_3:
#     if i in ip_3_1:
#         op_3_1.append(i)
#     else:
#         continue
# print(op_3_1)

#solution 3:
# count = 0
ip_3=(1,3,1,4,1,5,3,6,3,7,3,4,6,4)

rem_val_3=[]
op_3_1=[]

# for i in range(len(ip_3)):
#     if ip_3.count(ip_3[i]) <=2:
#         if ip_3[i] not in ip_3_1:
#             op_3_1.append(ip_3[i])
#         else:
#             rem_val_3.append(ip_3[i])

for i in ip_3:
    if ip_3.count(i) <=2 and i not in op_3_1:
        op_3_1.append(i)
    else:
        rem_val_3.append(i)

print(rem_val_3)
print(op_3_1)
#print(ip_3)