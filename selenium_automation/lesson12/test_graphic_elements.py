from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

eyes = Eyes()


class Test_Graphic:
    @classmethod
    def setup_class(cls):
        global driver
        # driver_service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=driver_service)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://applitools.com/helloworld/")
        driver.implicitly_wait(5)
        eyes.api_key = "nJSg2fuWMmiR109UrA3N68EaRSP1QFesIHrbyRD1049Xh3s110"

    @classmethod
    def teardown_class(cls):
        eyes.close()
        driver.quit()
        eyes.abort()

    def test_01(self):
        eyes.open(driver, "Hello world", "My first selenium test ")
        eyes.check_window('First Screen Shot')
        # driver.find_element(By.link_text, "?diff1").click()
        driver.find_element_by_link_text("?diff1").click()
        eyes.check_window("After click: ?diff1")
        # driver.find_element(By.link_text, "?diff2").click()
        driver.find_element_by_link_text("?diff2").click()
        eyes.check_window("After click: ?diff2")
        driver.find_element(By.XPATH, "//button").click()
        eyes.check_window("After click: button click")


