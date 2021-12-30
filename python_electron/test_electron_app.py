import time
from selenium import webdriver
from selenium.webdriver.common.by import By


electron_app = 'C:/Automation/Electron API Demos-win32-ia32/Electron API Demos.exe'
edriver = 'C:/Automation/electrondriver-v3.1.2-win32-x64/electrondriver.exe'

expected_menu_size = 6

class Test_Electron:
    def setup_class(self):
        options = webdriver.ChromeOptions()
        options.binary_location = electron_app
        global driver
        driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
        driver.implicitly_wait(5)

    def test_01_electron(self):
        category = driver.find_elements(By.CLASS_NAME, "nav-category")
        assert len(category) == 6


    def teardown_class(self):
        driver.quit()



