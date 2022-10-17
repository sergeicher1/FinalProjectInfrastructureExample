# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Test Cases for WEB
# Teacher     : Yoni Flenner
# Site        : [""]
# Server        : ["grafana 9"]
# ----------------------------------------------------------------------------------------
from time import sleep

import allure
import pytest

import WebMobile.TestCases.conftest as conf

from WebMobile.Utilities.CommonOps import *
from WebMobile.WorkFlows.WebFlows import *


# from FinalProjectCompleteInfrastructureGrafana.WorkFlows.WebFlows import testData


@pytest.mark.usefixtures("initWebDriver")
class Test_Web:
    # def test_Demo01(self):  # for first test, see driver's initialization
    #     sleep(1)
    @allure.title("Test 01: Verify Login Grafana")
    @allure.description("This test verifies a successful login to grafana")
    def test_VerifyLoginFlow(self):
        WebFlows.LoginFlow(GetData("UserName"), GetData("Password"))
        WebFlows.VerifyGrafanaTitle("Welcome to Grafana")

    @allure.title("Test 02: Verify upper menu buttons")
    @allure.description("This test verifies upper menu buttons are displayed")
    def test_VerifyUpperMenu(self):
        # WebFlows.VerifyUpperMenuButtonsFlow() Yoni's implementation
        WebFlows.VerifyUpperMenuButtonsFlowSmartAssertion()  # smart - assertion

    @allure.title("Test 03: Verify New User")
    @allure.description("This test creates and verifies new users")
    def test_VerifyNewUser(self):
        WebFlows.OpenUsers()
        WebFlows.CreateUser("Yoni1", "Flener1@gmail.com", "yonif1", "12345")
        WebFlows.CreateUser("Sergei", "Chernyahovsky@gmail.com", "sergei", "123456")
        WebFlows.VerifNumberOfUsers(3)

    @allure.title("Test 04: Filtering Users")
    @allure.description("This test filters users by search")
    @pytest.mark.parametrize("searchValue, expectedUsers", testData)
    def test_SearchUsers(self, searchValue, expectedUsers):
        WebFlows.OpenUsers()
        WebFlows.SearchUser(searchValue)
        WebFlows.VerifNumberOfUsers(int(expectedUsers))

    @allure.title("Test 05: Delete User")
    @allure.description("This test deletes users and verifies")
    def test_VerifyDeletedUser(self):
        WebFlows.OpenUsers()
        WebFlows.DeleteUser(By.user, "yonif1")
        WebFlows.DeleteUser(By.index, 1)
        WebFlows.VerifNumberOfUsers(1)

    '''Limited test, change to yes in data.xml if needed'''

    @allure.title("Test 06: Visual Testing")
    @allure.description("This Visual test of users table")
    @pytest.mark.skipif(GetData("ExecuteApplitools").lower() == "no",
                        reason="Limit tests on applitools, check if needed")
    def test_VisualVerifyDeletedUser(self):
        WebFlows.OpenUsers()
        # conf.eyes.open(conf.driver, "Grafana", "Grafana Testing User Table")
        # conf.eyes.check_window("User Table")

    def teardown_method(self):
        WebFlows.GetGrafanaHome(self)
