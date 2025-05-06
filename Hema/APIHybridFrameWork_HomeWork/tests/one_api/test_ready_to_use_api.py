import pytest
from modules.api.ready_to_use_api.ready_to_use_api_page_class import ReadyToUseApi

class TestReadyToUseAPI:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.r_api = ReadyToUseApi()

    def test_get_all_object_and_verify(self):
        response, st_code = self.r_api.get_all_lists_of_users()
        assert len(response) == 13
        assert st_code == 200

    def test_post_user_and_verify(self):
        response, st_code = self.r_api.create_new_user()
        assert st_code == 200
