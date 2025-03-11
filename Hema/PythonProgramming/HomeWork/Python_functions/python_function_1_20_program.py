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

elif ch == 9:
    '''
    9). Python function program that takes a list and returns a new list with unique elements of the first list.
    Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
    Output : [2, 3, 1, 4, 6 ]
    '''
    def unique_element_list(first_list):
        unique_list = []
        for i in first_list:
            if i not in unique_list:
                unique_list.append(i)
            else:
                continue
        return unique_list


    inp_var_9 = [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
    result_unique_list = unique_element_list(inp_var_9)

    print("The list elements are: ", inp_var_9)
    print("The unique elements of the first list: ", result_unique_list)

elif ch ==10:
    '''
    10). Python function program that take a number as a parameter and checks whether the number is prime or not.
    Input : 7
    Output : True
    '''

    prime_num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    def prime_number(num3):
        count = 0
        if num3 == 0 or num3 ==1:
            count = count + num3
            print("not a prime number: ",count)
        elif num3 ==2:
            count = count + num3
            print("True, Its a prime number", count)
            #print("True")
        elif num3 >2:
            if num3%2==1:
                count = count + num3
                #print("Its a prime number: ",count)
                if count in prime_num:
                    print("True, Number is prime", count)
                else:
                    print("False, Number not in prime number list", count)
            else:
                count = num3
                #print("Not a prime: ",count)
                if count not in prime_num:
                    print("False, Number not a prime number", count)
                else:
                    print("True, Number available in prime number", count)
        else:
            print("Not a prime number", count)


    num3 = int(input("Enter the number to check whether it is prime: "))

    prime_number(num3)

    #option 2: Not working

    def prime_number(num3):
        count = 0
        for i in range(2, num3):
            if num3%i == 0:
                count = count + 1
            else:
                count = 0
        if count > 0:
            print("False, not a prime")
        else:
            print("True, prime")

    num4 = int(input("Enter the number to check prime: "))
    prime_number(num4)

elif ch == 11:
        '''
        11). Python function program to find the even numbers from a given list.
        Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
        Output : [2, 4, 6, 8]
        '''

        def even_num(list4):
            even = []
            for i in range(len(list4)):
                if list4[i]%2==0:
                    even.append(list4[i])
                else:
                    continue
            return even
        list_var_11 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("The given list are: ", list_var_11)
        even_num_result = even_num(list_var_11)
        print("The even numbers from a given list: ", even_num_result)

elif ch == 12:
    '''
    12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.
    Input: 1 to 10
    Output: 1, 4, 9, 16, 25, 36, 49, 64, 81
    '''
    def square_num(num5):
        square = []
        for i in range(1, num5):
            square.append(i**2)
        return square
    num5 = int(input("Enter the number to check square: "))
    result_square = square_num(num5)
    print("The list of value: ", result_square)

elif ch == 13:
    '''
    13). Python function program to execute a string containing Python code.
    '''
    #DOUBT

elif ch==14:
        '''
        14). Python function program to access a function inside a function.
        '''
        #Doubt

        def calculator_operation():
            num1 = int(input('Enter any number: '))
            num2 = int(input('Enter second number: '))

            choice = int(input("Enter the operation choice to perform, Add(1), Subtract(2)\n"
                               ",Multiplication(3),Division(4),Floor division(5): "))

            if choice == 1:
                print("Performing addition operation")
                result = num1 + num2
            elif choice ==2:
                print("Performing subtraction operation")
                result = num1 - num2
            elif choice == 3:
                print("Performing multiplication operation")
                result = num1 * num2
            elif choice == 4:
                print("Performing division operation")
                result = num1/num2
            elif choice == 5:
                print("Performing floor division operation")
                result = num1%num2
            else:
                print("invalid operation")

            return result

        cal_result = calculator_operation()
        print(cal_result)

elif ch == 15:
        '''
        15). Python function program to find the LCM of two numbers.
        Input: 12, 20
        Output: 60
        '''
        def lcm(num1, num2):
            if num1 > num2:
                greater = num1
            else:
                greater = num2

            while (True):
                if ((greater % num1 == 0) and (greater % num2 == 0)):
                    lcm = greater
                    break
                greater += 1

            print(f"L.C.M of {num1} and {num2}: {lcm}")


        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        lcm(num1, num2)

elif ch == 16:
    '''
    16). Python function program to calculate the sum of numbers from 0 to 10.
    Output: 55
    
    Solution
    '''
    def cal_sum_num(n):
        sum = 0
        for i in range(n+1):
            sum  = sum + i
        return sum

    #n = int(input('Enter the range number to calculate sum of it: '))
    n = 10
    result_sum = cal_sum_num(n)
    print(f"The sum of numbers of range of {n} is: ", result_sum)

elif ch == 17:
    '''
17). Python function program to find the HCF of two numbers.
Input: 24 , 54
Output: 6

Solution
    '''

elif ch == 18:
    '''
18). Python function program to create a function with *args as parameters.
Input: 5, 6, 8, 7
Output: 125 216 512 343

Solution
    '''
    def func_param_arg(*args):
        list_var_18 = []
        for i in args:
            list_var_18.append(i**3)
        return list_var_18
    output = func_param_arg(5,6,8,7)
    print(output)
elif ch ==19:
    '''
19). Python function program to get the factorial of a given number.
Input: 5
Output: 120

Solution
    '''
    def fact(n):
        num =1
        for i in range(1, n+1):
            num = num * i
        return num

    n =5
    result = fact(n)
    print("factorial of given number: ", result)

    #option 2:
    def fac(n1):
        count = 1
        while n1 > 1:
            count = count * n1
            n1= n1-1
        return count

    result1 = fac(5)
    print(result1)
elif ch ==20:
    '''
20). Python function program to get the Fibonacci series up to the given number.
Input: 10
Output: 1 1 2 3 5 8 13 21 34
    '''
    # def fib(n):
    #     fib = []
    #     sum = 0
    #     for i in range(1,n+1):
    #         # if i<=0:
    #         #     print("Invalid number")
    #         # # elif i == 1:
    #         #     fib = fib + i
    #         #     print(fib)
    #         #if i>=1:
    #         print(i)
    #         temp = i
    #         print("temp: ", temp)
    #         sum = temp + sum
    #         print("sum: ",sum)
    #         i = sum
    #         print("i: ",i)
    #         #fib.append([sum,])
            #print(temp)
    def fib(n):
        n1,n2=0,1

        for i in range(1,n+1):
            print(n2, end=",")

            n1,n2 = n2,n1+n2

    n = 10
    fib(n)

elif ch ==21:
    '''
21). Python function program to check whether a combination of two numbers has a sum of 10 from the given list.
Input : [2, 5, 6, 4, 7, 3, 8, 9, 1]
Output : True

'''

    def comb_two_num(set_num):
        list_var_21 = []
        sum=10
        list_set_num = list(set_num)
        for i in range(len(list_set_num)):
            #print(list_set_num[i])
            for j in range(i+1,len(list_set_num)):
                #print(list_set_num[j])
                if list_set_num[i]+list_set_num[j] == sum:
                    list_var_21.append([list_set_num[i],list_set_num[j],])
                    #print("True, the combination numbers are: ", list_var_21)
                else:
                    continue

        print()
        return 'True, the combination numbers has a sum of 10 are:  ',list_var_21
    set_var_21 = [2,5,6,4,7,3,8,9,1]
    result = comb_two_num(set_var_21)
    print(result)


elif ch == 22:
    '''
    22). Python function program to get unique values from the given list.
    Input : [4, 6, 1, 7, 6, 1, 5]
    Output : [4, 6, 7, 5]

    '''

    def unique_value_list(list22):
        unique_list = []

        for i in list22:
            if i not in unique_list:
                unique_list.append(i)
            else:
                continue
        return unique_list

    list_var_22 = [4,6,1,7,6,1,5]
    print("The input list values are: ", list_var_22)
    result_unique_list = unique_value_list(list_var_22)
    print("Unique values are: ", result_unique_list)