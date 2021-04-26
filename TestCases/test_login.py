import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGenerator

class Test_001_Login():

    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGenerator.logGenerator()


    def test_homePageTitle(self,setup):
        self.logger.info("****Test_001_Login****")
        self.logger.info("****Verification of HomePage Title****")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        actual_title = self.driver.title

        if actual_title == "Your store. Loginasddasdasd":
            assert True
            self.logger.info("****Home page title test is PASSED SUCCESSFULLY****")
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****Home page title test is FAILED****")
            assert False


    def test_login(self, setup):
        self.logger.info("****VERIFICATION OF LOG IN****")
        self.driver = setup
        self.driver.maximize_window()

        self.driver.get(self.baseURL)
        self.loginPageObject = LoginPage(self.driver)
        self.loginPageObject.setUserName(self.username)
        self.loginPageObject.setPassword(self.password)
        self.loginPageObject.clickLogin()

        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.quit()
            self.logger.info("****Login test is PASSED SUCCESSFULLY****")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.quit()
            self.logger.error("****Login test is FAILED****")
            assert False

