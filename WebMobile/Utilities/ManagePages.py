# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Utilities  - Manage Pages
# Teacher     : Yoni Flenner
# Site        : ["http://localhost:3000/"]
# WebDriver   : Appium
# Version     : 3.141.0
# description : Appium ManagePages, change selenium to 3.141.0 and appium-python-client to 1.3.0
# Teacher     : Yoni Flenner
# Application : ["API Demos"]
# Device      : Tablet
# ----------------------------------------------------------------------------------------
from selenium.webdriver.common.by import By
from selenium import webdriver

from WebMobile.PageObjects.DesktopObjects.StandardPage import StandardPage
from WebMobile.PageObjects.ElectronObjects.TaskPage import TaskPage
from WebMobile.PageObjects.MobileObjects.CalculatorPage import CalculatorPage
from WebMobile.PageObjects.MobileObjects.SavedPage import SavedPage
from WebMobile.PageObjects.WebObjects.LeftMenuPage import LeftMenuPage
from WebMobile.PageObjects.WebObjects.ServerAdminMenuPage import \
    ServerAdminMenuPage
from WebMobile.PageObjects.WebObjects.ServerAdminNewUserPage import \
    ServerAdminNewUserPage
from WebMobile.PageObjects.WebObjects.ServerAdminPage import \
    ServerAdminPage
from WebMobile.PageObjects.WebObjects.UpperMenuPage import \
    UpperMenuPage
from WebMobile.TestCases import conftest
from WebMobile.PageObjects.WebObjects.LoginPage import LoginPage
from WebMobile.PageObjects.WebObjects.MainPage import MainPage

'''Web Objects'''
webLogin = None
webMain = None
webUpperMenu = None
leftMenu = None
serverAdmin = None
serverAdminMenu = None
serverAdminNewUser = None

'''Mobile Objects'''
mobileCalculator = None
mobileSaved = None

'''Electron Objects'''
electronTask = None

'''Desktop Objects'''
standardCalc = None


class ManagePages:
    # Initialization of web objects
    @staticmethod
    def InitWebPages():
        globals()["webLogin"] = LoginPage(conftest.driver)
        globals()["webMain"] = MainPage(conftest.driver)
        globals()["webUpperMenu"] = UpperMenuPage(conftest.driver)
        globals()["leftMenu"] = LeftMenuPage(conftest.driver)
        globals()["serverAdmin"] = ServerAdminPage(conftest.driver)
        globals()["serverAdminMenu"] = ServerAdminMenuPage(conftest.driver)
        globals()["serverAdminNewUser"] = ServerAdminNewUserPage(conftest.driver)

    # Initialization of mobile objects
    @staticmethod
    def initMobilePages():
        globals()["mobileCalculator"] = CalculatorPage(conftest.driver)
        globals()["mobileSaved"] = SavedPage(conftest.driver)

    # Initialization of electron objects
    @staticmethod
    def initElectronPages():
        globals()["electronTask"] = TaskPage(conftest.driver)

    # Initialization of desktop objects
    @staticmethod
    def iniDesktopPages():
        globals()["standardCalc"] = StandardPage(conftest.driver)
