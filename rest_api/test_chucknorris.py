import requests
import json


from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = "https://api.chucknorris.io/jokes"

class Test_Chucknorris:

    def test_print_categories(self):
        response = requests.get(url+"/categories")
        response_json = response.json()
        print(json.dumps(response_json, indent=4))

    def test_02(self):
        response = requests.get(url+"/search?query=Barack Obama")
        response_json = response.json()
        obama_num = response_json['total']
        response = requests.get(url+"/search?query=Charlie Sheen")
        response_json = response.json()
        sheen_num = response_json['total']
        if obama_num > sheen_num:
            print("obama")
        elif obama_num < sheen_num:
            print("sheen")
        else:
            print("equals")

    def test_03(self):
        for i in range(10):
            response = requests.get(url + "/random")
            response_json = response.json()
            with open('./chucknoris.txt', 'a') as f:
                json.dump(response_json['value'], f)
                f.write('\n')

    def test_04(self):
        response = requests.get(url + "/random")
        url_web = str(response.json()['url'])
        value = str(response.json()['value'])

        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(url_web)
        driver.implicitly_wait(5)
        try:
            assert driver.find_element(By.ID, 'content').text == value
        except Exception as e:
            print(e)
        finally:
            driver.quit()



