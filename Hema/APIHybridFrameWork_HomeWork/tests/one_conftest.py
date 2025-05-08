import os
import pytest
from utilities.utility_tools import Utils

def pytest_configure(config):
    util = Utils()
    unique_name = util.generate_unique_name()
    log_path=os.path.join(os.getcwd(), 'logs')

    if not os.path.exists(log_path):
        os.mkdir(log_path)

    log_file_name = f"execution_{unique_name}.log"
    log_file_path = f"{log_path}/{log_file_name}"
    config.option.log_file=log_file_path