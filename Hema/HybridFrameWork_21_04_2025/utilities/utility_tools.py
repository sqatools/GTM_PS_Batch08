import json
import os


class Utils:

    def read_json(self, file_path):
        with open(file_path, "r") as file:
            data = file.read()
            json_data = json.loads(data)
            return json_data




if __name__ == '__main__':
    cur_path = os.getcwd()
    #filepath = os.path(cur_path, 'modules/flight_booking_page/flight_page_data.json')
    filepath = r"E:\Trainings\GTM_PS_Batch08_6Jan25\GTM_PS_Batch08\Deepesh\HybridFrameWork\modules\flight_booking_page\flight_booking_data.json"
    util = Utils()
    data = util.read_json(filepath)
    print(data)
    print(data['source_city'])
