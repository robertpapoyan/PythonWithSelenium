import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGenerator
from Utilities import XLUtilities
import time

class Test_002_DDT_Login():   #DDT stands for Data Driven Testing

    baseURL = ReadConfig.getURL()
    pathToExcell = ".\\testData\\LoginData.xlsx"
    logger = LogGenerator.logGenerator()
    list_status = []

    def test_login_ddt(self, setup):
        self.logger.info("****Test_002_Login_DDT****")
        self.logger.info("****VERIFICATION OF LOG IN DDT****")

        # Browser setup
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.loginPageObject = LoginPage(self.driver)

        # Getting excel file and the raws
        self.rows = XLUtilities.getRowCount(self.pathToExcell, 'Sheet1')


        #This logic stands for reading the info from excell raws and lines
        for r in range(2, self.rows+1):
            self.user = XLUtilities.readData(self.pathToExcell, 'Sheet1', r, 1)
            self.password = XLUtilities.readData(self.pathToExcell, 'Sheet1', r, 2)
            self.expectedResult = XLUtilities.readData(self.pathToExcell, 'Sheet1', r, 3)

            # Setting up login parameters for login
            self.loginPageObject.setUserName(self.user)
            self.loginPageObject.setPassword(self.password)
            self.loginPageObject.clickLogin()



            time.sleep(5)

            actual_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if actual_title == exp_title:
                if self.expectedResult == "Pass":
                   self.logger.info("****Login test is PASSED SUCCESSFULLY****")
                   self.loginPageObject.clickLogOut()
                   self.list_status.append("Pass")
                   time.sleep(3)
                elif self.expectedResult == "Fail":
                    self.logger.error("*** Failed ***")
                    self.loginPageObject.clickLogOut()
                    self.list_status.append("Fail")
                    time.sleep(3)

            elif actual_title != exp_title:
                if self.expectedResult == 'Pass':
                   self.logger.info("**** failed ****")
                   self.list_status.append("Fail")
                   time.sleep(3)
                elif self.expectedResult == 'Fail':
                    self.logger.info("**** passed ****")
                    self.list_status.append("Pass")
                    time.sleep(3)

        if "Fail" not in self.list_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False


        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");