from base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def is_item_in_cart(self, item_name):
        self.driver.get('https://rozetka.com.ua/cart/')
        cart_items = self.driver.find_elements(By.XPATH, "//a[@class='cart-product__title']")
        for item in cart_items:
            if item_name in item.text:
                return True
        return False
