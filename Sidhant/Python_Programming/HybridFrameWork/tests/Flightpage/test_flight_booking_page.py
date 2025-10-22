
from modules.flight_booking_page.flight_page_class import FlightPage
from modules.flight_booking_page.flight_booking_test_data import *
from utilities.utility_tools import Utils
import time
import pytest


@pytest.mark.usefixtures("get_driver")
class TestFlightBooking:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        # create object of FlightPage class
        self.fp = FlightPage(self.driver)
        self.util = Utils()
        self.json_data = self.util.read_json(json_file_path)

    def test_src_dest_city(self, request):
        # launch goibibo website
        self.fp.log.info(f"Test Name: {request.node.name}")
        self.fp.close_popup()
        time.sleep(2)
        self.fp.close_popup_second()
        time.sleep(3)
        self.fp.select_source_city("Mumbai")
        self.fp.select_dest_city("New Delhi")
        self.fp.capture_screenshot()
        time.sleep(6)

    def test_select_travel_data(self):
        self.fp.select_travel_date(self.json_data['travel_date'])
        time.sleep(10)

    def test_travel_class(self):
        self.fp.select_Travel_and_class(self.json_data['adults'])
        time.sleep(5)
        self.fp.search_btn_All()
        self.fp.capture_screenshot()
