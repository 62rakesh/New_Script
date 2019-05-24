import os
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.webdriver import WebDriver
class MMCAF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver: webdriver = webdriver.Chrome()
        cls.driver.maximize_window()
        sleep(1)
    def test_login(self):
        self.driver.get("https://www.mondaymorning.in")
        self.driver.refresh()
        self.driver.find_element_by_link_text("Log In").click()
        self.driver.find_element_by_xpath("//INPUT[@name='user_login']").send_keys("rakesh_patra+585@mondaymorning.in")
        self.driver.find_element_by_xpath("//INPUT[@name='user_pwd']").send_keys("1234")
        self.driver.find_element_by_xpath("//INPUT[@id='login-model']").submit()
        self.driver.find_element_by_xpath("//img[@class='set-admin-login-pic']").click()
        self.driver.find_element_by_xpath("//A[@href='https://www.mondaymorning.in/user-full-profile']").click()
        self.driver.find_element_by_xpath("//IMG[@class='edit-icon']").click()
        sleep(2)
        obj = Select(self.driver.find_element_by_name("gender"))
        #sleep(2)
        obj.select_by_value("Male")
        sleep(1)
        #self.driver.find_element_by_xpath("//INPUT[@id='dob_date']").click()
        #sleep(1)
        #self.driver.find_element_by_xpath("//DIV[@role='period'][text()='June 1989']").click()
        #sleep(2)
        #self.driver.find_element_by_xpath("//DIV[text()='14']")
        #sleep(2)
        self.driver.find_element_by_xpath("//SPAN[@id='select2-city-container']").click()
        sleep(2)
        self.driver.find_element_by_xpath("(//INPUT[@class='select2-search__field'])[2]").send_keys("Bangalore")
        sleep(2)
        self.driver.execute_script("window.alert('Save the Profile details');")
        self.alert=self.driver.switch_to_alert()
        sleep(1)
        self.alert.accept()
        sleep(1)
        self.driver.find_element_by_xpath("//BUTTON[@type='submit'][text()='Save ']").click()
        sleep(1)
        self.driver.find_element_by_xpath("(//BUTTON[@type='button'])[2]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//IMG[@class='c-profile-pic clickchange ']")
        sleep(1)
        uploadElement = self.driver.find_element_by_id("upload_image")
        uploadElement.send_keys("C:\\Users\\lenovo\\Desktop\\images.jpg")
        sleep(2)
        #self.driver.find_element_by_xpath("//INPUT[@class='cr-slider active']")
        #leep(2)
        self.driver.find_element_by_xpath("//A[@id='crop_image']").click()
        sleep(5)
        print("Profile is updated")

        print("Changes Updated")





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("User Candidate Application Form is in Progress,\n\t please stay tuned with us")


if __name__== '__main__':
    unittest.main()




