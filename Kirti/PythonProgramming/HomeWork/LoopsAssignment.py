'''
1). Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
Input1:1500
Input2:2700
'''

num1=1500
num2=2700
list1=[]

for i in range (num1, num2+1, 1):
    if i%7==0 and i%5==0:
        list1.append(i)
    else:
        continue

print("Below are numbers which are divisible by 7 and multiple of 5 between 1500 to 2700 : \n", list1)


#------------------------------------------------------------------------------------------------------


'''
2). Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print("*", end=" ")
    print()

for k in range(5, 1, -1):
    for l in range(k, 1, -1):
        print("*", end=" ")
    print()


#-----------------------------------------------------------------------------------


'''
3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”
'''

word = input("Enter the string : ")
strChar=''

for i in range(0,len(word),1):
    strChar+= word[i]

print("Entered string = ",strChar)


#-----------------------------------------------------------------------------------


'''
4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
'''
list1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even=[]
odd=[]

for i in list1:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Number of even numbers: ", len(even))
print("Number of odd numbers: ", len(odd))


#---------------------------------------------------------------------------------------


'''
5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
'''

for i in range(0, 7, 1):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end = " ")



#---------------------------------------------------------------------------------------


'''
6). Write a program that print given number is palindrome or not using python.
'''

num1= int(input("Enter the number : "))
num2=num1
reverse = 0

while num2>0:
    temp=num2%10
    reverse = reverse*10+temp
    num2=num2//10

print("Reverse of the number : ", reverse)

if num1 == reverse:
    print("given number is palindrome", num1)
else:
    print("given number is not palindrome", num1)



#---------------------------------------------------------------------------------------


'''
7). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
'''

num1=0
num2=1
temp1=0
while temp1<20:
    print(num1, end= " ")
    temp=num1 +num2
    num1=num2
    num2=temp
    temp1+=1


#---------------------------------------------------------------------------------------


'''
8). Python loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4
'''