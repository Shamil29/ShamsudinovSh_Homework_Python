from selenium.webdriver.common.by import By


class YourInfoPage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/checkout-step-one.html")
        self.browser.maximize_window()

    def first_name(self, first_name):
        first_name_field = self.browser.find_element(By.ID, 'first-name')
        first_name_field.clear()
        my_first_name = first_name
        first_name_field.send_keys(my_first_name)

    def last_name(self, last_name):
        last_name_field = self.browser.find_element(By.ID, 'last-name')
        last_name_field.clear()
        my_last_name = last_name
        last_name_field.send_keys(my_last_name)

    def zip_postal_code(self, zip_postal_code):
        zip_postal_code_field = self.browser.find_element(By.ID, 'postal-code')
        zip_postal_code_field.clear()
        my_zip_postal_code = zip_postal_code
        zip_postal_code_field.send_keys(my_zip_postal_code)

    def button_continue(self):
        self.browser.find_element(By.ID, 'continue').click()
