# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Web Objects - Server Admin Page
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

search = (By.CSS_SELECTOR, ".css-yn255a-input-input")
newUser = (By.CSS_SELECTOR, ".css-1mhnkuh")
usersList = (By.XPATH, "//table[@class='filter-table form-inline filter-table--hover']/tbody/tr")
userByUserName = (By.CSS_SELECTOR, "a[title='ElfPumkin']")
delete = (By.XPATH, "//div/button[@class='css-mk7eo3-button']")
confirmDelete = (By.CSS_SELECTOR, "button[aria-label='Confirm Modal Danger Button']")


class ServerAdminPage:

    def __init__(self, driver):
        self.driver = driver

    def GetSearch(self):
        return self.driver.find_element(search[0], search[1])

    def GetNewUser(self):
        return self.driver.find_element(newUser[0], newUser[1])

    def GetUserList(self):
        return self.driver.find_elements(usersList[0], usersList[1])

    '''This method returns user by index from list'''

    def GetUserByIndex(self, index):
        return self.GetUserList()[index]

    def GetDelete(self):
        return self.driver.find_element(delete[0], delete[1])

    def GetConfirmDelete(self):
        return self.driver.find_element(confirmDelete[0], confirmDelete[1])

    '''One way to find record to delete, by Yoni'''

    def GetUserByUserName(self, name):
        return self.driver.find_element(userByUserName[0], userByUserName[1].replace("ElfPumkin", str(name)))
