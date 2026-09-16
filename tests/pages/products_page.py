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

    def is_products_screen_displayed(self, driver):
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.PRODUCTS_TITLE)
        )
        return elemento.is_displayed()

    def is_on_products_screen(self, driver, timeout=3):
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(self.PRODUCTS_TITLE)
            )
            return True
        except TimeoutException:
            return False

    def logout(self, driver):
        menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.MENU_ICON)
        )
        menu.click()

        logout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)
        )
        logout_btn.click()

        confirm_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_CONFIRM_BUTTON)
        )
        confirm_btn.click()

    def go_to_login_screen(self, driver):
        """Abre el menú y navega a la pantalla de login, ya sea desloguenado
        una sesión activa o tocando 'Log In' directamente si no hay sesión."""
        menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.MENU_ICON)
        )
        menu.click()

        try:
            logout_btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable(self.LOGOUT_BUTTON)
            )
            logout_btn.click()
            confirm_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(self.LOGOUT_CONFIRM_BUTTON)
            )
            confirm_btn.click()
        except TimeoutException:
            login_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(self.LOGIN_MENU_ITEM)
            )
            login_btn.click()

    def select_first_product(self, driver):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.PRODUCT_ITEMS)
        )
        productos = driver.find_elements(*self.PRODUCT_ITEMS)
        productos[0].click()

    def tap_add_to_cart(self, driver):
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
            f'new UiSelector().resourceId("{PACKAGE}:id/cartBt"))'
        )
        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.BOTON_AGREGAR_CARRITO)
        )
        boton.click()

    def go_to_cart(self, driver):
        carrito = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.CARRITO_ICON)
        )
        carrito.click()