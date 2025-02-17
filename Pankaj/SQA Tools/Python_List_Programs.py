# 1. Problem to get the square of all numbers In the python list
list1 = [1, 2, 3, 4, 5]
for value in list1:
    print(f"Square of {value} is: ", value ** 2)

# 2. Problem to add elements from list1 to list2.
list2 = [3, 4, 5, 6, 7]
list3 = [7, 8, 8, 9, 6]
print(list2 + list3)

# 3). Python program to calculate the sum of all elements from a list.
list4 = [2, 3, 4, 5]
summ = 0
for val in list4:
    summ += val
print(summ)

# 4). Python program to find a product of all elements from a given list.
list5 = [4, 4, 4, 4]
product = 1
for val in list5:
    product *= val
print(product)

# 5). Python program to find the minimum and maximum elements from the list.
list6 = [2, 33, 77, 99, 1, 100, 300]
sorted(list6)
print(list6)
print("Minimum Number : ", list6[0])
print("Maximum Number : ", list6[-1])

# 6). Python program to differentiate even and odd elements from the given list.
list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for value in list7:
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)
print("Even Num: ", even)
print("Odd Num: ", odd)

# 7). Python program to remove all duplicate elements from the list.
list8 = [2, 3, 4, 4, 3, 1]
for vale in list8:
    if vale == vale:
        print()
    

