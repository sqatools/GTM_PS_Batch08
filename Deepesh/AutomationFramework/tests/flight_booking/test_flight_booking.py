import pytest
from modules.flight_page.flight_booking_page import FlightBookingPage
from modules.flight_page.flight_booking_page_data import *


@pytest.mark.usefixtures("get_driver")
class TestFlightBooking:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.fb = FlightBookingPage(self.driver)


    def test_select_source_and_Dest_city(self):
        self.fb.close_login_popup()
        self.fb.enter_source_city(source_city_name)
        self.fb.enter_dest_city(dest_city_name)
        self.fb.select_depart_date(depart_date)
