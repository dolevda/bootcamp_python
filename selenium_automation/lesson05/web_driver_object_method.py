import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_WebDriverObjectMethods:

    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://www.imdb.com/")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_verify_imdb(self):
        driver.refresh()
        title = driver.title
        expected_result_title = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"
        print(title)
        if title == expected_result_title:
            print("Title Passed")
        else:
            print("Title Failed")

        url = driver.current_url
        expected_result_url = "https://www.imdb.com/"
        print(url)
        print(expected_result_url)
        if url == expected_result_url:
            print("Url Passed")
        else:
            print("Url Failed")





