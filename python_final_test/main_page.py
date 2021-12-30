from selenium.webdriver.common.by import By


class frontPage:
    def __init__(self, driver):
        self.driver = driver

    def list_books(self):
        return self.driver.find_elements(By.XPATH, "//*[@ID='productList']/li")

    def search_line(self):
        return self.driver.find_element(By.ID, "searchBar")

    def list_java_books(self):
        return self.driver.find_elements(By.XPATH, "//ul//li[not(@class='ui-li-has-thumb ui-screen-hidden')]")

    def action_search(self, value):
        self.search_line().click()
        self.search_line().send_keys(value)

    def first_book(self):
        return self.driver.find_element(By.XPATH, "//*[@class='ui-li-has-thumb ui-first-child']/a/h2")

    def last_book(self):
        return self.driver.find_element(By.XPATH, "//*[@class='ui-li-has-thumb ui-last-child']/a/h2")

    def price_books(self):
        return self.driver.find_elements(By.XPATH, "//*[@ID='productList']/li/a/p[2]")

