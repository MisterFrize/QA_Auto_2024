import pytest
from selenium import webdriver
from rozetka.main_page import MainPage
from rozetka.search_results_page import SearchResultsPage
from rozetka.cart_page import CartPage

@pytest.mark.ui
def test_add_to_cart():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    search_results_page = SearchResultsPage(driver)
    cart_page = CartPage(driver)

    item_name = "телефон"
    main_page.search_for_item(item_name)
    search_results_page.add_first_item_to_cart()

    assert cart_page.is_item_in_cart(item_name)

    driver.close()