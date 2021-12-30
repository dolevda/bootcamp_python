import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



def get_data(node_name):
    root = ET.parse("configuration.xml").getroot()
    return root.find(".//" + node_name).text


class Test_ExternalFiles:

    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/bmi/")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_external_files(self):
        driver.find_element(By.ID, "weight").send_keys(get_data("Weight"))
        driver.find_element(By.NAME, "height").send_keys(get_data("Height"))
        driver.find_element(By.ID, "calculate_data").click()
        expected_result = get_data("ExpectedResultBMI")
        actual_result = driver.find_element(By.ID, "bmi_result").get_attribute("value")
        assert expected_result == actual_result
