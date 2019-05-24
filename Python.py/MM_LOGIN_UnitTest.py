import os
from time import sleep
#import unittest

#import pytest

from selenium import webdriver

from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.webdriver import WebDriver


    #class LoginTest(unittest.TestCase):
    #@classmethod
    #def setUpClass(cls):
driver: webdriver = webdriver.Chrome()

driver.get("https://www.mondaymorning.in")

driver.save_screenshot("Screenshoot1.png")

driver.find_element_by_link_text("LOGIN").click()# Click to Login

driver.save_screenshot("Screenshoot2.png")
sleep(2)
driver.maximize_window()




#def Test_Login_Page(self):

driver.find_element_by_id("loginemail").send_keys("rakesh_patra+99@mondaymorning.in")

driver.save_screenshot("Screenshoot3.png")

driver.find_element_by_id("loginPassword").send_keys("test123#")

driver.save_screenshot("Screenshoot4.png")

driver.find_element_by_id("login-model").submit()

driver.save_screenshot("Screenshoot5.png")

sleep(2)

driver.find_element_by_id("my-profile").click()

driver.save_screenshot("Screenshoot6.png")
sleep(2)
driver.find_element_by_xpath("(//DIV)[13]").click()  # Click to Sign Out

driver.save_screenshot("Screenshoot7.png")

        #def tearDownClass(cls):
        #cls.driver.close()
        #cls.driver.quit()

print("Login and Logout is completed")

driver.save_screenshot("Screenshoot8.png ")

driver.close()


#if __name__ == '__main__':
    #unittest.main()







