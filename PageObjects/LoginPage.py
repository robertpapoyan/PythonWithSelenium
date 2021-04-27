class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_css_selector=".button-1"
    button_logut_css_selector=".ml-auto > li:nth-child(3) > a:nth-child(1)"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,userName):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(userName)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_css_selector(self.button_login_css_selector).click()

    def clickLogOut(self):
        self.driver.find_element_by_css_selector(self.button_logut_css_selector).click()