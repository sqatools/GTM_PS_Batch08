#8,13,18,19,20(question not clear)
print("1). Python program to calculate the square of each number from the given list.")
list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print(i,":",i**2)
print("_"*100)

print("2). Python program to combine two lists.")
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=list1+list2
print("List using concatenation:",list3)
list1.extend(list2)
print("List using extend: ",list1)
print("_"*100)

print("3). Python program to calculate the sum of all elements from a list.")
list3=[3,7,9,12,6]
sum=0
for x in list3:
    sum +=x
print(sum)
print("_"*100)

print("4). Python program to find a product of all elements from a given list.")
list4=[3,4,5]
product=1
for x in list4:
    product=product*x
print(product)
print("_"*100)

print("5). Python program to find the minimum and maximum elements from the list.")
list5=[34,89,2,7,90]
print("The maximum number is: ",max(list5))
print("The minimum number is: ",min(list5))

print("6). Python program to differentiate even and odd elements from the given list.")
list6=[3,5,6,8,90,23,34,9]
for x in list6:
    if x%2==0:
        print(x,": Even")
    else:
        print(x, ": Odd")
print("_"*100)

print("7). Python program to remove all duplicate elements from the list.")
List7=["Sita","Ram","Laxman","Hanuman","Sita","Sita","Hanuman","Ram","Laxman"]
list8=[]
for x in List7:
    if x not in list8:
        list8.append(x)
    else:
        continue
print(list8)
print("_"*100)

print("8). Python program to print a combination of 2 elements from the list whose sum is 10.")
#Did not understand the solution on website using itertools. Check if this program is ok
# List8=[0,1,2,3,4,5,6,7,8,9,10]
List8=[2,5,8,5,1,9]
print("The 10s partner are as follows: ")
for x in range(0,len(List8)):
    for y in range(x+1,len(List8)):
        if List8[x]+List8[y]==10:
            print(List8[x],"+",List8[y],"=",List8[x]+List8[y])
        else:
            continue
print("_"*100)

print("9). Python program to print squares of all even numbers in a list.")
list9=[7,2,34,6,8,57]
for x in list9:
    if x%2==0:
        print(x,"^ 2 =",x**2)
print("_" * 100)

print("10). Python program to split the list into two-part, the left side all odd values and the right side all even values.")
        # Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
        # Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
list10=[5,7,2,8,11,12,17,19,22]
outputeven=[]
outputodd=[]
for x in list10:
    if x%2==0:
        outputeven.append(x)
    else:
        outputodd.append(x)
#concatenating
print(outputodd+outputeven)
#using extend
outputodd.extend(outputeven)
print(outputodd)
print("_"*100)

print("11).  Python program to get common elements from two lists.")
# Input =
# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]
# Output : [4, 5, 7, 2]
list11=[4,5,7,9,2,1]
list12=[2,5,8,3,4,7]
output=[]
for x in range(0,len(list11)):
    if list11[x] in list12:
        output.append(list11[x])
print(output)
print("_"*100)

print("12). Python program to reverse a list with for loop.")
list12=[8,5,6,34,98,0,3]
print("Original: ", list12)
rev=[]
for x in range(-1,-len(list12)-1,-1):
    rev.append(list12[x])
print("Reverse: ",rev)
print("_"*100)

print("13). Python program to reverse a list with a while loop.")
#Did not understand website solution
list12=[9,3,6,34,12,15,80,2]
print("Original list: ",list12)
list121=[]
x=0
y=-1
while x<len(list12):
    list121.append(list12[y])
    y=y-1
    x=x+1
print("Reverse: ",list121)
print("_"*100)

print("")

print("14). Python program to reverse a list using index slicing.")
list14=[6,4,8,9,2,12,3,5,15]
print(list14)
list141=list14[-1:-len(list14)-1:-1]
print(list141)

print("15). Python program to reverse a list with reversed and reverse methods.")
List15=[2,8,3,4,1,90,34]
List15.reverse()
print("Using reverse",List15)# This will modify the list
list16=[2,8,3,4,1,90,34]
result1=list(reversed(list16))# converts to iterator object so converted to list
print("Using reversed",result1)
print("_"*100)

print("16). Python program to copy or clone one list to another list.")
list17=[2,4,6,76,45,90,9]
list18=list17.copy()
print("Deep copy",list18)
list17.append(100)
list18.append(200)
print((list17))
print(list18)

#Shallow Copy
list19=[2,40,6,99,5,33,90]
list20=list19
list19.append(300)
list20.append(2000)
print(list19)
print(list20)

#Making a copy of one list to anothrer using logic
list21=[3,7,45,23,12,24,161]
list22=[]
for x in list21:
    list22.append(x)
print("Using Logic or for loop",list22)
print("_"*100)

print("17). Python program to return True if two lists have any common member.")
list23=[3,7,4,22,4]
list24=[8,0,90,3]
t=True
for i in range(0,len(list23)):
    for j in range(0,len(list24)):
        if list23[i]==list24[j]:
            t=True
        else:
            t=False
print("1st way",t)

d=True
for val in list23:
    if val in list24:
        d=True
    else:
        d=False
print("2nd way",d)
print("_"*100)

print("18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.")
#Did not understand the element and enumerate as shown in solution on website
List25=[3,4,8,7,0,1,6,9]
list26=[]
for x in range(0,len(List25)):
    if x==1 or x==3 or x==6:
        continue
    else:
        list26.append(List25[x])
print("1st method", list26)

List27=[3,4,8,7,0,1,6,9]
a=List27[1]
b=List27[3]
c=List27[6]
for d in List27:
    if d==a or d==b or d==c:
        List27.remove(d)
    else:
        continue
print("2nd method",List27)
print("_"*100)

print("19). Python program to remove negative values from the list.")
#why it is not considering the last negative value
List28=[4,5,-2,3,-5,9,-90,3,-30,-1]
for x in List28:
    print(x)
    if x<0:
        List28.remove(x)
        print(List28)
print(List28)

# List29=[4,5,-2,3,-5,9,-90,3,-30,-1]
# length=len(List29)
# for x in range(length):
#     if List29[x]<0:
#         List29.remove(List29[x])
#         length=length-1
#
#     else:
#         continue
# print(List29)

#The following method is working correctly
List30=[4,5,-2,3,-5,9,-90,3,-30,-1]
List_30=[]
for x in List30:
    if x<0:
        continue
    else:
        List_30.append(x)
print("Solution by appending to a new list",List_30)
print("_"*100)

# List_31=[3,5,-8,0,-20,-55]
# x=0
# y=len(List_31)
# print(y)
# while x<y:#0<6,1<6,2<6,3<5,4<5
#     if List_31[x]<0:
#         List_31.remove(List_31[x])#[3,5,0,-20,-55]
#         print(List_31)
#         print(len(List_31))
#         x+=1#3,5
#         y=y-1#5,4
#     else:
#         x+=1#1,2,4
#         continue

List_31=[3,5,-8,0,-20,-55]
for val in List_31:
    if val<0:
        print(val)
        List_31.remove(val)
print(List_31)


print("20). Python program to get a list of all elements which are divided by 3 and 7.")
#got confused did it as 'and' but solution says 'or'
List31=[3,4,7,21,49,42,84]
List32=[]
for x in List31:
    if x%3==0 and x%7==0:
        List32.append(x)
print(List32)

List33=[3,7,0,2,6,14,88,21]
list34=[]
for x in List33:
    if x%3==0 or x%7==0:
        list34.append(x)
print(list34)
print("_"*100)

print("# write a python program to return the output list this")
list1 = [55, 77, 88, 11, 23, 56, 77]
# output = [(55, 'odd'), (77, 'odd'), (88, 'even'), (11, 'odd'), (23, 'odd'), (26, 'even')]
#output2 = [{55: 'odd'}, {77 :'odd'}, {88: 'even'}, {11: 'odd'}, {23:'odd'}, {26: 'even'}]
 













