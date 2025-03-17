""""
class  : class is nothing but the blueprint of the object where we define all the
         feature, attribute/method for the project
object : Object is an entity through which we can access all the property/attribute define in the class
        -> we can create  n number of object of the class
        -> we can access all method/variable with any of the object in the class
method : when we define any function inside the class then it becomes method with self as first parameter
         1. instance method
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


obj_a = UserDetails("Jaini", "manoj")
# obj_a.show_first_name()
# access method with object
obj_a.get_all_details_of_user()

# access class variable with class name
print("User city name:", UserDetails.user_city)
