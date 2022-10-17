# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : DataBase Actions
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------
import allure
from WebMobile.TestCases import conftest


class DbActions:

    @staticmethod
    @allure.step("Query builder")
    # Example: "SELECT user, password FROM Employees WHERE comments='correct'"
    def QueryBuilder(columns, table, whereName, whereValue):
        cols = ",".join(columns)
        query = "SELECT " + cols + " FROM " + table + " WHERE " + whereName + " = " + "'" + whereValue + "'"
        return query

    @staticmethod
    @allure.step("Get Query Result")
    def GetQueryResult(columns, table, whereName, whereValue):
        query = DbActions.QueryBuilder(columns, table, whereName, whereValue)
        dbCursor = conftest.dbConnector.cursor()
        dbCursor.execute(query)
        result = dbCursor.fetchall()
        return result  # Returns List of Tuples
