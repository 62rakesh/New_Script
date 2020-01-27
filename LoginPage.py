class LoginPage:
    textbox_username_email = "(//INPUT[@id='i0116'])"
    button_next_xpath = "(//INPUT[@id='idSIButton9'])['Next']"
    textbox_password_xpath = "(//INPUT[@id='i0118'])"
    button_signup_xpath = "(//INPUT[@id='idSIButton9'])"
    button_confirm_xpath = "(//INPUT[@id='idSIButton9'])['Yes']"
    drop_down_xpath = "(//BUTTON[@class='btn dropdown-toggle-split dropdown-toggle'])"
    admin_UI_xpath = "(//A[@class='dropdown-item'])[3]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_email).send_keys(username)

    def clickButton(self):
        self.driver.find_element_by_xpath(self.button_next_xpath).click()

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickSignup(self):
        self.driver.find_element_by_xpath(self.button_signup_xpath).click()

    def clickConfirm(self):
        self.driver.find_element_by_xpath(self.button_confirm_xpath).click()

    def dropdownButton(self):
        self.driver.find_element_by_xpath(self.drop_down_xpath).click()

    def AdminButton(self):
        self.driver.find_element_by_xpath(self.admin_UI_xpath).click()






