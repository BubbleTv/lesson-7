from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    
    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def add_backpack_to_cart(self):
        
        button = self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_BUTTON)
        )
        button.click()
        return self
    
    def add_bolt_tshirt_to_cart(self):
        
        button = self.wait.until(
            EC.element_to_be_clickable(self.BOLT_TSHIRT_BUTTON)
        )
        button.click()
        return self
    
    def add_onesie_to_cart(self):
      
        button = self.wait.until(
            EC.element_to_be_clickable(self.ONESIE_BUTTON)
        )
        button.click()
        return self
    
    def go_to_cart(self):
        
        cart = self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        cart.click()
        return self