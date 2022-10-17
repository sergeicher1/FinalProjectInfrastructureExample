# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Web Objects - Server Admin New User Page
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

name = (By.XPATH, "//div/input[@id='name-input']")
email = (By.XPATH, "//div/input[@id='email-input']")
userName = (By.XPATH, "//div/input[@id='username-input']")
password = (By.XPATH, "//div/input[@id='password-input']")
createUser = (By.CSS_SELECTOR, ".css-1mhnkuh")


class ServerAdminNewUserPage:

    def __init__(self, driver):
        self.driver = driver

    def GetName(self):
        return self.driver.find_element(name[0], name[1])

    def GetEmail(self):
        return self.driver.find_element(email[0], email[1])

    def GetUserName(self):
        return self.driver.find_element(userName[0], userName[1])

    def GetPassword(self):
        return self.driver.find_element(password[0], password[1])

    def GetCreateUser(self):
        return self.driver.find_element(createUser[0], createUser[1])
