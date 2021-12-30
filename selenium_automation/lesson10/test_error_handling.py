import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


class Test_ErrorHandler:
    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_01(self):
        remove_btm: WebElement = driver.find_element(By.ID, "btn")
        remove_btm.click()
        time.sleep(5)
        try:
            checkbox_elem: WebElement = driver.find_element(By.ID, "checkbox")
            checkbox_elem.is_displayed()
        except(Exception):
            print("WebDriver could not find the element but nevertheless test did not fail")
        finally:
            print("test is finished !")

    def test_02(self):
        remove_btm: WebElement = driver.find_element(By.ID, "btn")
        remove_btm.click()
        time.sleep(5)
        if len(driver.find_elements(By.ID, "checkbox")) > 0:
            print("Element exists on screen")
        else:
            print("Element does NOT exist on screen")
