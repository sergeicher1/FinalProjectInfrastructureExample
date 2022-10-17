# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : API Actions
# Teacher     : Yoni Flenner
# Site        : ["http://localhost:3000/"]
# ----------------------------------------------------------------------------------------
import allure
import requests
from requests.auth import HTTPBasicAuth

header = {"Content-type": "application/json"}


class APIActions:

    @staticmethod
    @allure.step("Get Request")
    def Get(path, user, password):
        response = requests.get(path, auth=HTTPBasicAuth(user, password))
        return response

    @staticmethod
    @allure.step("Extract value from response")
    def ExtractValueFromResponse(response, nodes):
        extractedValue = None
        rJSON = response.json()
        if len(nodes) == 1:
            extractedValue = rJSON[nodes[0]]
        elif len(nodes) == 2:
            extractedValue = rJSON[(nodes[0])][(nodes[1])]
        elif len(nodes) == 3:
            extractedValue = rJSON[(nodes[0])][(nodes[1])][(nodes[2])]
        return extractedValue

    @staticmethod
    @allure.step("Post Request")
    def Post(path, payload, user, password):
        response = requests.post(path, json=payload, headers=header, auth=HTTPBasicAuth(user, password))
        return response.status_code

    @staticmethod
    @allure.step("Put Request")
    def Put(path, payload, user, password):
        response = requests.put(path, json=payload, headers=header, auth=HTTPBasicAuth(user, password))
        return response.status_code

    @staticmethod
    @allure.step("Delete Request")
    def Delete(path, user, password):
        response = requests.delete(path, auth=HTTPBasicAuth(user, password))
        return response.status_code
