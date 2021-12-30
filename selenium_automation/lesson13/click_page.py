from selenium.webdriver.common.by import By


class ClickPage:
    def __init__(self, driver):
        self.driver = driver

    def btn_click(self):
        return self.driver.find_element(By.XPATH, "//*[@type=button]")

    def action_is_displayed(self):
        return self.btn_click().is_displayed()
