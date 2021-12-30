import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Test_Synchronization:
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

    def test_excplicitlywait(self):
        driver.find_element(By.ID, "rendered").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "finish2")))
        output = driver.find_element(By.ID, "finish2").text
        assert output == "My Rendered Element After Fact!"

    def test_sleep(self):
        driver.find_element(By.ID, "hidden").click()
        time.sleep(2)
        driver.find_element(By.ID, "loading1").is_displayed()

    def test_implicitlywait(self):
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "checkbox").is_displayed()
        driver.find_element(By.ID, "btn").click()
        driver.find_element(By.ID, "message").is_displayed()

