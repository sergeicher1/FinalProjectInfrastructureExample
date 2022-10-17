# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : API Test Cases
# Teacher     : Yoni Flenner
# Site        : ["http://localhost:3000/"]
# Server        : ["grafana 9"]
# ----------------------------------------------------------------------------------------
import allure

from WebMobile.Extensions.ApiActions import APIActions
from WebMobile.Extensions.Verifications import Verifications
from WebMobile.WorkFlows.ApiFlows import ApiFlows

teamName = "Sergei"
teamEmail = "sergei@gmail.com"
orgId = "3"


class Test_API:

    @allure.title("Test 01 Create team and verify status code")
    @allure.description("This test creates new team and verifies status code")
    def test_CreateAndVerify(self):
        actualCode = ApiFlows.CreateNewTeam(teamName, teamEmail, orgId)
        Verifications.VerifyEquals(actualCode, 200)

    @allure.title("Test 02 Verify team name")
    @allure.description("This test verifies team member name")
    def test_VerifyTeamMemberName(self):
        nodes = ["teams", 0, "name"]
        actual = ApiFlows.GetValueFromAPI(nodes)
        Verifications.VerifyEquals(actual, teamName)

    @allure.step("Test 03 Update team & Verify status code")
    @allure.description("This test updates team & Verifies status code")
    def test_UpdateAndVerifyTeamName(self):
        nodes = ["teams", 0, "id"]
        id = ApiFlows.GetValueFromAPI(nodes)
        actual = ApiFlows.UpdateTeam(teamName + " Chernyahovsky", teamEmail, orgId, id)
        Verifications.VerifyEquals(actual, 200)

    @allure.step("Test 04 Verify team name")
    @allure.description("This test verifies team member name")
    def test_VerifyTeamUpdatedName(self):
        nodes = ["teams", 0, "name"]
        actual = ApiFlows.GetValueFromAPI(nodes)
        Verifications.VerifyEquals(actual, teamName + " Chernyahovsky")

    @allure.step("Test 05 Delete team And Verify status code")
    @allure.description("This test deletes team and verifies status code")
    def test_DeleteTeamAndVerifyStatusCode(self):
        nodes = ["teams", 0, "id"]
        id = ApiFlows.GetValueFromAPI(nodes)
        actual = ApiFlows.DeleteTeam(id)
        Verifications.VerifyEquals(actual, 200)
