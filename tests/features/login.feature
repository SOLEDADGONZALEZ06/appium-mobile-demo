Feature: Login en la app mobile

  Scenario: Login exitoso con credenciales válidas
    Given la app está abierta en la pantalla de login
    When ingreso el usuario "bob@example.com" y la contraseña "10203040"
    And presiono el botón de login
    Then debería ver la pantalla de lista de productos

  Scenario: Login fallido con usuario bloqueado
    Given la app está abierta en la pantalla de login
    When ingreso el usuario "alice@example.com" y la contraseña "10203040"
    And presiono el botón de login
    Then debería ver un mensaje de error de usuario bloqueado

  #Scenario: Login fallido con campos vacíos
    #Given la app está abierta en la pantalla de login
    #When presiono el botón de login sin ingresar datos
    #Then debería ver un mensaje de error de campos requeridos