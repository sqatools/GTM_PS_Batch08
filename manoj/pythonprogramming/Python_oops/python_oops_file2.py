country = "India"  # global variable


class ITCompany:
    comp_name = "TCS"

    # parameterize construction
    def __int__(self, comp_address, comp_project, comp_revenue):
        self.company_address = comp_address  # instance variable
        self.company_project = comp_project  # instance variable
        self.company_revenue = comp_revenue  # instance variable

    # instance method
    def show_company_details(self):
        print("country name :", country)
        print("company address :", self.company_address)
        print("company project :", self.company_project)
        print("company revenue :", self.company_revenue)

    # class method
    def show_company_name(cls):
        print("company name :", cls.comp_name)

    @staticmethod
    def print_table(num1):
        for i in range(1, 11):
            print(i, "*", num1, ":", i * num1)


obj1 = ITCompany("Abids", "Aadharcentre", "10lak")

# what is self : self is nothing but the object of the current class,
#                whenever we call the instance method with the object of the class, then internally the object is the
#                first parameter to the method

# access the instance method with object
#obj1.show_company_details()

# access the class method
ITCompany.show_company_name()

# access the static method
ITCompany.print_table(7)

