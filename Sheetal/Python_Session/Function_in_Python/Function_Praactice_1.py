"""
def function_name():
    code

function_name()  #call function to pass values
"""
from Uttara.Homework.SQA_Strngprogrm import vowel

# Homework

print("1. WAPF to get max value from list")
def maximum_fun(l1):
    max_num = l1[0]
    for num in l1:
        if num > max_num:
            max_num = num
    return max_num

max_value = maximum_fun([57,88,43,22,1])
print(f"The maximum number from the list is {max_value}")

print("_"*40)
print("2. WAPF to return factorial value of number number")
# 5 = 120 : 5*4*3*2*1
def fact_num(num):
    fact_n = 1
    while num >0:
        fact_n = fact_n * num
        num = num-1
    return fact_n

fact_of_num = fact_num(5)

print(f"The Factorial of number is {fact_of_num}")


print("_"*40)
print("3. WAPF to calculate the number of consonants in given string.")
str1= "Hello We are Learning Python" # output = 16

def const_alp(str2,count_c):
    vowel = ("aeiouAEIOU")
    str3 = ""
    # count_const = 0
    for string1 in str2:
        if string1 not in vowel and string1.isalpha():
            str3 += string1
            count_c +=1

    return str3,count_c
# HllWrLrnngPythn

const_print, count_const = const_alp(str1, 0)
print(f"The final string is {const_print} and the count of the consonants are {count_const}")


