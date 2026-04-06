"""Inventory page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Inventory page object class."""

    # Locators
    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        """Add backpack to cart."""
        self.click_element(self.BACKPACK_BUTTON)
        return self

    def add_bolt_tshirt_to_cart(self):
        """Add bolt t-shirt to cart."""
        self.click_element(self.BOLT_TSHIRT_BUTTON)
        return self

    def add_onesie_to_cart(self):
        """Add onesie to cart."""
        self.click_element(self.ONESIE_BUTTON)
        return self

    def go_to_cart(self):
        """Go to cart."""
        self.click_element(self.CART_ICON)
        return self