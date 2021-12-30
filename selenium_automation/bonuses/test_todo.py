import time

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class Todos_Methods:

    def setup_class(self):
        global driver, action
        # driver_service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=driver_service)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://todomvc.com/examples/react/#/")
        action = ActionChains(driver)

        self.create_item("clean the house")
        self.create_item("Go to the supermarket")
        self.create_item("Cook lunch")
        time.sleep(3)

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def list_items(self):
        list_elem = driver.find_elements(By.XPATH, "//ul[@class='todo-list']//li")
        return list_elem

    @staticmethod
    def create_item(task):
        task_filed: WebElement = driver.find_element(By.XPATH, "//*[@class='new-todo']")
        task_filed.send_keys(task)
        task_filed.send_keys(Keys.RETURN)

    def delete_task(self, index):
        element_to_delete = self.list_items()[index]
        delete_button = element_to_delete.find_element(By.TAG_NAME, "button")
        action.move_to_element(element_to_delete).move_to_element(delete_button).click().perform()

    def edit_task(self, index, edit_task):
        task_to_edit = self.list_items()[index]
        print(task_to_edit)
        action.double_click(task_to_edit)
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        time.sleep(2)
        action.send_keys(edit_task, Keys.RETURN).perform()

    def filter_completed(self):
        driver.find_element(By.LINK_TEXT, "Completed").click()

    def get_completed_tasks_count(self):
        count = 0
        for i in self.list_items():
            if i.get_attribute("class") == "completed":
                count += 1
        return count


    def toggle_task(self, index):
        task_to_toggle = self.list_items()[index].find_element(By.XPATH, "//input[@class='toggle']")
        task_to_toggle.click()

    def filter_completed(self):
        driver.find_element(By.LINK_TEXT, "Completed").click()

    def filter_active(self):
        driver.find_element(By.LINK_TEXT, "Active").click()

    def filter_all(self):
        driver.find_element(By.LINK_TEXT, "All").click()

    def clear_completed(self):
        driver.find_element(By.XPATH, "//button[@class='clear-completed']").click()

class Test_Todos(Todos_Methods):
    @allure.title("crest tasks")
    @allure.description("verify that the takes is created")
    def test_num_todos(self):
        expected_num_todos = len(self.list_items())
        # self.create_item("Test task 4")
        time.sleep(2)
        assert expected_num_todos == 3

    @allure.title("Delete task")
    @allure.description("Verify task deleted")
    def test_delete_todos(self):
        self.delete_task(2)
        expected_tasks_after_delete = len(self.list_items())
        time.sleep(2)
        assert expected_tasks_after_delete == 2

    @allure.title("Edit task name")
    @allure.description("Verify name changed")
    def test_edit_name(self):
        expected_modified_task_name = "Task name edited"
        self.edit_task(1, expected_modified_task_name)
        assert self.list_items()[1].text == expected_modified_task_name

    @allure.title("Mark task as completed")
    @allure.title("Verify task marked as completed")
    def test_toggled_task(self):
        expected_class_name_after_toggle = "completed"
        # Mark first task as completed
        self.toggle_task(0)
        assert self.list_items()[0].get_attribute("class") == expected_class_name_after_toggle

    @allure.title("Filter completed")
    @allure.description("Verify tasks filtered - completed")
    def test_filter_completed(self):
        expected_completed_tasks = self.get_completed_tasks_count()
        self.filter_completed()
        assert len(self.list_items()) == expected_completed_tasks


    @allure.title("Filter active")
    @allure.description("Verify tasks filtered - active")
    def test_filter_active(self):
        self.filter_all()
        expected_active_tasks = len(self.list_items()) - 1
        self.filter_active()
        assert len(self.list_items()) == expected_active_tasks


    @allure.title("Delete completed")
    @allure.description("Verify completed tasks deleted")
    def test_delete_completed(self):
        self.filter_all()
        completed_tasks = self.get_completed_tasks_count()
        expected_count_after_delete = len(self.list_items()) - completed_tasks
        self.clear_completed()
        assert len(self.list_items()) == expected_count_after_delete
