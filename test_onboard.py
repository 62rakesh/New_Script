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
    driver.find_element_by_xpath("(//A[@href='https://www.mondaymorning.in/mm/login/NjE/c3Vic2NyaWJl'][text("
                                 ")='Subscribe Today'])").click()


def test_login():
    driver.fin


def test_teardown():
    driver.close()