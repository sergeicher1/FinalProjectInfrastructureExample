# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Verifications
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------
import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:

    @staticmethod
    @allure.step("Verify Equals")
    def VerifyEquals(actual, expected):  # here should NOT use type hints, because in future can be sent other type
        assert actual == expected, "Verify Equals FAILED, actual: " + str(
            actual) + " is not Equals to Expected: " + str(expected)

    @staticmethod
    @allure.step("Verify element is displayed")
    def VerifyIsDisplayed(elem: WebElement):
        assert elem.is_displayed(), "Verify Is Displayed FAILED, Element: " + elem.text + " is not displayed!"

    '''Method to append FAILED assertion to list, and check only in the end of test case'''

    # Verify Menu Buttons Using smart - assertion Yoni's implementation
    @staticmethod
    @allure.step("Soft Displayed elements")
    def SoftDisplayed(elements):
        failedElements = []
        for i in range(len(elements)):
            if not elements[i].is_displayed():
                failedElements.insert(len(failedElements), elements[i].get_attribute("aria-label"))
        if len(failedElements) > 0:
            for failedElement in failedElements:
                print("Soft Displayed FAILED, Element which have FAILED: ",
                      str(failedElement))  # Doesn't know what to expect, cast to string
            raise AssertionError("Soft Displayed FAILED")

    # Verify Menu Buttons Using Installed package smart - assertion
    @staticmethod
    @allure.step("Soft Assert(Verification) using soft_assert")
    def SoftAssert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step("Verify number of elements in table")
    def VerifyNumberOfElements(elems, size):
        assert len(elems) == size, "Number Of Elements in list: " + str(
            len(elems)) + " doesn't match expected size: " + str(size)
