"""Shop tests."""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_checkout():
    """Test shop checkout and total verification."""
    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=firefox_options)

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack_to_cart()
        inventory_page.add_bolt_tshirt_to_cart()
        inventory_page.add_onesie_to_cart()
        inventory_page.go_to_cart()

        cart_page.click_checkout()

        checkout_page.fill_checkout_form("Ivan", "Petrov", "123456")
        checkout_page.click_continue()

        total = checkout_page.get_total()
        assert total == "58.29", f"Expected '58.29', got '{total}'"

    finally:
        driver.quit()