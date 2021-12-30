from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_Support:
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

    def test_verify_bmi(self):
        expected_result = "20"
        weight: WebElement = driver.find_element(By.ID, "weight").send_keys("55")
        height: WebElement = driver.find_element(By.ID, "hight").send_keys("167")
        calculate_btn: WebElement = driver.find_element(By.ID, "calculate_data").click()
        actual_result: WebElement = driver.find_element(By.ID, "bmi_result").get_attribute("value")
        assert actual_result == expected_result

    def test_2_verify(self):
        calculate: WebElement = driver.find_element(By.ID, "calculate_data")
        calculate_width = calculate.size["width"]
        print(calculate_width)
        calculate_height = calculate.size["height"]
        print(calculate_height)
        calculate_x = calculate.location["x"]
        print(calculate_x)
        calculate_y = calculate.location["y"]
        print(calculate_y)

        assert calculate.is_displayed()
        assert calculate.is_enabled()
        assert not calculate.is_selected()

        assert "input" == calculate.tag_name
        assert calculate.get_attribute("value") == "Calculate BMI"

        message: WebElement = driver.find_element(By.ID, "new_input")
        assert not message.is_displayed()





