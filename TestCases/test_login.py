import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        actual_title = self.driver.title


        if actual_title == "Your store. Login":
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginPageObject = LoginPage(self.driver)
        self.loginPageObject.setUserName(self.username)
        self.loginPageObject.setPassword(self.password)
        self.loginPageObject.clickLogin()

        actual_title = self.driver.title


        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.quit()
            assert False

