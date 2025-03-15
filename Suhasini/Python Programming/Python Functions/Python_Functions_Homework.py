# 1. Python function program to check whether a combination of two numbers has a sum of 10 from the given list.
# Input : [2, 5, 6, 4, 7, 3, 8, 9, 1]
# Output : True
from os.path import split

print("1. check whether a combination of two numbers has a sum of 10 from the given list.")
def checksum(listA):
    for i in range (len(listA)):
        for j in range (i+1, len(listA)):
            if listA[i] + listA[j] == 20:
                print("The combination is:", listA[i], ",",listA[j])
                print("True")

checksum([10, 12, 2, 3, 4, 20, 1, 8])
print("_"*50)


# 2. Python function program to get unique values from the given list.
# Input : [4, 6, 1, 7, 6, 1, 5]
# Output : [4, 6, 7, 5]
print("2. Python function program to get unique values from the given list")

def findUnique(listA):
    listB = []
    for val in listA:
        if val not in listB:
            listB.append(val)

    print("The unique elements from given list are: ",listB)

findUnique([4, 6, 1, 7, 6, 1, 5])
print("_"*50)


# 3. Python function program to get the duplicate characters from the string.
# Input: Programming
# Output: {‘g’,’m’,’r’}

def findDuplicate(String1):
    list3 = []
    for char in String1:
        if String1.count(char) > 1:
            list3.append(char)

    print("Duplicate characters are: ",set(list3))

findDuplicate("Programming")
print("_"*50)


# 4. Python function program to get the square of all values in the given dictionary.
# Input = {‘a’: 4, ‘b’ :3, ‘c’ : 12, ‘d’: 6}
# Output = {‘a’: 16, ‘b’ : 9, ‘c’: 144, ‘d’, 36}
print("4. Python function program to get the square of all values in the given dictionary")
def findSquare(dict1):
    dict2 = {}
    for k,v in dict1.items():
        dict2[k] = v**2
    print("Dictionary after squaring values is:")
    print(dict2)

findSquare({'a': 4, 'b' :3, 'c' : 12, 'd': 6})
print("_"*50)


# 5. Python function program to create dictionary output from the given string.
# Note: Combination of the first and last character from each word should be
# key and the same word will the value in the dictionary.
# Input = “Python is easy to Learn”
# Output = {‘Pn’: ‘Python’, ‘is’: ‘is’, ‘ey’: ‘easy’, ‘to’: ‘to’, ‘Ln’: ‘Learn’}

def createDict(String):
    String1 = String.split()
    print(String1)
    dict1 = {}
    for word in String1:
        dict1[word[0]+word[-1]] = word

    print("Dictionary created is :",dict1)

createDict("Python is easy to Learn")
print("_"*50)


# 6. Python function program to print a list of prime numbers from 1 to 100.
print("6. Python function program to print a list of prime numbers from 1 to 100")
def printPrimeNum(lower, upper):
    print("prime numbers between ",lower, " and",upper, " are: ")
    for num in range(lower, upper+1):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print(i, end=" ")

printPrimeNum(1, 100)
print()
print("_"*50)


# 7. Python function program to get a list of odd numbers from 1 to 100
print("7. Python function program to get a list of odd numbers from 1 to 100")
def printOdd(lower, upper):
    print("Odd numbers between ",lower, " and",upper, " are: ")
    for i in range(lower, upper+1):
        if i % 2 != 0:
            print(i, end=" ")

printOdd(1, 100)
print()
print("_"*50)


"""
# 8. Python function program to print and accept login credentials.
print("8. Python function program to print and accept login credentials")
def acceptCredentials():
    uname = input("Enter user name: ")
    password = input("Enter password: ")
    print("Credentials accepted")

acceptCredentials()
print("_"*50)
"""


# 9. Python function program to get the addition with the return statement
print("9. Python function program to get the addition with the return statement")
def addition(num1, num2):
    sum = num1+num2
    return sum

sum = addition(10, 15)
print("Sum of the numbers is: ",sum)
print("_"*50)


# 10. Python function program to create a Fruit shop Management system
print("10. Python function program to create a Fruit shop Management system")
def fruitShopManagement(fruitName, fruitprice, fruitQuantity):
    print("Name of the fruit purchased is: ", fruitName)
    print("Quantity of fruits purchased is: ", fruitQuantity)
    print("Total Bill is: ", fruitprice*fruitQuantity)

fruitShopManagement("Mango", 10, 25)
print("_"*50)


# 11. Python function program to reverse an integer
print("11. Python function program to reverse an integer")
def reverseInt(num):
    rev = 0
    n = num
    while n > 0:
        r = n % 10
        rev = (rev * 10) + r
        n = n // 10
    print("Reverse number: ", rev)

reverseInt(1234)
print("_"*50)


# 12. Python function program to create a library management system
print("12. Python function program to create a library management system")
def libManageSys(borrowerName, bookName):
    print("The borrower's name is: ",borrowerName)
    print("The book borrowed is: ",bookName)

libManageSys("Suhasini", "Revolution 2020")
print("_"*50)


# 13. Python function program to add two Binary numbers
print("13. Python function program to add two Binary numbers")
def addBinaryNum(num1, num2):
    result = bin(int(num1,2)+int(num2,2))
    print(result[2:])

addBinaryNum('100010','101001')
print("_"*50)


# 14. Python function program to search words in a string
print("14. Python function program to search words in a string")
def searchWord(string1, word1):
    if word1 in string1:
        print("Word is present in string")
    else:
        print("Word id not present in string")

searchWord("Hello Good Morning", "Hi")
print("_"*50)


# 15. Python function program to get the length of the last word in a string.
print("15. Python function program to get the length of the last word in a string")
def findLastWordLen(String):
    String1 = String.split()
    length = len(String1[-1])
    print("Length of last word in String is: ",length, "and the word is: ",String1[-1])

findLastWordLen("Hello Good Morning")
print("_"*50)

"""
# 16. Python function program to get a valid mobile number
print("16. Python function program to get a valid mobile number")
def validMobileNum():
    num = int(input("Enter a number"))

    if len(str(num)) == 10:
        print("Entered number is a valid Mobile Number")
    else:
        print("Entered number is not a valid mobile number")

validMobileNum()
print("_"*50)
"""


# 17. Python function program to convert an integer to its word format
print("17. Python function program to convert an integer to its word format")
def intToWord(num):
    str1 = ""
    for i in str(num):
        if i == '1':
            str1 += 'One'
        elif i == '2':
            str1 += 'Two'
        elif i == '3':
            str1 += 'Three'
        elif i == '4':
            str1 += 'Four'
        elif i == '5':
            str1 += 'Five'
        elif i == '6':
            str1 += 'Six'
        elif i == '7':
            str1 += 'Seven'
        elif i == '8':
            str1 += 'Eight'
        elif i == '9':
            str1 += 'Nine'
        elif i == '0':
            str1 += 'Zero'

    print(str1)

intToWord(94056634)
print("_"*50)


# 18. Python function program to create a function with **kwargs as parameters
print("18. Python function program to create a function with **kwargs as parameters")
"""
write a python program update the user entry in the data base using *kwargs
->  we have company data, here we have to add 10 new member details in database
->  create a function which accept the users details using kwargs
->  add kwargs values to list
->  accept all the values using input 
"""
def enterUserData(**kwargs):
    print("New member details are: ")
    print("")
    for k, v in kwargs.items():
        print(k, ": ",v)
    print("-" * 30)

enterUserData(name='rahul', surname='gupta', email='rahul@gmail.com', phone=654645645, age=32)
enterUserData(name='rohit', surname='Sharma', email='rohit@gmail.com', phone=872347263, age=25)
enterUserData(name='Sham', surname='Mishra', email='Sham@gmail.com', phone=42654123, age=22)
enterUserData(name='Sundar', surname='Varma', email='Sundar@gmail.com', phone=746289747, age=28)
enterUserData(name='Ram', surname='Patil', email='ram@gmail.com', phone=24376523746, age=28)
enterUserData(name='Sita', surname='Kulkarni', email='sita@gmail.com', phone=2345577688, age=40)

print("_"*50)


# 19. Python function program to reverse a string.
# Input: Python1234
# Output: 4321nohtyp
print("19. Python function program to reverse a string")

def revString(str1):
    print("Original string is: ", str1)
    print("Reverse of the string is: ", str1[::-1])

revString("Python1234")
print("_"*50)


# 20. Python function program to check whether a number is in a given range
print("20. Python function program to check whether a number is in a given range")

def findInRange(min, max):
    num = int(input("Enter a number to find if it is in given range"))

    if num > min and num < max:
        print("Number is within the range:",min,",",max)
    else:
        print("Number is not within the range:", min,",",max)

findInRange(2, 20)
print("_"*50)








