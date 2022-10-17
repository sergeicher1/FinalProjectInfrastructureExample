# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Utilities, Common Ops for many classes and objects
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------
import csv
from time import time

from selenium.webdriver.support.wait import WebDriverWait
import WebMobile.TestCases.conftest as conf
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET

'''Function to read files'''


def ReadCsv(fileName):
    data = []
    with open(fileName, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data


def GetData(name):
    root = ET.parse(
        "D:\\AtidAutomation\\FinalProjectInfrastructure\\WebMobile\\Configuration\\data.xml") \
        .getroot()
    return root.find(".//" + name).text


'''Function to Explicitly Wait for elements'''


def Wait(forElement, elem):
    if forElement == "elementExists":
        WebDriverWait(conf.driver, int(GetData("WaitTime"))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif forElement == "elementDisplayed":
        WebDriverWait(conf.driver, int(GetData("WaitTime"))).until(EC.visibility_of_element_located((elem[0], elem[1])))
    '''Can be extended here '''


def GetTimeStamp():
    return time()


'''Enum for selecting displayed or exist element, my Wait method uses this enum'''


class For:
    elementExists = "elementExists"
    elementDisplayed = "elementDisplayed"


'''Enum for search users by text or by index '''


class By:
    user = "user"
    index = "index"


'''Enum for selecting whether we want to sve mortgage transaction or not'''


class Save:
    Yes = True
    No = False


'''Enum for selecting whether we want to save mortgage transaction or not '''


class Direction:
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
