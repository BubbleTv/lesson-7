"""Pytest fixtures."""

import pytest
from selenium import webdriver


@pytest.fixture
def chrome_driver():
    """Chrome WebDriver fixture."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    """Firefox WebDriver fixture."""
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()