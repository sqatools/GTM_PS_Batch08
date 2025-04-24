# print("""Create a Python class called Animal with attributes name and color.\n
# Include a method to print the animal’s name and color.""")
#
# class Animal():
#
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     def animal_display(self):
#
#         print(self.name,self.color)
#
# name, color = input("Enter the name and color of Animal separated with space").split(" ")
#
# Anim = Animal(name, color)
# Anim.animal_display()
#
# print("""Create a Python class called Dog that inherits from the Animal class.
# Add attributes breed and weight. Include a method to print the dog’s name, color, breed, and weight.""")
#
# class Animal_Dog(Animal):
#     def __init__(self,name, color, breed, weight):
#         super().__init__(name,color)
#         self.breed = breed
#         self.weight = weight
#
#     def print_dog_info(self):
#         print(f"Name {self.name} , color is {self.color} from the breed {self.breed} and it's weight {self.weight}")
#
#
# Dog1 = Animal_Dog("D1","Brown","D3","23Kg")
# Dog1.print_dog_info()
#
#
#
#
#
#
import pdb


#
# class Laptop:
#
#     def __init__(self,brand,name,weight):
#         self.brand = brand
#         self.name = name
#         self.weight = weight
#
#     def laptop_info(self):
#         print(f"Laptop brand {self.brand} and it's name is {self.name} having weight {self.weight}")
#
#
#     def price_per_weight(self, price):
#         self.price = price
#         Total_price = self.weight * self.price
#
#         print("The total price of laptop is: ", Total_price)
#
#
# Lap1 = Laptop('HP', 'Mini', 2765)
#
# Lap1.laptop_info()
# Lap1.price_per_weight(32)
#
# print("Create a Python class called VIPCustomer that inherits from the Customer class."
#       " Add attributes credit_limit and discount_rate. Include a method to calculate the customer’s "
#       "available credit.")
#
# class Customer:
#
#     def __init__(self,name,age,bank):
#         self.name = name
#         self.age = age
#         self.bank = bank
#
#     def customer_details(self):
#         print("The name of Customer is", self.name)
#         print("The age of Customer is: ", self.age)
#         print("The name of bank is: ", self.bank)
#
# class VIPCustomer(Customer):
#
#     def __init__(self,name,age,bank):
#         super().__init__(name,age,bank)
#
#     def available_credit(self,credit_limit, discount_rate):
#         self.credit = credit_limit
#         self.discount = discount_rate
#
#         print("The available credit with Customer is: ", self.credit)
#         print("The available discount for the customer is: ", self.discount)
#
#
#
# Cust =VIPCustomer("Mohit", 34 , "Axis")
# Cust.customer_details()
# Cust.available_credit(2345,"56%")
#
# class Count_Instance:
#     count = 0
#     def __init__(self,name):
#         Count_Instance.count +=1
#         self.n = name
#
#
#
# CI = Count_Instance("Sheetal")
# CI2 = Count_Instance("Mohit")
#
# print("The instance of the class",Count_Instance.count )
#
# print("Create a Python class called Manager that inherits from the Employee class."
# "Add attributes department and bonus. Include a method to calculate the manager’s total compensation.")
#
# class Employee:
#     role = "Sale"
#     def __init__(self,name):
#         self.n = name
#         # self.r = role
#
#     def emp_info(self):
#         print("The name of Employee: ",self.n)
#         print("The Role of the Employee: ",self.role)
#
# class Manager(Employee):
#
#     def __init__(self,department, bouns ,name,role):
#         super().__init__(name)
#         self.dep = department
#         self.bo = bouns
#
#     def manager_details(self):
#         self.emp_info()
#         print("The department Manager belongs to : ",self.dep)
#         print("The bonus Manager got : ", self.bo)
#
#
# Mag = Manager("Admin",2000,"Ashish", "OH")
#
# # Mag.emp_info()
# Mag.manager_details()
#
# def prime_nu(num):
#     list1 =[]
#     for num1 in range(2,num+1):
#         isPrime = True
#         for div in range (2, (num1//2) + 1):
#             if num1%div ==0:
#                 isPrime = False
#                 break
#             else:
#                 continue
#         if isPrime:
#             list1.append(num1)
#
#     return list1
#
# num2 = int(input("Enter number range from which you want to get the prime number"))
# list2 = prime_nu(num2)
#
# print(f"The list of Prime number between the 2 and {num2} is {list2}")
#
# def prime_nu1(num):
#     list1 = []
#     for num1 in range(2, num + 1):  # range from 2 to num
#         # If the number is divisible by any number other than 1 and itself, it's not prime
#         if all(num1 % div != 0 for div in range(2, int(num1**0.5) + 1)):
#             list1.append(num1)
#     return list1
# list3 = prime_nu1(num2)
#
# print(f"The list of Prime number between the 2 and {num2} is {list3}")
#
# def open_file(filepath):
#     with open(filepath,"rb") as f:
#         read_file = f.read()
#         print(read_file)
#         print(f.tell())
#         current_position = f.tell()
#         # new_position = max(0, current_position - 100)  # Don't go below position 0
#         # f.seek(new_position)
#         f.seek(-100,1)
#         print(f.tell())
#         read_file1 = f.read()
#         print(read_file1)
#         print(f.tell())
#
# open_file("D:\\PythonAutomation\\GTM_PS_Batch08\\Sheetal\\Notes.txt")
#

test,var = 1000, 2000
print(type(test), type(var))
print(type(set()))
print(type({}))

my_list = [1, 2, 3, 4, 5]
del my_list[2]
print(my_list)

# a) [1, 2, 3, 4, 5]
# b) [1, 2, 4, 5]
# c) [1, 2, 4]
# d) [1, 3, 4, 5]
