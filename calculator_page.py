from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    
    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    SCREEN_RESULT = (By.CLASS_NAME, "screen")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        return self
    
    def set_delay(self, seconds):
        
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self
    
    def click_button_7(self):
        
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_7)
        )
        button.click()
        return self
    
    def click_button_8(self):
       
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_8)
        )
        button.click()
        return self
    
    def click_button_plus(self):
    
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_PLUS)
        )
        button.click()
        return self
    
    def click_button_equals(self):
       
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_EQUALS)
        )
        button.click()
        return self
    
    def get_result(self, timeout=50):
      
        self.wait = WebDriverWait(self.driver, timeout)
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.SCREEN_RESULT)
        )
        return result_element.text