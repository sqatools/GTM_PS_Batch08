import json
import os
from datetime import datetime


class Utils:
    def read_json(self, file_path):
        with open( file_path, "r" ) as file:
            data = file.read()
            json_data = json.loads(data)
            return json_data

    def generate_unique_name(self):
        return datetime.now().strftime("%d_%m_%y_%H_%M_%S")


if __name__ == '__main__':
    cur_path = os.getcwd()
    # filepath = r"C:\Python Automation\Sid_Automation_code\GTM_PS_Batch08\Sidhant\Python_Programming\HybridFrameWork\modules\flight_booking_page\flight_booking_data.json"
    util = Utils()
    # data = util.read_json(filepath)
    # print(data)
    # print(data['travel_date'])
    print(util.generate_unique_name())