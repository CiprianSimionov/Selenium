import sys
sys.path.append("D:/stuff/udemy/github/selenium/emag_tests")

from selenium import webdriver
import unittest
from pages.login_page import LoginPage as LP

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()

    def test_login(self):
        loginPage = LP(self.driver)
        loginPage.GoToLogin()
        loginPage.setUsername("linkedInUser@mail.com")
        loginPage.setPassword("userLinkedIn")
        loginPage.clickSubmit()
        loginPage.verifyMeSection()


    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()