import os
from time import sleep
import unittest
from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.chrome.webdriver import WebDriver
#driver: webdriver=webdriver.Chrome()

class Assessments(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver: webdriver=webdriver.Chrome()
        cls.driver.maximize_window()
        sleep(2)
    def test_Login(self):
        self.driver.get("https://www.mondaymorning.in")
        self.driver.find_element_by_link_text("Log In").click()
        self.driver.find_element_by_xpath("//INPUT[@name='user_login']").send_keys("rakesh_patra+817@mondaymorning.in")
        self.driver.find_element_by_xpath("//INPUT[@name='user_pwd']").send_keys("1234")
        self.driver.find_element_by_xpath("//input[@id='login-model']").submit()
        sleep(2)
    #def test_Assessment(self):
        self.driver.find_element_by_xpath("//LI[@class='nav-item dropdown nav-border '][2]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//A[@class='dropdown-item waves-effect waves-light'][text()='All Assessments'][1]").click()
        sleep(1)
        #self.driver.find_element_by_xpath("//INPUT[@class='select-dropdown']").click()
        #self.driver.implicitly_wait(5)
        #self.driver.find_element_by_xpath("//INPUT[@class='search form-control w-100 d-block']").send_keys("Operations")
        #return(Assessments)
        self.driver.find_element_by_xpath("//h4[@class='card-title text-center'][text()='Operations - I']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//I[@class='fa fa-lock']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//BUTTON[@class='btn btn-deep-purple btn-sm confirm_pack'][text()='Unlock']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//DIV[@class='text-center mt-4 test_mar']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//A[@class='n-c-btn3  '][1]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//A[@class='float-right'][text()='Start Test'][1]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//BUTTON[@class='btn btn-primary'][text()='Full Screen']").click()
        self.driver.save_screenshot("Screenshoot1.png")
        sleep(2)
        self.driver.refresh()
        self.driver.find_element_by_xpath("//BUTTON[@class='btn btn-primary'][text()='Full Screen']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//INPUT[@class='quest'][1]").send_keys("A")
        sleep(2)
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[2]").send_keys("B")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[3]").send_keys("C")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[4]").send_keys("D")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[5]").send_keys("E")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[6]").send_keys("A")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[7]").send_keys("C")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[8]").send_keys("A")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[9]").send_keys("S")
        sleep(2)
        self.driver.find_element_by_xpath("//DIV[@class='submit_button btn-mat btn-mat-primary btn-p-rc'][text()='Save & Continue ']").submit()
        self.driver.save_screenshot("Screenshoot2.png")
        sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Grid_FIB'))




