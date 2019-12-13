import os
from _ast import Add

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver: webdriver = webdriver.Chrome()
driver.implicitly_wait(10)
warning = ['This name already exist! ']
variable1= ["(//BUTTON[@class='btn btn-primary btn-sm'])[text()='Add']"]


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
    driver.find_element_by_xpath("(//INPUT[@id='name'])[2]").send_keys("Automation Test Role")
    sleep(1)
    driver.find_element_by_xpath("(//LABEL[@class='switch'])[text()=' Active ']").click()
    sleep(1)
    driver.find_element_by_xpath("(//BUTTON[@class='btn btn-primary btn-sm'])['Add']").click()
    sleep(3)
    if variable1 == warning:
        try:
            driver.find_element_by_xpath("(//INPUT[@id='name'])[2]").clear()
            sleep(2)
            driver.find_element_by_xpath("(//INPUT[@id='name'])[2]").send_keys("Automation Test Role+1")
        except NameError:
            print("An Exception")
        finally:
            print("Proceed with the execution")
    else:
        print("Invalid Inputs,Please check with a valid")
    sleep(2)


def test_dev_Authorization_user():
    driver.find_element_by_xpath(
        "/html/body/app-root/app-admin/div/div[1]/div[2]/app-nav-menu/nav/ul/li[3]/ul/li[2]/a").click()
    sleep(2)


def test_hover():
    element_to_hover_over = driver.find_element_by_xpath("/html/body/app-root/app-admin/div/div[2]/app-users/div["
                                                         "2]/div/div/div/div/mat-table/mat-row[2]/mat-cell["
                                                         "6]/div/button")
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    sleep(2)
    driver.find_element_by_xpath("(//BUTTON[@class='dropdown-item'])[text()='Edit'][2]").click()
    sleep(5)


def test_edit_user():
    driver.find_element_by_xpath("(//SPAN[@class='slider ng-star-inserted'])[1]").click()
    # driver.find_element_by_xpath("(//BUTTON[@class='btn btn-outline-secondary btn-sm'])[text()='Save']").click()
    sleep(1)
    driver.find_element_by_xpath("(//DIV[@class='c-btn'])").click()
    sleep(1)
    driver.find_element_by_xpath("(//INPUT[@class='ng-star-inserted'])").click()
    sleep(1)
    driver.find_element_by_xpath("(//BUTTON[@class='btn btn-outline-secondary btn-sm'])[text()='Save']").click()
    sleep(1)
    driver.execute_script("window.alert('Please Logout')")
    sleep(3)
    alert = driver.switch_to_alert()
    alert.accept()
    sleep(2)


def test_Logout():
    driver.find_element_by_xpath("(//DIV[@class='img-box'])[text()=' JS ']").click()
    sleep(1)
    driver.find_element_by_xpath("(//A[@class='dropdown-item'])[text()='Sign out']").click()
    sleep(5)


def test_teardown():
    driver.close()
