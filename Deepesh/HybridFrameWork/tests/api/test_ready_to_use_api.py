import pytest
from modules.api.ready_to_use_api.ready_use_api_class import ReadyToUseAPI
from modules.api.ready_to_use_api.ready_to_use_api_data import *

class TestReadyToUseAPI:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.r_api = ReadyToUseAPI()

    def test_get_all_object_and_verify(self):
        response, st_code = self.r_api.get_all_list_of_users()
        assert  len(response) == 13
        assert  st_code == 200

    def test_specific_ids_details(self):
        response, st_code = self.r_api.get_specific_ids_details(users_ids)
        assert len(response) == 3
        assert st_code == 200


    def test_single_id_details(self):
        response, st_code = self.r_api.get_single_id_details(5)
        assert len(response) == 3
        assert st_code == 200

    def test_create_new_object_entry(self):
        response, st_code = self.r_api.add_new_object_entry(json_headers, create_object_payload)
        assert len(response) == 4
        assert st_code == 200
        assert response['name'] == 'Apple MacBook Pro 200'

    def test_update_new_object_entry(self):
        response, st_code, obj_id = self.r_api.update_object_details(json_headers,
                                                             post_payload1, put_payload1)
        assert len(response) == 4
        assert st_code == 200
        assert response['name'] == 'Apple MacBook Pro 500'
        assert response['id'] == obj_id


    def test_update_specific_value_entry(self):
        response, st_code, obj_id = self.r_api.update_specific_value_of_object(json_headers,
                                                             post_payload2, patch_payload)
        assert len(response) == 4
        assert st_code == 200
        assert response['name'] == 'Apple iPhone 20'
        assert response['id'] == obj_id

    def test_delete_object_entry(self):
        response, st_code, obj_id = self.r_api.delete_object_entry(json_headers,
                                                             post_payload3)
        assert len(response) == 1
        assert st_code == 200
        assert 'has been deleted' in response['message']


    def test_users_details_with_bearer_token(self):
        response, st_code = self.r_api.api_access_with_token()
        assert response
        assert st_code == 200





