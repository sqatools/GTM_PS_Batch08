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


# single inheritance:  When one class aquire the property of another class, then it is called single inheritance

# parent class / super class / base class
class father:
    def __init__(self, f_name, f_business, f_house):
        self.father_name = f_name
        self.father_business = f_business
        self.father_house = f_house

    def show_father_details(self):
        print("Father name :", self.father_name)
        print("Father Business :", self.father_business)
        print("Father House :", self.father_house)


# child class / sub class / derived class
class Son(father):
    """
    When we setup inheritance between 2 classes, then we can initiate the constructor of parent class
    into child class constructor with super keyword.


    """

    def __init__(self, son_name, f_name, f_business, f_house):
        super().__init__(f_name, f_business, f_house)
        self.son_name = son_name

    def show_son_name(self):
        print("Name of son :", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_son_name()


obj = Son("Mohit", "Mohan", "Construction", "4 BHK")
obj.show_family_details()

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


# multilevel inheritance: When we have multiple class are connected in sequence via inheritance then
#                         it is called multi level inheritance. e.g class A ->  class B ->  class C

def addition(n1, n2):
    print(n1+n2)

def math_operation(v1, v2, v3):
    addition(v1, v2, v3)
    print(v2*v3)

def fun3(n1, n2, n3, v3):
    math_operation(n1, n2, n3)
    print(v3**2)

fun3(40, 50, 60, 70)


class grand_father:
    def __init__(self, grand_f_name, grand_f_land):
        self.grand_f_name = grand_f_name
        self.grand_f_land = grand_f_land

    def show_grand_father_details(self):
        print("Grand father name :", self.grand_f_name)
        print("Grand father property :", self.grand_f_land)


# parent class / super class / base class
class father(grand_father):
    def __init__(self, f_name, f_business, f_house, grand_f_name, grand_f_land):
        super().__init__(grand_f_name, grand_f_land)
        self.father_name = f_name
        self.father_business = f_business
        self.father_house = f_house

    def show_father_details(self):
        print("Father name :", self.father_name)
        print("Father Business :", self.father_business)
        print("Father House :", self.father_house)


# child class / sub class / derived class
class Son(father):
    """
    When we setup inheritance between 2 classes, then we can initiate the constructor of parent class
    into child class constructor with super keyword.


    """

    def __init__(self, son_name, f_name, f_business, f_house, grand_f_name, grand_f_land):
        super().__init__(f_name, f_business, f_house, grand_f_name, grand_f_land)
        self.son_name = son_name

    def show_son_name(self):
        print("Name of son :", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_son_name()


obj = Son("Mohit", "Mohan", "Builder", "Banglow", "Ramchandra", "200Acr")
obj.show_grand_father_details()
obj.show_father_details()
obj.show_son_name()
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
        #super().__init__(f_name, f_business, f_house)
        self.son_name = son_name
        self.f_name = f_name
        self.f_business = f_business
        self.f_house = f_house
        self.fobj = Father(self.f_name, self.f_business, self.f_house)

    def show_son_name(self):
        print("Name of son :", self.son_name)

    def show_family_details(self):
        self.fobj.show_father_details()
        self.show_mother_details()
        self.show_son_name()


obj = Son("Mohit", "Jenny", "Fashion", "Rohan", "Media", "4BHK")
#obj.fobj.show_father_details()
obj.show_family_details()
# obj.show_mother_details()
# obj.show_son_name()

print("_"*50)
fobj = Father("Mohan", "Construction", "Bangalow")
fobj.show_father_details()

