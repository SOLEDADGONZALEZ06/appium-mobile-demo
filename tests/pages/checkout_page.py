from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PACKAGE = "com.saucelabs.mydemoapp.android"


class CheckoutPage:
    FULL_NAME_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/fullNameET")
    ADDRESS_LINE_1_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/address1ET")
    ADDRESS_LINE_2_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/address2ET")
    CITY_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/cityET")
    STATE_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/stateET")
    ZIP_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/zipET")
    COUNTRY_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/countryET")
    BOTON_IR_A_PAGO = (AppiumBy.ID, f"{PACKAGE}:id/paymentBtn")

    CARD_NAME_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/nameET")
    CARD_NUMBER_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/cardNumberET")
    EXPIRATION_DATE_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/expirationDateET")
    SECURITY_CODE_INPUT = (AppiumBy.ID, f"{PACKAGE}:id/securityCodeET")
    BOTON_REVISAR_ORDEN = (AppiumBy.ACCESSIBILITY_ID, "Saves payment info and launches screen to review checkout data")

    BOTON_CONFIRMAR_COMPRA = (AppiumBy.ACCESSIBILITY_ID, "Completes the process of checkout")
    TITULO_COMPRA_COMPLETADA = (AppiumBy.ID, f"{PACKAGE}:id/completeTV")

    def _scroll_to(self, driver, resource_id):
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
            f'new UiSelector().resourceId("{resource_id}"))'
        )

    def registrar_cliente(self, driver, nombre, direccion1, direccion2, ciudad, estado, codigo_postal, pais):
        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.FULL_NAME_INPUT)
        )
        campo.clear()
        campo.send_keys(nombre)

        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.ADDRESS_LINE_1_INPUT)
        )
        campo.clear()
        campo.send_keys(direccion1)

        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.ADDRESS_LINE_2_INPUT)
        )
        campo.clear()
        campo.send_keys(direccion2)

        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.CITY_INPUT)
        )
        campo.clear()
        campo.send_keys(ciudad)

        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.STATE_INPUT)
        )
        campo.clear()
        campo.send_keys(estado)

        self._scroll_to(driver, f"{PACKAGE}:id/zipET")
        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.ZIP_INPUT)
        )
        campo.clear()
        campo.send_keys(codigo_postal)

        self._scroll_to(driver, f"{PACKAGE}:id/countryET")
        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.COUNTRY_INPUT)
        )
        campo.clear()
        campo.send_keys(pais)

    def tap_to_payment(self, driver):
        self._scroll_to(driver, f"{PACKAGE}:id/paymentBtn")
        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.BOTON_IR_A_PAGO)
        )
        boton.click()

    def registrar_pago(self, driver, nombre_tarjeta, numero_tarjeta, vencimiento, codigo_seguridad):
        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.CARD_NAME_INPUT)
        )
        campo.clear()
        campo.send_keys(nombre_tarjeta)

        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.CARD_NUMBER_INPUT)
        )
        campo.clear()
        campo.send_keys(numero_tarjeta)

        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.EXPIRATION_DATE_INPUT)
        )
        campo.clear()
        campo.send_keys(vencimiento)

        campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.SECURITY_CODE_INPUT)
        )
        campo.clear()
        campo.send_keys(codigo_seguridad)

    def tap_review_order(self, driver):
        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.BOTON_REVISAR_ORDEN)
        )
        boton.click()

    def tap_place_order(self, driver):
        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.BOTON_CONFIRMAR_COMPRA)
        )
        boton.click()

    def is_checkout_complete_displayed(self, driver):
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.TITULO_COMPRA_COMPLETADA)
        )
        return elemento.is_displayed()