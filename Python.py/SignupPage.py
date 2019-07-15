class Signup():
    textbox_fname_xpath="(//INPUT[@id='name'])"
    textbox_lname_xpath="(//INPUT[@name='lastname'])"
    textbox_username_xpath = "(//INPUT[@name='user_login'])"
    textbox_password_xpath = "(//INPUT[@name='user_pwd'])"
    click_button_xpath="(//INPUT[@id='signip-submit'])"

    def __init__(self,driver):
        self.driver=driver
    def set_name(self,firstname):
        self.driver.find_element_by_xpath(firstname)
    def set_lname(self,lastname):
        self.driver.find_element_by_xpath(lastname)
    def set_email(self,email):
