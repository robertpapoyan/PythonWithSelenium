from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Firefox(executable_path="C://Users//Administrator//Desktop//QA//Drivers//geckodriver.exe")
    return driver