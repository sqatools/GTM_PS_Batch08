# 1). Python function program to add two numbers.
def add_num(a, b):
    sum1 = a + b
    return sum1


res = add_num( 4, 7 )
print( res )


# 2). Python function program to print the input string 10 times.
def string_fun(a):
    str1 = a * 10
    return str1


res1 = string_fun( 'HI bro,whats up\n' )
print( res1 )


# 3). Python function program to print a table of a given number.
def table_func(a):
    for i in range( 1, 11 ):
        res2 = a * i
        print( res2 )


table_func( 4 )


# 4). Python function program to find the maximum of three numbers.
def max_num(a, b, c):
    if a > b and a > c:
        print( 'A is maximum of three num.' )
    elif b > a and b > c:
        print( "B is maximum of three num." )
    else:
        print( "C is maximum of three num." )


max_num( 5, 8, 9 )


# 5). Python function program to find the sum of all the numbers in a list.
def num_sum(a):
    sum1 = 0
    for i in a:
        sum1 += i
    return sum1


list1 = [3, 5, 10, 25, 87, 45, 33, 96]
res = num_sum( list1 )
print( res )


#  6). Python function program to multiply all the numbers in a list.
def num_mul(a):
    mul1 = 1
    for i in a:
        mul1 *= i
    return mul1


list1 = [3, 50, 10]
safe = num_mul( list1 )
print( safe )


# 7). Python function program to reverse a string.
def reverse_str(a):
    res1 = a[::-1]
    return res1


str1 = "HI i am learning Python"
res = reverse_str( str1 )
print( res )


# 8). Python function program to check whether a number is in a given range.
def find_range(b):
    if b in range( 1, 20 ):
        print( True )
    else:
        print( False )


find_range( 20 )


# 9). Python function program that takes a list and returns a new list with unique elements of the first list.

def unique_list(a):
    list1 = []
    for i in a:
        if i not in list1:
            list1.append( i )
    return list1


list2 = [1, 2, 3, 4, 1, 2, 3, 6, 7, 6]
res = unique_list( list2 )
print( res )


# 10). Python function program that take a number as a parameter and checks whether the number is prime or not.
def prime_num_check(a):
    count = 0
    if a < 2:
        print( "no prime number" )

    for i in range( 2, a ):
        if a % i == 0:
            count += 1
    if count > 0:
        print( f"{a} is not prime number" )
    else:
        print( f"{a} is prime number" )


input1 = int( input( "Enter the num:" ) )
prime_num_check( input1 )


# 11). Python function program to find the even numbers from a given list.
def even_func(num):
    new_list = []
    for i in num:
        if i % 2 == 0:
            new_list.append( i )
    return new_list


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res1 = even_func( list1 )
print( res1 )


# 12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.
def square_num_func(b):
    new_list = []
    for i in b:
        res = i ** 2
        new_list.append( res )
    return new_list


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
final_res = square_num_func( list1 )
print( final_res )


# 13). Python function program to access a function inside a function.
def item(a):
    def add1(b):
        nonlocal a
        return a + b

    return add1


func = item( 10 )
print( func( 10 ) )


# 14). Python function program to access a function inside a function.
def item1(a):
    def item2(b):
        nonlocal a
        # a +=0

    return a + b


func = item( 10 )
print( func( 40 ) )


# 15). Python function program to find the LCM of two numbers.
def lcm_func(num1, num2):
    if num1 > num2:
        greater = num1

    else:
        greater = num2
    while (1):
        if (greater % num2 == 0) and (greater % num1 == 0):
            lcm = greater
            break
        greater += 1
    print( f"lcm of {num1} and {num2} is : {lcm}" )


inp1 = int( input( "Enter the first num:" ) )
inp2 = int( input( 'enter the second num:' ) )

lcm_func( inp1, inp2 )

# 17). Python function program to find the HCF of two numbers.


def HCF_func(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range( 1, smaller + 1 ):
        if (num1 % i == 0) and (num2 % i == 0):
            hcf = i

    return hcf


res = HCF_func( 90, 30 )
print( res )

# 18). Python function program to create a function with *args as parameters.
def func(*args):
    for num in args:
        print(num**2,end=" ")

func(2,3,4,5,6)

# # 19). Python function program to get the factorial of a given number.
def factorial_func(a):
    store =1
    while(a>0):
         store *=a
         a -=1
    print(store)

factorial_func(5)


# 20). Python function program to get the Fibonacci series up to the given number.
def Fibonacci_func(val):
    n1 =0
    n2 =1
    count =0
    while(count<val):
        print(n1,end =" ")
        n3 =n1+n2
        n1 = n2
        n2 =n3
        count +=1
Fibonacci_func(20)