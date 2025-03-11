"""
#13,15,21
print("1). Python function program to add two numbers.")


def add_numbers(num1, num2):
    sum1 = num1 + num2
    print(f"{num1}+{num2}={sum1}")
    return sum1


num4 = int(input("Enter 1st number :"))
num5 = int(input("Enter 2nd number :"))
add_numbers(num4, num5)
print("_" * 100)

####################################QUESTION#######################################################
print("2). Python function program to print the input string 10 times.")


# Check approach used for loop. * used in solutions

def print_ten_times(str1):
    for x in range(10):
        print(str1, end=" ")
    print()


str2 = input("Enter your string : ")
print_ten_times(str2)
print("_" * 100)
########################################################################################
print("3). Python function program to print a table of a given number.")


def generate_number_table(num3, stopnum):
    for x in range(1, stopnum + 1):
        answer = num3 * x
        print(f"{num3} x {x} = {answer}")


number1 = int(input("Enter the number for the table : "))
stopnum = int(input("Enter the number of multiples : "))
generate_number_table(number1, stopnum)
print("_" * 100)
####################################################################################################
print("4). Python function program to find the maximum of three numbers.")


# Input: 17, 21, -9
# Output: 21
def maximum_number(a, b, c):
    if a > b and a > c:
        print(f"The Maximum number is : {a}")
    elif b > a and b > c:
        print(f"The Maximum number is : {b}")
    elif c > a and c > b:
        print(f"The Maximum number is : {c}")
    else:
        print("None of the number is maximum")


num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))
num3 = int(input("Enter 3rd number :"))

maximum_number(num1, num2, num3)
print("_" * 100)
############################################################################################
print("5). Python function program to find the sum of all the numbers in a list.")


# Input : [6,9,4,5,3]
# Output: 27
def sum_of_list(l1):
    a = 0
    for x in l1:
        a = a + x
    print("Output :", a)
    return a


l2 = [6, 9, 4, 5, 3]
sum_of_list(l2)
print("_" * 100)

####################################################################################################
print("6). Python function program to multiply all the numbers in a list.")


# Input : [-8, 6, 1, 9, 2]
# Output: -864")

def multiply_num(l2):
    a = 1
    for x in l2:
        a = a * x
    print(f"Output: {a}")
    return a


list_a = [-8, 6, 1, 9, 2]
multiply_num(list_a)
print("_"*100)
#######################################################################################################
print("7). Python function program to reverse a string.")
# Input: Python1234
# Output: 4321nohtyp

def reverse_string(s1):
    output=""
    for x in range(-1,-len(s1)-1,-1):
        output+=s1[x]
    print(output)
    return output
s2=input("Your string to reverse: ")
reverse_string(s2)

print("_"*100)
###################################################################################################
print("8). Python function program to check whether a number is in a given range.")
# Input : num = 7, range = 2 to 20
# Output: 7 is in the range

def check_range(num1,range_start,range_stop):
    l1=[]
    for x in range(range_start,range_stop+1):
        l1.append(x)

    if num1 in l1:
        print(f"{num1} is in range {range_start} to {range_stop}")
    else:
        print(f"{num1} is in not in range {range_start} to {range_stop}")

check_range(7,2,20)
print("_"*100)
######################################################################################################
print("9). Python function program that takes a list and returns a new list with unique elements of the first list.")
# Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
# Output : [2, 3, 1, 4, 6 ]

def unique_elements_list(l1):
    l2=[]
    for x in l1:
        if x not in l2:
            l2.append(x)
    print(f"Output : {l2}")
    return l2

input1=[2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
unique_elements_list(input1)
print("_"*100)

##################################################################################################
print("10). Python function program that take a number as a parameter and checks whether the number is prime or not.")


# Input : 7
# Output : True

def prime_number(num1):
    c = 0
    for x in range(2, (num1 // 2) + 1):
        if num1 % x == 0:
            c += 1
    if c > 0 and num1 != 1:
        print(f"{num1} is not a prime number")
    elif num1 == 1:
        print(f"{num1} is neither prime nor composite number")
    else:
        print(f"{num1} is a prime number")


usernum = int(input("Enter number : "))
prime_number(usernum)
print("_" * 100)
###########################################################################################
print("11). Python function program to find the even numbers from a given list.")

# Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output : [2, 4, 6, 8]

def even_number(l11):
    l3 = []
    for x in l11:
        if x % 2 == 0:
            l3.append(x)
    print(f"Output: {l3}")

list11=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even_number(list11)
print("_"*100)

######################################################################################################
print("12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.")
# Input: 1 to 10
# Output: 1, 4, 9, 16, 25, 36, 49, 64, 81

def square_number(start,stop):
    for x in range(start,stop+1):
        print(f"{x} : {x**2}")

square_number(1,10)
print("_"*100)
#####################################QUESTION##################################################################
print("13). Python function program to execute a string containing Python code.")
#Could not understand the question requirement and was not able to understand the solution, uses exec?

print("_"*100)
#############################################################################################################
print("14). Python function program to access a function inside a function.")

def calculator():

    number1=int(input("Enter 1st Number : "))
    number2 = int(input("Enter 2nd Number : "))
    user_input1 = int(input("Enter Operation\n1 for Addition\n2 for Subtraction\n3 for multiplication\n4 for Division\nEnter Choice : "))

    if user_input1==1:
        add(number1,number2)
    elif user_input1==2:
        subtract(number1,number2)
    elif user_input1==3:
        multiply(number1,number2)
    elif user_input1==4:
        division(number1,number2)
    else:
        print("Invalid Entry")

def add(num1,num2):
    answer=num1+num2
    print(f"{num1} + {num2} = {answer}")
    return answer

def subtract(num1,num2):
    answer=num1-num2
    print(f"{num1} - {num2} = {answer}")
    return answer

def multiply(num1,num2):
    answer=num1*num2
    print(f"{num1} * {num2} = {answer}")
    return answer

def division(num1,num2):
    answer=num1/num2
    print(f"{num1} / {num2} = {answer}")
    return answer

calculator()

print("_"*100)
"""
################################QUESTION############################################
# Please check my approach. Was not able to understand the website solution.
print("15). Python function program to find the LCM of two numbers.")


# Input: 12, 20
# Output: 60

def lcm_number(num1, num2):
    bignum = max(num1, num2)
    small_num = min(num1, num2)

    for x in range(1, (bignum // 2) + 1):
        multiple = bignum * x
        if multiple % small_num == 0:
            print(f"The LCM of {num1} and {num2} is {multiple}")
            break
        else:
            continue


lcm_number(12, 20)


def factors_number(num1):
    list_factors = []
    for x in range(2, (num1 // 2) + 1):
        if num1 % x == 0:
            list_factors.append(x)
    # print(list_factors)


factors_number(20)
print("_" * 100)
#################################################################################################
print("16). Python function program to calculate the sum of numbers from 0 to 10.")


# Output: 55

def sum_numbers(startnum, stopnum):
    sum1 = 0
    for x in range(startnum, stopnum + 1):
        sum1 += x
    print(f"The sum of all the numbers from {startnum} to {stopnum} is {sum1}")


sum_numbers(0, 10)
print("_" * 100)
###################################################################################################
print("17). Python function program to find the HCF of two numbers.")


# Input: 24 , 54
# Output: 6

def hcf(num1, num2):
    list_factors1 = []
    list_factors2 = []
    for x in range(2, (num1 // 2) + 1):
        if num1 % x == 0:
            list_factors1.append(x)
    for x in range(2, (num2 // 2) + 1):
        if num2 % x == 0:
            list_factors2.append(x)
    print(list_factors1)
    print(list_factors2)
    common_factors = []
    for y in list_factors1:
        if y in list_factors2 and y not in common_factors:
            common_factors.append(y)
    print(common_factors)
    print(f"The HCF of {num1} and {num2} is {max(common_factors)}")


hcf(24, 54)
print("_" * 100)
#################################################################################################
print("18). Python function program to create a function with *args as parameters.")


# Input: 5, 6, 8, 7
# Output: 125 216 512 343

def cubes(*args):
    for x in args:
        print(f"{x} : {x ** 3}")


cubes(5, 6, 8, 7)
print("_" * 100)
##################################################################################################
print("19). Python function program to get the factorial of a given number.")
Input: 5
Output: 120


def factorial(num1):
    a = 1
    for x in range(1, num1 + 1):
        a = a * x
    print(f"The factorial of {num1} is {a}")
    return a


factorial(5)
print("_" * 100)
###################################################################################################
print("20). Python function program to get the Fibonacci series up to the given number.")

# Input: 10
# Output: 1 1 2 3 5 8 13 21 34

def fibonacci(num1):
    a, b = 1, 1
    print(a, b, end=" ")
    for x in range(1, num1 - 1):
        c = a + b
        a = b
        b = c
        print(b, end=" ")

fibonacci(10)
print()
print("_" * 100)
##################################QUESTION############################################################
# Question not clear. Please check approach.Explain website solution
print("21). Python function program to check whether a combination of two numbers has a sum of 10 from the given list.")


# Input : [2, 5, 6, 4, 7, 3, 8, 9, 1]
# Output : True

def tenspartner(l1):
    partner = []
    for x in range(len(l1)):
        for y in range(x + 1, len(l1)):
            if l1[x] + l1[y] == 10:
                partner.append((l1[x],l1[y]))

    print(partner)


list2 = [2, 5, 6, 4, 7, 3, 8, 9, 1]
tenspartner(list2)
