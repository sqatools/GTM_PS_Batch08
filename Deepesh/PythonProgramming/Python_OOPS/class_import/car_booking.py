from selenium_code import SeleniumCode

class CarBooking(SeleniumCode):


    def book_a_car(self):
        print("Method from Car Booking class")
        self.click_element()



if __name__ == '__main__':
    obj = CarBooking()
    # every python file default module name is __main__
    print(__name__)
    obj.book_a_car()
