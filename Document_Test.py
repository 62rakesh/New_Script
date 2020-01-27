import unittest
from time import sleep
from selenium import webdriver
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
import sys

sys.path.append("C://Users//Admin//PycharmProjects//HRM_Project")
from PageObject.LoginPage import LoginPage
# from PageObject.AdminPage import AdminPage


class LoginTest(unittest.TestCase):
    baseURL = "https://fourvision-webappsdocumentmanagementp5faq3pfwznlo.azurewebsites.net/employee/dashboard"
    username = "jason@development.fourvision.com"
    password = "FourVision@D3v"
    driver: webdriver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        sleep(2)
        lp.setUserName(self.username)
        sleep(2)
        lp.clickButton()
        sleep(2)
        lp.setPassword(self.password)
        sleep(2)
        lp.clickSignup()
        sleep(2)
        lp.clickConfirm()
        sleep(10)
        lp.dropdownButton()
        sleep(2)
        lp.AdminButton()
        sleep(5)
        self.assertEqual("Document", self.driver.title, "Page Not Found")

    def test_element_does_not_exist(self):
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_xpath("(//H4[text()='Getting started'])")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))
