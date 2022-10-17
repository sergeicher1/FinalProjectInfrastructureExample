# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Web Objects - Upper Menu Page
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

general = (By.XPATH, "//nav/a[@class='css-1f4j3ij']")
home = (By.XPATH, "//a/span[@class='css-aqkpyi']")
panel = (By.XPATH, "//div/button[@aria-label='Add panel']")
dashboardSettings = (By.CSS_SELECTOR, "button[aria-label='Dashboard settings']")
cycleViewMode = (By.CSS_SELECTOR, "button[aria-label='Cycle view mode']")


class UpperMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def GetGeneral(self):
        return self.driver.find_element(general[0], general[1])

    def GetHome(self):
        return self.driver.find_element(home[0], home[1])

    def GetPanel(self):
        return self.driver.find_element(panel[0], panel[1])

    def GetDashboardSettings(self):
        return self.driver.find_element(dashboardSettings[0], dashboardSettings[1])

    def GetCycleViewMode(self):
        return self.driver.find_element(cycleViewMode[0], cycleViewMode[1])
