import os
goibibo_url = "https://www.goibibo.com/"
source_city_name = "Mumbai,India"
dest_city_name = "New Delhi,India"
cur_path = os.getcwd()
# here location may change so we are using getcwd for dynamic path
json_file_path = os.path.join(cur_path, 'modules/flight_booking_page/flight_booking_data.json')
