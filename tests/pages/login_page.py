from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver

PACKAGE = "com.saucelabs.mydemoapp.android"

class LoginPage:
    USERNAME_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/nameET")
    PASSWORD_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ID, f"{PACKAGE}:id/loginBtn")
    USERNAME_ERROR = (AppiumBy.ID, f"{PACKAGE}:id/nameErrorTV")
    PASSWORD_ERROR = (AppiumBy.ID, f"{PACKAGE}:id/passwordErrorTV")

    def enter_username(self, driver, usuario):
        campo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(self.USERNAME_INPUT)
     )
        campo.clear()
        campo.send_keys(usuario)

    def enter_password(self, driver, password):
        campo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(self.PASSWORD_INPUT)
    )
        campo.clear()
        campo.send_keys(password)

    def tap_login(self, driver):
        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        boton.click()

    def get_password_error_text(self, driver):
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.PASSWORD_ERROR)
        )
        return elemento.text

   