from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGenerator
from PageObjects.AddCusstomerPage import AddCustomer
import pytest
from selenium import webdriver
import time
import string
import random

class Test_003_AddNewCustomer():

    baseURL = ReadConfig.getURL()
    userName = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logGen = LogGenerator.logGenerator()


    def test_addNewCustomer(self,setup):
        self.logGen.info("****TEST 003 IS LAUNCHED SUCCESSFULLY ****")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.userName)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        self.logGen.info("**** LOGGED IN SUCCESSFULLY ****")

        self.logGen.info("**** STARTING ADD NEW CUSTOMER TEST ****")

        self.addNewCustomer = AddCustomer(self.driver)
        time.sleep(3)
        self.addNewCustomer.clickCustomerMenuItem()
        time.sleep(3)
        self.addNewCustomer.clickCustomerMenuSubItem()

        time.sleep(3)

        self.addNewCustomer.clickAddNewCustomer()
        time.sleep(3)

        self.logGen.info("**** ENTERED PAGE ADD NEW CUSTOMER SUCCESSFULLY ****")
        self.logGen.info("**** ENTERING DATA FOR REGISTRATION ****")

        self.email = random_generator()+"@gmail.com"
        self.newCustomerPassword = "asdasd123"
        self.firstName = "Robert"
        self.lastName = "Papoyan"
        self.gender = "female"
        self.DOB = "7/27/1996"
        self.compName = "Atom"
        self.role = "Vendors"
        self.content = "Testing"

        self.addNewCustomer.setNewCustomerEmail(self.email)
        self.addNewCustomer.setNewCustomerPassword(self.newCustomerPassword)
        self.addNewCustomer.setNewCustomerFirstName(self.firstName)
        self.addNewCustomer.setNewCustomerLastName(self.lastName)
        self.addNewCustomer.setNewCustomerGender(self.gender)
        self.addNewCustomer.setNewCustomerDOB(self.DOB)
        self.addNewCustomer.setNewCustomerCompanyName(self.compName)
        self.addNewCustomer.setCustomerRoles(self.role)
        self.addNewCustomer.setNewCustomerContent(self.content)

        self.addNewCustomer.clickSaveButton()



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str