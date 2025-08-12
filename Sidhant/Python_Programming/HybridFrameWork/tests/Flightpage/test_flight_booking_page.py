from selenium.webdriver.common.by import By
from modules.flight_booking_page.flight_page_class import FlightPage
from modules.flight_booking_page.flight_booking_test_data import *
from utilities.utility_tools import Utils
import time
import pytest


@pytest.mark.usefixtures( "get_driver" )
class TestFlightBooking:
    @pytest.fixture( scope='function', autouse=True )
    def setup(self):
        # create object of FlightPage class
        self.fp = FlightPage( self.driver )
        self.util = Utils()
        self.json_data = self.util.read_json( json_file_path )

    def test_src_dest_city(self,request):
        # launch goibibo website
        self.fp.log.info(f"Test Name: {request.node.name}")
        self.fp.close_popup()
        time.sleep( 6 )
        self.fp.select_source_city( "Mumbai, India" )
        self.fp.select_dest_city( "New Delhi, India" )
        self.fp.capture_screenshot()


    def test_select_travel_data(self):
        self.fp.select_travel_date( self.json_data['travel_date'] )
        time.sleep(20)
