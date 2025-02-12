for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
print("-"*50)

#add all the elements of the list using while**
list1 = [2,5,8,0,1]
count = 0
total = 0
while count < len(list1):
    total += list1[count]
    count += 1
print(total)