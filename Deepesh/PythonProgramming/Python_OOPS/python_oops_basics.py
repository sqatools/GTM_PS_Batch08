"""
class  : class is nothing but the blueprint of the object where we defined all the feature and
        attribute/methods for the object.
object : Object is an entity through which we can access all the property/attribute defined in the class.
         ->  We can create n number of object of the one class.
         ->  We can access all method/variable with any of the object of the class.


Method :  When we define any function inside the class then it becomes method with self as first parameter.
          1. instance method:
          2. class method:
          3. static method:

variables :  1. instance variable:
             2. class variable:


constructor : Constructor which initialize the memory for the object of the class being created.
              we define the constructor with __init__ name
              ->  Constructor initialize automatically whenever will create a object of the class
                  no need to call the constructor.

              There are 2 types of constructor
              1.  Default constructor/: Default constructor being called internally whenever we create an object of the class.
              2.  Parametrize constructor :


"""


# creating a class
class Car:

    # default constructor
    def __init__(self):
        print("Welcome to TATA Motors")
        # print(self.car_color())

    # Method
    def car_name(self):
        return "TATA Safari"

    def car_price(self):
        return "20 Lac Rupee"

    def car_company(self):
        return "TATA"

    def car_color(self):
        return "Blue"


# create object of the class, outside the class
# obj = Car()
# calling the method with object
# print("Car Name :", obj.car_name())
#
# print(obj.car_price())
# print(obj.car_company())
# print(obj.car_color())

# obj1 = Car()
# obj2 = Car()
# obj3 = Car()


# class with parametrize constructor

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
        print("User Phone Number :", self.phone_num)

    def get_all_details_of_user(self):
        self.show_first_name()
        self.show_last_name()
        self.show_user_email()
        self.show_user_phone()


obj_a = UserDetails("Rohan", "Verma", "rohan@gmail.com", "897987987890")
#obj_a.show_first_name()
# access method with object
obj_a.get_all_details_of_user()


# access class variable with class name
print("Users city name:", UserDetails.user_city)

UserDetails.show_user_email()
