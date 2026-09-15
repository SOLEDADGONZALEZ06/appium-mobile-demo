# Appium Mobile Demo

Proyecto de portfolio para QA Automation: automatización mobile de la app **Sauce Labs
"My Demo App"** (Android nativo) usando **Appium + Python + pytest-bdd (BDD/Gherkin)** con
**Page Object Model (POM)**.

## Stack

- Appium + UiAutomator2
- Python 3.14
- pytest + pytest-bdd (Behavior Driven Development)
- Selenium WebDriver
- Page Object Model (POM)

## Requisitos

- Android Studio con un emulador (AVD) creado
- Java JDK 17+
- Node.js y Appium Server
- Python 3.10+

## Estructura del proyecto

tests/
├── conftest.py # fixture del driver de Appium
├── features/ # escenarios en Gherkin (BDD)
│ ├── login.feature
│ └── checkout.feature
├── step_defs/ # traduce cada paso del feature a código
│ ├── test_login_steps.py
│ └── test_checkout_steps.py
└── pages/ # Page Object Model: una clase por pantalla
├── login_page.py
├── products_page.py
├── cart_page.py
└── checkout_page.py


## Flujos automatizados

- **Login**: login exitoso, y login fallido con usuario bloqueado (con logout
  automático entre escenarios para evitar estado compartido).
- **Compra (camino feliz)**: login → seleccionar producto → agregar al carrito →
  checkout → completar datos de envío y pago → confirmar compra.

## Cómo correr los tests

**1. Preparar el emulador**

```bash
adb devices
```

**2. Instalar dependencias**

```bash
pip install -r requirements.txt
```

**3. Levantar Appium**

```bash
appium
```

**4. Correr los tests**

```bash
pytest tests/step_defs/test_login_steps.py -v
pytest tests/step_defs/test_checkout_steps.py -v
```

## Decisiones de diseño

- **pytest-bdd** en vez de Behave, porque reutiliza el fixture `driver` de
  `conftest.py` sin necesitar un runner aparte.
- Prioridad de locators: `id` (resource-id) > `accessibility id` > XPath, sacados
  con Appium Inspector y verificados en vivo.
- `noReset=True` en las capabilities, junto con un logout automático al inicio de
  cada escenario, para evitar que el estado de sesión de un escenario afecte al
  siguiente.