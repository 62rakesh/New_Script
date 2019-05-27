import os
from time import sleep
import unittest
import HtmlTestRunner
import span

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

class Onboarduser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver: webdriver = webdriver.Chrome()
        cls.driver.maximize_window()
        sleep(1)
    def test_signup(self):
        self.driver.get("https://www.mondaymorning.in")
        self.driver.find_element_by_xpath("//a[@class='btn-job']").click()
        print("User proceed for Registration Process")
        self.driver.find_element_by_xpath("//input[@name='fullname']").send_keys("Rakesh")
        self.driver.find_element_by_xpath("//input[@name='lastname']").send_keys("Patra")
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys("rakesh_patra+765@mondaymorning.in")
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("1234")
        self.driver.find_element_by_xpath("//input[@id='signip-submit']").click()
        sleep(2)


    #def test_onboard(self):
        self.driver.find_element_by_xpath("//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set yesBtn'][text()='Next']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//LABEL[@for='radior_1_5'][text()='have a die hard attitude']").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "//button[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//label[@for='radior_2_1'][text()='working']").click()
        sleep(1)
        self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[2]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//label[@for='radior_3_2'][text()='Frontline Manager']").click()
        sleep(1)
        self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[3]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='select2-list_4-container']/span").click()
        sleep(3)
        #obj = span (self.driver.find_element_by_class_name('select2-selection__rendered'))

        self.driver.find_element_by_xpath("//INPUT[@class='select2-search__field']").send_keys("Energy")
        sleep(2)
        self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[4]").click()

        #self.driver.find_element_by_xpath("//*[@id='step-4']/div/div/div[2]/button").click()
        #sleep(2)
        self.driver.execute_script("window.alert('Proceed');")
        alert=self.driver.switch_to_alert()
        sleep(1)
        alert.accept()

        self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[4]").click()
        sleep(1)
        self.driver.refresh()
        sleep(1)
        ########## Needs to handle IFRAME problem ##########
        self.driver.find_element_by_xpath("//A[@class='skipBtn btn btn-default   my-default-btn-set-2']").click()
        sleep(1)
        #self.driver.find_element_by_xpath("//*[@id='select2-list_5-container']/span").send_keys("Engineering")
        #self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[5]").click()
        #self.driver.find_element_by_xpath("//label[@for='radior_6_2'][text()='joining a competitive team/company']").click()
        #self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[6]").click()
        #self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'])[7]").click()
        print("User Onboarded.")
        self.driver.save_screenshot("Screenshoot2.png")
        sleep(2)
############### Explore ASSESSMENTS ###############
    #def test_Assessments(self):
        #self.driver.execute_script("window.alert('Explore Assessments');")
        #alert =self.driver.switch_to_alert()
        #sleep(1)
        #alert.accept()
        #self.driver.get("https://www.mondaymorning.in/assessment-zone")
        #self.driver.find_element_by_xpath("//h4[@class='card-title text-center'][text()='Apparel & Fashion']").click()
        #self.driver.find_element_by_xpath("//i[@style='color:#fff'][@class='fa fa-lock']").click()
        #sleep(1)
        #self.driver.find_element_by_xpath("//A[@href='https://www.mondaymorning.in/subscribe/MQ/ODM'][text()='Subscribe Now']").click()
        #sleep(2)
        #self.driver.find_element_by_xpath("//A[@type='button'][text()='Close']").click()
        #sleep(2)
        #self.driver.save_screenshot("Screenshoot1.png")
        #self.driver.refresh()
######## Applying for JOBS ############
        #self.driver.find_element_by_xpath("//A[@class='dropdown-item waves-effect waves-light'][text()='Browse']")
        #self.driver.find_element_by_xpath("//A[@id='navbarDropdownMenuLink-555']").click()
        #self.driver.save_screenshot("Screenshoot2.png")
        #sleep(2)
        #self.driver.find_element_by_link_text()("Browse").click()
        #sleep(2)
        #self.driver.find_element_by_xpath("//A[@href='https://www.mondaymorning.in/job-apply-status/MTg3']").click()
        #self.driver.save_screenshot("Screenshoot3.png")
        #sleep(2)
######### FILL JAF ############
        #self.driver.find_element_by_xpath("//INPUT[@name='mobile']").send_keys("9910768013")
        #self.select=self.Select(self.driver.find_element_by_name("gender"))
        #self.driver.find_element_by_
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report1'))

