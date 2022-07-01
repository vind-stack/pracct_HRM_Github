import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    serv_obj = Service("C:\\Users\\VINAYAK L DIXIT\\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    Location = os.getcwd()
    preferences = {"download.default_directory":Location}
    ops.add_experimental_option("prefs", preferences)
    #ops.add_argument("headless")
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    driver.maximize_window()
    return driver

def pytest_configure(config):
    config._metadata["Project Name"] = "OrangeHRM"
    config._metadata["Module Name"] = "Myinfo"
    config._metadata["Tester"] = "Vinayaka"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)

