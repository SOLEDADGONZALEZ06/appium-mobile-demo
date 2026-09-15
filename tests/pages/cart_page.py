from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    BOTON_PROCEDER_CHECKOUT = (AppiumBy.ACCESSIBILITY_ID, "Confirms products for checkout")

    def tap_proceed_to_checkout(self, driver):
        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.BOTON_PROCEDER_CHECKOUT)
        )
        boton.click()