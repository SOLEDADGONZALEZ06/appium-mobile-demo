from datetime import datetime
from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


def take_screenshot(driver, name="screenshot", output_dir=None):
    """Guarda una captura del estado actual de la app en un archivo .png."""
    screenshots_dir = Path(output_dir) if output_dir else Path(__file__).resolve().parent / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    file_path = screenshots_dir / f"{name}_{timestamp}.png"

    if hasattr(driver, "get_screenshot_as_file"):
        saved = driver.get_screenshot_as_file(str(file_path))
        if saved:
            return file_path

    if hasattr(driver, "save_screenshot"):
        driver.save_screenshot(str(file_path))
        return file_path

    raise AttributeError("El driver no tiene soporte para capturas de pantalla.")


@pytest.fixture(scope="function")
def driver():
    """Crea el driver de Appium para el emulador Android."""
    caps = dict(
        platformName="Android",
        automationName="UiAutomator2",
        deviceName="emulator-5554",
        appPackage="com.saucelabs.mydemoapp.android",
        appActivity=".view.activities.SplashActivity",
        appWaitActivity=".view.activities.*",
        noReset=True,
        newCommandTimeout=300,
        autoGrantPermissions=True,
    )

    options = UiAutomator2Options()
    for key, value in caps.items():
        options.set_capability(key, value)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    print(f"DEBUG: when={report.when}, failed={report.failed}, funcargs={list(item.funcargs.keys())}")
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        print(f"DEBUG: driver encontrado = {driver is not None}")
        if driver:
            screenshot_path = take_screenshot(driver, name="failure")
            print(f"DEBUG: screenshot guardada en {screenshot_path}")