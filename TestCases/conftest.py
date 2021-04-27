from selenium import webdriver
import pytest
import pytest_html


#Environment(browser) setup

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C://Users//Administrator//Desktop//QA//Drivers//chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C://Users//Administrator//Desktop//QA//Drivers//geckodriver.exe")
    else:
        driver = webdriver.Firefox(executable_path="C://Users//Administrator//Desktop//QA//Drivers//geckodriver.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


################## HTML Report ####################

#Adding environment info to html reprot
def pytest_configure(config):
    config._metadata['Project Name'] = 'My personal project'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Author Name'] = 'Robert P.'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)