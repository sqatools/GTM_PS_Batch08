from base.api_base import APIBase
from .ready_to_use_api_data import *


class ReadyToUseAPI(APIBase):

    def get_all_list_of_users(self):
        response, st_code = self.get_method(url=main_api_url)
        self.log.info(f"response: {response}")
        self.log.info(f"status_code :{st_code}")
        return response, st_code
