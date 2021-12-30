from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from smart_assertions import soft_assert, verify_expectations


class Test_Assert_Verifications:
    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("http://loudev.com/")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_1(self):
        support = Support()
        support.verify_elements(driver)


class Support:
    def verify_elements(self, driver):
        index = 2
        expected = 'elem '
        list_elen = driver.find_elements(By.XPATH, "//div[@id='ms-aloha']/div[1]/ul/li")
        for elem in list_elen:
            index += 1
            if "ms-selected" not in elem.get_attribute("class"):
                text_elem = elem.find_element_by_tag_name("span").text
                num = int(text_elem.replace("elem ", ""))
                soft_assert(num >= 3, "num elem less then 3")
            verify_expectations()
