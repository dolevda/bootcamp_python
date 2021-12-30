import time

from selenium.webdriver.common.by import By


class loginPage:

    def __init__(self, driver):
        self.driver = driver

    def txt_user(self):
        return self.driver.find_element(By.XPATH, "//*[@name='username2']")

    def txt_pass(self):
        return self.driver.find_element(By.XPATH, "//*[@name='password2']")

    def bth_login(self):
        return self.driver.find_element(By.ID, "submit")

    def action(self, user, password):
        self.txt_user().send_keys(user)
        self.txt_pass().send_keys(password)
        self.bth_login().click()


