import pytest
from modules.api.ready_to_use_api.ready_use_api_class import ReadyToUseAPI

class TestReadyToUseAPI:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.r_api = ReadyToUseAPI()

    def test_get_all_object_and_verify(self):
        response, st_code = self.r_api.get_all_list_of_users()
        assert  len(response) == 13
        assert  st_code == 200



