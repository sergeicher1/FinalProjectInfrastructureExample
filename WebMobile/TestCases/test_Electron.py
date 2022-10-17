# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Electron App Automation Test Cases
# Teacher     : Yoni Flenner
# Site        : [""]
# WebDriver   : Electron
# Version     : 3.141.0
# Teacher     : Yoni Flenner
# Application : ["To do List"]
# Device      : ""
# ----------------------------------------------------------------------------------------
import allure
import pytest

from WebMobile.Extensions.Verifications import Verifications
from WebMobile.WorkFlows.ElectronFlows import ElectronFlows


@pytest.mark.usefixtures("initElectronDriver")
class Test_Electron:

    def teardown_method(self):
        ElectronFlows.DeleteTaskFlow()  # To clear screen after each operation

    @allure.title("Test 01: Add and Verify New Task")
    @allure.description("This test adds a new task and verifies it in the list of tasks")
    def test_AddAndVerifyNewTask(self):
        ElectronFlows.AddNewTaskFlow("Learn JS")
        Verifications.VerifyEquals(ElectronFlows.GetNumberOfTasksFlow(), 1)

    @allure.title("Test 02: Add and verify New Tasks")
    @allure.description("This test adds a new tasks and verifies it in the list of tasks")
    def test_AddAndVerifyNewTasks(self):
        ElectronFlows.AddNewTaskFlow("Learn JS")
        ElectronFlows.AddNewTaskFlow("Learn Python")
        ElectronFlows.AddNewTaskFlow("Learn C#")
        Verifications.VerifyEquals(ElectronFlows.GetNumberOfTasksFlow(), 3)
