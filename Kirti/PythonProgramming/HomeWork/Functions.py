"""
# Home work
1. write a python function to get max value from list
2. write a python function to return factorial value of number number
5 = 120 : 5*4*3*2*1
3. Write a python function to calculate the number of consonants in given string.
str1= "Hello We are Learning Python" # output = 16
"""

'''
Q. 1. write a python function to get max value from list
'''
list1 = [3,7,4,56,345,6,78,79,8,1,0]

def get_max_value(l1:list):
    temp = 0
    for ele in l1:
        if ele > temp:
            temp = ele
        else:
            continue
    return temp

print("Max value from the list = ", get_max_value(list1))



'''
Q. 2. write a python function to return factorial value of number number
'''
def get_factorial_number(num:int):
    fact = 1
    for i in range(num + 1):
        if i >= 1:
            fact = fact * i
        else:
            continue
        i = i-1
    return fact

print("Factorial of number is : ", get_factorial_number(5))


"""
Q. 3. Write a python function to calculate the number of consonants in given string.
str1= "Hello We are Learning Python" # output = 16
"""
str1= "Hello We are Learning Python"

def get_consonants_count(str1):
    count1 = 0
    for i in range(len(str1)):
        if str1[i].lower() in 'aeiou':
            continue
        elif  str1[i]== ' ':
            continue
        else:
            count1 += 1
    return count1



print("Number of consonants in the given string = ", get_consonants_count(str1))