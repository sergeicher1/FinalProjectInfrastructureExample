# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : API Flows
# Teacher     : Yoni Flenner
# Site        : ["http://localhost:3000/"]
# ----------------------------------------------------------------------------------------
import allure

from WebMobile.Extensions.ApiActions import APIActions
from WebMobile.Utilities.CommonOps import GetData

url = GetData("URLAPI")
resources = "api/teams/"
user = GetData("UserName")
password = GetData("Password")


class ApiFlows:

    @staticmethod
    @allure.step("Get Value from grafana api flow")
    def GetValueFromAPI(nodes):
        response = APIActions.Get(url + "api/teams/search", user, password)
        return APIActions.ExtractValueFromResponse(response, nodes)

    @staticmethod
    @allure.step("Create New Team")
    def CreateNewTeam(name, email, orgID):
        payload = {"name": name, "email": email, "orgId": orgID}
        statusCode = APIActions.Post(url + resources, payload, user, password)
        return statusCode

    @staticmethod
    @allure.step("Update Team Flow")
    def UpdateTeam(name, email, orgID, id):
        payload = {"name": name, "email": email, "orgId": orgID}
        statusCode = APIActions.Put(url + resources + str(id), payload, user, password)
        return statusCode

    @staticmethod
    @allure.step("Delete Team")
    def DeleteTeam(id):
        statusCode = APIActions.Delete(url + resources + str(id), user, password)
        return statusCode
