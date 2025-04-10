"""
Data hiding and encapsulation:
data hiding can be achieved in OOPS concept with the help of single underscore(_) or double underscoore (__)
as prefix with the name of variables/methods

-> when we define method/variables with single/double underscore ass prefix , then all the variables
   and methods
"""
class school:
    school_name = 'Delhi public school'
    _school_city = 'hyderabad'
    __school_code = 'Icse-7894'

    def __int__(self, fee, total_students, address):
        self.school_fee = fee
        self._total_students = total_students
        self.__school_address = address

    def show_school_fee_name(self):
        print("school name :", self.school_name)
        print("school fee :", self.school_fee)



    def _show_city_total_students(self):
        print("school city :", self._school_city)
        print(" total number odd students :", self._total_students)



    def __show_school_code_address(self):
        print("school code :", self.__school_code)
        print("school address :", self.__school_address)


obj = school("2 lac", "500", "Hyderabad Begumpet")

#any variable/method with single underscore as prefix, we can access directly if we know the names
obj._show_city_total_students()