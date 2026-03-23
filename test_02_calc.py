import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.calculator_page import CalculatorPage


def test_calculator():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    
    try:

        calculator = CalculatorPage(driver)
        
    
        calculator.open() \
            .set_delay(45) \
            .click_button_7() \
            .click_button_plus() \
            .click_button_8() \
            .click_button_equals()
        
        result = calculator.get_result(timeout=50)
        

        assert result == "15", f"Expected result '15', but got '{result}'"
        
    finally:
        driver.quit()