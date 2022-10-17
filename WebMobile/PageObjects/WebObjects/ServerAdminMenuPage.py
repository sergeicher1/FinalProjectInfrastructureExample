# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Web Objects - Server Admin Menu Page
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------


from selenium.webdriver.common.by import By

'''In new version of grafana First expand sidebar!!! IN FLOW !!! '''
expandButton = (
    By.CSS_SELECTOR, "button[aria-label='Open navigation menu']")  # Click this first to find other elements!!!
serverAdmin = (By.XPATH, "//*[@id='reactRoot']/div[1]/div/nav/div[4]/div[1]/div[2]/ul/li[7]")
users = (By.CSS_SELECTOR, "/html/body/div[2]/div[1]/nav/div/div[1]/ul/li[8]/div[1]")
orgs = (By.CSS_SELECTOR, "a[href='/admin/orgs']")
settings = (By.CSS_SELECTOR, "a[href='/admin/settings']")
plugins = (By.CSS_SELECTOR, "a[href='/admin/plugins']")
stats = (By.CSS_SELECTOR, "a[href='/admin/upgrading']")


class ServerAdminMenuPage:

    def __init__(self, driver):
        self.driver = driver

    # To see other elements first should click expand button !!!!
    def GetExpandButton(self):
        return self.driver.find_element(expandButton[0], expandButton[1])

    def GetServerAdmin(self):
        return self.driver.find_element(serverAdmin[0], serverAdmin[1])

    def GetUsers(self):
        return self.driver.find_element(users[0], users[1])

    def GetOrgs(self):
        return self.driver.find_element(orgs[0], orgs[1])

    def GetSettings(self):
        return self.driver.find_element(settings[0], settings[1])

    def GetPlugins(self):
        return self.driver.find_element(plugins[0], plugins[1])

    def GetStats(self):
        return self.driver.find_element(stats[0], stats[1])
