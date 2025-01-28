"""Python Basics Problems"""

print("_" * 50)

# 1). Python Program to add two integer values.
int_1 = 30
int_2 = 40

result = int_1 + int_2
print(result)  # 70

print("_" * 50)

# 2). Python Program to subtract two integer values.
int_1 = 30
int_2 = 40

result = int_1 - int_2
print(result)  # -10

print("_" * 50)

# 3). Python program to multiply two numbers.
int_1 = 30
int_2 = 40

result = int_1 * int_2
print(result)  # 1200

print("_" * 50)

"""
4). Python program to repeat a given string 5 times.
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools”
"""

str1 = "SQATools"
result = str1 * 5
matched_str = "SQAToolsSQAToolsSQAToolsSQAToolsSQATools"
if result == matched_str:
    print("As per output code write")  # As per output code write

print("_" * 50)

"""
5). Python program to get the Average of given numbers.
Formula: sum of all the number/ total number
Input:
a = 40
b = 50
c = 30
Output :
Average = 40
"""
a = 40
b = 50
c = 30
sum_of_all_numbers = a + b + c
total_number = 3
average = sum_of_all_numbers // total_number

print("average : ", average)


print("_" * 50)

"""
6). Python program to get the median of given numbers.
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66
"""
Input_nums = [45, 60, 61, 66, 70, 77, 80]
sort_list = Input_nums.sort()
number_of_values = len(Input_nums)
median_value = 0
if number_of_values % 2 == 1:  # Odd number of values
    median_value += Input_nums[number_of_values // 2]
else:  # Even number of values
    median_value += (Input_nums[number_of_values // 2 - 1] + Input_nums[number_of_values // 2]) / 2
print("median value is :", median_value)


print("_" * 50)

"""
7). Python program to print the square and cube of a given number.
Input :
num1 = 9
Output :
Square = 81
Cube =   729
"""
print("_" * 50)
"""
8). Python program to interchange values between variables.
Input :
a = 10
b = 20
Output :
a = 20
b = 10
"""
a = 10
b = 20

if a == 10:
    a = 20
    b = 10
    print("a :", a, "b : ", b)
else:
    print("a :", a, "b : ", b)

print("_" * 50)

