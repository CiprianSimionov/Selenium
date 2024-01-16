from selenium import webdriver
from pages.home_page import HomePage as HP
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_EmagLogo(self):
        homePage = HP(self.driver)
        homePage.goToHome()
        homePage.verifyEmagLogo()

    def test_EmagTitle(self):
        homePage = HP(self.driver)
        homePage.goToHome()
        homePage.verifyEmagTitle()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()    