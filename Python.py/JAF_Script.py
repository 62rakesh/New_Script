import os
import unittest
from time import sleep
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.webdriver import WebDriver

class JAF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver: webdriver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_jaf(self):
        self.driver.get("https://www.mondaymorning.in")
        self.driver.find_element_by_link_text("Log In").click()

        self.driver.find_element_by_xpath("//INPUT[@name='user_login']").send_keys("rakesh_patra+645@mondaymorning.in")
        self.driver.find_element_by_xpath("//INPUT[@name='user_pwd']").send_keys("1234")
        self.driver.find_element_by_xpath("//input[@id='login-model']").submit()
        sleep(2)
########### User Onboarded ##############
     #self.driver.find_element_by_xpath("//button[@class='btn btn-default mw-btn-300  my-default-btn-set yesBtn'][text()='Next']").click()
     #sleep(1)
     #self.driver.find_element_by_xpath("//LABEL[@for='radior_1_5'][text()='have a die hard attitude']").click()
     #sleep(1)
     #self.driver.find_element_by_xpath("//button[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next']").click()
     #sleep(1)
     #self.driver.find_element_by_xpath("//label[@for='radior_2_1'][text()='working']").click()
     #self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[2]").click()
     #self.driver.find_element_by_xpath("//label[@for='radior_3_2'][text()='Frontline Manager']").click()
     #self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[3]").click()
     #self.driver.find_element_by_xpath("//INPUT[@id='list4']").send_keys("Energy")
     #self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[4]").click()
     #self.driver.find_element_by_xpath("//INPUT[@id='list5']").send_keys("Engineering")
     #self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[5]").click()
     #self.driver.find_element_by_xpath("//label[@for='radior_6_2'][text()='joining a competitive team/company']").click()
     #self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[6]").click()
     #self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'])[7]").click()
     #sleep(2)
     #print("User Onboarded.")
    #ef test_jaf(self)
        self.driver.execute_script("window.alert('Apply for the job');")  #####Proceeding for JAF Process
        self.alert =self.driver.switch_to_alert()
        sleep(2)
        self.alert.accept()
        self.driver.find_element_by_xpath("//A[@id='navbarDropdownMenuLink-555'][text()='Jobs']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//A[@class='dropdown-item waves-effect waves-light']").click()
        sleep(2)
        self.driver.save_screenshot("Screenshoot1.png")
        self.driver.find_element_by_xpath("//A[@class='btn btn-fb btn-rounded float-right  btn-sm waves-effect waves-light'][text()='Apply'][1]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//A[@class='float-right'][text()=' Apply']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//INPUT[@name='mobile']").send_keys("9910768013")
        sleep(1)
        self.driver.find_element_by_xpath("//select[@class='form-control browser-default custom-select']").click()
        sleep(1)
        obj = Select(self.driver.find_element_by_name("gender"))
        obj.select_by_visible_text("Male")
        sleep(1)
        self.driver.find_element_by_xpath("//SPAN[@id='select2-city-container']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//INPUT[@class='select2-search__field']").send_keys("Noida")
        sleep(2)
        uploadElement = self.driver.find_element_by_id("resume")
        uploadElement.send_keys("C:\\Users\\lenovo\\Downloads\\3rd_Year_Mark_Sheet42.pdf")
        # driver.find_element_by_xpath("//div[@class='float-right span-browse'][text()='Browse']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//button[@id='nextBtn']").click()
        sleep(1)
        obj = Select(self.driver.find_element_by_name("pg_university"))
        sleep(1)
        obj.select_by_visible_text("Ahmedabad University")
        sleep(1)
        obj = Select(self.driver.find_element_by_name("pg_degree"))
        sleep(1)
        obj.select_by_visible_text("ME/ M.Tech./ MS (Engg/ Sciences)")
        sleep(1)
        self.driver.find_element_by_xpath("//INPUT[@id='pg_perc']").send_keys("70")
        sleep(1)
        obj = Select(self.driver.find_element_by_name("pg_passing"))
        obj.select_by_visible_text("2018")
        sleep(1)
        self.driver.find_element_by_xpath("//button[@id='nextBtn'][text()='Save & Continue']").click()
        sleep(3)
        self.driver.execute_script("window.alert('JAF COMPLETED');")
        alert =self.driver.switch_to_alert()
        sleep(1)
        self.alert.accept()
        sleep(1)
        self.driver.save_screenshot("Screenshoot1.png")
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='JAF'))









