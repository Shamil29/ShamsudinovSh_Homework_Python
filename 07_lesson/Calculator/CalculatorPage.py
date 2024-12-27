from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.browser.maximize_window()

    def field_waits(self):
        waits = self.browser.find_element(By.CSS_SELECTOR, '#delay')
        waits.clear()
        waits.send_keys('45')

    def click_button_1(self):
        self.browser.find_element(By.XPATH, '//span[text()="7"]').click()

    def click_button_2(self):
        self.browser.find_element(By.XPATH, '//span[text()="+"]').click()

    def click_button_3(self):
        self.browser.find_element(By.XPATH, '//span[text()="8"]').click()

    def click_button_4(self):
        self.browser.find_element(By.XPATH, '//span[text()="="]').click()

    def find_result(self):
        waiter = WebDriverWait(self.browser, 50)
        waiter.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'screen'), '15'))
        result = self.browser.find_element(By.CLASS_NAME, 'screen').text
        return result
