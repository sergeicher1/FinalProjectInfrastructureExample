# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Desktop Test Cases
# Teacher     : Yoni Flenner
# Site        : [""]
# WebDriver   : WinAppDriver
# Version     : 3.141.0
# Teacher     : Yoni Flenner
# Application : ["Calculator"]
# Device      : Windows
# ----------------------------------------------------------------------------------------
import allure
import pytest

from WebMobile.Extensions.Verifications import Verifications
from WebMobile.WorkFlows.DesktopFlow import DesktopFlows


@pytest.mark.usefixtures("initDesktopDriver")
class Test_Desktop:

    @allure.title("Test 01: Adding two numbers")
    @allure.description("This test adds 2 numbers nad verifies result")
    def test_AddNumbersAndVerify(self):
        DesktopFlows.CalculateFlow("1+7")
        Verifications.VerifyEquals(DesktopFlows.GetResultFlow(), "8")

    @allure.title("Test 02: Arithmetic actions")
    @allure.description("This test does some Arithmetic actions and Verifies it")
    def test_ArithmeticActions(self):
        DesktopFlows.CalculateFlow("2*5+50/2-25")
        Verifications.VerifyEquals(DesktopFlows.GetResultFlow(), "5")

    def teardown_method(self):
        DesktopFlows.ClearFlow()  # To clear screen after each operation
