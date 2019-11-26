import os
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver: webdriver = webdriver.Chrome()
driver.implicitly_wait(10)


def test_Setup():
    driver.maximize_window()


def test_dev_succession_login():
    driver.get("https://fourvision-webappssuccessionp5faq3pfwznlo.azurewebsites.net/employee/dashboard")
    driver.find_element_by_xpath("(//INPUT[@id='i0116'])").send_keys("Jason@development.fourvision.com")
    driver.find_element_by_xpath("(//INPUT[@id='idSIButton9'])['Next']").click()
    sleep(2)
    driver.find_element_by_xpath("(//INPUT[@id='i0118'])").send_keys("FourVision@D3v")
    sleep(2)
    driver.find_element_by_xpath("(//INPUT[@id='idSIButton9'])").submit()
    sleep(1)
    driver.find_element_by_xpath("(//INPUT[@id='idSIButton9'])['Yes']").click()
    sleep(2)


def test_dev_admin():
    driver.find_element_by_xpath("(//BUTTON[@class='btn dropdown-toggle-split dropdown-toggle'])").click()
    sleep(1)
    driver.find_element_by_xpath("(//A[@class='dropdown-item'])[text()='Succession admin']").click()
    sleep(5)


def test_dev_admin_Authorizations():
    driver.find_element_by_xpath("(//I[@class='icon-navbar'])[1]").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div[1]/div[2]/app-nav-menu/nav/ul/li[3]/a").click()
    sleep(1)
    driver.find_element_by_xpath(
        "/html/body/app-root/app-admin/div/div[1]/div[2]/app-nav-menu/nav/ul/li[3]/ul/li[1]").click()
    sleep(3)
    driver.find_element_by_xpath(
        "/html/body/app-root/app-admin/div/div[2]/app-role/div[1]/ul/li[2]/app-add-role/div").click()
    sleep(1)
    driver.find_element_by_xpath("(//INPUT[@id='name'])[2]").send_keys("Automation")
    sleep(1)
    driver.find_element_by_xpath("(//BUTTON[@class='btn btn-primary btn-sm'])['Add']").click()


def test_teardown():
    driver.close()
