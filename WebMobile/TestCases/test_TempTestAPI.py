# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : GET PUT POST DELETE Request Test Grafana API
# Teacher     : Yoni Flenner
# Site        : ["http://localhost:3000/"]
# ----------------------------------------------------------------------------------------
import json

import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:3000/"
resources = "api/teams"
user = password = "admin"
basic = HTTPBasicAuth(user, password)

header = {"Content-type": "application/json"}


class Test_Temporary:
    @staticmethod
    def test_01CreateTeam():
        payload = {
            "name": "Sergei Team",
            "email": "test@gmail.com",
            "orgId": 3
        }
        response = requests.post(url + resources, json=payload, headers=header, auth=basic)
        print("response: ", response)
        rJSON = response.json()
        print("rJSON: ", rJSON)
        print("json.dumps: ", json.dumps(rJSON, indent=2))
        assert response.status_code == 200

    def test_02GetTeams(self):
        response = requests.get(url + resources + "/search", auth=basic)
        print("response: ", response)
        rJSON = response.json()
        print("rJSON: ", rJSON)
        print("json.dumps: ", json.dumps(rJSON, indent=2))
        myTeamID = rJSON["teams"][0]["id"]
        print("myTeamID: ", myTeamID)
        assert myTeamID == 3
