# Practice 20 programs on if-else
#1. Python program to print the square of the number if it is divided by 11

programNo = int(input("Enter program to execute : "))

if programNo == 1:
    print("Program #1: Python program to print the square of the number if it is divided by 11")
    num1= int(input("Enter number"))
    if num1 % 11 == 0:
        result1 = num1**2
        print("result is", result1)
    else:
        print("number is not divisible by 11")

#---------------------------------------------------------------------------------------------------------

elif programNo == 2:
    print("Program #2: Python program to check given number is a prime number or not.")
    num = int(input("Enter the number : "))
    count = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                count = count + 1

        if count >= 1:
            print("Number is not prime number")
        else:
            print("Number is prime number", num)
    else:
        print("Enter whole number greater than 1")

#--------------------------------------------------------------------------------------------

elif programNo == 3:
    print("Program #3:Python program to check given number is odd or even")

    num = int(input("Enter number: "))
    if num%2 == 0:
        print("Entered number is Even")
    else:
        print("Entered number is Odd")


#--------------------------------------------------------


elif programNo == 4:
    print("Program #4:Python program to check a given number is part of the Fibonacci series from 1 to 10.")

    number1 = int(input("Enter number"))
    list1 = [0,1,1,2,3,5,8,13,21,34]
    if number1 in list1:
        print("Number is part of fibonacci series 1-10")
    else:
        print("Number is not part of fibonacci series 1-10")


#-------------------------------------------------------------------------------------


elif programNo == 5:
    print("Program #5: Program to check the authentication of username and password")
    name= 'kirti25'
    pwd= 'Kirti@5'
    Uname = input("Enter Username : ")
    password = input("Enter password : ")
    if name == Uname and pwd == password:
        print("Valid credentials, Logging in")
    else:
        print("InValid credentials, try again")


#----------------------------------------------------------------------------------------


elif programNo == 6:
    print("Program #6: Python program to validate user_id in the list of user_ids.")

    uid_list = ['abc', 'pqr', 'xyz', 'userx', 'usery','userz']

    user = input("Enter user name : ")

    if user in uid_list:
        print("User is in the list of user_ids")
    else:
        print("User is not in the list of user_ids")



#--------------------------------------------------------------------------------------


elif programNo == 7:
    print("Program #7: Python program to check given number is divided by 3 or not.")
    num = int(input("Enter number : "))
    if num%3 == 0:
        print("Number is divisible by 3")
    else:
        print("Number is not divisible by 3")



#----------------------------------------------------------------------------------------



elif programNo == 8:
    print("Program #8: If else program to get all the numbers divided by 3 from 1 to 30.")

    list1=list()
    for i in range(1,31):
        if i%3 == 0:
             list1.append(i)

    print(list1)


#----------------------------------------------------------------------------------------



elif programNo == 9:
    print("Program #9: Python program to check the given number divided by 3 and 5.")

    num = int(input("Enter number : "))
    if num%3 == 0 and num%5 == 0:
        print("given number is divisible by 3 & 5")
    else:
        print("given number is not divisible by 3 & 5")

elif programNo == 10:
    print("Program #10: Python program to print a square or cube if the given number is divided by 2 or 3 respectively.")

    num = int(input("Enter number : "))
    result = 0
    if num%2==0:
        result = num**2
    elif num%3 == 0:
        result = num**3
    else:
        print("Entered number is not divisible by 2 or 3 ")

    print("result = ", result)



#-------------------------------------------------------------------------------------------------



elif programNo == 11:
    print("Program #11: Verify string is palindrome or not")

    str1 = input("Enter string : ")
    list1 = list(str1)
    list2 = []
    length = len(list1)
    print(length)

    for i in range(-1, -(length+1), -1):
        list2.append(list1[i])

    print(list1, list2)
    if list1 == list2:
        print("string is palindrome")
    else:
        print("string is not palindrome")


#------------------------------------------------------------------------------------------



elif programNo == 12:
    print("Program #12: Print vowels and consonants in the string")
    str1 = input("Enter String : ")
    list1 = ['a','e','i','o','u']
    str2=str1.lower()
    length = len(str1)

    vowels=[]
    consonants=[]

    for i in range (0, length):
        if str2[i] in list1:
            vowels.append(str2[i])
        else:
            consonants.append(str2[i])

    print("vowels = ",vowels, len(vowels))

    print("Consonants = ", consonants, len(consonants))


#------------------------------------------------------------------


elif programNo == 13:
    print("Program #13:")

elif programNo == 14:
    print("Program #20:")

elif programNo == 20:
    print("Program #20:")

else:
    print("Enter program between 1 to 20")
"""
If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""

