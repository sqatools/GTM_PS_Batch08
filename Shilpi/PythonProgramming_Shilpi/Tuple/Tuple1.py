print("1). Python tuple program to create a tuple with 2 lists of data.")
# Input lists:
# list1 = [4, 6, 8]
# list2 = [7, 1, 4]
# Output= ((4, 7), (6, 1), (8, 4))

list1 = [4, 6, 8]
list2 = [7, 1, 4]
list3=tuple(zip(list1,list2))
print(list3)
print("_"*100)

list4=[4,6,8,7]
list5=[7,1,4]
list7=[]
for x in range(len(list4)):
    if x<=len(list5):
        list7.append((list4[x]))
    else:
        list7.append(list4[x])
print(list7)


tup11=(4,6,2)
sum1=sum(tup11)
print("Using sum function",sum1)

print("14). Python tuple program to add row-wise elements in Tuple Matrix")#Check approach
#No solution on website to check
# Input:
# A = [[(‘sqa’, 4)], [(‘tools’, 8)]]
# B = (3,6)
# Output:
# [[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]

A = [[('sqa', 4)], [('tools', 8)],[('shilpi', 3)]]
#[[('sqa', 4, 3)], [('tools', 8, 6)], [('shilpi', 3,4)],[(5)]]
B = (3,6)
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
######################################################################################
#17). Python tuple program to join tuples if the initial elements of the sub-tuple are the same.
# Input:
# [(3,6,7),(7,8,4),(7,3),(3,0,5)]
# Output:
# [(3,6,7,0,5),(7,8,4,3)]
Input=[(3,6,7),(7,8,4),(7,3),(3,0,5)]
output=[]
for x in range(len(Input)):
    for y in range(x+1,len(Input)):
        if Input[x][0]==Input[y][0]:
            output.append(tuple(list(Input[x])+list(Input[y][1:])))
print(output)