"""Calculator tests."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.calculator_page import CalculatorPage


def test_calculator():
    """Test calculator addition with delay."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        calculator = CalculatorPage(driver)
        calculator.open()
        calculator.set_delay(45)
        calculator.click_button_7()
        calculator.click_button_plus()
        calculator.click_button_8()
        calculator.click_button_equals()

        result = calculator.get_result(timeout=50)
        assert result == "15", f"Expected '15', got '{result}'"

    finally:
        driver.quit()