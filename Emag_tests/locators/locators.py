from selenium.webdriver.common.by import By

class LoginLocator:
    username=(By.ID,"session_key")
    password=(By.ID,"session_password")
    submit=(By.XPATH,"//*[@id='main-content']/section[1]/div/div/form/div[2]/button")
    areaAfterLogin=(By.ID, "ember14")

class HomeLocator:
    logoEmag = (By.CSS_SELECTOR, ".navbar-brand > img")