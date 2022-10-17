# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Web Objects - Left Menu Page
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------


from selenium.webdriver.common.by import By

grafanaHome = (By.XPATH, "//div/a[@aria-label='Home']")
searchDashboard = (By.CSS_SELECTOR, "button[aria-label='Search dashboards']")
starred = (By.CSS_SELECTOR, "button[aria-label='Starred']")
dashBoard = (By.CSS_SELECTOR, "a[aria-label='Dashboards']")
explore = (By.CSS_SELECTOR, "a[aria-label='Explore']")
alerting = (By.CSS_SELECTOR, "a[aria-label='Alerting']")
configuration = (By.XPATH, "//*[@aria-label='Configuration']")
serverAdmin = (By.XPATH, "//li/div/a[@aria-label='Server admin']")
admin = (By.XPATH, "//li/div/a[@aria-label='admin']")
helpElem = (By.XPATH, "//*[@aria-label='Help']")


class LeftMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def GetGrafanaHome(self):
        return self.driver.find_element(grafanaHome[0], grafanaHome[1])

    def GetSearchDashboard(self):
        return self.driver.find_element(searchDashboard[0], searchDashboard[1])

    def GetStarred(self):
        return self.driver.find_element(starred[0], starred[1])

    def GetDashboard(self):
        return self.driver.find_element(dashBoard[0], dashBoard[1])

    def GetExplore(self):
        return self.driver.find_element(explore[0], explore[1])

    def GetAlerting(self):
        return self.driver.find_element(alerting[0], alerting[1])

    def GetConfiguration(self):
        return self.driver.find_element(configuration[0], configuration[1])

    def GetServerAdmin(self):
        return self.driver.find_element(serverAdmin[0], serverAdmin[1])

    def GetAdmin(self):
        return self.driver.find_element(admin[0], admin[1])

    def GetHelpElem(self):
        return self.driver.find_element(helpElem[0], helpElem[1])
