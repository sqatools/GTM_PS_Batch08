#Write a tuple program to get max from tuple without using max function
t1=(55,77,203,5,1,7)
maxnum=t1[0]
for x in t1:
    for y in range(0,len(t1)):
        if t1[y]>maxnum:
            maxnum=t1[y]
print("The maximum number is",maxnum)
print("_"*100)

##############################################################################
#Write a python program to get the list of combination of two values whose sum is 20

t2=(3,6,9,10,11,12,8,14,6)
for x in range(0,len(t2)):
    for y in range(x,len(t2)):
        if t2[x]+t2[y]==20:
            print((t2[x],t2[y]))
print("_"*100)

#################################################################################
#Write a python program to remove value which is repeated more than two times and store in list
t3=(1,3,1,4,1,5,3,6,3,7,3,4,6,4)
#output[5,6,7]
output=[]
for x in t3:
    if t3.count(x)<=2 and x not in output:
        output.append(x)
print(output)

#Using list comprehension
output1=[]
[output1.append(x) for x in t3 if t3.count(x)<=2 and x not in output1]
print("Using list comprehension",output1)
