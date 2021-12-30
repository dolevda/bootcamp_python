import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement


class Test_Allure_Report:

    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    @allure.title("login flow")
    @allure.description("Test login")
    def test_verify_login(self):
        try:
            self.step_login()
            self.verify_login()
        except Exception as e:
            self.attach_image()
            pytest.fail("Test failed, see details: ", e)

    @allure.step("login action")
    def step_login(self):
        item_email: WebElement = driver.find_element(By.ID, "Email")
        item_email.clear()
        item_email.send_keys("admin@yourstore.com")
        item_pass: WebElement = driver.find_element(By.ID, "Password")
        item_pass.clear()
        item_pass.send_keys("admin")
        driver.find_element(By.XPATH, "//button").click()

    @allure.step("verify title")
    def verify_login(self):
        assert driver.find_element(By.CLASS_NAME, "content-header").is_displayed()

    def attach_image(self):
        image = "C:/Users/dolev/PycharmProjects/test_automation/selenium_automation/screen-shot/screen.png"
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
