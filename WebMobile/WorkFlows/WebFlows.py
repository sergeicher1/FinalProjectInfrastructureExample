# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : WorkFlows, Web - Flows
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------
from time import sleep

import allure

from WebMobile.PageObjects.WebObjects import ServerAdminPage
from WebMobile.PageObjects.WebObjects import ServerAdminMenuPage
from WebMobile.Extensions.UiActions import UiActions
from WebMobile.Extensions.Verifications import Verifications
import WebMobile.Utilities.ManagePages as pages
from WebMobile.Utilities.CommonOps import *
import WebMobile.PageObjects.WebObjects.MainPage as main

data = ReadCsv(GetData("CSVLocation"))
testData = [
    (data[0][0], data[0][1]),
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1]),
    (data[3][0], data[3][1]),
    (data[4][0], data[4][1])
]

'''Import classes to work with created objects, import module to work with module itself!!!'''


# Business Flows

class WebFlows:
    testData = None

    @staticmethod
    @allure.step("Login to grafana flow")
    def LoginFlow(userName: str, password: str):
        UiActions.UpdateText(pages.webLogin.GetUserName(), userName)
        UiActions.UpdateText(pages.webLogin.GetPassword(), password)
        UiActions.Click(pages.webLogin.GetSubmit())
        UiActions.Click(pages.webLogin.GetSkip())

    @staticmethod
    @allure.step("Verify grafana title")
    def VerifyGrafanaTitle(expected: str):
        # Expected issue, in future may be added waiting, otherwise test will fail
        Wait(For.elementExists, main.mainTitle)  # For from common ops, main from main page
        actual = pages.webMain.GetMainTitle().text
        Verifications.VerifyEquals(actual, expected)

    # Verify Menu Buttons Using smart - assertion Yoni's implementation
    # @staticmethod
    # def VerifyUpperMenuButtonsFlow():
    #     elems = [
    #         pages.webUpperMenu.GetGeneral(),
    #         pages.webUpperMenu.GetHome(),
    #         pages.webUpperMenu.GetPanel(),
    #         pages.webUpperMenu.GetDashboardSettings(),
    #         pages.webUpperMenu.GetCycleViewMode()
    #     ]
    #     Verifications.SoftDisplayed(elems)

    # Verify Menu Buttons Using Installed package smart - assertion
    @staticmethod
    @allure.step("Verify displayed upper menu buttons flow Using smart-assertions")
    def VerifyUpperMenuButtonsFlowSmartAssertion():
        elems = [
            pages.webUpperMenu.GetGeneral(),
            pages.webUpperMenu.GetHome(),
            pages.webUpperMenu.GetPanel(),
            pages.webUpperMenu.GetDashboardSettings(),
            pages.webUpperMenu.GetCycleViewMode()
        ]
        Verifications.SoftAssert(elems)

    @staticmethod
    @allure.step("Go to users flow")
    def OpenUsers():
        UiActions.Click(pages.serverAdminMenu.GetServerAdmin())
        '''there is dynamic change of elements, look up how to do it later'''
        # UiActions.Click(pages.serverAdminMenu.GetExpandButton())  # First click to expand
        # # UiActions.MouseHover(pages.serverAdminMenu.GetServerAdmin(),pages.serverAdminMenu.GetUsers())
        # UiActions.Click(pages.serverAdminMenu.GetServerAdmin())
        # UiActions.Click(pages.serverAdminMenu.GetUsers())
        # Wait(For.elementDisplayed, pages.serverAdminMenu.GetUsers())
        # UiActions.Click(pages.serverAdminMenu.GetUsers())

    @staticmethod
    @allure.step("Create new user flow")
    def CreateUser(name, email, user, password):
        UiActions.Click(pages.serverAdmin.GetNewUser())
        UiActions.UpdateText(pages.serverAdminNewUser.GetName(), name)
        UiActions.UpdateText(pages.serverAdminNewUser.GetEmail(), email)
        UiActions.UpdateText(pages.serverAdminNewUser.GetUserName(), user)
        UiActions.UpdateText(pages.serverAdminNewUser.GetPassword(), password)
        UiActions.Click(pages.serverAdminNewUser.GetCreateUser())
        sleep(0.5)  # for tests, popup blocks New User button!!!

    @staticmethod
    @allure.step("Verify number of users in table")
    def VerifNumberOfUsers(number):
        if number > 0:
            Wait(For.elementDisplayed, ServerAdminPage.usersList)
            Verifications.VerifyNumberOfElements(pages.serverAdmin.GetUserList(), number)

    @staticmethod
    @allure.step("Search user from users table flow")
    def SearchUser(searchValue):
        UiActions.Clear(pages.serverAdmin.GetSearch())
        UiActions.UpdateText(pages.serverAdmin.GetSearch(), searchValue)

    # By index number
    # @staticmethod
    # def DeleteUser(index):
    #     UiActions.Click(pages.serverAdmin.GetUserByIndex(index))
    #     UiActions.Click(pages.serverAdmin.GetDelete())
    #     UiActions.Click(pages.serverAdmin.GetConfirmDelete())

    # By value - Best Practice
    @staticmethod
    @allure.step("Delete user from users table flows")
    def DeleteUser(By, value):
        if By == "user":
            UiActions.Click(pages.serverAdmin.GetUserByUserName(value))
        elif By == "index":
            UiActions.Click(pages.serverAdmin.GetUserByIndex(value))
        UiActions.Click(pages.serverAdmin.GetDelete())
        UiActions.Click(pages.serverAdmin.GetConfirmDelete())

    @staticmethod
    @allure.step("Go home grafana flow")
    def GetGrafanaHome(self):
        self.driver.get(GetData("URL"))
