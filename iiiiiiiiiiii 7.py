import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_checkout():
    """Тест для проверки интернет-магазина с использованием Page Object"""
    # Настройка Firefox
    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=firefox_options)
    
    try:
        # Создаем объекты страниц
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        
        # Выполняем сценарий с использованием Page Object
        login_page.open() \
            .login("standard_user", "secret_sauce")
        
        inventory_page.add_backpack_to_cart() \
            .add_bolt_tshirt_to_cart() \
            .add_onesie_to_cart() \
            .go_to_cart()
        
        cart_page.click_checkout()
        
        checkout_page.fill_checkout_form("Иван", "Петров", "123456") \
            .click_continue()
        
        # Получаем итоговую сумму
        total = checkout_page.get_total()
        
        # Проверяем итоговую сумму
        assert total == "58.29", f"Expected total '58.29', but got '{total}'"
        
    finally:
        driver.quit()