# 1. Python program to find the common elements between two sets
print("1. Python program to find the common elements between two sets")

set1 = {1, 2, 3}
set2 = {3, 4, 5}
val = set1.intersection(set2)
print("Common elements between the sets are: ",val)
print("_"*50)


# 2. Python program to remove a specific element from a set.
print("2. Python program to remove a specific element from a set.")
set1 = {1, 2, 3,5, 6, 2, 7, 4}
val = set1.pop()
print("Element removed from set is: ",val)
print("Set after removing element from set: ",set1)
print("_"*50)


# 3. Python program to add multiple elements to a set.
print("3. Python program to add multiple elements to a set.")
set3 = {1, 2, 3,5, 6, 2, 7, 4}

set3.add(100)
set3.add(100)
set3.add(200)
print("Set after adding values: ",set3)
print("_"*50)


# 4. Python program to remove multiple elements from a set
print("4. Python program to remove multiple elements from a set")
set4 = {1, 2, 3, 4, 5, 6, 7, 200, 100}

set4.remove(2)
set4.remove(6)
print("Set after removing element from set: ",set4)
print("_"*50)


# 5. Python program to check if a set is empty.
print("5. Python program to check if a set is empty.")
set5 = {3, 5}
if len(set5) == 0:
    print("Set is empty")
else:
    print("Set is not empty")
print("_"*50)


# 6. Python program to check if two sets are equal.
print("6. Python program to check if two sets are equal.")
set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3, 4, 5, 6}

val = set1.intersection(set2)
#print(val)
if val == set1 and val == set2:
    print("Sets are equal")
else:
    print("Sets are not equal")
print("_"*50)


##################### Doubt 37th on website
#7. Python program to check if a set is a frozen set.
print("7. Python program to check if a set is a frozen set.")
set7 = {1, 2, 3, 4, 5, 6}



# 8. Python program to find the difference between multiple sets
print("8. Python program to find the difference between multiple sets")
setA = {1, 2, 3, 4, 5, 6, 8, 9, 11, 34, 23}
setB = {1, 2, 3, 4, 5, 6}

val = setA.difference(setB)
print("The difference of multiple sets is: ",val)
print("_"*50)


# 9. Python program to find the intersection between multiple sets.
print("9. Python program to find the intersection between multiple sets.")
setA = {1, 2, 3, 4, 5, 6, 8, 9, 11, 34, 23}
setB = {1, 2, 3, 4, 5, 6}

val = setA.intersection(setB)
print("The intersection between the sets is: ",val)
print("_"*50)


# 10. Python program to check if any element in a set is a substring of a given string.
print("10. Python program to check if any element in a set is a substring of a given string")
setA = {"Suhasini", "Pruthvi"}
str1 = "learning Python is fun"
count = 0

for word in setA:
    if word in str1:
        count += 1

if count > 0:
    print("Element in the set is a substring of given String")
else:
    print("Element in the set is not a substring of given String")
print("_" * 50)


# 11. Python program to convert a set to a dictionary with each element as key
# and value to an empty set.
print("11. Python program to convert a set to a dictionary with each element as key and value to an empty set")
setA = {1, 2, 3, 4, 5}
dictA = {}

for i in setA:
    dictA[i] = {}

print("Dictionary created is: ",dictA)
print("_" * 50)


# 12. Python program to create a set of even numbers from 1 to 20.
print("12. Python program to create a set of even numbers from 1 to 20.")
list12 = []

for i in range (1, 21):
    if i % 2 == 0:
        list12.append(i)

print("Set of even numbers is: ",set(list12))
print("_" * 50)


# 13. Python program to create a set of odd numbers from 1 to 20.
print("13. Python program to create a set of odd numbers from 1 to 20.")
list12 = []

for i in range (1, 21):
    if i % 2 != 0:
        list12.append(i)

print("Set of odd numbers is: ",set(list12))
print("_" * 50)


# 14. Python program to create a set of your favorite actors.
print("14. Python program to create a set of your favorite actors.")
set14 = {"Shahid", "Akshay", "Jason", "Punnet", "Surya"}
print("Set of favourite actors is:")
print(set14)
print("_"*50)


# 15. Python program to find the longest word in a set.
print("15. Python program to find the longest word in a set.")
set15 = {"Hi","Hello","Bye","Good Morning","Good night"}
length = 0
maxlen = 0
longword = ""
for word in set15:
    length = len(word)
    if length > maxlen:
        maxlen = length
        longword = word

print("Longest word is: ",longword, "and its length is :",maxlen)
print("_"*50)


# 16. Python program to add an element to a set.
print("16. Python program to add an element to a set.")
set16 = {1, 3, 5}
print("Original set is: ",set16)
set16.add(7)
print("Set after adding element: ",set16)
print("_"*50)


# 17. Python program to remove an element from a set.
print("17. Python program to remove an element from a set.")
set17= {1, 2, 3, 4, 5, 6, 7, 200, 100}
print("Original set: ",set17)
set17.remove(200)
set17.remove(7)
print("Set after removing elements: ", set17)
print("_"*50)


# 18. Python program to find the length of a set
print("18. Python program to find the length of a set")
set18= {1, 2, 3, 4, 5, 6, 7, 200, 100}
a = len(set18)
print("Length of set is: ",a)
print("_"*50)


# 19. Python program to find the union of two sets.
print("19. Python program to find the union of two sets")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print("Union of the sets is: ", set3)
print("_"*50)


# 20. Python program to check if an element is present in a set.
print("20. Python program to check if an element is present in a set.")
set20 = {1, 2, 3, 4, 5, 6, 7, 200, 100}
a = int(input("Enter a number to check if it is present in set"))

if a in set20:
    print("Value is present in set")
else:
    print("Value is not present in set")
print("_"*50)



