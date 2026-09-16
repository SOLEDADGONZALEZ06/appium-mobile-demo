from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage
import time

scenarios("../features/login.feature")

login_page = LoginPage()
products_page = ProductsPage()


@given("la app está abierta en la pantalla de login")
def app_abierta_en_login(driver):
    if products_page.is_on_products_screen(driver):
        products_page.go_to_login_screen(driver)
        time.sleep(2)
    print("ACTIVITY ACTUAL:", driver.current_activity)

@when(parsers.parse('ingreso el usuario "{usuario}" y la contraseña "{password}"'))
def ingresar_credenciales(driver, usuario, password):
    login_page.enter_username(driver, usuario)
    time.sleep(4)
    login_page.enter_password(driver, password)
    time.sleep(4)

@when("presiono el botón de login")
def presionar_login(driver):
    login_page.tap_login(driver)
    time.sleep(4)

@then("debería ver la pantalla de lista de productos")
def ver_pantalla_productos(driver):
    assert products_page.is_products_screen_displayed(driver)

@when("presiono el botón de login sin ingresar datos")
def presionar_login_sin_datos(driver):
    login_page.tap_login(driver)
    time.sleep(4)

@then("debería ver un mensaje de error de usuario bloqueado")
def ver_error_usuario_bloqueado(driver):
    mensaje = login_page.get_password_error_text(driver)
    assert "locked out" in mensaje

@then("debería ver un mensaje de error de campos requeridos")
def ver_error_campos_requeridos(driver):
    mensaje = login_page.get_username_error_text(driver)
    assert "required" in mensaje