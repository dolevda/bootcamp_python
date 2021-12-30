from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

import csv


class Test_W3:
    @classmethod
    def setup_class(cls):
        global driver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
        driver.get("https://www.w3schools.com/html/html_tables.asp")

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_rows_columns(self):
        table_elem: WebElement = driver.find_element(By.ID, "customers")
        num_rows = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr")
        print("num of row:", len(num_rows))
        num_cols = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr/th")
        print("num of columns:", len(num_cols))

    def test_europe_company(self):
        europe = ['Germany', 'Italy', 'UK', 'Austria']
        europe_company_list = []
        cols_country = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr/td[3]")
        cols_company = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr/td[1]")
        for i in range(int(len(cols_company))):
            if cols_country[i].text in europe:
                europe_company_list.append(cols_company[i].text)

        for i in range(int(len(europe_company_list))):
            print(europe_company_list[i])

    def test_write_csv(self):
        headline = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr/th")
        rows_elem = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr")
        temp = []
        titles = []


        f = open('C:/Users/dolev/PycharmProjects/test_automation/selenium_automation/bonuses/w3.csv', 'w')

        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        for i in range(len(headline)):
            titles.append(headline[i].text)

        # write a row to the csv file
        writer.writerow(titles)

        for i in rows_elem[1:]:
            data = []
            temp = i.find_elements(By.TAG_NAME, "td")
            for j in range(len(temp)):
                data.append(temp[j].text)

            writer.writerow(data)

        # close the file
        f.close()


