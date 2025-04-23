import pytest
from flight_booking_page import FlightBookingPage

@pytest.mark.usefixtures("get_driver")
class TestFlightBooking:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.fp = FlightBookingPage(self.driver)


    def test_select_source_and_dest_city(self):
        self.fp.close_singup_popup()
        self.fp.select_source_city(city_name='Mumbai, India')
        self.fp.select_dest_city(dest_city="New Delhi, India")



