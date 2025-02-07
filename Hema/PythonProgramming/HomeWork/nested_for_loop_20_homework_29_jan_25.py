#29th Jan'25

ch = int(input("Enter number to check the for loop program: "))

if ch == 1:
    '''
    Program1:
    2) Python Loops program to construct the following pattern, using a nested for loops.
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
    print("="*50)
    print("program 1")
    print("Program to print a pattern using nested for loops")

    for c in range(6):
        print(c*"*")
    for c in range(4, -1, -1):
        print(c*"*")

elif ch==2:
    '''
    Program 2:
    3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”

    '''
    print("="*50)
    print("program 2")
    #word = input("Enter the word: ")
    word = 'python'
    str1 = ""
    len_word=len(word)
    for i in range(len_word):
        str1 += word[i]

    print(str1)

elif ch==3:
    '''
    Program 3:
    4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
    '''
    print("Solution1: ")
    print("="*50)
    input=(1,2,3,4,5,6,7,8,9)
    even=[]
    odd=[]
    list_input=list(input)
    print(list_input)
    for i in range(0, len(list_input)):
        if (list_input[i]+1)%2!=0:
            even.append(i+1)
            #even.append(i)
        else:
            odd.append(i+1)
    print("Number of even numbers are: ",len(even),":",even)
    print("Number of add numbers are: ", len(odd), ";", odd)

    print("Solution 2: ")
    print("*"*50)
    num= (1,2,3,4,5,6,7,8,9)
    even_num = 0
    odd_num = 0
    for i in num:
        if i%2 == 0:
            even_num = even_num + 1
            #print("*"*50)
            #print(even_num)
        else:
            odd_num = odd_num + 1
            #print(odd_num)
    print("Total number of even: ",even_num)
    print("Total number of odd: ", odd_num)

elif ch == 4:
    '''
    Program 5:
    5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
    '''
    print("#"*50)
    print("To Print all numbers from 0 to 6, except 3 and 6")

    for j in range(0, 7):
        if j!=3 and j!=6:
            print(j, end=" ")
elif ch ==5:
    '''
    Program 6:
    7). Write a program that iterates the integers from 1 to 30 using python. 
    For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”. 

    '''

    print("#" * 50)
    print("program that iterates the integers from 1 to 30 using for loop")
    print("solution 1: ")
    for i in range(1, 31):
        if i%3==0 and i%5==0:
            print("Number divisible by 3 and 5: ", i, ":FizzBuzz")
        elif i%3==0:
            print("Number divisible by 3: ",i, ": Fizz")
        elif i%5==0:
            print("The number divisble by 5: ", i, ": Buzz")

    print("#"*50)
    print("solution 2:")
    print("program that iterates the integers from 1 to 30 using for loop")
    num =[]
    for i in range(1, 31):
        if i%3==0 or i%5==0:
            num.append(i)
    print("Filtered numbers which is divisible by 3 and 5: ", num)
    for j in num:
        if j%3 == 0 and j%5==0 :
            print("The number multplies of 3 and 5: ",j, ": FizzBuzz")
        elif j%3==0:
             print("The number multiples of 3: ", j, ": Fizz")
        elif j%5==0:
             print("The number multiples of 5: ", j, ": Buzz")

elif ch ==6:
    '''
    14). Python Loops program to print all even numbers between 1 to 100 in python.
    '''
    print("#"*50)
    print("Program 6")
    print("program to print all even numbers between 1 to 100")
    even = []
    for i in range(1, 101):
        if i%2==0:
            #print("even number: ", i, end=" ")
            even.append(i)
    print("The even numbers are: ", even)

elif ch==7:
    '''
    15). Python Loops program to print all odd numbers between 1 to 100 using python.
    '''
    print("#"*50)
    print("Program to print all odd numbers from 1 to 100")
    odd = []
    for i in range(1, 101):
        if i%2!=0:
            odd.append(i)
    print("The odd number values are: ", odd)

elif ch ==9:
    '''
    65). Write a program to create an empty list and add odd numbers from 1-10 in it including 1 using Python.
Input = []
Output : [1,3,5,7,9]
    '''
    print("="*50)
    odd=[]
    for i in range(1, 11):
        if i%2!=0:
            odd.append(i)
    print("The odd numbers are: ", odd)

elif ch ==8:
    '''
    62). Write a program to display numbers from a list using Python Loops.
Input = [1,5,8,0,4]
Output = 1,5,8,0,4
    '''
    print("#"*50)
    print("program to display numbers from a list using Python Loops")
    input_list = [1,5,8,0,4]
    for i in input_list:
        print(i, end=",")

elif ch ==10:
    '''
    64). Write a program to create an empty list and add even numbers from 1-10 in it including 10 using Python Loops.
Input = []
Output :
[2,4,6,8,10]
        '''
    print("Solution1: ")
    print("="*50)
    even=[]
    for i in range(1, 11):
        if i%2==0:
            even.append(i)
    print("The even numbers are: ",even)

elif ch==11:
    '''
    63). Write a program to print each word in a string on a new line using Python Loops.
Input = Sqatools
Output :
S
q
a
t
o
o
l
s
    '''
    print("#"*50)
    print("program to print each word in a string on a new line using Python Loops")
    string_input = 'Sqatools'

    for i in string_input:
        print(i)
elif ch==12:
    '''
    76). Write a program to add even numbers in an empty list from a given list using Python Loops.
Input :
A=[2,3,5,76,9,0,16], B=[]
Output = [2,76,0,16]
    '''
    print("#"*50)
    print("program to add even numbers in an empty list from a given list using Python Loops")
    B=[]
    A=[2,3,5,76,9,0,16]
    for i in A:
        if i%2==0:
            B.append(i)

    print("Output: ", B)

elif ch ==13:
    '''
    75). Write a program to find the total number of special characters in a string using Python Loops.
Input = ‘@sqa#tools!!’
Output = 4
    '''
    print("#"*50)
    print("a program to find the total number of special characters in a string using Python Loops")
    input = "@sqa#tools!!"
    list_input=list(input)
    empty_list = []
    for i in list_input:
        #print(i)
        if i == '@' or i == '#' or i =='!':
            empty_list.append(i)
    #print(empty)
    print("total number of special characters in a string: ",len(empty_list))

elif ch ==14:
    '''
    61). Write a program to print the first 20 natural numbers using for loop in Python.
Output = 1,2,3,….,20
    '''
    print("#"*50)
    print("program to print the first 20 natural numbers using for loop in Python")
    print("First 20 natural numbers: ")
    for i in range(1, 21):
        print(i, end=" ")

elif ch==15:
    '''
    60). Write a program to print a table of 5 using for loop using Python Loops.
Output :
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
    '''
    print("#"*50)
    print("print a table of 5 using for loop")
    num = 5
    for i in range(1, 11):
        print(num, "*", i, "=",  num*i)

elif ch==16:
    '''
    59). Write a program to print the following pattern using Python Loops.
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
    print("#"*50)
    print("print pattern")
    # for i in range(1, 10):
    #     for j in range(0, i, 1):
    #         print("*",end=" ")
    #         if i>5:
    #             for j_one in range(j, j-2):
    #                 print("*",end=" ")
    for i in range(1,5):
        print(i*"*")
    for j in range(5, 0, -1):
        print(j*"*")
    print()
    '''
    10). Python for loop program to print the alphabet pattern ‘O’ using python.
Output:
  ***  
*       *
*       *
*       *
*       *
*       *
   ***  

    '''
elif ch ==17:
    '''
    55). Write a program to construct the following pattern, using a nested for loop in Python.
Output :
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
    '''
    print("#"*50)
    for i in range(1, 6):
        for j in range(i):
            print(i, end=" ")
        print()
elif ch ==18:
    '''
    54). Write a program to construct the following pattern, using a for loop in Python.
Output :
* * * * *
* * * *
* * *
* *
*
    '''
    print("#"*50)
    for i in range(5, 0, -1):
        print(i*" *")
    print()

elif ch ==19:
    '''
    53). Write a program to construct the following pattern, using a for loop in Python.
Output :
*
* *
* * *
* * * *
* * * * *
    '''
    print("#"*50)
    for i in range(1, 6):
        print(i*" *")
    print()

elif ch ==20:
    '''
    48). Write a program to get input from the user if it is a string insert it into an empty list using Python Loops.
Input :
L=[]
‘sqatools007’
Output = [‘s’,’q’,’a’,’t’,’o’,’o’,’l’,’s’]
    '''
    print("#"*50)
    L=[]
    str = 'sqatools007'
    list_str = list(str)
    for i in range(0,len(list_str)-3):
        #print(list_str[i])
        L.append(list_str[i])

    print(L)
