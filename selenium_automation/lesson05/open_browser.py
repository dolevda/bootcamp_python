from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from webdriver_manager.microsoft import EdgeDriverManager
from selenium import webdriver

class Test_open_browsers:
    def test_drivers(self):
        global driver

        # # Open Chrome
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://www.google.co.il/")
        driver.quit()

        #Open Edge
        # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        # driver.get("http://www.google.com/")
        # driver.quit()

        # Open Firefox
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.google.co.il/")
        driver.quit()
