print('_'*50)
# Print the following pattern as shown using Python
"""
A
B C
D E F
G H I J
K L M N O
Q R S T
U V W
X Y
Z

"""
num1 = 65
for i in range(5):
    for j in range(i+1):
        print(chr(num1), end=" ")
        num1 += 1
    print()

for k in range(5, 0, -1):
    for l in range(k-1):
        num1 += 1
        print(chr(num1), end=" ")
    print()

print('_'*50)
# Program to find the maximum number from the list
list1 = [25,14,45,88,63,97,88,400]
max_1 = 0

for i in list1:
    if i > max_1:
        max_1 = i

print("Maximum number: ",max_1)

print('_'*50)
#Add elements from one list to another list

l1 = [2,5,8,0,1,4]
l2 = []

for ele in l1:
    l2.append(ele)

sorted(l2,reverse = True)
print(sorted(l2,reverse = True))

print('_'*50)
#Program to sort a list using for loop in Python.

li = [6,8,2,3,1,0,5]

for i in range(len(li)):
    for j in range(i,len(li)):
        if li[i]>li[j]:
            temp=li[i]
            li[i]=li[j]
            li[j]=temp
print(li)

