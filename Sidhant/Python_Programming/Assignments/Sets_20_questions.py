# 1). Python program to create a set with some elements.
set1 ={1,2,3,3,4,5}
print(set1)

# 2). Python program to add an element to a set.
set1 ={1,2,3,4,4,5}
set1.add(6)
print(set1)

# 3). Python program to remove an element from a set.
thisset = {"apple", "banana", "cherry"}

thisset.remove("apple")

print(thisset)

# 4). Python program to find the length of a set.
set1 ={"apple",'sid',1,2,3,34,77}
print(len(set1))

# 5). Python program to check if an element is present in a set.
set1 ={"apple",'sid',1,2,3,34,77}
if 'sid'in set1:
    print(True)
else:
  print(False)

# 6). Python program to find the union of two sets.
set1 ={"apple",'sid',1,2,3,34,77}
set2 ={ "ok sid ",'ready for python'}
set3 = set1 |set2
print(set3)

# 7). Python program to find the difference of two sets.
set1 ={ 1,2,4,5,6}
set2 ={1,4,3,7,6,34}
print(set1 - set2)

# 8). Python program to find the difference of two sets.
set1 ={ 1,2,4,5,6}
set2 ={1,4,3,7,6,34}
print(set1.intersection(set2))

# 9). Python program to find the symmetric difference of two sets.
set1 ={ 1,2,4,5,6}
set2 ={1,4,3,7,6,34}
print(set1.symmetric_difference(set2))

# 10). Python program to show if one set is a subset of another set.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
print(x.issubset(y))

# 11). Python program to check if two sets are disjoint.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

# 12). Python program to convert a list to a set.
list1 =['apple','banana',1, 2, 3]
set1 =set(list1)
print(set1)
print(type(set1))

# 13). Python program to convert a set to a list.
set1 ={'apple','banana',1, 2, 3}
list1 =list(set1)
print(list1)
print(type(list1))

# 14). Python program to find the maximum element in a set.
set1 ={1,34,4,56,96,22}
for i in set1:
    print(max(set1))
    break

# 15). Python program to find the minimum element in a set.
set1 ={93,44,56,6,11,33,43,120}
print("minimum element is:",min(set1))

# 16). Python program to find the sum of elements in a set.
set1 ={1,2,3,4,5}
total_sum =sum(set1)
print(total_sum)

# 17). Python program to find the average of elements in a set.
set1 ={1,2,3,4,5}
avg =sum(set1)/len(set1)
print(avg)

# 18). Python program to check if all elements in a set are even.
set1 ={2,4,68,88,8,2,46,40}
count =0
for i in set1:
    if i % 2 ==0:
        count +=1
if count == len(set1):
    print("all are even elements")
else:
    print("all are not even elements")

# 19). Python program to check if all elements in a set are odd.
set1 ={2,4,87,88,8,2,46,40}
count =0
for i in set1:
    if i % 2 !=0:
        count +=1
if count == len(set1):
    print("all are even elements")
else:
    print("all are not even elements")

# 20). Python program to check if all elements in a set are prime.
set1 ={2,3,5,7,11,8}
prime_count =0
nonprime =0
for num in set1:
    if num<1:
        nonprime+=1
        break
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            nonprime+=1
            break
        else:
            prime_count+=1
if nonprime>0:
    print("all elements in a set are not prime")
else:
    print("all elements in a set are prime")
