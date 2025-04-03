"""
Polymorphism : In this concept when we defined any single method can perform multiple task , then it is
called polymorphism
1.  Method Overriding :  when we have 2 classes and set the inheritance between them, if both the class
                        have same method name with different params,then the child class method will override
                        the parent class method and child class method will get priority.

2.  Method Overloading : When one class have two methods with same name but different parameter, then it
                          is called method overloading,  and python does not support method overloading
                          if we define two method with same name, then latest defined method will get
                          a priority.

3.  Operator Overloading :  When one operator perform multiple task, then it is called operator over loading
                        e.g. ->  plus (+) operator can add 2 int value, 2 string value and 2 list as well
                             ->  star(*) operator can multiple 2 int values, can multiply int with string, can multiply
                             list with int.
"""

# Parent class
class ABC:
    def greeting(self, n1):
        print(n1)
        print("Good Morning from ABC")

    def get_square(self, num):
        print("square of value :", num ** 2)

# Child class
class XYZ(ABC):

    def greeting(self, n1, n2):
        print(n1, n2)
        print("Good Evening From XYZ")

    def get_cube(self, num):
        print("cube of value :", num ** 3)

   # this method will be ignored.
    def addition(self, v1, v2):
        print("addition :", v1+v2)

    # This method will be considered
    def addition(self, p1, p2, p3):
        print("addition :", p1+p2+p3)

obj = XYZ()
obj.greeting(20, 40)
obj.get_square(20)

obj.addition(40, 50, 70)



####### Operator overloading #######
num1 = 100
num2 = 500

print("add numbers :", num1+num2) # 600
print("add numbers :", num1.__add__(num2)) # 600
print(dir(int))

s1 = "Hello"
s2 = "Python"
print("add words :", s1 + s2) #  HelloPython
print("add words :", s1.__add__(s2)) #  HelloPython
print(dir(str))


l1= [4, 6, 7]
l2 = ['a', 'b', 'c']
print("add list values :", l1+l2)  # [4, 6, 7, 'a', 'b', 'c']
print("add list values :", l1.__add__(l2))  # [4, 6, 7, 'a', 'b', 'c']



p1 = 60
p2 = 50
print("multiplication :", p1*p2) # 3000
print("multiplication :", p1.__mul__(p2)) # 3000

q1 = 10
q2 = 90
print("compare values :", q1 == q2)
print("compare values :", q1.__eq__(q2))

print(q1.__sub__(q2)) # -80

"""
data hiding and encapsulation:
# Encapsulation: when we bind the class data in a single unit, then it is called encapsulation. it also
restrict direct access to the some components, which helps protect the integrity of the data and
ensure proper usage.


Data hiding can be achieved in OOPS concept with help of single underscore or double underscore as prefix
with the name of variables/methods.

-> when we define method/variables with single/double underscore as prefix, then all the variables
   and methods will not show in suggestion list.

->
"""
class School:
    school_name = 'Emerald Internation School'
    _school_city = 'Mumbai'
    __school_code = 'CBSC-45852'

    def __init__(self, fee, total_st, address):
        self.school_fee = fee
        self._total_students = total_st
        self.__school_address = address

    def show_school_fee_name(self):
        print("school name :", self.school_name)
        print("school fee :", self.school_fee)


    def _show_city_total_st(self):
        print("school city :", self._school_city)
        print("Total number of student :", self._total_students)

    def __show_school_code_address(self):
        print("school code :", self.__school_code)
        print("school address :", self.__school_address)



obj = School("1 Lac", 500, "Mumbai Borwali")


obj.show_school_fee_name()
# Any variable/method with single underscore as prefix, we can access directly if we know the names
obj._show_city_total_st()


# Any variable/method with double underscore as prefix, we have to follow the pattern to access the data
# _class__variable/method

obj._School__show_school_code_address()
print(dir(obj))

print(obj._School__school_address)



# ['_School__school_address', '_School__school_code', '_School__show_school_code_address', '_school_city', '_show_city_total_st', '_total_students', 'school_fee', 'school_name', 'show_school_fee_name']

