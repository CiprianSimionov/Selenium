from selenium import webdriver
from pages.about_page import AboutPage as AP
import unittest

class ProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_aboutSection(self):
        aboutPage = AP(self.driver)
        aboutPage.goToAboutSection()
        aboutPage.verifyTitle()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()    