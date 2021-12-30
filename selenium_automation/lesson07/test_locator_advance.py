from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


class Test_Locator_Advance:
    @classmethod
    def setup_class(cls):
        global driver
        driver_device = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_device)
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_locators.html")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_verify_locators_advanced(self):
        locator_1: WebElement = driver.find_element(By.ID, "locator_id")
        locator_2: WebElement = driver.find_element(By.NAME, "locator_name")
        locator_3: WebElement = driver.find_element(By.TAG_NAME, "p")
        locator_4: WebElement = driver.find_element(By.CLASS_NAME, "locator_class")
        locator_5: WebElement = driver.find_element(By.PARTIAL_LINK_TEXT, "myLocator(5)")
        locator_6: WebElement = driver.find_element(By.LINK_TEXT, "Find my locator (6)")
        locator_7: WebElement = driver.find_element(By.CSS_SELECTOR, "input[myname='selenium']")
        locator_8: WebElement = driver.find_element(By.XPATH, "//*[@class='btn btn-2'][2]")

        print(locator_1)
        print(locator_2)
        print(locator_3)
        print(locator_4)
        print(locator_5)
        print(locator_6)
        print(locator_7)
        print(locator_8)

        print(locator_1.text)
        print(locator_2.text)
        print(locator_3.text)
        print(locator_4.text)
        print(locator_5.text)
        print(locator_6.text)
        print(locator_7.get_attribute("value"))
        print(locator_8.text)
