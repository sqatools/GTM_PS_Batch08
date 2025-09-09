from base.api_base import APIBase
from .ready_to_use_api_data import *


class ReadyToAPI(APIBase):
    def get_all_list_of_users(self):
        response, st_code = self.get_method(url=main_api_url)
        self.log.info(f"response: {response}")
        self.log.info(f"status_code: {st_code}")
        return response, st_code

    def get_specified_list_of_object(self, id_list):
        new_url = f"{main_api_url}?"
        for id_value in id_list:
            new_url += f"id={id_value}&"
        response, st_code = self.get_method(url=new_url)
        self.log.info(f"response: {response}")
        self.log.info(f"status_code: {st_code}")
        return response, st_code

    def get_single_id_details(self, id_value):
        response, st_code = self.get_method(url=f"{main_api_url}/{id_value}")
        self.log.info(f"response: {response}")
        self.log.info(f"status_code: {st_code}")
        return response, st_code

    def create_an_object(self, headers, request_data):
        response, st_code = self.post_method(url=main_api_url, headers=headers, payload=request_data)
        self.log.info(f"response: {response}")
        self.log.info(f"status_code: {st_code}")
        return response, st_code

    def update_an_object(self, headers, post_data, put_data):
        response, st_code = self.post_method(url=main_api_url, headers=headers, payload=post_data)
        self.log.info(f"response: {response}")
        self.log.info(f"status_code: {st_code}")
        object_id = response['id']
        self.log.info(f"new id: {object_id}")
        new_url = f"{main_api_url}/{object_id}"
        put_response, put_st_code = self.put_method(url=new_url, headers=headers, payload=put_data)
        self.log.info(f"put_response: {put_response}")
        self.log.info(f"put_status_code: {put_st_code}")
        return put_response, put_st_code, object_id

    def update_specific_value_of_object(self, headers, post_data, patch_data):
        response, st_code = self.post_method(url=main_api_url, headers=headers, payload=post_data)
        self.log.info(f"response: {response}")
        self.log.info(f"status_code: {st_code}")
        object_id = response['id']
        self.log.info(f"new id: {object_id}")
        new_url = f"{main_api_url}/{object_id}"
        patch_response, patch_st_code = self.patch_method(url=new_url, headers=headers, payload=patch_data)
        return patch_response, patch_st_code, object_id

    def delete_object_entry(self, headers, post_data):
        response, st_code = self.post_method(url=main_api_url, headers=headers, payload=post_data)
        self.log.info(f"response: {response}")
        self.log.info(f"status_code: {st_code}")
        object_id = response['id']
        self.log.info(f"new id: {object_id}")
        new_url = f"{main_api_url}/{object_id}"
        delete_response, delete_st_code = self.delete_method(url=new_url)
        self.log.info(f"delete_response: {delete_response}")
        self.log.info(f"delete_status_code: {delete_st_code}")
        return delete_response, delete_st_code, object_id

    def api_access_with_token(self):
        response, st_code = self.get_method(url=token_api_url, headers=auth_headers)
        self.log.info(f"response: {response}")
        self.log.info(f"status_code: {st_code}")
        return response, st_code
