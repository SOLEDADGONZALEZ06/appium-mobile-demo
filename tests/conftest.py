from datetime import datetime
from pathlib import Path
import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APK_PATH = Path(__file__).resolve().parent.parent / "apps" / "mda.apk"


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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(scope="function")
def driver(request):
    """Crea el driver de Appium para el emulador Android."""
    caps = dict(
        app=str(APK_PATH),
        platformName="Android",
        automationName="UiAutomator2",
        deviceName="emulator-5554",
        appPackage="com.saucelabs.mydemoapp.android",
        appActivity=".view.activities.SplashActivity",
        appWaitActivity=".view.activities.MainActivity",
        appWaitDuration=30000,
        noReset=True,
        newCommandTimeout=300,
        autoGrantPermissions=True,
    )

    options = UiAutomator2Options()
    for key, value in caps.items():
        options.set_capability(key, value)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)

    time.sleep(5)

    yield driver

    if getattr(request.node, "rep_call", None) is not None and request.node.rep_call.failed:
        screenshot_path = take_screenshot(driver, name="failure")
        print(f"DEBUG: screenshot guardada en {screenshot_path}")

    driver.quit()