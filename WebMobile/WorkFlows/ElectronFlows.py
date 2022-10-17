# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Electron App Automation Work Flow
# Teacher     : Yoni Flenner
# Site        : [""]
# WebDriver   : Electron
# Version     : 3.141.0
# Teacher     : Yoni Flenner
# Application : ["To do List"]
# Device      : ""
# ----------------------------------------------------------------------------------------


from time import sleep

import allure
from selenium.webdriver.common.keys import Keys

from WebMobile.Extensions.UiActions import UiActions
import WebMobile.Utilities.ManagePages as pages


class ElectronFlows:

    @staticmethod
    @allure.step("Add new task flow")
    def AddNewTaskFlow(taskName):
        UiActions.UpdateText(pages.electronTask.GetCreate(), taskName)
        UiActions.UpdateText(pages.electronTask.GetCreate(), Keys.RETURN)

    @staticmethod
    @allure.step("Return number of tasks")
    def GetNumberOfTasksFlow():
        return len(pages.electronTask.GetTasks())

    @staticmethod
    @allure.step("Delete task from list")
    def DeleteTaskFlow():
        for i in range(ElectronFlows.GetNumberOfTasksFlow()):
            sleep(0.5)
            UiActions.MouseHoverTooltip(pages.electronTask.GetDeleteBtns()[0])
