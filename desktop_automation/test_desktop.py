import result as result
from appium import webdriver
from selenium.webdriver.common.by import By


class Test_Desktop:
    def setup_class(self):
        global driver
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        desired_caps["platformName"] = "Windows"
        desired_caps["deviceName"] = "WindowsPC"
        driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
        driver.implicitly_wait(5)

    def teardown_class(self):
        driver.quit()

    def test_multiplication(self):
        driver.find_element_by_name("Five").click()
        driver.find_element_by_name("Multiply by").click()
        driver.find_element_by_name("Five").click()
        driver.find_element_by_name("Equals").click()

        result = driver.find_element(By.XPATH, "//*[@AutomationId='CalculatorResults']").text
        res = int(result.replace("Display is ", ""))
        assert res == 25