# 1. Python oops program to create a class with the constructor.
print("1. Python oops program to create a class with the constructor")
class ITCompany:
    def __init__(self, comp_name, comp_project, comp_address):
        self.compName = comp_name
        self.compProj = comp_project
        self.compAddress = comp_address

    def displayCompDetails(self):
        print("Company Name: ",self.compName)
        print("Company Project: ",self.compProj)
        print("Company Address: ",self.compAddress)

obj = ITCompany("TCS", "Govt Project", "Bangalore, Karnataka")
obj.displayCompDetails()
print("_"*80)


# 2. Python oops program to create a class with an instance variable.
print("2. Python oops program to create a class with an instance variable")

class InstClass:
    def __init__(self):
        self.instance_var = 21

obj = InstClass()
print("Instance Variable is: ",obj.instance_var)
print("_"*80)


# 3. Python oops program to create a class with Instance methods
print("Python oops program to create a class with Instance methods")

class UserDetails:
    # class variable
    user_city = "Mumbai"

    # parametrize constructor
    def __init__(self, firstname, lastname, email, phone):
        print("Welcome to users class")
        self.first_name = firstname  # instance variable
        self.last_name = lastname  # instance variable
        self.user_email = email  # instance variable
        self.phone_num = phone  # instance variable

    # instance method
    def show_first_name(self):
        print("User First Name :", self.first_name)

    # instance method
    def show_last_name(self):
        print("Last name :", self.last_name)

    def show_user_email(self):
        print("User Email :", self.user_email)

    def show_user_phone(self):
        self.country = "India" # instance in the method.

        print("User Phone Number :", self.phone_num)

    def show_country_name(self):
        print("Country Name :", self.country)

obj = UserDetails("Rohan", "Verma", "rohan@gmail.com", "897987987890")
obj.show_first_name()
obj.show_last_name()
obj.show_user_email()
obj.show_user_phone()
obj.show_country_name()
print("*"*80)


# 4. Python oops program to create a class with class variables.
print("4. Python oops program to create a class with class variables")

class myClass:

    var1 = "This is class variable"

print("Class Variable is: ",myClass.var1)
print("*"*80)


# 5. Python oops program to create a class with a static method
print("5. Python oops program to create a class with a static method")

































"""
text = "Hello World"
print(text.join('-'))


my_dict = {'grapes':2, 'banana':3, 'blue-berry':4}
for key in my_dict:
    print(key)


for i in range(1,6):
    if i ==3:
        continue
    print(i)

print("_"*50)


dict1 = {'x':10, 'y':20, 'c':50, 'f':44}
dict2 = {'x':60, 'c':25, 'y':56}
dict3 ={}
val = 0

for k,v in dict1:
    for k1, v1 in dict2:
        if dict1.k == dict2.k1:
            dict3.k = dict1[v]+dict2[v1]

print(dict3)


list1 = [2, -16, 6, 44, -71,18,-11,-1]
list2 = []
list3 = []
for val in list1:
    if val > 0:
        list2.append(val)
    else:
        list3.append(val)

print("List after moving positive numbers to left and negative numbers to right side of list",list2+list3)



for i in range(0,2):
    print("*"*8)

for i in range(0,5):
    print(" "*2,"*"*2)
    


str = "Rahul, Mohit, John, Rahul, Vaibhav, John"
list1 = str.split()
print(list1)
list2 = []

for i in range(0,5):
    for j in range(i+1,5):
        if list1[i] == list1[j]:
            list2.append(list1[j])
        else:
            continue

print(list2)



list1 = [("mike",1),("sarah",20), ("jim",16)]
dict1= {}

for val in list1:
    dict1[val[0]] = val[1]

print(dict1)


data = ""
def read_file_contents(filepath):
    with open(filepath,"r") as file:
        data = file.read()
        print(data)

        len = 0
        for word in data:
            if len(word) > len:
                len = len(word)
                long_word = word

        print("longest word: ",long_word)
        print("length of longest word: ",len)


def write_content_to_file(filepath, new_content):
    with open(filepath, "w") as file:
        file = open(filepath, "w")
        file.write(new_content)
        file.close()

read_file_contents("read_data.txt")
write_content_to_file("read_data.txt", "Learning Python is Fun")
"""

