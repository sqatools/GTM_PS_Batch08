from selenium.webdriver.common.by import By
#from modules.sqaautomationtoolspage.sqaautomationtools_page_class import SqaAutomationToolsPage
#from modules.sqaautomationtoolspage.sqaautomationtools_test_data import *
#from utilities.utility_tools import Utils
from Hema.HybridFrameWork_04_05_2025.utilities.utility_tools import Utils
import time
import pytest

from Hema.HybridFrameWork_04_05_2025.modules.sqaautomationtoolspage.sqaautomationtools_page_class import SqaAutomationToolsPage
from Hema.HybridFrameWork_04_05_2025.modules.sqaautomationtoolspage.sqaautomationtools_test_data import *


@pytest.mark.usefixtures("get_driver_sqaautomation")
class TestSqaAutomationTools:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.sqa = SqaAutomationToolsPage(self.driver)
        self.util = Utils()
        self.json_data = self.util.read_json(json_filepath)

    def test_title(self,request):
        #self.sqa.log.info(f'Test name: {request.mode.name}')
        self.sqa.sqatoolsdummywebsite()
        self.sqa.choose_option()
        self.sqa.passenger_details(first_name=self.json_data['first_name'],last_name=self.json_data['last_name'],dob=self.json_data['dob'])

#command to execute:
#(.venv) PS D:\Hema\PythonAutomation\GTM_PS_Batch08\Hema\HybridFrameWork_04_05_2025> python -m pytest -v .\tests\sqaautomation_page\test_sqaautomationtools_page.py
