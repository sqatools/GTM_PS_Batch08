#5th Mar'25

'''
What is Function?
It is a block of code that executes when it is called.
To create a function we use def keyword.
'''

ch=int(input('Enter the number: '))
if ch==1:
    '''
    1). Python function program to add two numbers.
    '''
    #option 1:
    def add_num(num1,num2):
        add_result = num1 + num2
        return add_result

    result = add_num(5,6)
    print("Adding two numbers: ", result)

    #option 2:
    def add_number(num1, num2):
        add = num1 + num2
        print(f"Adding {num1} + {num2} numbers: ",add)

    add_number(5,5)
elif ch ==2:
    '''
    2). Python function program to print the input string 10 times.
    '''
    #option 1
    def prog_inp_string(str1):
        result_str = str1 * 10
        print("To print the input string 10 times: ",result_str)

    prog_inp_string("Test")

    #option 2
    def prog_input(str2):
        result_str1 = str2 * 10
        print("print values 10 times: ",result_str1)

    str2 = input("Enter the string value: ")

    prog_input(str2)

elif ch==3:
    '''
    3). Python function program to print a table of a given number.
    '''
    def print_table_number(num3):
        for i in range(1,11):
            print(f'{i} * {num3} = {i*num3}')

    num = int(input("Enter the number to print table: "))

    print_table_number(num)

elif ch==4:
    '''
    4). Python function program to find the maximum of three numbers.

Input: 17, 21, -9
Output: 21
    '''
    #option 1:

    def max_numbers(n1,n2,n3):
        if n1 > n2 and n1 > n3:
            print(f"The maximum number of {n1},{n2},{n3} is: ", n1)
        elif n2>n1 and n2>n3:
            print(f"The maximum number of {n1},{n2},{n3} is: ", n2)
        elif n3>n1 and n3>n2:
            print(f"The maximum number of {n1},{n2},{n3} is: ", n3)
        else:
            print("Invalid values")

    max_numbers(17,21,-9)

    #option 2:
    def max_numbers(n1,n2,n3):
        if n1 > n2 and n1 > n3:
            print(f"The maximum number of {n1},{n2},{n3} is: ", n1)
        elif n2>n1 and n2>n3:
            print(f"The maximum number of {n1},{n2},{n3} is: ", n2)
        elif n3>n1 and n3>n2:
            print(f"The maximum number of {n1},{n2},{n3} is: ", n3)
        else:
            print("Invalid values")

    n1 = int(input("enter first number: "))
    n2 = int(input("enter second number: "))
    n3 = int(input("enter third number: "))

    max_numbers(n1,n2,n3)

elif ch==5:
    '''
    5). Python function program to find the sum of all the numbers in a list.
    Input : [6,9,4,5,3]
    Output: 27
    '''
    def sum_all_num(l1):
        count = 0
        sum = 0
        while count <1:
            for i in range(len(l1)):
                sum = sum + l1[i]
            count = count + 1
        print("Sum of list values is: ", sum)

    l1 = [6,9,4,5,3]
    sum_all_num(l1)

elif ch ==6:
    '''
    6). Python function program to multiply all the numbers in a list.
    Input : [-8, 6, 1, 9, 2]
    Output: -864
    '''
    def multiply_num(l2):
        mul = 1
        for i in range(len(l2)):
            mul = l2[i] * mul
        print("Multiply all numbers in a list: ", mul)
    l2 = [-8, 6, 1, 9, 2]
    multiply_num(l2)

elif ch == 7:
    '''
    7). Python function program to reverse a string.
    Input: Python1234
    Output: 4321nohtyp
    '''
    def reverse_string(str2):
        #option 1

        reverse_output = str2[::-1]
        print("The reversed string value is: ",reverse_output)

        #option 2

        temp = ''
        for i in range(len(str2)):
            temp = temp + str2[-i-1]
        print("reverse value without built-in function: ",temp)

    str2 = 'Python1234'
    reverse_string(str2)

elif ch == 8:

    '''
    8). Python function program to check whether a number is in a given range.
    Input : num = 7, range = 2 to 20
    Output: 7 is in the range
   '''
    def num_given_range(num):
        lst = []
        for i in range(2,21):
            lst.append(i)
        if num in lst:
            print(f"{num} is in a given range 1 to 20")
        else:
            print(f"{num} is Not in range")
    num = 20
    num_given_range(num)
'''
9). Python function program that takes a list and returns a new list with unique elements of the first list.
Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
Output : [2, 3, 1, 4, 6 ]

Solution
10). Python function program that take a number as a parameter and checks whether the number is prime or not.
Input : 7
Output : True

Solution
11). Python function program to find the even numbers from a given list.
Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Output : [2, 4, 6, 8]

Solution
12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.
Input: 1 to 10
Output: 1, 4, 9, 16, 25, 36, 49, 64, 81

Solution
13). Python function program to execute a string containing Python code.

Solution
14). Python function program to access a function inside a function.

Solution
15). Python function program to find the LCM of two numbers.
Input: 12, 20
Output: 60

Solution
16). Python function program to calculate the sum of numbers from 0 to 10.
Output: 55

Solution

17). Python function program to find the HCF of two numbers.
Input: 24 , 54
Output: 6

Solution
18). Python function program to create a function with *args as parameters.
Input: 5, 6, 8, 7
Output: 125 216 512 343

Solution
19). Python function program to get the factorial of a given number.
Input: 5
Output: 120

Solution
20). Python function program to get the Fibonacci series up to the given number.
Input: 10
Output: 1 1 2 3 5 8 13 21 34

Solution
21). Python function program to check whether a combination of two numbers has a sum of 10 from the given list.
Input : [2, 5, 6, 4, 7, 3, 8, 9, 1]
Output : True

Solution
22). Python function program to get unique values from the given list.
Input : [4, 6, 1, 7, 6, 1, 5]
Output : [4, 6, 7, 5]

'''