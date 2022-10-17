# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-10-05 21:00
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 3.141.0
# Title       : Full stack test Python Automation
# description : Appium conftest, change selenium to 3.141.0 and appium-python-client to 1.3.0
# Teacher     : Yoni Flenner
# Application : ["Mortgage Calculator UK"]
# Device      : Tablet
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

amount = (By.ID, "tvAmount")
term = (By.ID, "tvTerm")
rate = (By.ID, "tvRate")
repayment = (By.ID, "tvRepayment")
interest = (By.ID, "tvInterestOnly")
delete = (By.ID, "btnDel")
confirmDelete = (By.XPATH, "//*[@text='OK']")


class SavedPage:

    def __init__(self, driver):
        self.driver = driver

    def GetAmount(self):
        return self.driver.find_element(amount[0], amount[1])

    def GetTerm(self):
        return self.driver.find_element(term[0], term[1])

    def GetRate(self):
        return self.driver.find_element(rate[0], rate[1])

    def GetRepayment(self):
        return self.driver.find_element(repayment[0], repayment[1])

    def GetInterest(self):
        return self.driver.find_element(interest[0], interest[1])

    def GetDelete(self):
        return self.driver.find_element(delete[0], delete[1])

    def GetConfirmDelete(self):
        return self.driver.find_element(confirmDelete[0], confirmDelete[1])
