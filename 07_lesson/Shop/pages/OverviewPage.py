from selenium.webdriver.common.by import By


class OverviewPage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/checkout-step-two.html")
        self.browser.maximize_window()

    def total_price(self):
        summary_text = self.browser.find_element(
            By.CLASS_NAME, 'summary_total_label').text
        return summary_text
