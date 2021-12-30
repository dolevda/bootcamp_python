from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_SwitchNavigation:
    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_switch_navigation.html")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_verify_alert(self):
        driver.find_element(By.ID, "btnAlert").click()
        alert = driver.switch_to.alert
        output_alert = alert.text
        alert.accept()
        print(output_alert)
        output = driver.find_element(By.ID, "output").text
        assert output == "Alert is gone."

    def test_verify_prompt(self):
        driver.find_element(By.ID, "btnPrompt").click()
        alert = driver.switch_to.alert
        alert.send_keys("Dolev")
        output_alert = alert.text
        alert.accept()
        print(output_alert)
        output = driver.find_element(By.ID, "output").text
        assert output == "Dolev"

    def test_verify_confirmed(self):
        driver.find_element(By.ID, "btnConfirm").click()
        alert = driver.switch_to.alert
        output_alert = alert.text
        alert.accept()
        print(output_alert)
        output = driver.find_element(By.ID, "output").text
        assert output == "Confirmed."

    def test_verify_iframe(self):
        iframe = driver.find_element(By.XPATH, "//iframe[@src='ex_switch_newFrame.html']")
        driver.switch_to.frame(iframe)
        elem_text_iframe = driver.find_element(By.ID, "iframe_container")
        output = elem_text_iframe.text
        driver.switch_to.default_content()
        assert output == "This is an IFrame !"

    def test_verify_tab(self):
        win_handle_main = driver.current_window_handle
        driver.find_element(By.ID, "btnNewTab").click()
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        output_tab = driver.find_element(By.ID, "new_tab_container").text
        driver.close()
        driver.switch_to.window(win_handle_main)
        assert output_tab == "This is a new tab"


    def test_verify_win(self):
        win_handle_main = driver.current_window_handle
        driver.find_element(By.XPATH, "//*[@id='contact_info_left']/a").click()
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        output_tab = driver.find_element(By.ID, "new_window_container").text
        driver.close()
        driver.switch_to.window(win_handle_main)
        assert output_tab == "This is a new window"




