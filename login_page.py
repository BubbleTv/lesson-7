"""Login page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object class."""

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        """
        Open login page.

        Returns:
            LoginPage instance for chaining
        """
        url = "https://www.saucedemo.com/"
        super().open(url)
        return self

    def login(self, username: str, password: str):
        """
        Perform login.

        Args:
            username: Username
            password: Password

        Returns:
            LoginPage instance for chaining
        """
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        return self