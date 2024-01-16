from selenium.webdriver.support.wait import WebDriverWait
from assertpy import assert_that, soft_assertions
from locators.locators import HomeLocator

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def goToHome(self):
         self.driver.get("https://emag.ro")
         self.driver.maximize_window()

    def verifyEmagLogo(self):
        logo = self.driver.find_element(*HomeLocator.logoEmag)
        with soft_assertions():
            assert_that(logo).is_true()

    def verifyEmagTitle(self):
        with soft_assertions():
            assert_that(self.driver.title).contains("eMAG.ro -")