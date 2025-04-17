from car_booking import CarBooking
from flight_booking import FlightBooking
from train_booking import TrainBooking
from hotel_booking import HotelBooking

class UseCases:

    def book_a_car_and_verify(self):
        car = CarBooking()
        car.book_a_car()
        print("module name :", car.__module__)


    def book_flight_and_verify(self):
        fl = FlightBooking()
        fl.book_a_flight()

    def book_hotel_and_verify(self):
        htl = HotelBooking()
        htl.book_a_Hotel()


    def book_train_and_verify(self):
        trn = TrainBooking()
        trn.book_a_Train()



obj = UseCases()

#obj.book_train_and_verify()
# print("_"*50)
obj.book_a_car_and_verify()
# print("_"*50)
# obj.book_flight_and_verify()
# print("_"*50)
# obj.book_hotel_and_verify()
