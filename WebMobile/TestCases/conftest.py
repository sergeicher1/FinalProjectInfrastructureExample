# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : configuration of pytest
# Teacher     : Yoni Flenner
# Site        : [""]
# WebDriver   : Appium
# Version     : 3.141.0
# description : Appium, Electron, Desktop=> change selenium to 3.141.0 and appium-python-client to 1.3.0
# Teacher     : Yoni Flenner
# Application : ["API Demos"]
# Device      : Tablet
# ----------------------------------------------------------------------------------------
import os
from time import sleep
import logging
import allure
import appium
import mysql.connector
import pytest
import selenium
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver as SWebDriver
from appium import webdriver as AWebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
# from applitools.selenium import Eyes
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from WebMobile.Utilities.EdgeDriverFix import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager
from WebMobile.Utilities.CommonOps import *
from WebMobile.Utilities.EventListener import EventListener
from WebMobile.Utilities.ManagePages import ManagePages

'''Objects Initialization'''
driver = None
action = None
action2 = None
multiAction = None
mobileSize = None
dbConnector = None
# eyes = Eyes()  # Applitools

# webDriver = "Chrome" for first initiation

'''WebDriver initiation'''


# Only Web with Selenium 4 X
@pytest.fixture(scope="class")  # If autouse=True added, every test will initiate the driver !!!
def initWebDriver(request):
    if GetData("ExecuteApplitools").lower() == "yes":  # Applitools
        globals()["driver"] = GetWebDriver()
        '''For Applitools, It doesn't support Events'''
    else:
        edriver = GetWebDriver()
        globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()["driver"]
    driver.maximize_window()
    driver.implicitly_wait(int(GetData("WaitTime")))
    driver.get(GetData("URL"))
    request.cls.driver = driver
    globals()["action"] = ActionChains(driver)
    ManagePages.InitWebPages()

    # if GetData("ExecuteApplitools").lower() == "yes":  # Applitools
    #     eyes.api_key = GetData("ApplitoolsKey")
    yield
    driver.quit()
    # if GetData("ExecuteApplitools").lower() == "yes":  # Applitools
    #     eyes.close()
    #     eyes.abort()


def GetWebDriver():
    webDriver = GetData("Browser")
    # webDriver = os.getenv("Browser") # For Jenkins with parameters
    if webDriver.lower() == "chrome":
        driver = GetChrome()
    elif webDriver.lower() == "firefox":
        driver = GetFirefox()
    elif webDriver.lower() == "msedge":
        driver = GetMSEdge()
    elif webDriver.lower() == "ie":
        driver = GetIE()
    else:
        driver = None
        raise Exception("Wrong input, unrecognized browser!")
    return driver


def GetChrome():
    # ser = ChromeService(ChromeDriverManager().install())  # Selenium 4x
    # chromeDriver = SWebDriver.Chrome(service=ser)
    chromeDriver = SWebDriver.Chrome(ChromeDriverManager().install())  # Selenium 3x
    return chromeDriver


def GetFirefox():
    # ser = FirefoxService(GeckoDriverManager().install())  # Selenium 4x
    # ffDriver = SWebDriver.Firefox(service=ser)
    ffDriver = SWebDriver.Firefox(GeckoDriverManager().install())  # Selenium 3x
    return ffDriver


def GetMSEdge():
    # ser = EdgeService(EdgeChromiumDriverManager().install())  # Selenium 4x
    # edgeDriver = SWebDriver.Edge(service=ser)
    edgeDriver = SWebDriver.Edge(EdgeChromiumDriverManager().install())  # Selenium 3x
    return edgeDriver


def GetIE():
    # ser = IEService(IEDriverManager().install())  # Selenium 4x
    # ieDriver = SWebDriver.Ie(service=ser)
    ieDriver = SWebDriver.Ie(IEDriverManager().install())  # Selenium 3x
    return ieDriver


'''MobileDriver initiation'''


@pytest.fixture(scope="class")
def initMobileDriver(request):
    edriver = GetMobileDriver()
    globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()["driver"]
    driver.implicitly_wait(int(GetData("WaitTime")))
    request.cls.driver = driver
    globals()["action"] = TouchAction(driver)  # Actions for mobile
    request.cls.action = globals()["action"]
    globals()["action2"] = TouchAction(driver)  # Actions for mobile
    request.cls.action2 = globals()["action2"]
    globals()["multiAction"] = MultiAction(driver)  # Multi Actions for mobile(zoom/pinch)
    request.cls.multiAction = globals()["multiAction"]
    globals()["mobileSize"] = driver.get_window_size()
    request.cls.mobileSize = globals()["mobileSize"]

    ManagePages.initMobilePages()
    yield
    driver.quit()


def GetMobileDriver():
    if GetData("MobileDevice").lower() == "android":
        driver = GetAndroid(GetData("Udid"))
    elif GetData("MobileDevice").lower() == "ios":
        driver = GetIOS(GetData("Udid"))
    else:
        driver = None
        raise Exception("Wrong input, Unrecognized mobile operating system")
    return driver


def GetAndroid(udid):
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = GetData("AppPackage")
    dc['appActivity'] = GetData("AppActivity")
    dc['platformName'] = 'android'
    androidDriver = AWebDriver.Remote(GetData("AppiumServer"), dc)  # alias AWebDriver
    return androidDriver


def GetIOS(udid):
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = GetData("BundleID")
    dc['platformName'] = 'ios'
    iosDriver = AWebDriver.Remote(GetData("AppiumServer"), dc)
    return iosDriver


'''Electron Driver Initiation'''


@pytest.fixture(scope="class")
def initElectronDriver(request):
    # edriver = GetElectronDriver()
    # globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
    # driver = globals()["driver"]
    globals()["driver"] = GetElectronDriver()
    driver = globals()["driver"]
    driver.implicitly_wait(int(GetData("WaitTime")))
    request.cls.driver = driver
    globals()["action"] = ActionChains(driver)
    request.cls.driver = globals()["action"]
    ManagePages.initElectronPages()

    yield
    driver.quit()


def GetElectronDriver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = GetData("ElectronApp")
    # ser = GetData("ElectronDriver")  # new way of passing as service
    # driver = selenium.webdriver.Chrome(chrome_options=options, service_args=ser)  # new way of passing as service
    driver = selenium.webdriver.Chrome(options=options, executable_path=GetData("ElectronDriver"))
    # driver = selenium.webdriver.Chrome(options=options, executable_path=ser)
    # executable_path, DEPRECATED
    return driver


'''Desktop Driver Initiation'''


@pytest.fixture(scope="class")
def initDesktopDriver(request):
    edriver = GetDesktopDriver()
    globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()["driver"]
    driver.implicitly_wait(int(GetData("WaitTime")))
    request.cls.driver = driver
    ManagePages.iniDesktopPages()

    yield
    driver.quit()


def GetDesktopDriver():
    dc = {}
    dc["app"] = GetData("ApplicationName")
    dc["platformName"] = "Windows"
    dc["deviceName"] = "WinowsPC"
    driver = appium.webdriver.Remote(GetData("WinAppDriverService"), dc)
    return driver


'''Database connection'''


@pytest.fixture(scope="class")
def initDBConnection(request):  # Open session
    dbConnector = mysql.connector.connect(
        host=GetData("DbHost"),
        database=GetData("DbName"),
        user=GetData("DbUser"),
        password=GetData("DbPassword")
    )
    globals()["dbConnector"] = dbConnector
    request.cls.dbConnector = dbConnector

    yield
    dbConnector.close()  # Close session


'''Catch Exceptions Errors and Screenshots'''


def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()["driver"] is not None:  # If it is None -> This is exception from API test
            image = GetData("ScreenshotPath") + "screen_" + str(GetTimeStamp()) + ".png"
            globals()["driver"].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
