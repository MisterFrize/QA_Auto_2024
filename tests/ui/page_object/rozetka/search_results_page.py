from base_page import BasePage
from selenium.webdriver.common.by import By

class SearchResultsPage(BasePage):
    def add_first_item_to_cart(self):
        first_item = self.driver.find_element(By.XPATH, "//span[@class='goods-tile__title']")
        first_item.click()
        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'buy-button')]")
        add_to_cart_button.click()