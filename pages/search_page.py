# pages/search_page.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.input_search = (AppiumBy.ACCESSIBILITY_ID, "search_input")
        self.btn_search = (AppiumBy.ACCESSIBILITY_ID, "search_button")
        self.first_result_title = (AppiumBy.XPATH, "(//android.view.View[@content-desc='result_title'])[1]")

    def search_keyword(self, keyword):
        self.driver.find_element(*self.input_search).click()
        self.driver.find_element(*self.input_search).clear()
        self.driver.find_element(*self.input_search).send_keys(keyword)
        self.driver.find_element(*self.btn_search).click()

    def open_first_result(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_result_title)
        )
        self.driver.find_element(*self.first_result_title).click()
        return self.driver.find_element(*self.first_result_title).text