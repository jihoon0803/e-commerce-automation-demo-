# pages/auth_page.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators (예시: resource-id / xpath는 실제 앱에 맞게 수정)
        self.btn_signup = (AppiumBy.ACCESSIBILITY_ID, "signup_button")
        self.btn_login = (AppiumBy.ACCESSIBILITY_ID, "login_button")
        self.input_email = (AppiumBy.ACCESSIBILITY_ID, "email_input")
        self.input_password = (AppiumBy.ACCESSIBILITY_ID, "password_input")
        self.btn_submit = (AppiumBy.ACCESSIBILITY_ID, "submit_button")
        self.txt_welcome = (AppiumBy.ACCESSIBILITY_ID, "welcome_text")
        self.toast_error = (AppiumBy.XPATH, "//android.widget.Toast")  # 안드로이드 Toast 예시

    def signup(self, email, password):
        self.driver.find_element(*self.btn_signup).click()
        self.driver.find_element(*self.input_email).send_keys(email)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.btn_submit).click()

    def login(self, email, password):
        self.driver.find_element(*self.btn_login).click()
        self.driver.find_element(*self.input_email).send_keys(email)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.btn_submit).click()

    def wait_welcome(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.txt_welcome)
        )
        return self.driver.find_element(*self.txt_welcome).text
