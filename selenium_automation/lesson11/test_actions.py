import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement


class Test_Actions:

    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_actions.html")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_drag_and_drop(self):
        drag_elem: WebElement = driver.find_element(By.ID, "draggable")
        drop_elem: WebElement = driver.find_element(By.ID, "droppable")
        action = ActionChains(driver)
        action.drag_and_drop(drag_elem, drop_elem).perform()

    def test_select_elem3(self):
        list_elem: WebElement = driver.find_elements(By.XPATH, "//*[@id='select_items']/li")
        action = ActionChains(driver)
        action.click_and_hold(list_elem[1]).click_and_hold(list_elem[2]).perform()

    def test_double_click(self):
        dbl_elem: WebElement = driver.find_element(By.ID, "dbl_click")
        action = ActionChains(driver)
        action.double_click(dbl_elem).perform()
        hide_text = driver.find_element(By.ID, "demo").text

        assert hide_text == 'Hello World'

    def test_mouse_hover(self):
        mouse_over_elem: WebElement = driver.find_element(By.ID, "mouse_hover")
        action = ActionChains(driver)
        action.move_to_element(mouse_over_elem).perform()
        # text = "background-color: rgb(255, 255, 0);"
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//span[@style='background-color: rgb(255, 255, 0);']").is_displayed()

    def test_scrolled(self):
        driver.execute_script("scrollTo(0,1000);")
        scrolled_elem: WebElement = driver.find_element(By.ID, "scrolled_element")
        exp_result = "This Element is Shown When Scrolled"
        assert exp_result == scrolled_elem.text



