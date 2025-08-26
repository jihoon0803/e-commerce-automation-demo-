# conftest.py
import os, pytest
from appium import webdriver

@pytest.fixture(scope="session")
def driver():
    caps = {
        "platformName": os.getenv("PLATFORM", "Android"),         # "iOS"도 가능
        "deviceName": os.getenv("DEVICE_NAME", "Android Emulator"),
        "automationName": os.getenv("AUTOMATION", "UiAutomator2"),
        "app": os.getenv("APP_PATH", "/path/to/app.apk"),
        # Webview가 있다면:
        # "chromedriverExecutable": "/path/to/chromedriver",
        "newCommandTimeout": 120
    }
    driver = webdriver.Remote(os.getenv("APPIUM_URL", "http://127.0.0.1:4723/wd/hub"), caps)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
