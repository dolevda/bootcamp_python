from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Super_calc_1:

    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("http://juliemr.github.io/protractor-demo/")
        driver.set_page_load_timeout(10)
        # driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_multiplication_table(self):
        field_num1: WebElement = driver.find_element(By.XPATH, "//input[@ng-model='first']")
        operator = Select(driver.find_element(By.XPATH, "//select[@ng-model='operator']"))
        operator.select_by_value("MULTIPLICATION")
        field_num2: WebElement = driver.find_element(By.XPATH, "//input[@ng-model='second']")
        btn_go: WebElement = driver.find_element(By.ID, "gobutton")
        count = 3
        for i in range(1, count + 1):
            for j in range(1, count + 1):
                field_num1.send_keys(i)
                field_num2.send_keys(j)
                btn_go.click()
                WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.CLASS_NAME, "ng-binding"), str(i * j)))

        total_result = count * count
        for x in range(1, total_result + 1):
            print(driver.find_element(By.XPATH, "//tbody/tr[" + str(x) + "]/td[3]").text)
