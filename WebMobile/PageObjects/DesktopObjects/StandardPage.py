# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Standard Calculator Page
# Teacher     : Yoni Flenner
# Site        : [""]
# WebDriver   : Appium
# Version     : 3.141.0
# Teacher     : Yoni Flenner
# Application : ["Calculator"]
# Device      : Windows
# ----------------------------------------------------------------------------------------


from selenium.webdriver.common.by import By

zero = (By.NAME, "Zero")
one = (By.NAME, "One")
two = (By.NAME, "Two")
three = (By.NAME, "Three")
four = (By.NAME, "Four")
five = (By.NAME, "Five")
six = (By.NAME, "Six")
seven = (By.NAME, "Seven")
eight = (By.NAME, "Eight")
nine = (By.NAME, "Nine")
plus = (By.NAME, "Plus")
minus = (By.NAME, "Minus")
mul = (By.NAME, "Multiply by")
div = (By.NAME, "Divide by")
equals = (By.NAME, "Equals")
result = (By.XPATH, "//*[@AutomationId='CalculatorResults']")
clear = (By.NAME, "Clear")


class StandardPage:

    def __init__(self, driver):
        self.driver = driver

    def GetZero(self):
        return self.driver.find_element(zero[0], zero[1])

    def GetOne(self):
        return self.driver.find_element(one[0], one[1])

    def GetTwo(self):
        return self.driver.find_element(two[0], two[1])

    def GetThree(self):
        return self.driver.find_element(three[0], three[1])

    def GetFour(self):
        return self.driver.find_element(four[0], four[1])

    def GetFive(self):
        return self.driver.find_element(five[0], five[1])

    def GetSix(self):
        return self.driver.find_element(six[0], six[1])

    def GetSeven(self):
        return self.driver.find_element(seven[0], seven[1])

    def GetEight(self):
        return self.driver.find_element(eight[0], eight[1])

    def GetNine(self):
        return self.driver.find_element(nine[0], nine[1])

    def GetPlus(self):
        return self.driver.find_element(plus[0], plus[1])

    def GetMinus(self):
        return self.driver.find_element(minus[0], minus[1])

    def GetMultiply(self):
        return self.driver.find_element(mul[0], mul[1])

    def GetDivide(self):
        return self.driver.find_element(div[0], div[1])

    def GetEquals(self):
        return self.driver.find_element(equals[0], equals[1])

    def GetResult(self):
        return self.driver.find_element(result[0], result[1])

    def GetClear(self):
        return self.driver.find_element(clear[0], clear[1])
