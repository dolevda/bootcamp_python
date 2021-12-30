import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_Basic_Locator:

    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://www.selenium.dev/")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_locator_basic(self):
        logo_id: WebElement = driver.find_elements(By.ID, "Selenium_Logo")
        print(logo_id)
        logo_class: WebElement = driver.find_elements(By.CLASS_NAME, "navbar-logo")
        print(logo_class)
        logo_class_2: WebElement = driver.find_elements(By.CLASS_NAME, "navbar-brand")
        print(logo_class_2)
        logo_tag_name: WebElement = driver.find_elements(By.TAG_NAME, "svg"[0])
        print(logo_tag_name)

        links = driver.find_elements(By.TAG_NAME, "a")
        print("sum links", str(len(links)))
        link_contain_selenium: WebElement = driver.find_elements(By.PARTIAL_LINK_TEXT, "Selenium")
        print("Number of total links in page: " + str(len(links)))
        print("Number of links in page with word: Selenium is: " + str(len(link_contain_selenium)))


class Test_wiki:
    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://www.wikipedia.org/")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_locator_basic_2(self):
        search_filed: WebElement = driver.find_element(By.ID, "searchInput")
        search_language: WebElement = driver.find_element(By.ID, "searchLanguage")
        footer_sidebar_content: WebElement = driver.find_element(By.CLASS_NAME, "footer-sidebar-content")
        logo: WebElement = driver.find_element(By.CLASS_NAME, "central-featured-logo")
        wiki_elem = [search_filed, search_language, footer_sidebar_content,logo]
        for elem in wiki_elem:
            print(elem)

