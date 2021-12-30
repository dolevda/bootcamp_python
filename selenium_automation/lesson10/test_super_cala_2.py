from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_DDT:

    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_sum(self):
        iframe = driver.find_element(By.XPATH, "//*[@id='homepage-generator']/iframe")
        driver.switch_to.frame(iframe)
        gender_elem = driver.find_element(By.XPATH, "//input[@type='button']")
        gender_elem.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//center/span")))
        rand_num = int(driver.find_element(By.XPATH, "//center/span").text)
        sum_total = 0

        for i in range(rand_num-1, 0, -1):
            sum_total = sum_total + rand_num*i

        print("The random num is:",  rand_num)
        print("The total sum is:", sum_total)







