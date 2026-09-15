Feature: Compra de un producto

  Scenario: Compra exitosa de un producto (camino feliz)
    Given la app está abierta en la pantalla de login
    When ingreso el usuario "bob@example.com" y la contraseña "10203040"
    And presiono el botón de login
    Then debería ver la pantalla de lista de productos
    When selecciono el primer producto de la lista
    And presiono el botón de agregar al carrito
    And voy al carrito
    And presiono el botón de proceder al checkout
    And completo los datos del cliente
    And presiono el botón de continuar al pago
    And completo los datos de pago
    And presiono el botón de revisar la orden
    And presiono el botón de confirmar la compra
    Then debería ver el mensaje de compra completada