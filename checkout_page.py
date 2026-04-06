"""Checkout page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Checkout page object class."""

    # Locators
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        """
        Fill checkout form.

        Args:
            first_name: First name
            last_name: Last name
            postal_code: Postal code

        Returns:
            CheckoutPage instance for chaining
        """
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.POSTAL_CODE_INPUT, postal_code)
        return self

    def click_continue(self):
        """Click continue button."""
        self.click_element(self.CONTINUE_BUTTON)
        return self

    def get_total(self) -> str:
        """
        Get total amount.

        Returns:
            Total amount as string without dollar sign
        """
        total_text = self.get_text(self.TOTAL_LABEL)
        return total_text.split("$")[1]