# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-10-05 21:00
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 3.141.0
# Title       : Full stack test Python Automation
# description : Mobile Actioins(inherit from UiActions), change selenium to 3.141.0 and appium-python-client to 1.3.0
# Teacher     : Yoni Flenner
# Application : ["Mortgage Calculator UK"]
# Device      : Tablet
# ----------------------------------------------------------------------------------------
import allure

from WebMobile.Extensions.UiActions import UiActions
from WebMobile.TestCases import conftest


class MobileActions(UiActions):

    @staticmethod
    @allure.step("Tap on Element")
    def Tap(elem, times=1):
        conftest.action.tap(elem, times).perform()

    @staticmethod
    @allure.step("Swipe Screen")
    def Swipe(startX, startY, endX, endY, duration):
        conftest.driver.swipe(startX, startY, endX, endY, duration)

    @staticmethod
    @allure.step("Zoom Screen")
    def Zoom(element, pixels=200):
        action1 = conftest.action
        action2 = conftest.action2
        multiAction = conftest.multiAction
        xLoc = element.rect["x"]
        yLoc = element.rect["y"]
        action1.long_press(x=xLoc, y=yLoc).movet_to(x=xLoc, y=yLoc + pixels).wait(500).release()
        action2.long_press(x=xLoc, y=yLoc).movet_to(x=xLoc, y=yLoc - pixels).wait(500).release()
        multiAction.add(action1, action2)
        multiAction.perform()

    @staticmethod
    @allure.step("Pinch Screen")
    def Pinch(element, pixels=200):
        action1 = conftest.action
        action2 = conftest.action2
        multiAction = conftest.multiAction
        xLoc = element.rect["x"]
        yLoc = element.rect["y"]
        action1.long_press(x=xLoc, y=yLoc + pixels).movet_to(x=xLoc, y=yLoc).wait(500).release()
        action2.long_press(x=xLoc, y=yLoc - pixels).movet_to(x=xLoc, y=yLoc).wait(500).release()
        multiAction.add(action1, action2)
        multiAction.perform()
