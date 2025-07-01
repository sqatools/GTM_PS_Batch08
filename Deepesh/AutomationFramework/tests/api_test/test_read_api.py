import pytest
from api.ready_api.ready_api_class import ReadyAPI
from api.ready_api.ready_api_data import *

class TestReadyAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.r_api = ReadyAPI()

    def test_get_object_and_verify(self):
        res, st_code = self.r_api.get_all_objects_details()
        assert len(res) == 13
        assert st_code == 200

    def test_get_ids_list_object_verify(self):
        res, st_code = self.r_api.get_list_of_objects(ids_list)
        assert len(res) == 3
        assert st_code == 200

    def test_get_one_object_and_verify(self):
        res, st_code = self.r_api.get_one_object_details(4)
        assert len(res) == 3
        assert res['name'] == 'Apple iPhone 11, 64GB'
        assert st_code == 200

    def test_add_new_object_verify(self):
        res, st_code = self.r_api.add_new_object()
        assert len(res) == 4
        assert res['name'] == 'Apple MacBook Pro 16'
        assert st_code == 200

    def test_update_new_object_verify(self):
        res, st_code = self.r_api.update_new_object_details()
        assert len(res) == 4
        assert res['name'] == 'Apple MacBook Pro 20'
        assert st_code == 200

    def test_patch_new_object_verify(self):
        res, st_code = self.r_api.patch_new_object_details()
        assert len(res) == 4
        assert res['name'] == 'Apple MacBook Pro 25 (Updated Name)'
        assert st_code == 200

    def test_delete_new_object_verify(self):
        res, st_code = self.r_api.delete_new_object_details()
        assert len(res) == 1
        assert "has been deleted" in res['message']
        assert st_code == 200

    def test_get_all_users_details_verify(self):
        res, st_code = self.r_api.get_all_users_details_with_token()
        assert st_code == 200


