import os
import time

import pytest
from modules.bus_page.bus_booking_page_class import BusBooking
from modules.bus_page.bus_booking_page_data import *
from utilities.utils_tools import UtilTools

@pytest.mark.usefixtures("get_driver")
class TestBusBooking():

    @pytest.fixture(autouse=True)
    def setup(self):
        self.bus = BusBooking(self.driver)
        self.util = UtilTools()
        cur_dir = os.getcwd()
        self.json_data = self.util.read_json_content(f"{cur_dir}\\modules\\bus_page\\bus_booking_data.json")

    @pytest.mark.smoke
    def test_navigate_to_bus(self, request):
        self.bus.log.info(f"TEST CASE: {request.node.name}")
        self.bus.goto_bus_booking_page()

    def test_select_src_city(self, request):
        self.bus.log.info(f"TEST CASE: {request.node.name}")
        self.bus.select_from_city(src_city)

    def test_select_dest_city(self, request):
        self.bus.log.info(f"TEST CASE: {request.node.name}")
        self.bus.select_dest_city(dest_city)

    def test_select_depart_date(self, request):
        self.bus.log.info(f"TEST CASE: {request.node.name}")
        self.bus.select_depart_date(next_2_days_date)

    def test_click_to_search_button(self, request):
        self.bus.log.info(f"TEST CASE: {request.node.name}")
        self.bus.click_search_button()
        time.sleep(20)
    def test_select_bus_to_travel(self, request):
         self.bus.log.info(f"TEST CASE: {request.node.name}")
         self.bus.select_bus(self.json_data['select_bus_name'])
         self.bus.select_boarding_point(self.json_data['boarding_point'])
         self.bus.select_dropping_point(self.json_data['dropping_point'])
         self.bus.select_seat()
         time.sleep(5)
         self.bus.click_to_continue_button()
         time.sleep(5)
         self.bus.enter_passenger_details(
             name=self.json_data['passenger_name'],
             age=self.json_data['age'],
             email=self.json_data['email'],
             phone=self.json_data['phone'],
             address=self.json_data['address'],
             pincode=self.json_data['pincode'],
             state_name=self.json_data['state_name'],
             flight_type=self.json_data['flight_type'],
             gender=self.json_data['gender']
         )
         self.bus.add_promo_code(self.json_data['promo_code'])
         self.bus.click_to_pay_button()
         time.sleep(10)
