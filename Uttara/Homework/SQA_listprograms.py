
#1. WAP in python to Adding two list data
ls1 = [5,8,10,15,20]
ls2 = [3,6,9,12,15,18,20]

output =ls1+ ls2

#Printing output
print("Addition of list:",output)

###########################################################################################################
#2.Python program to combine two lists.

list1 = [5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4]

#Adding lists
result = list1 + list2
print("Combination of two list:",result)

#3.WAP to print the sum of all elements in a list.

list1 = [10,55,88,6,11]

#Creating a variable
var = 0

for value in list1:
    var += value

print(var)

#4.WAP to differentiate even and odd elements from a list.

list4 = [23,11,78,90,34,55]

#creating empty lists
odd = []
even = []

for value in list4:
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)

#printing output
print("Even numbers: ", even)
print("Odd numbers: ", odd)

###############################################################################################################

#5.WAP to remove all the duplicate elements from a list.

list5 = [5,7,8,2,5,0,7,2]

#Creating empty list
list6 = []
for value in list5:
    if value not in list6:
        list6.append(value)

#Printing Output
print("Removing duplicate value from list",list6)

#6.WAP to print squares of even numbers from a list.
list7 = [2,4,9,8,9,1,5]

for value in list7:
    if value % 2 == 0:
        #Printing output
        print(value,":",value**2)

###################################################################################################################

#7.WAP to get common elements from two lists.

list8 = [4, 5, 7, 9, 2, 1]
list9 = [2, 5, 8, 3, 4, 7]

#Creating empty list
common_list = []
for value in list8:
    if value in list9:
        common_list.append(value)

#Printing output
print(common_list)

#8.WAp to print list in reverse order using index slicing.
#Input list
list10 = [2,4,6,8]

#Creating a variable
list11 = list10[::-1]

#Printing output
print(list11)

#[8, 6, 4, 2]

##########################################################################################################
#9 WAP to copy the list to another list.
list12 = [1,2,4,7,0,5]

#Creating an empty list
list13 = []

for value in list12:
    list13.append(value)

#Printing output
print(list13)

#10.WAp o print true if common elements between lists.
#Input list
list13 = [2,4,7,8,3]
list14 = [4,5,0]

for value in list13:
    if value in list14:
        #Printing output
        print("True")
#true

#11.WAP to get a list of elements divided by a number

list111 = [3,7,0,2,6,14,88,21]

#Creating empty list
list22 = []

for value in list111:
#Checking whether the value is
#divided by either 3 or 7

    if value % 3 == 0 or value % 7 == 0:
        list22.append(value)

#Printing output
print(value)

###########################################################################################################
#12.WAP to remove negative elements from the list
list15 = [3,5,-8,0,-20,-55]

#Checking for positive values
for value in list15:
    if value >= 0:
        #Printing output
        print(value,end=" ")

   #3 5 0

#13 WAP to check whether the list is palindrome or not.

list17 = [2,4,6,6,4,2]

#Creating variable and assign
# value to it
list20 = list17[::-1]

#Printing output
if list17 == list20:
    print("List is palindrome")
else:
    print("List is not palindrome")

#List is palindrome

#14 WAP to add two lists using extend method.

list19 = [2,4,6,8,1]
list21 = [23,56,11,89]

#Combining lists
list19.extend(list21)

#Printing output
print(list19)

##########################################################################################################

#15. WAPto sort a list using the sort and sorted method.

list1 = [23,11,78,45,33]

#Using sort
list1.sort()
print("By sort function: ",list1)

#o/p : By sort function:  [11, 23, 33, 45, 78]

#16 WAP to find the second largest number in the list.

list11111 = [22,11,78,45,90,44]

#sorting the list
list11111.sort()

#printing the output
print("2nd largest number: ", list11111[-2])

#output:2nd largest number:  78

#17.WAP to get all the unique numbers in the list.

#using for loop

list1 = [12,34,78,12,45,34]

#Creating empty list
list23 = []

for value in list1:
    if value not in list23:
        list23.append(value)

#Printing output
print(list23)

#o/p: [12, 34, 78, 45]

###################################################################################################
#18 WAP  to convert a string into a list.

string = "I am a girl"

#Splitting the string
list100 = string.split(" ")

#Printing output
print(list100)

#o/p: ['I', 'am', 'a', 'girl']

#19.WAp to print list elements separately.

list1 = [("This", "is", "a","bird"), (5, 85, 60), (1,4,8)]

for value in list1:
    print(value)

#o/p: ("This", "is", "a","bird")
    #(5, 85, 60)
    #(1,4,8)

#'20.WAP Python program to convert the 3rd character of each word to a capital case from the given list.
#Input: [‘Hello’, ‘student’, ‘are’, ‘learning’, ‘Python’, ‘Its’, ‘Python’, ‘Language’]
#Output: [‘HelLo’, ‘stuDent’, ‘are’, ‘leaRning’, ‘PytHon’, ‘Its’, ‘PytHon’, ‘LanGuage’]

list1 = ["Hello", "student", "are", "learning",
         "Python", "Its", "Python", "Language"]
list2 = []
for value in list1:
    if len(value)>3:
        list2.append(value[:3]+value[3].upper()
                     +value[4:])
    else:
        list2.append(value)

#Printing output
print(list2)

#o/p:['HelLo', 'stuDent', 'are', 'leaRning', 'PytHon', 'Its', 'PytHon', 'LanGuage']

