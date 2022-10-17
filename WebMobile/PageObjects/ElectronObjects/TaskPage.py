# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Electron App Automation
# Teacher     : Yoni Flenner
# Site        : [""]
# WebDriver   : Electron
# Version     : 3.141.0
# Teacher     : Yoni Flenner
# Application : ["To do List"]
# Device      : ""
# ----------------------------------------------------------------------------------------
from selenium.webdriver.common.by import By

create = (By.XPATH, "//input[@placeholder='Create a task']")
tasks = (By.CLASS_NAME, "view_2Ow90")
deleteBtns = (By.XPATH, "//div[@class='view_2Ow90']/*[name()='svg']")


class TaskPage:

    def __init__(self, driver):
        self.driver = driver

    def GetCreate(self):
        return self.driver.find_element(create[0], create[1])

    def GetTasks(self):
        return self.driver.find_elements(tasks[0], tasks[1])

    def GetDeleteBtns(self):
        return self.driver.find_elements(deleteBtns[0], deleteBtns[1])
