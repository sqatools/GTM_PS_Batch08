"""
1.  Single level Inheritance:
     class A(father) ->  class B (Son)

2.  Multilevel Inheritance:
      class A(grand father) ->  class B (Father ) ->  class C (Son)

3.  Multiple Inheritance:
    class A (father) ->  class B (Son)
    class C (mother)  -> class B (Son)

4.  Hierarchical Inheritance
    class A(Father)  ->  class B (Son1)
    class A (Father) ->  class C (Son2)

5.  Hybrid  Inheritance


"""
# multiple Inheritance :  When one class can access the property of two other classes, then it is called
#                         multiple inheritance


# parent class / super class / base class
class Mother:
    def __init__(self, mother_name, mother_business):
        self.mother_name = mother_name
        self.mother_business =  mother_business


    def show_mother_details(self):
        print("Mother Name :", self.mother_name)
        print("Mother Business :", self.mother_business)

    def greeting(self):
        print("Welcome to Mother class")


# parent class / super class / base class
class Father:
    def __init__(self, f_name, f_business, f_house):
        self.father_name = f_name
        self.father_business = f_business
        self.father_house = f_house

    def show_father_details(self):
        print("Father name :", self.father_name)
        print("Father Business :", self.father_business)
        print("Father House :", self.father_house)

    def greeting(self):
        print("Welcome to Father class")

# MRO (Method Resolution Order) :  When we setup multiple inheritance and define 2 class to the base
#                                  class to setup inheritance, then which ever class is defined first
#                                  will get priority to initiate the construction in the child class.

class Son(Mother, Father):
    """
    When we setup inheritance between 2 classes, then we can initiate the constructor of parent class
    into child class constructor with super keyword.


    """

    def __init__(self, son_name, mother_name, mother_business, f_name, f_business, f_house):
        super().__init__(mother_name, mother_business)
        self.son_name = son_name
        self.father_name = f_name
        self.father_business = f_business
        self.father_house = f_house

    def show_son_name(self):
        print("Name of son :", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_mother_details()
        self.show_son_name()

    def greeting(self):
        print("Welcome to Son class")


obj = Son("Mohit", "Jenny", "Fashion", "Rohan", "Media", "4BHK")
obj.show_family_details()
obj.show_father_details()
print("_"*50)
obj.greeting()
