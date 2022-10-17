# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-10-05 21:00
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 3.141.0
# Title       : Full stack test Python Automation
# description : Mobile Flows, change selenium to 3.141.0 and appium-python-client to 1.3.0
# Teacher     : Yoni Flenner
# Application : ["Mortgage Calculator UK"]
# Device      : Tablet
# ----------------------------------------------------------------------------------------
import allure
import WebMobile.Utilities.ManagePages as pages
from WebMobile.TestCases import conftest

from WebMobile.Extensions.MobileActions import MobileActions
from WebMobile.Extensions.Verifications import Verifications
from WebMobile.Utilities.CommonOps import GetData


class MobileFlow:

    @staticmethod
    @allure.step("Fill in mortgage details flow")
    def MortgageFlow(amount, term, rate, save):
        MobileActions.UpdateText(pages.mobileCalculator.GetAmount(), amount)
        MobileActions.UpdateText(pages.mobileCalculator.GetTerm(), term)
        MobileActions.UpdateText(pages.mobileCalculator.GetRate(), rate)
        MobileActions.Click(pages.mobileCalculator.GetCalculate())
        if save:
            MobileActions.Click(pages.mobileCalculator.GetSave())

    @staticmethod
    @allure.step("Verification repayment flow")
    def VerifyMortgageRepayment(expected):
        actual = pages.mobileCalculator.GetRepayment().text
        Verifications.VerifyEquals(actual, "£" + expected)

    @staticmethod
    @allure.step("Swipe to saves screen flow")
    def SwipeScreen(direction):
        width = conftest.mobileSize["width"]
        height = conftest.mobileSize["height"]

        startX, startY, endX, endY = None, None, None, None
        # startY = None
        # endX = None
        # endY = None
        if direction == "left":  # multiply by percents, because each screen has different pixels !!!
            startX = width * 0.9  # From bigger to smaller(right to left)
            endX = width * 0.1
            startY = endY = height * 0.5
        if direction == "right":  # multiply by percents, because each screen has different pixels !!!
            startX = width * 0.1  # From smaller to bigger(left to right)
            endX = width * 0.9
            startY = endY = height * 0.5
        if direction == "up":
            startY = height * 0.9
            endY = height * 0.1
            startX = endX = width * 0.5
        if direction == "down":
            startY = height * 0.1
            endY = height * 0.9
            startX = endX = width * 0.5

        MobileActions.Swipe(startX, startY, endX, endY, int(GetData("SwipeDuration")))

    @staticmethod
    @allure.step("Verify and delete saved transactions flow")
    def VerifyRateDeleteTransaction(expected):
        actual = pages.mobileSaved.GetRate().text()
        Verifications.VerifyEquals(actual, expected + "%")
        MobileActions.Tap(pages.mobileSaved.GetDelete())  # Can be added: , 2 times...
        MobileActions.Tap(pages.mobileSaved.GetConfirmDelete())  # Can be added: , 2 times...
