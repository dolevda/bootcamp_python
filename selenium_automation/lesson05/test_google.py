from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Google:
    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://www.google.co.il/")



    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_verify_google(self):
        driver.get("https://www.bing.com/")
        driver.back()
        print(driver.title)
        source = driver.page_source
        word = "bubble"
        if word in source:
            print("Bubble in source page")
        else:
            print("Bubble isn't in source page")
