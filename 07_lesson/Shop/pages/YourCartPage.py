from selenium.webdriver.common.by import By


class YourCartPage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/cart.html")
        self.browser.maximize_window()

    def button_checkout(self):
        self.browser.find_element(By.ID, 'checkout').click()
