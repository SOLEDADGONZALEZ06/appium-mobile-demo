from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage
import time

scenarios("../features/checkout.feature")

login_page = LoginPage()
products_page = ProductsPage()
cart_page = CartPage()
checkout_page = CheckoutPage()


@given("la app está abierta en la pantalla de login")
def app_abierta_en_login(driver):
    if products_page.is_on_products_screen(driver):
        products_page.logout(driver)
        time.sleep(2)
    print("ACTIVITY ACTUAL:", driver.current_activity)

@when(parsers.parse('ingreso el usuario "{usuario}" y la contraseña "{password}"'))
def ingresar_credenciales(driver, usuario, password):
    login_page.enter_username(driver, usuario)
    time.sleep(2)
    login_page.enter_password(driver, password)
    time.sleep(2)

@when("presiono el botón de login")
def presionar_login(driver):
    login_page.tap_login(driver)
    time.sleep(2)

@then("debería ver la pantalla de lista de productos")
def ver_pantalla_productos(driver):
    assert products_page.is_products_screen_displayed(driver)

@when("selecciono el primer producto de la lista")
def seleccionar_primer_producto(driver):
    products_page.select_first_product(driver)
    time.sleep(2)

@when("presiono el botón de agregar al carrito")
def agregar_al_carrito(driver):
    products_page.tap_add_to_cart(driver)
    time.sleep(2)

@when("voy al carrito")
def ir_al_carrito(driver):
    products_page.go_to_cart(driver)
    time.sleep(2)

@when("presiono el botón de proceder al checkout")
def proceder_al_checkout(driver):
    cart_page.tap_proceed_to_checkout(driver)
    time.sleep(2)

@when("completo los datos del cliente")
def completar_datos_cliente(driver):
    checkout_page.registrar_cliente(
        driver,
        nombre="Ana Gomez",
        direccion1="Av. Siempre Viva 742",
        direccion2="Depto 3B",
        ciudad="Buenos Aires",
        estado="Buenos Aires",
        codigo_postal="1425",
        pais="Argentina"
    )
    time.sleep(2)

@when("completo los datos de pago")
def completar_datos_pago(driver):
    checkout_page.registrar_pago(
        driver,
        nombre_tarjeta="Ana Gomez",
        numero_tarjeta="4111111111111111",
        vencimiento="12/28",
        codigo_seguridad="123"
    )
    time.sleep(2)

@when("presiono el botón de continuar al pago")
def continuar_al_pago(driver):
    checkout_page.tap_to_payment(driver)
    time.sleep(2)

@when("presiono el botón de revisar la orden")
def revisar_orden(driver):
    checkout_page.tap_review_order(driver)
    time.sleep(2)

@when("presiono el botón de confirmar la compra")
def confirmar_compra(driver):
    checkout_page.tap_place_order(driver)
    time.sleep(2)

@then("debería ver el mensaje de compra completada")
def ver_compra_completada(driver):
    assert checkout_page.is_checkout_complete_displayed(driver)