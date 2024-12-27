from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/")
        self.browser.maximize_window()

    def username(self, user_name):
        user_name_field = self.browser.find_element(By.ID, 'user-name')
        user_name_field.clear()
        login = user_name
        user_name_field.send_keys(login)

    def password(self, password):
        password_field = self.browser.find_element(By.ID, 'password')
        password_field.clear()
        my_password = password
        password_field.send_keys(my_password)

    def login_button(self):
        self.browser.find_element(By.ID, 'login-button').click()
