from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

PACKAGE = "com.saucelabs.mydemoapp.android"

class ProductsPage:
    PRODUCTS_TITLE = (AppiumBy.ID, f"{PACKAGE}:id/productTV")
    MENU_ICON = (AppiumBy.ID, f"{PACKAGE}:id/menuIV")
    LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Logout Menu Item")
    LOGOUT_CONFIRM_BUTTON = (AppiumBy.ID, "android:id/button1")
    LOGIN_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
    PRODUCT_ITEMS = (AppiumBy.ID, f"{PACKAGE}:id/productIV")
    BOTON_AGREGAR_CARRITO = (AppiumBy.ID, f"{PACKAGE}:id/cartBt")
    CARRITO_ICON = (AppiumBy.ACCESSIBILITY_ID, "View cart")
    CONTINUE_SHOPPING_BTN = (AppiumBy.ACCESSIBILITY_ID, "Continue Shopping")

    def is_products_screen_displayed(self, driver):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(self.PRODUCTS_TITLE)
            )
            return True
        except TimeoutException:
            return False

    def is_on_products_screen(self, driver, timeout=3):
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(self.PRODUCTS_TITLE)
            )
            return True
        except TimeoutException:
            return False

    def ensure_on_products_screen(self, driver):
        if not self.is_on_products_screen(driver, timeout=3):
            try:
                continue_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BTN)
                )
                continue_btn.click()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(self.PRODUCTS_TITLE)
                )
            except TimeoutException:
                pass

    def logout(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.MENU_ICON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_CONFIRM_BUTTON)
        ).click()

    def go_to_login_screen(self, driver):
        self.ensure_on_products_screen(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.MENU_ICON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_MENU_ITEM)
        ).click()

    def select_first_product(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.PRODUCT_ITEMS)
        ).click()

    def tap_add_to_cart(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.BOTON_AGREGAR_CARRITO)
        ).click()

    def go_to_cart(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.CARRITO_ICON)
        ).click()