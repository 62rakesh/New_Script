import os
from time import sleep
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
class CaseStudy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver: webdriver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    def test_case_study(self):
        self.driver.get("https://www.mondaymorning.in")
        #self.driver.find_element_by_link_text("Log In").click()
        self.driver.execute_script("window.alert('proceed for Login');")
        alert=self.driver.switch_to_alert()
        alert.accept()
        sleep(1)
    def test_casestudy_Login(self):
        #self.driver.find_element_by_link_text("Log In").click()
        self.driver.get("https://www.mondaymorning.in/mm/login?a=head")
        self.driver.refresh()
        self.driver.find_element_by_xpath("//INPUT[@name='user_login']").send_keys("rakesh_patra+020@mondaymorning.in")
        self.driver.find_element_by_xpath("//INPUT[@name='user_pwd']").send_keys("1234")
        self.driver.find_element_by_xpath("//input[@id='login-model']").submit()
        self.driver.save_screenshot("Screenshoot1.png")
        sleep(2)
        self.driver.execute_script("window.alert('Login Completed');")
        alert=self.driver.switch_to_alert()
        sleep(1)
        alert.accept()
        sleep(1)
    #def test_casestudy_Assessments(self):
        #self.driver.get("https://uat.mondaymorning.in/home")   ##### Error:-Error Occurs when user reload the same page ########
        sleep(1)
        self.driver.find_element_by_xpath("//LI[@class='nav-item dropdown nav-border '][2]").click()
        self.driver.find_element_by_xpath("//A[@class='dropdown-item waves-effect waves-light'][text()='All Assessments']").click()
        self.driver.find_element_by_xpath("//LI[@class='page-item'][2]").click()
        sleep(1)
        self.driver.execute_script("window.alert('Select a case_study_Mcq_Submission assessments');")

        alert=self.driver.switch_to_alert()
        sleep(1)
        alert.accept()
        sleep(2)
        self.driver.find_element_by_xpath("//LI[@class='page-item'][2]").click()
        sleep(1)
    def test_casestudy_Strategy(self):
        self.driver.get("https://www.mondaymorning.in/assessment-detail/strategy-i")
        self.driver.find_element_by_xpath("(//I[@class='fa fa-lock'])[1]").click()
        self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-deep-purple btn-sm confirm_pack'])[text()='Unlock']").click()
        sleep(1)
        self.driver.find_element_by_xpath("(//DIV[@class='text-center mt-4 test_mar'])").click()
        sleep(1)
        # self.driver.find_element_by_xpath("//A[@class='n-c-btn3  '][1]").click()

        self.driver.find_element_by_xpath("(//A[@class='n-c-btn3  '])[2]").click()
        self.driver.find_element_by_xpath("(//A[@class='float-right'])[text()='Start Test'][1]").click()
        sleep(1)
        self.driver.refresh()
        sleep(1)
        try:
            self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-lblue btn-p-rc skip'])[1]").click()
            sleep(1)
            self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-lblue btn-p-rc skip'])[2]").click()
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-lblue btn-p-rc skip'])[3]").click()
            sleep(1)
            self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-lblue btn-p-rc skip'])[4]").click()
            sleep(1)
            self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-lblue btn-p-rc skip'])[5]").click()
            sleep(1)
            self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-blue'])[text()='confirm']").click()
            self.driver.save_screenshot("Screenshoot3.png")
            sleep(2)
            self.driver.find_element_by_xpath("(//INPUT[@id='userfile'])").click()
            UploadElement = self.driver.find_element_by_id("userfile")
            UploadElement.send_keys("C:\\Users\\lenovo\\Downloads\\MJ1_Bugs.pptx")
            sleep(1)
        except:
            self.driver.find_element_by_xpath("(//DIV[text()='2%'])[1]").click()
            sleep(2)
            self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-primary btn-p-rc'])[1]").click()
            sleep(2)
            self.driver.find_element_by_xpath("(//DIV[text()='5%'])[1]").click()
            sleep(2)
            self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-primary btn-p-rc'])[2]").click()
            sleep(1)
            self.driver.find_element_by_xpath("(//DIV[text()='38.4'])[2]").click()
            sleep(1)
            self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-primary btn-p-rc'])[3]").click()
            sleep(2)
            self.driver.find_element_by_xpath("(//DIV[text()='35.7'])[1]").click()
            sleep(1)
            self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-primary btn-p-rc'])[4]").click()
            sleep(1)
            self.driver.find_element_by_xpath("(//DIV[text()='10% increase'])[1]").click()
            sleep(1)
            self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-primary btn-p-rc'])[5]").click()
            sleep()
        ######## In Case User don't want to Select an Option ###########




    #class Assessments(unittest.TestCase):
    #@classmethod
    #def setUpClass(cls):
        #cls.driver: webdriver=webdriver.Chrome()
        #cls.driver.get("https://www.mondaymorning.in/home")
        #cls.driver.execute_script("window.alert('Proceed for Assessments');")
        #alert =cls.driver.switch_to_alert()
        #sleep(2)
        #alert.accept()

        #cls.driver.find_element_by_xpath("//LI[@class='nav-item dropdown nav-border '][2]").click()
        #cls.driver.find_element_by_xpath("//A[@class='dropdown-item waves-effect waves-light'][text()='All Assessments'][1]").click()
        #cls.driver.find_element_by_xpath("//H4[@class='card-title text-center'][text()='Finance - I']").click()
        #sleep(2)
    #@classmethod
    #def tearDownClass(cls):
        #cls.driver:webdriver=webdriver.Chrome()
        #cls.driver.close()


    @classmethod
    def tearDownClass(cls):
        cls.driver:webdriver=webdriver.Chrome()
        cls.driver.close()
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Case_Study_Mcq'))
