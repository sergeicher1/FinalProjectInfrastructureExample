# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Desktop Flows
# Teacher     : Yoni Flenner
# Site        : [""]
# WebDriver   : WinAppDriver
# Version     : 3.141.0
# Teacher     : Yoni Flenner
# Application : ["Calculator"]
# Device      : Windows
# ----------------------------------------------------------------------------------------

import allure

from WebMobile.Extensions.UiActions import UiActions
import WebMobile.Utilities.ManagePages as pages


class DesktopFlows:

    @staticmethod
    @allure.step("Calculate equation")  # 1+9-5*100
    def CalculateFlow(equation):
        for i in equation:
            DesktopFlows.CalculatorClick(i)
        UiActions.Click(pages.standardCalc.GetEquals())

    @staticmethod
    @allure.step("Get Calculator Result")
    def GetResultFlow():
        result = pages.standardCalc.GetResult().text.replace("Display is",
                                                             "").strip()  # strip - remove spaces before and after
        return result

    @staticmethod
    @allure.step("Clear calculator screen")
    def ClearFlow():
        UiActions.Click(pages.standardCalc.GetClear())

    @staticmethod
    # This one is for input with string expressions (loops) - INFRASTRUCTURE
    def CalculatorClick(value):
        if value == "0":
            UiActions.Click(pages.standardCalc.GetZero())
        elif value == "1":
            UiActions.Click(pages.standardCalc.GetOne())
        elif value == "2":
            UiActions.Click(pages.standardCalc.GetTwo())
        elif value == "3":
            UiActions.Click(pages.standardCalc.GetThree())
        elif value == "4":
            UiActions.Click(pages.standardCalc.GetFour())
        elif value == "5":
            UiActions.Click(pages.standardCalc.GetFive())
        elif value == "6":
            UiActions.Click(pages.standardCalc.GetSix())
        elif value == "7":
            UiActions.Click(pages.standardCalc.GetSeven())
        elif value == "8":
            UiActions.Click(pages.standardCalc.GetEight())
        elif value == "9":
            UiActions.Click(pages.standardCalc.GetNine())
        elif value == "+":
            UiActions.Click(pages.standardCalc.GetPlus())
        elif value == "-":
            UiActions.Click(pages.standardCalc.GetMinus())
        elif value == "*":
            UiActions.Click(pages.standardCalc.GetMultiply())
        elif value == "/":
            UiActions.Click(pages.standardCalc.GetDivide())

        else:
            raise Exception("Invalid Input: " + value)
