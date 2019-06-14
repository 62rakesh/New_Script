import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.webdriver import WebDriver
driver:webdriver=webdriver.Chrome()

def test_setup():
    global driver
    # driver:webdriver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
def test_login():
    driver.get("https://www.mondaymorning.in")
    sleep(1)
    driver.find_element_by_link_text("Log In").click()
    sleep(1)
    driver.find_element_by_xpath("//INPUT[@name='user_login']").send_keys("rakesh_patra+0051@mondaymorning.in")
    sleep(1)
    driver.find_element_by_xpath("//INPUT[@name='user_pwd']").send_keys("1234")
    sleep(1)
    driver.find_element_by_xpath("//input[@id='login-model']").submit()
    sleep(1)
    print("Login is Completed")
def test_Applyjob():
    driver.execute_script("window.alert('Apply for the job');")  #####Proceeding for JAF Process
    alert = driver.switch_to_alert()
    sleep(2)
    alert.accept()
    driver.find_element_by_xpath("//A[@id='navbarDropdownMenuLink-555'][text()='Jobs']").click()
    sleep(1)
    driver.find_element_by_xpath("//A[@class='dropdown-item waves-effect waves-light']").click()
    sleep(2)
    driver.save_screenshot("Screenshoot1.png")
    driver.find_element_by_xpath("(//A[@class='btn btn-fb btn-rounded float-right  btn-sm waves-effect waves-light'])[text()='Apply'][5]").click()
    sleep(2)
    driver.find_element_by_xpath("//A[@class='float-right'][text()=' Apply']").click()
    sleep(2)
    print("One job has been Processed")
def test_Jaf():
    driver.find_element_by_xpath("//INPUT[@name='mobile']").send_keys("9910768013")
    sleep(1)
    driver.find_element_by_xpath("//select[@class='form-control browser-default custom-select']").click()
    sleep(1)
    obj = Select(driver.find_element_by_name("gender"))
    obj.select_by_visible_text("Male")
    sleep(1)
    driver.find_element_by_xpath("//SPAN[@id='select2-city-container']").click()
    sleep(1)
    driver.find_element_by_xpath("//INPUT[@class='select2-search__field']").send_keys("Noida")
    sleep(2)
    uploadElement=driver.find_element_by_name("resume")
    uploadElement.send_keys("C:\\Users\\lenovo\\Desktop\\3rd Year Mark_Sheet.pdf")
    #driver.find_element_by_xpath("//div[@class='float-right span-browse'][text()='Browse']").click()
    #sleep(1)
    driver.find_element_by_xpath("//button[@id='nextBtn']").click()
    sleep(1)
    obj = Select(driver.find_element_by_name("pg_university"))
    sleep(1)
    obj.select_by_visible_text("Ahmedabad University")
    sleep(1)
    obj = Select(driver.find_element_by_name("pg_degree"))
    sleep(1)
    obj.select_by_visible_text("ME/ M.Tech./ MS (Engg/ Sciences)")
    sleep(1)
    driver.find_element_by_xpath("//INPUT[@id='pg_perc']").send_keys("70")
    sleep(1)
    obj = Select(driver.find_element_by_name("pg_passing"))
    obj.select_by_visible_text("2018")
    sleep(1)
    driver.find_element_by_xpath("(//BUTTON[@id='nextBtn'])['Next']").click()
    sleep(1)
    driver.find_element_by_xpath("(//textarea[@class='comp form-control '])").send_keys("No")
    sleep(2)
    driver.find_element_by_xpath("//button[@id='nextBtn'][text()='Save & Continue']").click()
    sleep(3)
    print("JAF is completed")
    # driver.find_element_by_xpath("(//A[@class='btn btn-info preview_submit waves-effect waves-light'])").click()
    # sleep(1)
    # driver.find_element_by_xpath("(//LABEL[@class='form-check-label'])").click()
    # sleep(1)
    # driver.find_element_by_xpath("(//BUTTON[@type='button'])[1]").click()
    # sleep(1)

def test_edit_jafpreview():
    driver.find_element_by_xpath("(//IMG[@class='edit-icon'])[2]").click()
    driver.find_element_by_xpath("(//TEXTAREA[@type='text'])").send_keys("Great things has been achieved")
    driver.find_element_by_xpath("(//A[@type='button'])[1]").click()
    sleep(2)
    print("Jaf Preview is completed")
def test_edit_education():
    driver.find_element_by_xpath("(//IMG[@class='edit-icon'])[7]").click()
    select=Select(driver.find_element_by_name("pg_degree"))
    select.select_by_visible_text("ME/ M.Tech./ MS (Engg/ Sciences)")
    select1=Select(driver.find_element_by_name("pg_institution"))
    select1.select_by_visible_text("Ahmedabad University")
    driver.find_element_by_id("pg_perc").send_keys("80%")
    select2=Select(driver.find_element_by_name("pg_year_pass"))
    select2.select_by_visible_text("2017")
    driver.find_element_by_xpath("(//BUTTON[@type='button'])[5]").submit()
    sleep(1)
    print("Post Graduation details added.")
def test_upload_resume():
    uploadElement=driver.find_element_by_id("resume_upl")
    uploadElement.send_keys("C:\\Users\\lenovo\\Desktop\\3rd Year Mark_Sheet.pdf")
    driver.find_element_by_id("resume_upload").click()
    sleep(2)
    driver.find_element_by_xpath("(//A[@type='button'])[2]").click()
    sleep(5)
    print("Highest education details is filled.")
def test_Dasboard():
    driver.find_element_by_xpath("(//A[@class='nav-link waves-effect waves-light'])[1]").click()
def test_Assessments():
    driver.find_element_by_xpath("(//LI[@class='nav-item dropdown nav-border '])[2]").click()
    sleep(1)
    driver.find_element_by_xpath("(//A[@class='dropdown-item waves-effect waves-light'])[text()='All Assessments']").click()
    sleep(1)
    driver.find_element_by_xpath("(//H4[@class='card-title text-center'])[4]").click()
    sleep(1)
    driver.find_element_by_xpath("(//I[@class='fa fa-lock'])['Unlock Package'][1]").click()
    print("Assessments Processed")
    driver.find_element_by_xpath("(//A[@class='btn btn-success '])[text()='Subscribe Now']").click()
    sleep(1)
    driver.find_element_by_xpath("(//A[@type='button'])[2]").click()
    sleep(1)
    driver.find_element_by_xpath("(//A[@type='button'])[4]").click()
    sleep(1)
    driver.find_element_by_xpath("(//INPUT[@type='number'])").send_keys(9910768013)
    sleep(1)
    driver.find_element_by_xpath("(//INPUT[@type='text'])[6]").send_keys("MOMO100")
    sleep(1)
    driver.find_element_by_xpath("(//BUTTON[@type='button'])[2]").click()
    sleep(1)
    driver.find_element_by_xpath("(//BUTTON[@type='button'])[1]").click()
    sleep(1)
    driver.find_element_by_xpath("(//A[@class='  c-float-right btn-sm '])").click()
    sleep(2)
    driver.find_element_by_xpath("(//A[@class='n-c-btn3  '])[1]").click()
    sleep(1)
    driver.find_element_by_xpath("(//A[@id='view_sc'])[text()='Start Test']").click()
    sleep(3)
    print("Subscription Completed and One Assessments Unlocked")

def test_teardown():
    driver.close()
    print("E2E completed.")

