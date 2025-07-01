from base.api_base import APIBase
from .ready_api_data import  *

class ReadyAPI(APIBase):

    def get_all_objects_details(self):
        response, st_code = self.get_method(url=ready_api_url)
        return response, st_code

    def get_list_of_objects(self, ids_list):
        updated_url = f"{ready_api_url}?"
        for id in ids_list:
            updated_url = updated_url + f"id={id}&"
        response, st_code = self.get_method(url=updated_url)
        return response, st_code

    def get_one_object_details(self, id):
        updated_url = f"{ready_api_url}/{id}"
        response, st_code = self.get_method(url=updated_url)
        return response, st_code

    def add_new_object(self):
        response, st_code = self.post_method(url=ready_api_url, payload=object_json_payload, headers=headers)
        new_id = response['id']
        self.log.info(f"new object id: {new_id}")
        return response, st_code

    def update_new_object_details(self):
        response, st_code = self.post_method(url=ready_api_url, payload=object_json_payload, headers=headers)
        new_id = response['id']
        updated_url = f"{ready_api_url}/{new_id}"
        self.log.info(f"new object id: {new_id}")
        response, st_code = self.put_method(url=updated_url, payload=put_object_details_json, headers=headers)
        return response, st_code

    def patch_new_object_details(self):
        response, st_code = self.post_method(url=ready_api_url, payload=object_json_payload, headers=headers)
        new_id = response['id']
        updated_url = f"{ready_api_url}/{new_id}"
        self.log.info(f"new object id: {new_id}")
        response, st_code = self.patch_method(url=updated_url, payload=patch_object_details_json, headers=headers)
        return response, st_code

    def delete_new_object_details(self):
        response, st_code = self.post_method(url=ready_api_url, payload=object_json_payload, headers=headers)
        new_id = response['id']
        updated_url = f"{ready_api_url}/{new_id}"
        self.log.info(f"new object id: {new_id}")
        response, st_code = self.delete_method(url=updated_url)
        return response, st_code


    def get_all_users_details_with_token(self):
        response, st_code = self.get_method(url=users_details_url, headers=auth_headers)
        return response, st_code


