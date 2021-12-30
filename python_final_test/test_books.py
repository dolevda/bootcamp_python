import time

import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from python_final_test.main_page import frontPage


class Test_Dimension:
    @classmethod
    def setup_class(cls):
        global driver, front
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://automationbookstore.dev/")
        front = frontPage(driver)
        # action = ActionChains(driver)

    @classmethod
    def teardown_class(cls):
        driver.quit()

    @allure.title("number books")
    @allure.description("verify number of books is 8")
    def test_num_books(self):
        print("Num of books:", len(front.list_books()))
        assert len(front.list_books()) == 8

    @allure.title("number java books")
    @allure.description("verify number less then 8")
    def test_java_books(self):
        front.action_search("java")
        time.sleep(1)
        assert len(front.list_java_books()) < len(front.list_books())

    @allure.title("print first and last")
    @allure.description("print first and last books")
    def test_print_first_last(self):
        time.sleep(1)
        print("title first book:", front.first_book().text)
        print("title last book:", front.last_book().text)

    @allure.title("print books")
    @allure.description("Printing books from the cheapest to the most expensive")
    def test_print_books(self):
        list_price = front.price_books()
        prices = []
        j = 0
        for i in list_price:
            temp = float(i.text.replace("$", ""))
            prices.insert(j, i.text)
            j += 1

        prices.sort()
        for i in prices:
            print(i)









