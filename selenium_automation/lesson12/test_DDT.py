import pytest
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
        driver.get("https://en.wikipedia.org/wiki/Wikipedia")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    @pytest.mark.parametrize(
        "search_value, expected_heading",
        [
            ("Israel", "Israel"),
            ("Automation", "Automation"),
            ("BlahBlah", "Search results")
        ]
    )
    def test_ddt(self, search_value, expected_heading):
        filed_search: WebElement = driver.find_element(By.XPATH, "//*[@id = 'simpleSearch']//input")
        filed_search.send_keys(search_value)
        search_btn: WebElement = driver.find_element(By.ID, "searchButton")
        search_btn.click()
        title_search: WebElement = driver.find_element(By.ID, "firstHeading")
        assert title_search.text == expected_heading
        # driver.get("http://wikipedia.org/")