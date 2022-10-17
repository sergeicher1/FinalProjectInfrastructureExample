# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : DataBase Web Test
# Teacher     : Yoni Flenner
# Site        : [""]
# Server        : ["grafana 9"]
# ----------------------------------------------------------------------------------------
import allure
import pytest

from WebMobile.Extensions.Verifications import Verifications
from WebMobile.WorkFlows.DbFlows import DbFlows
from WebMobile.WorkFlows.WebFlows import WebFlows


@pytest.mark.usefixtures("initWebDriver")
@pytest.mark.usefixtures("initDBConnection")
class Test_WebViaDataBase:

    @allure.title("Test 01: Login to Grafana VIA DB")
    @allure.description("This test verify Login flow using data from Database")
    def test_VerifyLoginViaDb(self):
        DbFlows.LoginGrafanaViaDB()
        WebFlows.VerifyGrafanaTitle("Welcome to Grafana")
