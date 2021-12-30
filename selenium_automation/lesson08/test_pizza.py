from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def check_price():
    price: WebElement = driver.find_element(By.XPATH, "//*[@class='ginput_total ginput_total_5']")
    return price.text


class Test_Pizza:
    start_price = "$7.50"
    price_after_delivery= "$10.50"
    first_name = "Dolev"
    last_name = "Sigron"

    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/pizza/")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_verify_start_price(self):
        current_price = check_price()
        assert current_price == Test_Pizza.start_price

    def test_verify_price_after_entry_data(self):
        elen_first_name: WebElement = driver.find_element(By.XPATH, "//*[@id='input_5_22_3_container']/input")
        elen_first_name.send_keys(Test_Pizza.first_name)

        elen_last_name: WebElement = driver.find_element(By.XPATH, "//*[@id='input_5_22_6_container']/input")
        elen_last_name.send_keys(Test_Pizza.last_name)

        get_delivery = Select(driver.find_element(By.XPATH, "//*[@class='ginput_container']/select[@id='input_5_21']"))
        get_delivery.select_by_visible_text("Delivery +$3.00")

        current_price = check_price()
        assert current_price == Test_Pizza.price_after_delivery

    def test_iframe_alert(self):
        iframe: WebElement = driver.find_element(By.XPATH, "//iframe[@src='coupon.html']")
        driver.switch_to.frame(iframe)
        elem_coupon: WebElement = driver.find_element(By.XPATH, "//*[@id='coupon_Number']")
        num_coupon = elem_coupon.text
        driver.switch_to.default_content()

        elen_enter_coupon: WebElement = driver.find_element(By.XPATH, "//*[@id='field_5_20']/div/textarea")
        elen_enter_coupon.send_keys(num_coupon)
        submit_btb: WebElement = driver.find_element(By.ID, "gform_submit_button_5")
        submit_btb.click()

        popup = driver.switch_to.alert
        popup_text = popup.text
        popup.accept()
        expected_text = Test_Pizza.first_name + " " + Test_Pizza.last_name + " " + num_coupon
        print(expected_text)

        assert popup_text == expected_text
