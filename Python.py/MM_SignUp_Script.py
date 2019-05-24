import os

from time import sleep



from selenium import webdriver



from selenium.webdriver.chrome.webdriver import WebDriver

#import unittest

driver: webdriver = webdriver.Chrome()

#class SignUp(unittest.TestCase):
    #@classmethod
    #def setUpClass(cls):
#driver: webdriver = webdriver.Chrome()
driver.maximize_window()
sleep(2)
# @classmethod
# def MM_SignUp(self):
driver.get("https://www.mondaymorning.in")
driver.find_element_by_xpath("/html/body/app-root/app-landing-page/app-sidebar/header/div[1]/a").click()
sleep(1)
driver.find_element_by_id("name").send_keys("Rakesh")
sleep(1)
driver.find_element_by_id("lastname").send_keys("Patra")
sleep(1)
driver.find_element_by_name("user_email").send_keys("rakesh_patra+190@mondaymorning.in")
sleep(1)
driver.find_element_by_id("password").send_keys("test123#")
sleep(1)
driver.save_screenshot("Screenshoot1.png")
driver.find_element_by_id("signip-submit").click()
driver.save_screenshot("Screenshoot2.png")

    #def MM_Onboard(self):
driver.find_element_by_xpath("//*[@id='step-0']/div/div/div/button").click()
sleep(1)
driver.save_screenshot("Screenshoot3.png")
driver.find_element_by_xpath("//LABEL[@for='radior_1_5'][text()='have a die hard attitude']").click()
sleep(1)
driver.save_screenshot("Screenshoot4.png")
driver.find_element_by_xpath(
    "(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[1]").click()
sleep(1)
driver.find_element_by_xpath("//LABEL[@for='radior_2_1'][text()='working']").click()
sleep(1)
driver.save_screenshot("Screenshoot5.png")
driver.find_element_by_xpath(
    "(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[2]").click()
sleep(1)
driver.find_element_by_xpath("//LABEL[@for='radior_3_1'][text()='Individual Contributor']").click()
sleep(1)
driver.save_screenshot("Screenshoot6.png")
driver.find_element_by_xpath(
    "(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[3]").click()
sleep(1)
driver.find_element_by_id("list4").send_keys("Machine Learning")
driver.save_screenshot("Screenshoot7.png")
driver.find_element_by_xpath(
    "(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[4]").click()
sleep(1)
driver.find_element_by_id("list5").send_keys("Functional Testing")
driver.find_element_by_xpath(
    "(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[5]").click()
sleep(1)
driver.save_screenshot("Screenshoot8.png")
driver.find_element_by_xpath("//LABEL[@for='radior_6_2'][text()='joining a competitive team/company']").click()
sleep(1)
driver.find_element_by_xpath(
    "(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'][text()='Next'][text()='Next'])[6]").click()
sleep(1)
driver.save_screenshot("Screenshoot9.png")
driver.find_element_by_xpath(
    "(//BUTTON[@class='btn btn-default mw-btn-300  my-default-btn-set nextBtn'])[7]").click()
sleep(1)
driver.save_screenshot("Screenshoot10.png")


driver.execute_script("window.alert('User On-boarded');")
alert = driver.switch_to_alert()
sleep(2)
alert.accept()

sleep(2)

driver.get("https://www.mondaymorning.in/contest-zone")

#driver.find_element_by_xpath("//*[@id='step-0']/div[3]/button']").click()
#driver.find_element_by_xpath("//*[@id='step-0']").click()
#sleep(2)
#driver.save_screenshot("Screenshoot11.png")
#driver.find_element_by_xpath("//BUTTON[@class='btn btn-default'][text()='Got it!']").click()
#sleep(1)
#driver.save_screenshot("Screenshoot12.png")
#driver.find_element_by_xpath("//BUTTON[@class='btn btn-default'][text()='Got it!']").click()
#sleep(1)
#driver.save_screenshot("Screenshoot13.png")

#driver.find_element_by_xpath("//BUTTON[@class='btn btn-default'][text()='Got it!']").click()
#sleep(1)
#driver.save_screenshot("Screenshoot14.com")
    #@classmethod
    #def tearDownClass(cls):
#driver.close()
#driver.quit()
print("SignUp is completed")

sleep(2)

# AUTOMATING CONTEST FROM HERE

driver.find_element_by_xpath("(//DIV[@class='btn btn-fb btn-rounded btn-sm waves-effect waves-light'][text()='Participate Now'][text()='Participate Now'])[1]").click()
sleep(1)
driver.find_element_by_link_text("Unlock Contest").click()
sleep(1)
driver.find_element_by_link_text("Unlock").click()
sleep(1)
driver.find_element_by_class_name("m-t-sm").click()











