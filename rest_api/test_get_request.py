import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Q1
# https://api.openweathermap.org/data/2.5/weather?q=Haifa&appid=8c2fc29f650ab651a5e1d332a46914ca

# units=metric:
# https://api.openweathermap.org/data/2.5/weather?q=Haifa&units=metric&appid=8c2fc29f650ab651a5e1d332a46914ca

# Q2
url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "8c2fc29f650ab651a5e1d332a46914ca";


class Test_ApiRequest:
    city = "Haifa, IL"
    params = dict(appid=api_key, q=city, units='metric')
    response = requests.get(url, params)

    def test_01(self):
        # response = requests.get(url, self.params)
        print(self.response)  # print status_code
        result = self.response.json()
        print(result)  # print all in the same row
        print(json.dumps(result, indent=4))  # print in json
        print(self.response.status_code)
        print("Data:", self.response.headers["date"])
        content_type = self.response.headers['Content-Type']
        assert content_type == 'application/json; charset=utf-8'

    def test_02(self):
        assert self.response.status_code == 200


# Q3

class Test_Rest_Assured:
    city = "Jerusalem,IL"
    params = dict(q=city, appid=api_key, units='metric')
    response = requests.get(url, params)
    response_json = response.json()

    def test_03(self):
        print(json.dumps(self.response_json, indent=4))
        assert self.response_json['sys']['country'] == 'IL'

    def test_04(self):
        humidity_api = self.response_json['main']['humidity']

        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get('https://openweathermap.org')
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='desktop-menu']/form/input[1]")))
            search_elem = driver.find_element(By.XPATH, "//*[@id='desktop-menu']/form/input[1]")
            search_elem.send_keys(self.city)
            search_elem.send_keys(Keys.RETURN)
            link_place = driver.find_element(By.LINK_TEXT, "Jerusalem, IL")
            link_place.click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@class="weather-items text-container orange-side standard-padding"]')))
            humidity_web = driver.find_element(By.XPATH,
                                               "//*[@class='weather-items text-container orange-side standard-padding']/li[3]").text
            humidity_web = humidity_web.split("\n")[1]
            print("humidity_web: ", humidity_web)
            humidity_api = str(humidity_api) + "%"
            print("humidity_api: ", humidity_api)
            assert humidity_web == humidity_api
        except Exception as e:
            print("Error:", e)
        finally:
            driver.quit()
