from selenium.webdriver.common.by import By
from modules.flight_booking_page.flight_page_class import FlightPage
import time
import pytest

@pytest.mark.usefixtures("get_driver")
class TestFlightBooking:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        # create object of FlightPage class
        self.fp = FlightPage(self.driver)

    def test_src_dest_city(self):
        # launch goibibo website
        self.driver.get("https://www.goibibo.com/")
        time.sleep(5)
        self.fp.select_source_city("Mumbai, India")
        self.fp.select_dest_city("New Delhi, India")
        time.sleep(10)


