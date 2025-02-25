#write tuple program to get max from tuple without using max function.

my_tup=(6,7,4,9,44,23,64,21,1)
my_lst=list(my_tup)
my_lst.sort()
print(my_lst)
print(my_lst[8::])
print("*"*50)


#write a python program to get list of combination of two values whose sum is 20
import itertools

list1 = (3, 6, 9, 10, 11, 12, 8, 14, 6)

#Creating variable
var = 20

#Creating empty list
list3 = []

for i in range(len(list1)):
    for combi in itertools.combinations(list1,i):
        if sum(combi) == var:
            list3.append(combi)

#Printing output
print(list3)

print("*"*50)

"""l1 = (3, 6, 9, 10, 11, 12, 8, 14, 6)
for i in range(len(l1)):
    for j in range(len(l1)):
        if (i+j==20):
            print("(",i,j,")")
        else:
            continue"""
