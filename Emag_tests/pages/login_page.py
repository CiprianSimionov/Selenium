from assertpy import soft_assertions, assert_that
from locators.locators import LoginLocator

class LoginPage():
    def __init__(self, driver):
        self.driver=driver

    def GoToLogin(self):
        self.driver.get("https://www.linkedin.com")

    def setUsername(self,userVal):  
        username= self.driver.find_element(*LoginLocator.username)
        username.clear()
        username.send_keys(userVal) 
    
    def setPassword(self,passVal):  
        password= self.driver.find_element(*LoginLocator.password)
        password.clear()
        password.send_keys(passVal)

    def clickSubmit(self):
        submitButton= self.driver.find_element(*LoginLocator.submit)
        submitButton.click()

    def verifyMeSection(self):
        about=self.driver.find_element(*LoginLocator.areaAfterLogin)
        with soft_assertions():
           assert_that(about).is_true()
