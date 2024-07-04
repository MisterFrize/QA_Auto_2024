from selenium import webdriver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def close(self):
        self.driver.close()