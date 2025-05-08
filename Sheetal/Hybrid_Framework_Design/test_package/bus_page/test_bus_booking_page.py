from module.bus_booking_page.bus_page_class import BusPage

import pytest
print(pytest.__version__)
import time


@pytest.mark.usefixtures("get_driver")
class TestBusBooking:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        # create object of FlightPage class
        self.bp = BusPage(self.driver)

    def test_src_dest_city(self):
        # launch goibibo website
        self.driver.get("https://www.goibibo.com/")
        time.sleep(5)
        self.bp.close_popup()
        self.bp.bus_loc_click()
        self.bp.select_source_city("Mumbai")
        self.bp.select_dest_city("Delhi")
        time.sleep(10)
