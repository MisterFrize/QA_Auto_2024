import pytest
from selenium import webdriver
from page_object.sign_in_page import SignInPage

@pytest.mark.ui
def test_sign_in():
    driver = webdriver.Chrome()
    page = SignInPage(driver)
    
    page.sign_in("invalid_user", "invalid_pass")
    
    assert page.is_title_matches("Sign in to GitHub")
    
    page.close()