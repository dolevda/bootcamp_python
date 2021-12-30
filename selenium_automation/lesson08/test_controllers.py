from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

first_name = "Dolev"
last_name = "Sigron"


class Test_Controllers:
    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_controllers.html")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_controller(self):
        field_first_name: WebElement = driver.find_element(By.NAME, "firstname").send_keys(first_name)
        field_last_name: WebElement = driver.find_element(By.NAME, "lastname").send_keys(last_name)
        my_continent: WebElement = Select(driver.find_element(By.ID, "continents"))
        my_continent.select_by_visible_text("South America")
        button_btn: WebElement = driver.find_element(By.ID, "submit").click()
        url = driver.current_url

        if first_name in url and last_name in url:
            print("Test pass")
        else:
            print("Test failed")

    def test_2_controller(self):
        field_first_name: WebElement = driver.find_element(By.NAME, "firstname").send_keys(first_name)
        field_last_name: WebElement = driver.find_element(By.NAME, "lastname").send_keys(last_name)
        my_continent = Select(driver.find_element(By.ID, "continents"))
        my_continent.select_by_visible_text("South America")
        button_btn: WebElement = driver.find_element(By.ID, "submit").click()
        gender: WebElement = driver.find_element(By.ID, "sex-1").click()
        years_of_experience: WebElement = driver.find_element(By.ID, "exp-1").click()
        profession: WebElement = driver.find_element(By.ID, "profession-1").click()
        select_file: WebElement = driver.find_element(By.ID, "photo").send_keys("C:/Users/dolev/Desktop/1.jpg")
        auto_tool: WebElement = driver.find_element(By.ID, "tool-2").click()
        selenium_commands = Select(driver.find_element(By.ID,"selenium_commands"))
        selenium_commands.select_by_visible_text("Navigation Commands")
        date_picker: WebElement = driver.find_element(By.ID, "datepicker").click()
        date_widget: WebElement = driver.find_element(By.ID, "ui-datepicker-div")
        columns = date_widget.find_elements(By.TAG_NAME, "td")
        for cell in columns:
            if cell.text == "13":
                cell.click()
                break


