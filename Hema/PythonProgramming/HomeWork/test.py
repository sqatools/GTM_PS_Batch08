str1 = "Rahul Mohit John Rahul Vaibhav John"
str1_list = str1.split()
str3 = []
str4= ''
count = 0
for ch1 in str1_list:
    if str1_list.count(ch1)> 1 and ch1 not in str3:
        str3.append(ch1)

print(str3)
result = ' '.join(str3)
print(result)


with open('read.txt', 'r') as file:
    data= file.read()
    data_list = data.split()
    print(data_list)
    temp = 0
    for val in data_list:
        len_list_str = len(val)
        if len_list_str > temp:
            temp = len_list_str
    print(temp)

'''
* * * * * * * *

 * * * * * * * *
       **
       **
       **
       **



'''
# for i in range(6):
#     if i < 2:
#         print("*"*8)
#     else:
#         print(" "*6 + "*" * 2)
#     print()

for i in range(6):
    if i < 2:
        print("*" * 8)
    else:
        print(" " * 3 + "*" * 2)




dict1 = { 'x': 10, 'y': 20, 'c': 50, 'f': 44 }
dict2 = { 'x': 60, 'c': 25, 'y': 56 }

dict_value = {}

for key in dict1:
    if key in dict2:
        dict_value[key] = dict1[key] + dict2[key]

print(dict_value)

#Output = “Rahul John”
# str2 = ''
# for ch in str1:
#     str2 = str2 + ch
#     if ch not in str2:
#         continue
#     else:
#         str2 = str2+ch
# print(str2)

'''
Input: [2, -16, 6, 44, -71, 18, -11, -1]

Output: [2, 6, 44, 18, -16, -71, -11, -1]
'''

var = [2, -16, 6, 44, -71, 18, -11, -1]
positive_var = []
negative_var = []

for i in var:
    if i > 0:
        positive_var.append(i)
    else:
        negative_var.append(i)

positive_var.extend(negative_var)
print(positive_var)


# x = 10
#
# if x > 5:
#
#     print("A")
#
# if x > 7:
#
#     print("B")
#
# if x > 15:
#
#     print("C")
#
# else:
#
#     print("D")
#
# my_dict = {'grapes': 2, 'banana': 3, 'blue-berry': 4}
#
# for key in my_dict:
#
#     print(key)


# text = "Hello World"
#
# print(text.join("-"))
#

# list1 = [("mike",1),("sarah",20),("jim", 16)]
#
# dict1 = {}
#
# for val in list1:
#
#     dict1[val[0]] = val[1]
#
# print(dict1)
#

# i = 0
#
# while i < 15:
#
#       print(i)
#
#       i += 3

# i = 10
#
# while True:
#
#     print(i)
#
#     i -= 3
#
#     if i == 1:
#
#         break
#
# class MyClass():
#     def __init__(self):
#         self.__private_var = 25
#
#
#     def __private_method(self):
#         print("Private method")
#
#
#     def public_method(self):
#         print("Public method")
#
#         self.__private_method()
#
#
# # Create an object of the class
#
# obj = MyClass()
#
# # Access public method and variable
#
# obj.public_method()
#
# print(obj._MyClass__private_var)


Dict1 = { 'x':10, 'y':20, 'c':50, 'f':44 }

Dict2 = {'x':60,'c':25,'y':56}

#Output = {‘x’: 70, ‘c’: 75, ‘y’: 76}
dict3_1 = {}
for k in Dict1:
    print(k)
    if k in Dict2:
        dict3_1[k] = Dict1[k] + Dict2[k]

print(dict3_1)


for i in range(1,4):
    if i == 1 or i ==3:
        print("* " * 3)
    #if i == 2:
    else:
        print("* "+" "+ " *")


for i in range(1,4):
    if i == 1:
        print("* ")
    elif i == 2:
        print("* " * 2)
    else:
        print("* " * 3)

for i in range(1,4):
    if i == 1:
        print(" "*2 + "* " + " "*2)
    elif i == 2:
        print(" " + "* " * 3+" ")
    elif i == 3:
        print("* " * 5)