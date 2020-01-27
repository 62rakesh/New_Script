class AdminPage:
    Authorization_xpath = "(//I[@class='icon-navbar'])[1]"

    def __init__(self,driver):
        self.driver=driver

    def clickAuthorization(self):
        self.driver.find_element_by_xpath(self.Authorization_xpath).click()







