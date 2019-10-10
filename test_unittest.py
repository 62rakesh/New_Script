import random
from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver: webdriver = webdriver.Chrome()
Assessments = ["(//A[@id='myInput'])[text()='Technology']",
               "(//A[@id='myInput'])[text()='Free']",
               "(//A[@id='myInput'])[text()='Strategy']",
               "(//A[@id='myInput'])[text()='Operations']",
               "(//A[@id='myInput'])[text()='Marketing']",
               "(//A[@id='myInput'])[text()='Consulting']",
               "(//A[@id='myInput'])[text()='Finance']"
               ]


def test_setup():
    global driver
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_assessment():
    driver.get("https://www.mondaymorning.in")
    driver.find_element_by_link_text("Assessments").click()
    driver.find_element_by_xpath("(//A[@class=' dropdown-toggle mr-4'])['Choose category ']").click()
    sleep(2)
    driver.find_element_by_xpath(random.choice(Assessments)).click()
    sleep(3)
    driver.execute_script("window.scrollTo(0,800);")
    sleep(2)
    driver.find_element_by_xpath("(//A[@class='btn btn-primary-blue  btn-lg tw-mt-40 waves-effect waves-light'])["
                                 "text()='Subscribe Today']").click()


def test_login():
    driver.find_element_by_xpath("(//INPUT[@id='loginemail'])").send_keys("rakesh_patra+2020@mondaymorning.in")
    sleep(2)
    driver.find_element_by_xpath("(//INPUT[@id='loginPassword'])").send_keys("1234")
    sleep(1)
    driver.find_element_by_xpath("(//INPUT[@id='login-model'])").click()


# @pytest.mark.skip(reason="Skip as of now")
def test_subscribe():
    driver.find_element_by_xpath("(//A[@type='button'])[text()='Close']").click()
    sleep(1)
    # delay = 3 # seconds
    # try:
    #     myElem = EC.presence_of_element_located((By.XPATH,"(//A[@type='button'])[text()='Close']"))
    #     WebDriverWait(driver,timeout=3).until(myElem)

    # print("Element is located")
    # except:
    #     print("Element is taking Too-much time to load")
    # act=ActionChains(driver)
    # act.click().perform()    ###### This will be a left click only
    subscribe = ["(//SPAN[@class='hide-mobile'])['NOW'][1]",
                 "(//SPAN[@class='hide-mobile'])['NOW'][2]",
                 "(//SPAN[@class='hide-mobile'])['NOW'][3]",
                 "(//SPAN[@class='hide-mobile'])['NOW'][4]",
                 ]
    driver.find_element_by_xpath(random.choice(subscribe)).click()
    sleep(2)


# @pytest.mark.skip(reason="Skip as of now")
def test_billing():
    driver.find_element_by_xpath("(//INPUT[@id='promo_code'])").send_keys("MM100off")
    driver.find_element_by_xpath("(//BUTTON[@id='check_coupon'])['Apply']").click()
    if "(//INPUT[@id='promo_code'])" == "MM100off" or "MOMO100":

        try:
            driver.find_element_by_xpath("(//INPUT[@id='promo_code'])").clear()
        finally:
            driver.find_element_by_xpath("(//INPUT[@id='promo_code'])").send_keys("MOMO100")
            driver.find_element_by_xpath("(//BUTTON[@id='check_coupon'])['Apply']").click()
            driver.find_element_by_xpath("(//BUTTON[@id='pay_now'])").click()
    sleep(3)
    driver.find_element_by_xpath(
        "(//A[@class='btn btn-assessment btn-indigo center-block waves-effect waves-light'])").click()
    sleep(2)


# @pytest.mark.skip(reason="Skip as of now")
def test_assessments():
    driver.find_element_by_xpath("//H4[@class='card-title text-center'][text()='Consulting Capsule']").click()
    assignments = ['Marketing',
                   'Operations',
                   'Finance',
                   'Strategy'
                   ]
    driver.find_element_by_link_text('Marketing').click()
    sleep(2)
    driver.find_element_by_xpath("(//I[@class='fa fa-lock'])[' Unlock Package'][1]").click()
    sleep(2)
    driver.find_element_by_xpath(
        "(//BUTTON[@class='btn btn-deep-purple btn-sm confirm_pack'])[text()='Unlock']").click()
    sleep(2)
    driver.find_element_by_xpath(
        "(//A[@class='btn btn-cyan mt-1 waves-effect waves-light sidebar-active'])[text()='OK']").click()
    sleep(2)
    driver.find_element_by_link_text(random.choice(assignments)).click()
    sleep(1)
    driver.find_element_by_xpath("(//A[@class=' n-c-btn3'])").click()
    sleep(2)


def test_master_tool():
    driver.find_element_by_xpath("(//LABEL[@class='form-check-label'])").click()
    sleep(2)
    driver.find_element_by_xpath("(//BUTTON[@type='button'])[text()='Start Test ']").click()
    sleep(2)
    driver.find_element_by_xpath("(//BUTTON[@type='button'])[text()='Ok']").click()
    sleep(2)


def test_drag_drop_tool():
    source_element = driver.find_element_by_xpath("(//LI[@class='list-group-item fixed'])[1]")
    dest_element = driver.find_element_by_xpath("(//LI[@class='list-group-item fixed'])[3]")
    ActionChains(driver).drag_and_drop(source_element, dest_element).perform()


# ############## Implicitly Wait:-Is a kind of wait where we ask the webdriver to wait for a certain amount of
# seconds,until unless all the elements in the ## web page will get load,it's only applied once and can be executed
# after every time the script will execute.

# ###### Explicit Wait:-Is a wait which can be applied more than one time and also can be applied on any specific web
# element.


def test_teardown():
    driver.close()
