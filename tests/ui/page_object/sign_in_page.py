from .base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)

    def sign_in(self, username, password):
        self.driver.find_element(By.ID, 'login_field').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.NAME, 'commit').click()

    def is_title_matches(self, title):
        return title in self.driver.title