import os
import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
path = 'C:\\Users\\lenovo\\PycharmProjects\\Page_Object_Model'
import sys
sys.path.append(path)
from PageObject.LoginPage import Login
class UserLogin(unittest.TestCase):
    driver = "C:\\Users\\lenovo\\PycharmProjects\\Page_Object_Model\\Drivers"
    username = 'rakesh_patra@mondaymorning.in'
    password = 'test123#'
    @classmethod
    def setUpClass(cls):
        cls.driver:webdriver=webdriver.Chrome()
        cls.driver.get("https://www.mondaymorning.in")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_login(self):
        self.driver.find_element_by_link_text("Log In").click()
        time.sleep(1)
        self.Lp = Login(self.driver)
        time.sleep(1)
        self.Lp.set_username(self.username)
        time.sleep(1)
        self.Lp.set_password(self.password)
        time.sleep(1)
        self.Lp.click_button()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports"))





