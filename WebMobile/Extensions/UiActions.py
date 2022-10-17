# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : UI Actions, Extension to override selenium actions
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from WebMobile.TestCases import conftest
from WebMobile.TestCases.conftest import action


class UiActions:
    @staticmethod
    @allure.step("Click on element")
    def Click(elem: WebElement):  # Type hint, so the IDE will know it should get web-element
        # Explicit_wait(can be added) for example, that's why we need to override selenium functions
        elem.click()

    @staticmethod
    @allure.step("Clear field")
    def Clear(elem: WebElement):
        elem.clear()

    @staticmethod
    @allure.step("Updating text")
    def UpdateText(elem: WebElement, value: str):
        elem.send_keys(value)

    @staticmethod
    @allure.step("Mouse hover")
    def MouseHover(elem1: WebElement, elem2: WebElement):
        action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step("Mouse hover tooltip")  # Because of dynamic rendering actionChains should be initialized every time
    def MouseHoverTooltip(elem: WebElement):
        ActionChains(conftest.driver).move_to_element(elem).click().perform()

    @staticmethod
    @allure.step("Mouse right click")
    def MouseRightClick(elem: WebElement):
        action.context_click(elem).perfom()

    @staticmethod
    @allure.step("Drag And Drop")
    def DragAndDrop(elem1: WebElement, elem2: WebElement):
        action.drag_and_drop(elem1, elem2).perform()
