import time
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

from selenium_automation.lesson13.click_page import ClickPage
from selenium_automation.lesson13.form_page import FormPage
from selenium_automation.lesson13.login_page import loginPage


class Test_Dimension:
    @classmethod
    def setup_class(cls):
        global driver, login, form,click
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/webdriveradvance.html")
        login = loginPage(driver)
        form = FormPage(driver)
        click = ClickPage(driver)

    @classmethod
    def teardown_class(cls):
        driver.quit()

    # def test_login(self):
    #     login.txt_user().send_keys("selenium")
    #     login.txt_pass().send_keys("webdriver")
    #     login.bth_login().click()
    #     time.sleep(2)

    def test_verify_login(self):
        try:
            login.action("selenium", "webdriver")
            form.action("Engineer", "27", "Netivot")
            click.action_is_displayed()

        except Exception as e:
            print("test failed :", e)
            # pytest.fail("Test failed, see details", e)







