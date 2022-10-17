# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : WEB - Main Page
# Teacher     : Yoni Flenner
# Site        : ["http://localhost:3000/"]
# ----------------------------------------------------------------------------------------
from selenium.webdriver.common.by import By
from selenium import webdriver

mainTitle = (By.CLASS_NAME, "css-1aanzv4")


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def GetMainTitle(self):
        return self.driver.find_element(mainTitle[0], mainTitle[1])
