# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : WEB - Login Page
# Teacher     : Yoni Flenner
# Site        : ["http://localhost:3000/login"]
# ----------------------------------------------------------------------------------------
from selenium.webdriver.common.by import By
from selenium import webdriver

userName = (By.NAME, "user")
password = (By.NAME, "password")
submit = (By.CLASS_NAME, "css-1mhnkuh")
skip = (By.XPATH, "//div/button[@aria-label='Skip change password button']")


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def GetUserName(self):
        return self.driver.find_element(userName[0], userName[1])

    def GetPassword(self):
        return self.driver.find_element(password[0], password[1])

    def GetSubmit(self):
        return self.driver.find_element(submit[0], submit[1])

    def GetSkip(self):
        return self.driver.find_element(skip[0], skip[1])
    