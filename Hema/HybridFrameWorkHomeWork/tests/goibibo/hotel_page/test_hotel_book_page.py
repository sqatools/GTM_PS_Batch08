from selenium.webdriver.common.by import By
from Hema.HybridFrameWorkHomeWork.modules.goibibo.hotel_booking_page.hotel_page_class import HotelPage
from Hema.HybridFrameWorkHomeWork.modules.goibibo.hotel_booking_page.hotel_booking_test_data import *
from Hema.HybridFrameWorkHomeWork.utilities.utiltity_tools import Utils
import time
import pytest

@pytest.mark.usefixtures("get_driver")
class TestHotelBooking:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        # create object of HotelBook class
        self.fp = HotelPage(self.driver)
        self.util = Utils()
        self.json_data = self.util.read_json(json_file_path)

    def test_hotel(self, request):
        self.fp.log.info(f"Test Name: {request.node.name}")
        # launch goibibo website
        self.fp.close_popup()
        self.fp.select_location(where_to)
        self.fp.capture_screenshot()

    def test_select_travel_date(self, request):
        self.fp.log.info(f"Test Name: {request.node.name}")
        self.fp.select_checkin_date( self.json_data['check-in'])
        self.fp.capture_screenshot(passed_images)
        time.sleep(10)
        self.fp.select_checkout_date(self.json_data['check-out'])
        self.fp.capture_screenshot(passed_images)
        time.sleep(10)
        self.fp.click_guest_room()
        self.fp.capture_screenshot(passed_images)
        time.sleep(10)
        self.fp.select_room_count(self.json_data['room_count'])
        self.fp.capture_screenshot(passed_images)
        time.sleep(10)
        self.fp.select_adult_count(self.json_data['adult_count'])
        self.fp.capture_screenshot(passed_images)
        time.sleep(10)
        self.fp.select_child_count(self.json_data['child_count'])
        self.fp.capture_screenshot(passed_images)
        time.sleep(10)
        self.fp.done_option()
        self.fp.search_click()
