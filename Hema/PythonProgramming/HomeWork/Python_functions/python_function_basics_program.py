

'''
1. write a python function to get max value from list
2. write a python function to return factorial value of number number
5 = 120 : 5*4*3*2*1
3. Write a python function to calculate the number of consonants in given string.
str1= "Hello We are Learning Python" # output = 16
'''

print("#"*50)
print("To check consonants in given string")
def cal_num_constant(str1):
    vowels = 'aeiouAEIOU'
    count = 0
    print("The given string is: ", str1)
    for ch in str1:
        if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
            if ch not in vowels:
                count = count + 1
                print("the consonants value are: ",ch,end=",")
            else:
                continue
    print()
    return count

str1= "Hello We are Learning Python"

c1 = cal_num_constant(str1)
print(c1)

print("&"*50)
print("To check maximum number")
def max_num(lst):
    # if i not in lst:
    #     print("Empty")
    print("list value is: ", lst)
    max_num = lst[0]

    for num in lst[1:]:
        if num > max_num:
            max_num = num
    print(max_num)

lst = [2, 3,5,1,4,6]
max_num(lst)


print("_"*50)
print("To check factorial")
def fact(n):
    result = 1
    for n1 in range(n+1):
        if n1 == 0 or n1 == 1:
            result = 1

        elif n > 1:
            result = result * n1

        else:
            print('invalid input')

    print(result)

num = int(input("Enter the number to check factorial: "))
fact(num)

"""
write a python program update the user entry in the data base using *kwargs
->  we have company data, here we have to add 10 new member details in database
->  create a function which accept the users details using kwargs
->  add kwargs values to list
->  accept all the values using input
"""

# def get_user_details(user_member_details,name,**kwargs):
#     #user_member_details = []
#     member_details ={}
#     # for k,v in kwargs.items():
#     #     member_details[k]=v
#     # count=0
#     # while count<num:
#     #     count = count + 1
#     for k,v in kwargs.items():
#          user_member_details.append([k,v,])
#
#     print(user_member_details)
#     dict_user_member_details = dict(user_member_details)
#     print(dict_user_member_details)
#
# num=int(input('How many records you want to add: '))
# #ch=input("Do you waant to enter records: ")
# name = input("Enter username: ")
# surname = input("Enter surname: ")
# age = int(input('Enter age: '))
# email = input("Enter mail id: ")
#
# user_member_details = []
#
# #while ch == 'y':
# for _ in range(num):
#     get_user_details(user_member_details = [],name,surname=surname,age_num=age,mail=email)


