from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class AddCustomer:

    customerMenuItem_css_selector = "li.has-treeview:nth-child(4) > a:nth-child(1) > p:nth-child(2)"
    customerMenuSubItem_css_xpath = "li.has-treeview:nth-child(4) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > p:nth-child(2)"

    addNewCustomer_button_css_selector = "a.btn-primary"

    addNewCustomerEmail_textfield_id = "Email"
    addNewCustomerPassword_textfield_id = "Password"
    addNewCustomerFirstName_textfield_id = "FirstName"
    addNewCustomerLastName_textfield_id = "LastName"

    addNewCustomerGender_Male_radioButton_id = "Gender_Male"
    addNewCustomerGender_Female_radioButton_id = "Gender_Female"

    addNewCustomerDateOfBirth_textfield_css_selector = "#DateOfBirth"
    addNewCustomerCompanyName_textfield_id = "Company"
    addNewCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    addNewCustomerRolesLstItemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    addNewCustomerRolesLstItemRegistered_xpath = "//li[contains(text(),'Registered')]"
    addNewCustomerRolesLstItemGuests_xpath = "//li[contains(text(),'Guests')]"
    addNewCustomerRolesLstItemVendors_xpath = "//li[contains(text(),'Vendors')]"
    addNewCustomerRolesLstItemOfVendor_xpath = "//*[@id='VendorId']"
    addNewCustomerContent_id = "AdminComment"

    saveNewCustomer_css_selector = "button.btn-primary:nth-child(1)"

    def __init__(self, driver):
        self.driver = driver

    # Reching the "Add customer page"
    def clickCustomerMenuItem(self):
        self.driver.find_element(By.CSS_SELECTOR, self.customerMenuItem_css_selector).click()

    def clickCustomerMenuSubItem(self):
        self.driver.find_element(By.CSS_SELECTOR, self.customerMenuSubItem_css_xpath).click()

    def clickAddNewCustomer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.addNewCustomer_button_css_selector).click()

    # Filling the form to add new customer
    def setNewCustomerEmail(self, email):
        self.driver.find_element(By.ID, self.addNewCustomerEmail_textfield_id).send_keys(email)

    def setNewCustomerPassword(self, password):
        self.driver.find_element(By.ID, self.addNewCustomerPassword_textfield_id).send_keys(password)

    def setNewCustomerFirstName(self, firstName):
        self.driver.find_element(By.ID, self.addNewCustomerFirstName_textfield_id).send_keys(firstName)

    def setNewCustomerLastName(self, lastName):
        self.driver.find_element(By.ID, self.addNewCustomerLastName_textfield_id).send_keys(lastName)

    def setNewCustomerGender(self, gender):
        gender.lower()
        if gender == "male":
            self.driver.find_element(By.ID,self.addNewCustomerGender_Male_radioButton_id).click()
        elif gender == "female":
            self.driver.find_element(By.ID, self.addNewCustomerGender_Female_radioButton_id).click()
        else:
            self.driver.find_element(By.ID,self.addNewCustomerGender_Male_radioButton_id).click()

    def setNewCustomerDOB(self, dob):
        self.driver.find_element(By.CSS_SELECTOR, self.addNewCustomerDateOfBirth_textfield_css_selector).send_keys(dob)

    def setNewCustomerCompanyName(self, companyName):
        self.driver.find_element(By.ID, self.addNewCustomerCompanyName_textfield_id).send_keys(companyName)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.addNewCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.addNewCustomerRolesLstItemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.addNewCustomerRolesLstItemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.addNewCustomerRolesLstItemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.addNewCustomerRolesLstItemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.addNewCustomerRolesLstItemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.addNewCustomerRolesLstItemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        dropDownMenu = Select(self.driver.find_element(By.ID, self.drpmgrOfVendor_xpath))
        dropDownMenu.select_by_visible_text(value)

    def setNewCustomerContent(self,content):
        self.driver.find_element(By.ID, self.addNewCustomerContent_id).send_keys(content)

    def clickSaveButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.saveNewCustomer_css_selector).click()