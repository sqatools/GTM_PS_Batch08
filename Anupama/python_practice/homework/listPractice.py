#*** program to calculate square of the values in list**
list1 = [3, 5, 7, 1, 8]

for val in list1:
    print(val, ":", val**2)
print("-"*50)

#**program to slice the values from the list**
list2=[2,4,6,7,8,46,67,84,85]
print(list2[3:7])
print(list2[-5:-1])
print(list2[1:8:2])
print(list2[-2:-10:-2])
print(list2[-8:-1:2])
print("_"*50)

#**program to add 2 lists**
list1=[1,2,3,4,5,6,7,8]
list2=[9,10,11,12,13,14]
#output=list1+list2
output=list1.extend(list2)
#print(output)
print(list1)
print("_"*50)\

#program to reverse list**
list_a=[2,9,75,65]
print(list_a[-1:-5:-1])
print("_"*50)

#**print the sum of all elements in a list****
list1 = [2,5,8,0,1]
var = 0
for value in list1:
    var += value
print(var)
print("_"*50)

#****list Methods Append,insert, extend***********
#print(dir(list))
list_c=[45,86,96,70,97,65,76]
list_c.append(400)
list_c.append("hello")
list_c.insert(2,[4,6,8]) #shifts to right
list_c.insert(3,"pyt") #to insert value at a specific position(3)
print(list_c)
print("_"*50)

#extend adds the data to end of the another list
lst1 = [a,g,f,d,t,u]
lst2 = [1,5,8]
lst2.extend(lst1)
print(lst2)
print("_"*50)

#replace a data in the list** we can replace data with the help of index pos
lst1 =[5,6,7,9,33,56]
lst1[3]= 100 #replace data at 3 index
print(lst1)




