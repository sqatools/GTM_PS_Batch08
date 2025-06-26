import time

import pytest
from flight_booking_page import FlightBookingPage


@pytest.mark.usefixtures("get_driver")
class TestFlightBookingPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.fp = FlightBookingPage(self.driver)


    def test_src_dest_city(self):
        self.fp.close_icon()
        time.sleep(5)
        self.fp.notification_cancel()
        time.sleep(5)
        self.fp.default_content_switch()
        time.sleep(5)
        self.fp.select_source_city(city_name="Chennai, India")
        self.fp.select_dest_city(dest_city_name='Mumbai, India')
        #time.sleep(5)

    def test_departure(self):
        self.fp.select_departure_date(date_value='Thu May 08 2025')
        time.sleep(10)

    def test_traveller_details(self):
        self.fp.select_travellers_details()
        time.sleep(10)
        self.fp.click_done_button()
        time.sleep(5)

    def test_search_view(self):
        self.fp.search_button()
        time.sleep(10)

    def okay_test_got_it(self):
        self.fp.okay_gotit()
        time.sleep(5)
    def test_travel_select(self):
        self.fp.compare_close_button()
        time.sleep(5)
    def test_fare_details(self):
        self.fp.fare_details()

    def test_book_now(self):
        self.fp.book_now()

    # def test_user_consent(self):
    #     self.fp.user_consent()

    def test_summary(self):
        summary = self.fp.summary()
        print(summary)

