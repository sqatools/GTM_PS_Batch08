import json

from base.api_base import APIBase
from .ready_to_use_api_data import *

class ReadyToUseApi(APIBase):

    def get_all_lists_of_users(self):
        response, st_code = self.get_method(url=main_api_url)
        self.log.info(f"response: {response}")
        self.log.info(f"status_code: {st_code}")
        return response, st_code


    def create_new_user(self, data):
        payload=json.dumps(json_create_one_data)
        response, st_code = self.post_method(url=main_api_url, headers=headers, data=payload)
        #print(response.text)
        self.log.info(f"respnse: {response}")
        self.log.info(f"status_code: {st_code}")
        return response, st_code

    # def write_json_data(filepath, new_content):
    #     with open(filepath, "w") as file:
    #         print(new_content)
    #         json_dump = json.dumps(new_content)
    #         print(json_dump)
    #         file.write(json_dump)

