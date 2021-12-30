import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setup_class(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '2269b6b83a0d7ece'
        self.dc['appPackage'] = 'com.example.android.apis'
        self.dc['appActivity'] = '.ApiDemos'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def teardown_class(self):
        self.driver.quit()

    def test_check_elements(self):
        list_elem = self.driver.find_elements(By.ID, "text1")
        assert len(list_elem) == 11

    # def test_size_content(self):
    #     elem_content = self.driver.find_element(By.XPATH, "//*[@text='Content']")
    #     print("x:", elem_content.rect["x"])
    #     print("y:", elem_content.rect["y"])
    #     print("width", elem_content.rect["width"])
    #     print("height", elem_content.rect["height"])

    def test_data_hour(self):
        print("activity:", self.driver.current_activity)
        print("date and hour:", self.driver.get_device_time())

    def test_is_install(self):
        print("is install: ", self.driver.is_app_installed("com.experitest.ExperiBank"))

    def test_is_portrait(self):
        if self.driver.orientation:
            print("portrait")
        else:
            print("Landscape")

    def test_screen_shot(self):
        self.driver.open_notifications()
        time.sleep(1)
        self.driver.save_screenshot("notification.png")
        self.driver.press_keycode(3)
        self.driver.save_screenshot("home.png")

    def test_check_lock(self):
        if self.driver.unlock():
            self.driver.lock()
        time.sleep(3)
        self.driver.unlock()

    def test_listView_times(self):
        source = self.driver.page_source
        assert source.count("ListView") == 4
