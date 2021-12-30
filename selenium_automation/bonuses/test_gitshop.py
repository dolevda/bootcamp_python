from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from smart_assertions import soft_assert, verify_expectations


class Test_Shop:
    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://thegithubshop.com/")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_hoodies(self):
        search_elem: WebElement = driver.find_element(By.XPATH, "//*[@class ='searchbox']/form/input")
        search_elem.send_keys("Hoodies")
        search_elem.send_keys(Keys.RETURN)

        clothes_elem = driver.find_elements(By.XPATH, "//*[@class='search__results']/div")
        assert len(clothes_elem) == 9

    def test_prices(self):
        prices_elem: WebElement = driver.find_elements(By.XPATH, "//*[@class='product-thumbnail__price__cost']")
        for i in prices_elem:
            price = i.text
            price = price.replace("$", "")
            soft_assert(float(price) > 10)
        verify_expectations()

    def test_quantity(self):
        driver.find_element(By.XPATH, "//*[@alt='Invertocat Hoodie']").click()
        quantity_elem: WebElement = driver.find_element(By.ID, "Quantity")
        value_quantity = quantity_elem.get_attribute("value")
        assert int(value_quantity) == 1

