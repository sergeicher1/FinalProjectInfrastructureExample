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

amount = (By.ID, "etAmount")
term = (By.ID, "etTerm")
rate = (By.ID, "etRate")
calculate = (By.ID, "add_schedule_text")
save = (By.ID, "btnSave")
repayment = (By.ID, "tvRepayment")
interest = (By.ID, "tvInterestOnly")


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def GetAmount(self):
        return self.driver.find_element(amount[0], amount[1])

    def GetTerm(self):
        return self.driver.find_element(term[0], term[1])

    def GetRate(self):
        return self.driver.find_element(rate[0], rate[1])

    def GetCalculate(self):
        return self.driver.find_element(calculate[0], calculate[1])

    def GetSave(self):
        return self.driver.find_element(save[0], save[1])

    def GetRepayment(self):
        return self.driver.find_element(repayment[0], repayment[1])

    def GetInterest(self):
        return self.driver.find_element(interest[0], interest[1])
