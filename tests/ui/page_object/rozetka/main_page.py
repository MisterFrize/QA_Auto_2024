from base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    URL = 'https://rozetka.com.ua/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)

    def search_for_item(self, item_name):
        search_box = self.driver.find_element(By.NAME, 'search')
        search_box.send_keys(item_name)
        search_box.submit()
