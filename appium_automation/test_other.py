import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Test_Other:
    reportDirectory = 'C:/Users/dolev/PycharmProjects/test_automation/appium_automation/appium_reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'report.html'
    driver = None

    def setup_class(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '2269b6b83a0d7ece'
        self.dc['appPackage'] = 'com.experitest.ExperiBank'
        self.dc['appActivity'] = '.LoginActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)


    def test_01_cool_stuff(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "usernameTextField").send_keys('company')
        self.driver.find_element(By.ID, "passwordTextField").send_keys('company')
        self.driver.find_element(By.ID, "loginButton").click()
        self.driver.find_element(By.ID, "logoutButton").click()



    def teardown_class(self):
        self.driver.quit()


