# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : DataBase Flows
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------
import allure

from WebMobile.Extensions.DbActions import DbActions
from WebMobile.WorkFlows.WebFlows import WebFlows


class DbFlows:

    @staticmethod
    @allure.step("Login to Grafana via DataBase Flow")
    def LoginGrafanaViaDB():
        columns = ["name", "password"]
        result = DbActions.GetQueryResult(columns, "Employees", "comments", "correct")
        WebFlows.LoginFlow(result[0][0], result[0][1])  # 2 items, because we call user and password only
