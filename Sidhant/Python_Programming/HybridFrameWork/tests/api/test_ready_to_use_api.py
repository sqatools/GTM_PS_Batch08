import pytest
from modules.api.ready_to_use_api.ready_use_api_class import ReadyToAPI
from modules.api.ready_to_use_api.ready_to_use_api_data import *
import pprint




class TestReadyToUseAPI:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.r_api = ReadyToAPI()

    # def test_get_all_object_and_verify(self):
    #     response, st_code = self.r_api.get_all_list_of_users()
    #     assert len(response) == 13
    #     assert st_code == 200
    # def test_get_specific_data(self):
    #     response, st_code = self.r_api.get_specified_list_of_object(user_id)
    #     assert len(response) == 3
    #     assert st_code == 200
    #
    # def test_single_id_details(self):
    #     response, st_code = self.r_api.get_single_id_details(7)
    #     assert len(response) == 3
    #     assert st_code == 200

    def test_add_new_object(self):
        response, st_code = self.r_api.create_an_object(json_header, create_object_payload1)
        assert len(response) == 4
        assert st_code == 200
        pprint.pprint(response)
        assert response['name'] == "Apple MacBook Pro 160"

    # def test_updated_new_object(self):
    #     response, st_code, obj_id = self.r_api.update_an_object(json_header, post_payload, put_payload)
    #     assert len(response) == 4
    #     assert st_code == 200
    #     assert response['name'] == "Apple MacBook Pro 260"
    #     assert response['id'] == obj_id
    #
    # def test_update_specific_value_id(self):
    #     response, st_code, obj_id = self.r_api.update_specific_value_of_object(json_header, post_payload, patch_payload)
    #     assert len(response) == 4
    #     assert st_code == 200
    #     assert response['name'] == "Apple Iphone Pro 160"
    #     assert response['id'] == obj_id
    #
    # def test_delete_object_detail(self):
    #     response, st_code, obj_id = self.r_api.delete_object_entry(json_header, post_payload1)
    #     assert len(response) == 1
    #     assert st_code == 200
    #     assert response['message'] == f"Object with id = {obj_id} has been deleted."
    #
    # def test_users_details_with_bearer_token(self):
    #     response, st_code = self.r_api.api_access_with_token()
    #     assert response
    #     assert st_code == 200