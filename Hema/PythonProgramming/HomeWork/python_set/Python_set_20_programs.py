
ch = int(input("Enter number from 1 to 20: "))

if ch==1:
    '''
    1). Python program to create a set with some elements.
    '''
    set_var_1 = {1,2,3,4}
    set_var_1.add(5)
    print(set_var_1)

elif ch==2:
    '''
2). Python program to add an element to a set.

    '''
    set_var_2= set()
    print(type(set_var_2))
    set_var_2.add(1)
    print(set_var_2)
    set_var_2.add(2)
    print(set_var_2)

elif ch==3:
    '''
3). Python program to remove an element from a set.
'''
    set_var_3 = {2,3,4,5,6}
    print("original set: ", set_var_3)
    set_var_3.remove(5)
    print(set_var_3)


elif ch==4:
    '''
4). Python program to find the length of a set.

'''
    set_var_4 = {1,2,3,4,5,6}
    print("original set: ", set_var_4)
    print("length of set: ",len(set_var_4))

elif ch==5:
    '''
5). Python program to check if an element is present in a set.

'''
    set_var_5 = set()
    for i in range(1,5):
        set_var_5.add(i)
    print(set_var_5)
    num = 4
    if num in set_var_5:
        print("Element ", num ,"  is present in set")
    else:
        print(num ,"element is not present")

elif ch==6:
    '''
    6). Python program to find the union of two sets.
    '''
    set_var_6 = {1,2,3,4}
    set_var_6_1 = {5,6,4,2}
    result = set_var_6.union(set_var_6_1)
    print(result)

elif ch==7:
    '''
    7). Python program to find the intersection of two sets.
    '''
    set_var_7 = {1, 2, 3, 4}
    set_var_7_1 = {5, 6, 4, 2}
    result = set_var_7.intersection(set_var_7_1)
    print(result)

elif ch == 8:
    '''
    8). Python program to find the difference of two sets.
    '''
    set_var_8 = {1, 2, 3, 4}
    set_var_8_1 = {5, 6, 4, 2}
    result = set_var_8.difference(set_var_8_1)
    print(result)

elif ch == 9:
    '''
    9). Python program to find the symmetric difference of two sets.
    '''
    set_var_9 = {1, 2, 3, 4}
    set_var_9_1 = {5, 6, 4, 2}
    result = set_var_9.symmetric_difference(set_var_9_1)
    print(result)
elif ch == 10:
    '''
    10). Python program to show if one set is a subset of another set.
    '''
    set_var_10={1,2,3,4,5}
    set_var_10_1 = {3,2,6,8,9}
    set_var_10_2={2,3,4,5,1}
    print(set_var_10.issubset(set_var_10_2))

elif ch == 11:
    '''
    11). Python program to check if two sets are disjoint.
    '''
    set_var_11={1,2,3,4,5}
    set_var_11_1 = {3,2,6,8,9}
    set_var_11_2={2,3,4,5,1}
    set_var_11_3={1,2,3,4,5}
    print(set_var_11.isdisjoint(set_var_11_3))
elif ch == 12:
    '''
    12). Python program to convert a list to a set.
    '''
    list_var_12=[1,2,3,4,5]
    set_var_12 = set(list_var_12)
    print(set_var_12)

    if type(list_var_12) == list:
        set_var_12 = set(list_var_12)
        print("The converted list value to set is: ", set_var_12)
    else:
        print("Not converted to set")

elif ch == 13:
    '''
    13). Python program to convert a set to a list.
    '''
    set_var_13 = {1,2,3,4,5}
    list_var_13 = list(set_var_13)

    print(list_var_13)

    if type(set_var_13) == set:
        list_var_13 = list(set_var_13)
        print("Converted set to list: ", list_var_13)
    else:
        print("Not converted to list")

elif ch == 14:
    '''
    14). Python program to find the maximum element in a set.
    '''
    set_var_14 = {9,1,2,6,4,5}
    max_val = 0
    for i in set_var_14:
        if i > max_val:
            max_val = i
        else:
            continue
    print("The maximum value is: ", max_val)
elif ch == 15:
    '''
    15). Python program to find the minimum element in a set.
    '''
    set_var_15 = {6,5,4,3,8,9}
    list_set_var_15 = list(set_var_15)
    min_val = list_set_var_15[0]
    for i in set_var_15:
        if i < min_val:
            min_val = i
        else:
            continue
    print("The minimum value is: ", min_val)
elif ch == 16:
    '''
    16). Python program to find the sum of elements in a set.
    '''
    set_var_16 = {1,2,3,4,5}
    sum = 0
    for i in set_var_16:
        sum = sum + i
    print("The sum of set elements: ", sum)
elif ch == 17:
    '''
    17). Python program to find the average of elements in a set.
    '''
    set_var_17 = {1,2,3,4,5}
    len_set_var_17 = len(set_var_17)
    sum = 0
    for j in set_var_17:
        sum = sum + j
        avg = sum/len_set_var_17
    print("The average of elements is set is: ", avg)
elif ch == 18:
    '''
    18). Python program to check if all elements in a set are even.
    '''
    set_var_18 = set()
    count = 0

    for i in range(2, 11, 2):
        set_var_18.add(i)

    for j in set_var_18:
        if j%2 == 0:
            count = count + 1

    if count == len(set_var_18):
        print(f"All elements in a set {set_var_18} are even and length of even is {count}")
    else:
        print(f"All elements in set{set_var_18} are not even and length of even is {count}")
elif ch == 19:
    '''
    19). Python program to check if all elements in a set are odd.
    
    '''
    set_var_19=set()
    odd = set()
    for i in range(11, 20 , 2):
        set_var_19.add(i)
    for j in set_var_19:
        if j%2 == 1:
            odd.add(j)
        else:
            continue
    if len(set_var_19) == len(odd):
        print(f"All elements in set{set_var_19} are odd{odd}")
    else:
        print(f"Not all elements in set{set_var_19} are odd {odd}")
    print(set_var_19)
elif ch == 20:
    '''
    20). Python program to check if all elements in a set are prime.
    '''
    #doubt
    set_var_20 = set()
    prime = []
    for i in range(2,7):
        set_var_20.add(i) #{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    for j in set_var_20:
        print("j value: ",j)
        print("#"*50)
        count = 0
        for num in range(2, j):
            print("num value: ",num)
            print("num_j value: ",j)
            if j%num == 0:
                count = count + 1
                print(count)
        if count == 0:
            prime.append(j)
            print(prime)
    print(prime)
    if len(prime) == len(set_var_20):
        print("prime")
    else:
        print("Not a prime")



    print(set_var_20)

elif ch == 21:
    '''
    21). Python program to check if a set is a proper subset of another set.
    #What is the proper subset? : A proper subset is one that contains a few elements of the original set
    '''
    set_var_21_1 = {1,2,3,4,5}
    set_var_21_2 = {5,2,4}
    proper_subset = set()
    for i in set_var_21_2:
        if i in set_var_21_1:
            proper_subset.add(i)
        else:
            continue
    if len(proper_subset) == len(set_var_21_2):
        print(set_var_21_2, "is a proper subset of ", set_var_21_1)
    else:
        print("Not a proper subset")

'''    
22). Python program to find the cartesian product of two sets.

Solution
23). Python program to find the power set of a set.

24). Python program to remove all elements from a set.

Solution
25). Python program to remove a random element from a set.

Solution
26). Python program to find the difference between two sets using the “-” operator.

Solution
27). Python program to find the intersection between two sets using the “&” operator.

Solution
28). Python program to find the union of multiple sets using the | operator.

Solution
29). Python program to find the symmetric difference of two sets using the “^” operator

Solution
30). Python program to check if a set is a superset of another set.

Solution
31). Python program to find the common elements between two sets.

Solution
32). Python program to remove a specific element from a set.

Solution
33). Python program to add multiple elements to a set.

Solution
34). Python program to remove multiple elements from a set.

Solution
35). Python program to check if a set is empty.

Solution
36). Python program to check if two sets are equal.

Solution
37). Python program to check if a set is a frozen set.

Solution
38). Python program to create a frozen set.

Solution
39). Python program to find the difference between multiple sets.

Solution
40). Python program to find the intersection between multiple sets.

Solution
41). Python program to check if any element in a set is a substring of a given string.

Solution
42). Python program to check if any element in a set is a prefix of a given string.

43). Python program to check if any element in a set is a suffix of a given string.

44). Python program to find the index of an element in a set.

Solution
45). Python program to convert a set to a dictionary with each element as key and value to an empty set.

Solution
46). Python program to create a set of even numbers from 1 to 20.

Solution
47). Python program to create a set of odd numbers from 1 to 20.

Solution
48). Python program to create a set of your favorite actors.

Solution
49). Python program to create a set of your favorite movies.

Solution
50). Python program to create two sets of books and find the intersection of sets.

Solution
51). Python program to find the longest word in a set.

'''


# def fact(n):
#         result =1
#         for val in range(2,n+1):
#             if val==1:
#                 result= 1
#             elif val>1:
#                 result= result * val
#             else:
#                 print(f"invalid")
#         return result
#
#     result1 = fact(5)
#     print(result1)
#
#     def cal_num_consonants():
#         str1 = 'Hello We Are Learning Python'
#         vowel = ('a','e','i','o','u')
#         consonant =''
#         for i in str1:
#             if i in vowel:
#                 continue
#             else:
#                 consonant +=i
#         print(len(consonant))
#
#     cal_num_consonants()


# def num():
#     #global a
#     a = 20
#     a = a + 10
#     print(a)
#
#
# a = 10
#
# num()
# print(a)

