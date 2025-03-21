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
