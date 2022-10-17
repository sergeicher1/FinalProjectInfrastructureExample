# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-10-05 21:00
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 3.141.0
# Title       : Full stack test Python Automation
# description : Mobile Test Cases, change selenium to 3.141.0 and appium-python-client to 1.3.0
# Teacher     : Yoni Flenner
# Application : ["Mortgage Calculator UK"]
# Device      : Tablet
# ----------------------------------------------------------------------------------------
import allure
import pytest

from WebMobile.Utilities.CommonOps import Save
from WebMobile.WorkFlows.MobileFlows import MobileFlow

'''
Figure out new implementation,
may be separate Infrastructure,
uses selenium 3, and causes problems to main infrastructure
  '''


@pytest.mark.usefixtures("initMobileDriver")
class Test_Mobile:
    @allure.step("Test 01: Verify Mortgage Repayment")
    @allure.description("this test verifies the mortgage repayment")
    def test_VerifyRepayment(self):
        MobileFlow.MortgageFlow("1000", "5", "2.5", Save.No)
        MobileFlow.VerifyMortgageRepayment("17.94")
