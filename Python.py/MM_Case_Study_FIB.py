import os
from time import sleep
from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.chrome.webdriver import WebDriver

class casestudy_FIB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver: webdriver = webdriver.Chrome()
        cls.driver.get("https://www.mondaymorning.in")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
    def test_login(self):
        self.driver.find_element_by_xpath("(//A[@class='c-white waves-effect waves-light c-white'])[3]").click()
        sleep(2)
        self.driver.find_element_by_xpath("(//INPUT[@type='text' or @name='user_login'])[1]").send_keys("rakesh_patra+087@mondaymorning.in")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='password' or @name='user_pwd'])[1]").send_keys("1234")
        sleep(1)
        self.driver.find_element_by_id("login-model").click()
        sleep(1)
        self.driver.execute_script("window.alert('Proceed with Assessments');")
        sleep(1)
        alert=self.driver.switch_to_alert()
        sleep(1)
        alert.accept()
        sleep(1)
        while True:
            try:
                self.driver.find_element_by_xpath("(//LI[@class='nav-item dropdown nav-border '])[2]").click()
                sleep(1)
                self.driver.find_element_by_xpath("(//A[@class='dropdown-item waves-effect waves-light'])[text()='All Assessments']").click()
                sleep(1)
                self.driver.find_element_by_xpath("(//H4[@class='card-title text-center'])[4]").click()
                sleep(1)
                self.driver.find_element_by_xpath("(//A[@class='n-c-btn3  '])[1]").click()

            except:
                self.driver.find_element_by_xpath("(//I[@class='fa fa-lock'])[1]").click()
                sleep(1)
                self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-deep-purple btn-sm confirm_pack'])[text()='Unlock']").click()
                sleep(1)
                self.driver.find_element_by_xpath("(//A[@class='btn btn-cyan mt-1 waves-effect waves-light sidebar-active'])").click()
                sleep(1)
                self.driver.find_element_by_xpath("(//A[@class='n-c-btn3  '])[1]").click()
                continue
            else:
                print("Thank you for the update! \n")
                break
            finally:
                self.driver.find_element_by_xpath("(//A[@id='view_sc'])[text()='Start Test']").click()
                self.driver.find_element_by_xpath("(//A[@class='fibeditable editable editable-click editable-empty'])[text()='Click to fill'][1]").click()
                self.driver.find_element_by_xpath("(//INPUT[@class='form-control input-sm'])").send_keys("280")
                self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-primary btn-sm editable-submit'])").click()
                sleep(3)
                self.driver.find_element_by_xpath("(//A[@class='fibeditable editable editable-click editable-empty'])[text()='Click to fill'][2]").click()
                self.driver.find_element_by_xpath("(//INPUT[@class='form-control input-sm'])").send_keys("11230")
                self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-primary btn-sm editable-submit'])").click()
                sleep(3)
                self.driver.find_element_by_xpath("(//A[@class='fibeditable editable editable-click editable-empty'])[text()='Click to fill'][3]").click()
                self.driver.find_element_by_xpath("(//INPUT[@class='form-control input-sm'])").send_keys("11")
                self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-primary btn-sm editable-submit'])").click()
                sleep(3)
                self.driver.find_element_by_xpath("(//A[@class='fibeditable editable editable-click editable-empty'])[text()='Click to fill'][4]").click()
                self.driver.find_element_by_xpath("(//INPUT[@class='form-control input-sm'])").send_keys("10500000")
                self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-primary btn-sm editable-submit'])").click()
                sleep(3)
                self.driver.find_element_by_xpath("(//A[@class='fibeditable editable editable-click editable-empty'])[text()='Click to fill'][5]").click()
                self.driver.find_element_by_xpath("(//INPUT[@class='form-control input-sm'])").send_keys("395")
                self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-primary btn-sm editable-submit'])").click()
                sleep(3)
                self.driver.find_element_by_xpath("(//A[@class='fibeditable editable editable-click editable-empty'])[text()='Click to fill'][6]").click()
                self.driver.find_element_by_xpath("(//INPUT[@class='form-control input-sm'])").send_keys("7230")
                self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-primary btn-sm editable-submit'])").click()
                sleep(3)
                self.driver.find_element_by_xpath("(//A[@class='fibeditable editable editable-click editable-empty'])[text()='Click to fill'][7]").click()
                self.driver.find_element_by_xpath("(//INPUT[@class='form-control input-sm'])").send_keys("900")
                self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-primary btn-sm editable-submit'])").click()
                sleep(2)
                self.driver.find_element_by_xpath("(//A[@class='fibeditable editable editable-click editable-empty'])[text()='Click to fill'][8]").click()
                self.driver.find_element_by_xpath("(//INPUT[@class='form-control input-sm'])").send_keys("45000")
                self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-primary btn-sm editable-submit'])").click()
                sleep(2)
                self.driver.refresh()
                self.driver.find_element_by_xpath("(//DIV[@class='submit_button btn-mat btn-mat-primary btn-p-rc'])[text()='Save & Submit ']").click()
                self.driver.find_element_by_xpath("(//BUTTON[@class='btn btn-blue'])[text()='confirm']").click()
                sleep(5)


    @classmethod
    def tearDown(cls):
        cls.driver: webdriver=webdriver.Chrome()
        cls.driver.close()
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output='Casestudy_Fib'))
