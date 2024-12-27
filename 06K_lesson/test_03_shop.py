from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

user_name = 'standard_user'
password = 'secret_sauce'

first_name = 'Shamil'
last_name = 'Shamsudinov'
zip_postal_code = '171381'


def test_swag_labs():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    user_name_field = driver.find_element(By.ID, 'user-name')
    user_name_field.clear()
    user_name_field.send_keys(user_name)

    password_field = driver.find_element(By.ID, 'password')
    password_field.clear()
    password_field.send_keys(password)

    button1 = driver.find_element(By.ID, 'login-button')
    button1.click()

    sauce_labs_backpack = driver.find_element(
        By.ID, 'add-to-cart-sauce-labs-backpack')
    sauce_labs_backpack.click()

    sauce_labs_bolt_T_Shirt = (driver.find_element
                               (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'))
    sauce_labs_bolt_T_Shirt.click()

    sauce_labs_onesie = driver.find_element(
        By.ID, 'add-to-cart-sauce-labs-onesie')
    sauce_labs_onesie.click()

    shopping_cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    shopping_cart.click()

    button2 = driver.find_element(By.ID, 'checkout')
    button2.click()

    first_name_field = driver.find_element(By.ID, 'first-name')
    first_name_field.clear()
    first_name_field.send_keys(first_name)

    last_name_field = driver.find_element(By.ID, 'last-name')
    last_name_field.clear()
    last_name_field.send_keys(last_name)

    zip_postal_code_field = driver.find_element(By.ID, 'postal-code')
    zip_postal_code_field.clear()
    zip_postal_code_field.send_keys(zip_postal_code)

    button3 = driver.find_element(By.ID, 'continue')
    button3.click()

    summary_text = driver.find_element(
        By.CLASS_NAME, 'summary_total_label').text
    print(summary_text)

    assert "$58.29" in driver.find_element(
        By.CLASS_NAME, 'summary_total_label').text

    driver.quit()
