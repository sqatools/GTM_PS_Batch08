def main():
    l1 = [2, 3, 6, 8, 10, 101]
    num1=5
    s1="Hello We are Learning Python"
    print("The Maximum value is: ",MaximumVal(l1))
    print("The Factorial value of",num1,"is",FactorialVal(num1))
    print("The number of consonants in the string is",consonant(s1))

# 1. write a python function to get max value from list
def MaximumVal(list1:list):
    """
    This function gets the Maximum value from list
    :param list1: list datatype
    :return: Maximum Value
    """
    maxval=max(list1)
    return maxval

# 2. write a python function to return factorial value of number number
# 5 = 120 : 5*4*3*2*1
def FactorialVal(n1:int):
    """
    This function returns the factorial value of a number
    :param n1: int datatype
    :return: Factorial value
    """
    fv=1
    for x in range(1,n1+1):
        fv=fv*x
    return fv
# 3. Write a python function to calculate the number of consonants in given string.
# # str1= "Hello We are Learning Python" # output = 16
def consonant(str1:str):
    """
    This function calculates the number of consonants in a given string
    :param str1: string datatype
    :return: number of consonants in the string
    """
    vowels="aeiouAEIOU"
    count_of_consonants=0
    for x in str1:
        if x not in vowels and x.isalpha()==True:
            count_of_consonants+=1
    return count_of_consonants

main()



# # Home work
# 1. write a python function to get max value from list
# 2. write a python function to return factorial value of number number
# 5 = 120 : 5*4*3*2*1
# 3. Write a python function to calculate the number of consonants in given string.
# str1= "Hello We are Learning Python" # output = 16