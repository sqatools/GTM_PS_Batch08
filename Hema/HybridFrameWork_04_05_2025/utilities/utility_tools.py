import json
import os
from datetime import datetime


class Utils:

    def read_json(self, filepath):
        with open(filepath, "r") as file:
            data = file.read()
            json_data = json.loads(data)
            return json_data

    def generate_unique_name(self):
        return datetime.now().strftime("%d_%m_%y_%H_%M_%S")

if __name__=='__main__':
    cur_path = os.getcwd()
    util = Utils()