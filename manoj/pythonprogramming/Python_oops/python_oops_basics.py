""""
class  : class is nothing but the blueprint of the object where we define all the
         feature, attribute/method for the project
object : Object is an entity through which we can access all the property/attribute define in the class
        -> we can create  n number of object of the class
        -> we can access all method/variable with any of the object in the class
method : when we define any function inside the class then it becomes method with self as first parameter
         1. instance method : when we defined any method we self as first parameter, then it is called
            instance method.

         -> Instance variable value can be change while creating the variable
         -> Instance variable value we can change outside of the class with help of
            setter(__setattr__) and getter(__getattribute__)
         2. class method
         3.static method
constructor : constructor initialize the memory for the object of the class being created
              we define the constructor with the help of  __int__name
              -> constructor initialize automatically whenever will create object of the class
                no need to call the constructor .

              There are 2 types of constructor
              1. Default constructor : Default constructor being called internally whenever we create the object of the class.
              2. Parameterize constructor:

"""

# creating a class

class Car:
    # default constructor
    def __int__(self):
        print("welcome to TATA")

        #print(self.car_color())

    # method
    def car_name(self):
        return " xuv300"

    def car_price(self):
        return "15lac rupees"

    def car_company(self):
        return "TATA"

    def car_color(self):
        return "black"


# create object of the class
obj = Car()
# calling the method with object
# print("Car Name :", obj.car_name())
#
# print(obj.car_company())
# print(obj.car_price())
# print(obj.car_color())

# obj1 = Car()
# obj2 = Car()
# obj3 = Car()


# class with parametrize constructor

class UserDetails:
    # class variable
    user_city = "Hyderabad"

    # parametrize constructor
    def __int__(self, firstname, lastname, email, phone):
        print(" welcome to the users")
        self.first_name = firstname
        self.last_name = lastname
        self.user_email = email
        self.phone_num = phone

    def show_first_name(self):
        print(" user First Name :", self.first_name)

    def show_last_name(self):
        print("lastname :", self.last_name)

    def show_user_email(self):
        print("user email:", self.user_email)

    def show_phone_num(self):
        print("user phone number:", self.phone_num)

    def get_all_details_of_user(self):
        self.show_last_name()
        self.show_first_name()
        self.show_user_email()
        self.show_phone_num()

    @classmethod
    def show_class_city_name_variable(cls):

    @staticmethod
    def get_factorials(num1):
        fact = 1
        for i in range(num1, 0, -1):
            fact =fact*i

        print(f"factorials: {num1}", fact)


obj_a = UserDetails("manoj", "jaini")
obj_a.show_first_name()
# access method with object
obj_a.get_all_details_of_user()

# access class variable with class name
print("User city name:", UserDetails.user_city)



# get instance variable value with getter
first_name_value = obj_a.__getattribute__("first_name")
print("first name variable name :", first_name_value)

# set instance variable with setter
obj_a.__setattr__("first_name", "SQATools")
print("New value of first_name :", obj_a.first_name)

# setting new value to class variable
obj_a.__setattr__("user_city :", "kolkata")
print("class variable value :", obj_a.user_city)

UserDetails.user_city = "Bangalore"
print(" class variable value :", obj_a.user_city)


# call the class method with obj
obj_a.show_class_city_name_variable()

# call class method with class name
UserDetails.show_class_city_name_variable()

# call the static method with class name
UserDetails.get_factorials(5)
