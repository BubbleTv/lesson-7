"""Cart page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Cart page object class."""

    # Locators
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        """Click checkout button."""
        self.click_element(self.CHECKOUT_BUTTON)
        return self