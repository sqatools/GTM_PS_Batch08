import time

from selenium.webdriver.common.by import By
from modules.flight_booking_page.flight_page_class import FlightPageBase
import pytest

@pytest.mark.usefixtures("get_driver")
class TestFlightBooking:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.fp = FlightPageBase(self.driver)

    def test_src_dest_city(self):
        self.driver.get("https://www.goibibo.com/")
        time.sleep(10)
        self.fp.select_source_city("Mumbai, India")
        self.fp.select_dest_city("New Delhi, India")
        time.sleep(10)
        self.fp.