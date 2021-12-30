from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def txt_occupation(self):
        return self.driver.find_element(By.ID, "occupation")

    def txt_age(self):
        return self.driver.find_element(By.ID, "age")

    def txt_location(self):
        return self.driver.find_element(By.ID, "location")

    def clickme_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@value='Click Me']")

    def action(self, occupation, age, location):
        self.txt_occupation().send_keys(occupation)
        self.txt_age().send_keys(age)
        self.txt_location().send_keys(location)
        self.clickme_btn().click()

