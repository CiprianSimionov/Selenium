from assertpy import assert_that, soft_assertions

class AboutPage:
    def __init__(self, driver):
        self.driver = driver

    def goToAboutSection(self):
        self.driver.get("https://about.emag.ro/")  
        self.driver.maximize_window() 
        
    def verifyTitle(self):
        with soft_assertions():
            assert_that(self.driver.title).contains("Bine ai venit la eMAG")