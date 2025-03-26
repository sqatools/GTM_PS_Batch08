"""
class  : class is nothing but the blueprint of the object where we defined all the feature and
        attribute/methods for the object.
object : Object is an entity through which we can access all the property/attribute defined in the class.
         ->  We can create n number of object of the one class.
         ->  We can access all method/variable with any of the object of the class.


Method :  When we define any function inside the class then it becomes method with self as first parameter.
          1. instance method: when we defined any method we self as first parameter, then it is
             called instance method.

          2. class method:
          3. static method:

variables :  1. instance variable: instance variable that we declare with self keyword inside
                constructor, we can access the instance variable anywhere in the class.
                ->  we can instance variable inside any method as well, but to initial
                    that variable we have to call method.

                ->  Instance variable value can be changed while creating the variable.
                ->  Instance variable value we can change outside of the class with the help of
                    setter(__setattr__) and getter (__getattribute__)

             2. class variable: The variable that we declare on class level and has to assign initial value.

                ->  Can not change the value of class variable while creating the object.
                ->  can not change the class variable value with the help of class object
                ->  We can change the class variable value with the class name only
                    className.variable_name = new_value

constructor : Constructor which initialize the memory for the object of the class being created.
              we define the constructor with __init__ name
              ->  Constructor initialize automatically whenever will create a object of the class
                  no need to call the constructor.

              There are 2 types of constructor
              1.  Default constructor/: Default constructor being called internally whenever we create an object of the class.
              2.  Parametrize constructor : parametrize constructor accept the parameter and we can provide
                  values to the parameters during while creating the object of the class



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
        self.country = "India" # instance in the method.

        print("User Phone Number :", self.phone_num)

    def show_country_name(self):
        print("Country Name :", self.country)


    def get_all_details_of_user(self):
        self.show_first_name()
        self.show_last_name()
        self.show_user_email()
        self.show_user_phone()


    @classmethod
    def show_class_city_name_variable(cls):
        print(cls.user_city)
        UserDetails.get_factorials(6)
        # factorials of : 6 720


    @staticmethod
    def get_factorials(num1):
        fact = 1
        for i in range(num1, 0, -1):
            fact = fact*i

        print(f"factorials of : {num1}", fact)
        # factorials of : 5 120

obj_a = UserDetails("Rohan", "Verma", "rohan@gmail.com", "897987987890")
#obj_a.show_first_name()
# access method with object
#obj_a.get_all_details_of_user()
obj_a.show_user_phone()
#print("count name :", obj_a.country)
obj_a.show_country_name()

# access class variable with class name
print("Users city name:", UserDetails.user_city) # Users city name: Mumbai
# access class variable with object
print("City Name :", obj_a.user_city) # City Name : Mumbai

#UserDetails.show_user_email()

print("_"*50)
# get instance variable value with getter

first_name_value = obj_a.__getattribute__("first_name")
print("first name variable name :", first_name_value)

# set instance variable value with setter.
obj_a.__setattr__("first_name", "SQATools")
print("New value of first_name :", obj_a.first_name)

# setting new value to class variable
# can not change the class variable value with class object
obj_a.__setattr__("user_city :", "Kolkata")
print("class variable value :", obj_a.user_city) # Mumbai

# We can change the variable value with the help of class name
UserDetails.user_city = "Bangalore"
print("class variable value :", obj_a.user_city) # Bangalore


print("_"*50)
# call the class method with object of class.
obj_a.show_class_city_name_variable() # Bangalore


# call class method with class name.
UserDetails.show_class_city_name_variable() # Bangalore

# call the static method with class name
UserDetails.get_factorials(5) # factorials of : 5 120

