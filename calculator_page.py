"""Calculator page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CalculatorPage(BasePage):
    """Calculator page object class."""

    # Locators
    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    SCREEN_RESULT = (By.CLASS_NAME, "screen")

    def open(self):
        """
        Open calculator page.

        Returns:
            CalculatorPage instance for chaining
        """
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        super().open(url)
        return self

    def set_delay(self, seconds: int):
        """
        Set delay before calculation.

        Args:
            seconds: Delay in seconds

        Returns:
            CalculatorPage instance for chaining
        """
        self.input_text(self.DELAY_INPUT, str(seconds))
        return self

    def click_button_7(self):
        """Click button 7."""
        self.click_element(self.BUTTON_7)
        return self

    def click_button_8(self):
        """Click button 8."""
        self.click_element(self.BUTTON_8)
        return self

    def click_button_plus(self):
        """Click plus button."""
        self.click_element(self.BUTTON_PLUS)
        return self

    def click_button_equals(self):
        """Click equals button."""
        self.click_element(self.BUTTON_EQUALS)
        return self

    def get_result(self, timeout: int = 50) -> str:
        """
        Get calculation result.

        Args:
            timeout: Wait timeout in seconds

        Returns:
            Calculation result
        """
        self.wait_for_text(self.SCREEN_RESULT, "15", timeout)
        return self.get_text(self.SCREEN_RESULT, timeout)