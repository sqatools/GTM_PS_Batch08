print("_"*50)
##########
#Q1 write a python program to get average of all list value without using any function or method.
list1 = [55, 66, 33, 22, 12]
total_sum = 0
count = 0

for i in list1:
    total_sum= total_sum + i
    count = count+1
average = total_sum/count
print(average) #37.6

print("_"*50)

# Q2 . write a python check value can be divide by 3 and 7

list2 = [9, 42, 33, 21, 28, 25]
# output : [42, 21]
for i in list2:
    if i%3 == 0 and i%7==0:
        print(i,end=" ")

print("_"*50)

print("_"*50)
#1). Python program to calculate the square of each number from the given list.

list3 = [3, 5, 7, 1, 8]
for i in list3:
    print( i,":",i**2)

print("_"*50)

#2). Python program to combine two lists.
List_One = [11,34,25,17]
List_Two = ['a','b','c','d']
print(List_One+List_Two) #[11, 34, 25, 17, 'a', 'b', 'c', 'd']
#Using extend method
(List_One.extend(List_Two))
print(List_One) # [11, 34, 25, 17, 'a', 'b', 'c', 'd']

print("_"*50)

#3). Python program to calculate the sum of all elements from a list.
List5 = [1,2,3,4,5]
sum1 = 0
count = 0
for i in List5:
    sum1 = sum1+ i
    count = count +1
print(sum1)  #15
#Using function
print(sum(List5))  #15


print("_"*50)

#4). Python program to find a product of all elements from a given list.
List5 = [1,2,3,4,5]

ele=1
for i in List5:
    ele = ele*i
print(ele)  #1*2*3*4*5=10


print("_"*50)

#5). Python program to find the minimum and maximum elements from the list.

list_5 = [23,56,12,89]
#Using max function
print(max(list_5)) #89
#Using min function
print(min(list_5)) #12


list_5.sort()
print("Min Number:",list_5[0]) #Min Number: 12
print("Max Number:",list_5[-1]) #Max Number: 89

print("_"*50)

#6). Python program to differentiate even and odd elements from the given list.

list6 =[23,11,78,90,34,55]
even = []
odd = []

for val in list6:
    if val%2 == 0:
        even.append(val)
    else:
        odd.append(val)
print("Odd list:", odd) #Odd list: [23, 11, 55]
print("Even List:",even) #Even List: [78, 90, 34]


print("_"*50)

#7). Python program to remove all duplicate elements from the list.

duplist =[23,11,34,78,90,11,5,34,55,23]

list6 = []

for value in duplist:
    if value not in list6:
        list6.append(value)
print(list6) #[23, 11, 34, 78, 90, 5, 55]

print("_"*50)

"""
#8). Python program to print a combination of 2 elements from the list whose sum is 10.
list8 = [4,6,5,3,7,5]
listEmpty = []
for val in list8:
    if 


"""
print("_"*50)

#9). Python program to print squares of all even numbers in a list.

List9= [2,5,6,7,9,10]
for val in List9:
    if val%2 == 0:
        print(val,"Square of even nio is:", val**2)

"""
Output:
2 Square of even nio is: 4
6 Square of even nio is: 36
10 Square of even nio is: 100
"""

print("_"*50)
"""
10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
"""
list10 = [5, 7, 2, 8, 11, 12, 17, 19, 22]

even=[]
odd=[]
for val in list10:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)
odd.extend(even)
print(odd)


print("_"*50)
"""
#11).  Python program to get common elements from two lists.
Input =
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
Outputt : [4, 5, 7, 2]
"""

list11_a = [4, 5, 7, 9, 2, 1]
list11_b = [2, 5, 8, 3, 4, 7]
commonele=[]

for value in list11_a:
    if value in list11_b:
        commonele.append(value)
print(commonele) #[4, 5, 7, 2]


print("_"*50)

#12). Python program to reverse a list with for loop.

list12= [4, 5, 7, 9, 2, 1]
for i in range(len(list12)-1,-1,-1):
    print(list12[i],end=" ")


print("_"*50)
#13). Python program to reverse a list with a while loop.



print("_"*50)

#14). Python program to reverse a list using index slicing.

list14 = [2,4,6,8]

Revlist = list14[::-1]

print(Revlist)

print("_"*50)
#15). Python program to reverse a list with reversed and reverse methods.


list15 = [2,3,7,9,3,1]

#using reverse method
list15.reverse()
print("Using reverse: ", list15) #[1, 3, 9, 7, 3, 2]

#Using reversed method
print("Using reversed: ",list(reversed(list1))) #  [12, 22, 33, 66, 55]


print("_"*50)
#16). Python program to copy or clone one list to another list.

list1 = [1,2,4,7,0,5]
list2 = []

for value in list1:
    list2.append(value)
print(list2)


print("_"*50)
#17). Python program to return True if two lists have any common member.

list1 = [2,4,7,8,3]
list2 = [4,5,0]
for val in list1:
    if val in list2:
        print("True")


print("_"*50)
#18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.

list1 = [3,4,8,7,0,1,6,9]
list2 =[]
for val in list1:


    print("_" * 50)

    """
#19).Python program to removenegativevalues  from the list.

list19 = [3,5,-8,0,-20,-55]
for i in list19:
   if i > = 0:
        print(i)

"""
print("_" * 50)

#20). Python program to get a list of all elements which are divided by 3 and 7.

listA= [3,7,0,2,6,14,88,21]
listB=[]
for i in listA:
    if i%3==0 or i%7==0:
       listB.append(i)
print(listB) #[3, 7, 0, 6, 14, 21]