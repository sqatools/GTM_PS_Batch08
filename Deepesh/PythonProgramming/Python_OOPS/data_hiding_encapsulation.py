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

# Any variable/method with single underscore as prefix, we can access directly if we know the names
obj._show_city_total_st()


# Any variable/method with double underscore as prefix, we have to follow the pattern to access the data
# _class__variable/method

obj._School__show_school_code_address()
print(dir(obj))

print(obj._School__school_address)



# ['_School__school_address', '_School__school_code', '_School__show_school_code_address', '_school_city', '_show_city_total_st', '_total_students', 'school_fee', 'school_name', 'show_school_fee_name']

