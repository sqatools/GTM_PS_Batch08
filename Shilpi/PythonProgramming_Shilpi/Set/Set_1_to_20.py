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

