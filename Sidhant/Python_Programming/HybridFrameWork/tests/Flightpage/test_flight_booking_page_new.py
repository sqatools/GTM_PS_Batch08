from selenium.webdriver.common.by import By
from modules.flight_booking_page.flight_page_class import FlightPage
from modules.flight_booking_page.flight_booking_test_data import *
from utilities.utility_tools import Utils
import time
import pytest


@pytest.mark.usefixtures( "get_driver_goibibo" )
class TestFlightBooking:
    @pytest.fixture( scope='function', autouse=True )
    def setup(self):
        # create object of FlightPage class
        self.fp = FlightPage( self.driver )
        self.util = Utils()
        self.json_data = self.util.read_json( json_file_path )

    def test_src_dest_city(self):
        # launch goibibo website
        self.fp.close_popup()
        time.sleep( 6 )
        self.fp.select_source_city( "Mumbai, India" )
        time.sleep( 10)
        self.fp.select_dest_city( "New Delhi, India" )
        time.sleep( 10 )

    def test_select_travel_data(self):
        self.fp.select_travel_date( self.json_data['travel_date'] )
        time.sleep(20)
    def test_login_functionality(self,get_user_cred):
        user_creds = get_user_cred
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.fp.login_to_student_website(username=user_creds[0], password=user_creds[1])
