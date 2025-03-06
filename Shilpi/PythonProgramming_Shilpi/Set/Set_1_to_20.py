# Check with sir for 14 max value third way.

print("1). Python program to create a set with some elements.")
set1={2,3,5,6,8,9,0,23}
print(set1,type(set1))
print("_"*100)

######################################################################################
print("2). Python program to add an element to a set.")
set2={3,5,6,7,8,90,12}
print("Original set :", set2)
set2.add(45)
print("New set after adding an element :",set2)
print("_"*100)
######################################################################################
print("3). Python program to remove an element from a set.")
set3={3,2,6,4,5,9,0,67}
print("Original set :", set3)
set3.remove(67)
print("New set after removing an element using remove method:",set3)
set3.discard(0)
print("New set after removing an element using discard method :",set3)
print("_"*100)
#########################################################################################
print("4). Python program to find the length of a set")
set4={2,3,4,5}
print(set4)
l1=len(set4)
print("Length of the set:",l1)
print("_"*100)
###########################################################################################
print("5). Python program to check if an element is present in a set.")
set5={1,2,3,4,5}
var1=2
if var1 in set5 :
    print(var1, "is present in the set")
else:
    print(var1,"is not present in the set")
print("_"*100)
############################################################################################
print("6). Python program to find the union of two sets.")
set6={1,2,3}
set6_1={4,5,6}
print("Original set 1:",set6)
print("Original set 2:",set6_1)
set6_2=set6.union(set6_1)
print("Set after using union",set6_2)
print("_"*100)
############################################################################################
print("7). Python program to find the intersection of two sets.")
set7={1,2,3,4,5,6,7}
set7_1={4,5,8,9,10}
set7_2=set7.intersection(set7_1)
print("Intersection of the two sets:",set7_2)
print("_"*100)
#############################################################################################
print("8). Python program to find the difference of two sets.")
set7={1,2,3,4,5,6,7}
set7_1={4,5,8,9,10}
set8=set7.difference(set7_1)
print("Difference set1:",set8)
set8_1=set7_1.difference(set7)
print("Difference set2:",set8_1)
print("_"*100)
#############################################################################################
print("9). Python program to find the symmetric difference of two sets.")
set7={1,2,3,4,5,6,7}
set7_1={4,5,8,9,10}
set9=set7.symmetric_difference(set7_1)
print("The symmetric difference",set9)
print("_"*100)
##############################################################################################
print("10). Python program to show if one set is a subset of another set.")
set10_1={2,4,6,8,10,12,14}
set10_2={2,4,6}
set10_3={2,3,4}
print("Subset:",set10_2.issubset(set10_1))#True
print("Subset:",set10_3.issubset(set10_1))#False
print("_"*100)
##############################################################################################
print("11). Python program to check if two sets are disjoint.")
set10_1={2,4,6,8,10,12,14}
set11_1={100,101,102}
set11_2={2,3,4}
print("Disjoint: ",set11_1.isdisjoint(set10_1))#True
print("Disjoint: ",set11_2.isdisjoint(set10_1))#False
print("_"*100)
##################################################################################################
print("12). Python program to convert a list to a set.")
l1=[2,3,4,5,6,2,4]
print("List: ",l1)
set12=set(l1)
print("List converted to set:",set12)
print("_"*100)
###################################################################################################
print("13). Python program to convert a set to a list.")
set12_1={2, 3, 4, 5, 6}
print(set12_1)
l1=list(set12_1)
print("set converted to list: ",l1)
print("_"*100)
###################################################################################################
print("14). Python program to find the maximum element in a set.")
set14={2,3,8,9,10,101}
mxval=0
for val in set14:
    if val>mxval:
        mxval=val
print("The maximum value using logic is: ",mxval)

set14={2,3,8,9,10,101}
maxval=max(set14)
print("The maximum value using max function in the set is:",maxval)

#By logic
set14={2,3,8,9,10,101}
l2=list(set14)
maxval1=0
for x in range(len(l2)):
    if l2[x]>maxval1:
        maxval1=l2[x]
print("Tha maximum value by list and logic is:",maxval1)

#Another method
set14={2,3,8,9,10,101}
l2=list(set14)
l2.sort()
print("Tha maximum value by using sort list method: ", l2[len(l2)-1])
print("_"*100)


########################################################################################################
print("15). Python program to find the minimum element in a set.")
set15={2,3,6,12,4,5,1}
minval=min(set15)
print(f"Minimum value using min function is {minval}")

#Another method by converting to list
set15={2,3,6,12,4,5,1,8,9}
l3=sorted(list(set15))
print(f"Minimum value is {l3[0]}")
print("_"*100)
##########################################################################################################
print("16). Python program to find the sum of elements in a set.")
set16={3,5,6,8,1,9}
sum1=sum(set16)
print(f"Sum using sum function is {sum1}")

set16={3,5,6,8,1,9}
sum2=0
for s in set16:
    sum2=sum2+s
print(f"The sum using logic is {sum2}")
print("_"*100)

####################################################################################################
print("17). Python program to find the average of elements in a set.")
set17={1,2,3,3,4,5,6,7}
sum3=0
for s in set17:
    sum3+=s
l=len(set17)
avg1=sum3/l
print(f"The average of numbers is {avg1}")
print("_"*100)
####################################################################################################
print("18). Python program to check if all elements in a set are even.")
set18={8,4,6,2,10,8}
count1=0
for x in set18:
    if x%2!=0:
        count1+=1

if count1>0:
    print("All elements in a set are not even")
else:
    print("All elements in a set are even")
print("_"*100)
####################################################################################################
print("19). Python program to check if all elements in a set are odd.")
set19={3,7,5,9}
count2=0
for x in set19:
    if x%2==0:
        count2+=1
print(count2)
if count2>0:
    print("All elements in the set are not odd")
else:
    print("All elements in the set are odd")
print("_"*100)
#######################################################################################################
print("20). Python program to check if all elements in a set are prime.")
set20={2,3,5,7,11}
count3=0
for x in set20:
    if x==1:
        break
    a=x//2
    for y in range(2,a+1):
        if x%y==0:
            count3=count3+1
if count3>0 or x==1:
    print("All elements in the set are not prime")
else:
    print("All elements in the set are prime")
print("_"*100)








