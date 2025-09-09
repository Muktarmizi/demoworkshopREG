import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    driver.maximize_window()
    return driver

























# import pytest
# import configparser
# import os
# from selenium import webdriver
#
# # Load config.ini
# config = configparser.ConfigParser()
# config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
#
# @pytest.fixture(scope="session")
# def base_url():
#     """Provide base URL from config.ini"""
#     return config["common info"]["baseURL"]
#
# @pytest.fixture(scope="session")
# def driver():
#     """Provide WebDriver instance"""
#     browser = config["common info"]["browser"]
#     if browser.lower() == "chrome":
#         driver = webdriver.Chrome()
#     elif browser.lower() == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise Exception(f"Unsupported browser: {browser}")
#     driver.maximize_window()
#     yield driver
#     driver.quit()
